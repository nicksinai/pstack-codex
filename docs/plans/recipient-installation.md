# Recipient installation observation

October 12, 2026. Followed the public GitHub marketplace route using codex-cli 0.133.0. Marketplace registration succeeded; portable-root-only version 0.1.0 failed installation with `missing plugin.json`. Version 0.1.1 adds the officially supported `.codex-plugin/plugin.json` compatibility manifest while retaining the portable manifest and preserving its identity, version and description. The compatibility manifest explicitly declares `./skills/`.

Installed 0.1.1 from the public fix branch using `codex plugin add pstack-codex@pstack-codex-marketplace`. The CLI reported `installed, enabled`, and all 219 cached package files matched the fetched public source byte-for-byte. Existing configuration entries were compared with a pre-install backup and preserved. Deterministic source/package qualification and archive assembly passed.

This machine's older standalone CLI cannot parse the desktop's nested `features.context_management` setting. The command-only override `-c features.context_management=false` allowed marketplace/install commands to execute without changing the persisted feature setting. Recipients should only use this workaround for that exact configuration error; it is not a package requirement.

Computer Use blocks access to the Codex desktop app. Desktop skill-picker visibility therefore still needs human observation after reload/restart; CLI installation is not reported as observed desktop activation. Model-role setup needs the recipient's confirmed location and budget. No PStack helper dependencies or personal role choices were installed as part of package installation.
