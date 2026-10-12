# Final review fixes

Reviewed candidate: `1525016` on the integration branch. The specification review found no actionable deviations or scope creep. The standards review identified one required correction: the committed adaptation diff still represented the foundation slice rather than the completed source mapping.

Regenerated `provenance/adaptations.patch` from `scripts/adaptation-diff.py` (6,136 lines). `scripts/validate-provenance.py` now invokes that generator with its own Python interpreter and requires exact byte equality with the committed artifact. The generator reads the immutable baseline, ownership mapping, and mapped targets; it neither reads this artifact nor invokes the validator, so the check is not circular.

Direct deterministic checks established that changing the artifact alone fails qualification and changing a mapped adapted target without regenerating the artifact also fails qualification. Both temporary changes were restored. Full qualification then passed: 164 source items with original hashes, 13 agreed deferrals, 51 skills, 24 principles, 23 playbook targets, two wrappers, 5,951 catalog characters, and the 218-file package allowlist. No packaged file or baseline file changed in this correction.

`git diff --check` passes for authored changes when the generated patch is excluded. Its whitespace warnings on the generated patch reflect literal unified-diff context lines and preserved source whitespace; normalizing them would break the exact source-derived artifact. This is structural/source evidence, not recipient installation or observed workflow execution. The root README now identifies the result as an implemented candidate pending human review and recipient installation.
