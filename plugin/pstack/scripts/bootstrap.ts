import { createHash } from "node:crypto";
import { existsSync, readFileSync, writeFileSync, mkdirSync, readdirSync, copyFileSync, realpathSync, rmdirSync } from "node:fs";
import { join, resolve, relative, isAbsolute, dirname, basename } from "node:path";

// Imported before external dependencies by both launchers. Never install into
// the plugin or rely on Bun's implicit package installation.
export function ensureDependenciesInstalled(): void {
  const source = import.meta.dir;
  const configured = process.env.PSTACK_TOOLS_CACHE;
  if (!configured || !isAbsolute(configured)) {
    throw new Error("Set PSTACK_TOOLS_CACHE to a recipient-owned absolute directory outside the plugin; read references/orchestration.md");
  }
  // Resolve existing ancestors (including symlinks) before creating anything.
  const missing: string[] = [];
  let ancestor = resolve(configured);
  while (!existsSync(ancestor)) {
    missing.unshift(basename(ancestor));
    const parent = dirname(ancestor);
    if (parent === ancestor) throw new Error("Cannot resolve dependency cache parent");
    ancestor = parent;
  }
  const cache = join(realpathSync(ancestor), ...missing);
  const plugin = realpathSync(join(source, ".."));
  const files: string[] = [];
  function collect(directory: string, prefix = ""): void {
    for (const entry of readdirSync(directory, { withFileTypes: true }).sort((a,b) => a.name.localeCompare(b.name))) {
      if (entry.name === "node_modules" || entry.name.startsWith(".")) continue;
      const name = join(prefix, entry.name);
      if (entry.isDirectory()) collect(join(directory, entry.name), name);
      else if (entry.isFile()) files.push(name);
    }
  }
  collect(source);
  const digest = createHash("sha256");
  for (const file of files) digest.update(file).update("\0").update(readFileSync(join(source, file))).update("\0");
  const key = digest.digest("hex");
  const runtime = join(cache, key);
  const marker = join(runtime, ".pstack-dependencies-ready");
  const ready = () => existsSync(join(runtime, "node_modules/commander/package.json")) &&
    existsSync(marker) && readFileSync(marker, "utf8").trim() === key;
  // A cached invocation rehashes the copied source and proves its exact location.
  if (realpathSync(source) === runtime && ready()) return;
  if (cache === plugin || cache.startsWith(`${plugin}/`)) {
    throw new Error("PSTACK_TOOLS_CACHE must be outside the installed plugin");
  }
  const setup = process.argv.includes("--setup-dependencies");
  if (!ready()) {
    if (!setup) throw new Error("Dependencies absent for this package revision. Explicitly run the same launcher with --setup-dependencies, using bun --no-install; this installs locked dependencies only in PSTACK_TOOLS_CACHE.");
    mkdirSync(runtime, { recursive: true });
    const lock = join(runtime, ".setup-lock");
    try { mkdirSync(lock); } catch { throw new Error("Dependency setup already in progress or interrupted; inspect .setup-lock before retrying"); }
    try {
      for (const file of files) {
        mkdirSync(resolve(runtime, file, ".."), { recursive: true });
        copyFileSync(join(source, file), join(runtime, file));
      }
      const result = Bun.spawnSync([process.execPath, "install", "--frozen-lockfile", "--ignore-scripts"], { cwd: runtime, stdout: "inherit", stderr: "inherit" });
      if (result.exitCode !== 0 || !existsSync(join(runtime, "node_modules/commander/package.json"))) throw new Error("Locked dependency setup failed; no ready marker written");
      writeFileSync(marker, `${key}\n`);
    } finally { rmdirSync(lock); }
  }
  const entry = relative(source, resolve(process.argv[1]!));
  if (entry.startsWith("..") || isAbsolute(entry)) throw new Error("Launcher must be inside the packaged scripts directory");
  const args = process.argv.slice(2).filter((arg) => arg !== "--setup-dependencies");
  const child = Bun.spawnSync([process.execPath, "--no-install", join(runtime, entry), ...args], {
    cwd: process.cwd(), env: process.env, stdin: "inherit", stdout: "inherit", stderr: "inherit",
  });
  process.exit(child.exitCode ?? 1);
}
