# Where the numbers come from

Every number in [README.md](README.md) and [method/README.md](method/README.md), and the file in this repository it is taken from. They are written into the README by the script that assembles this repository, from the records made when the work was done (19 October 2026), not typed by hand.

| number | meaning | source in this repository |
|---|---|---|
| 68 lines, 2052 signs; per-page lines and signs | size of the reading | rows and sign names of `data/<page>/signs.txt` |
| 0.8463, 0.8519 | share of positions where all five passes agree, f. 385r, f. 385v | `data/<page>/reading.json` `all_agree_share` |
| 16 applied, 12 rejected, 13 decided on the image | corrections | `data/<page>/corrections.json` `applied`, `rejected`, `decided_on_the_image` |
| 28, 23 | decoder switches, f. 385r, f. 385v | `data/<page>/corrections.json` `decoder_switches` |
| 168 signs | reference signs of f. 104r cipher lines 18–24 | `data/known-text/scores/*.score.json` `ref_signs`; `data/known-text/ref-104r-l18-24.txt` |
| 0.9167 / 0.9345 / 0.9107 | sign accuracy of passes a / b / c | `data/known-text/scores/f104r-pass_a.score.json`, `-pass_b`, `-pass_c` `accuracy`; recomputed by `method/score_heldout.py` |
| 0.929 | sign accuracy of the vote (156 / 168) | `data/known-text/scores/f104r-vote.score.json` `accuracy`; recomputed by `method/score_heldout.py` |
| 0.917 | the same, strict (first accepted name only) | `data/known-text/scores/f104r-vote.strict.score.json`; `method/score_heldout.py --strict` |
| share read as French, bits per letter, shuffled seeds 1–3, held-out last fifth, without target-prompted words | controls per page | `data/<page>/controls.json` `reading`, `shuffled_seed1`–`3`, `held_out_last_fifth`, `without_target_prompted` |
| 0.868 (0.879) | known-answer yardstick, f. 104r lines 18–24, without (with) the words only its own decipherment contributes | our stage C record (not in this repository) |
| 6 | lexicon additions the target prompted | `data/lexicon-additions.tsv`, source `period-target-prompted` |
| 89 items: 12 code signs, 41 doubtful words, 36 unread | open items | [reading/unresolved-v0.2.md](reading/unresolved-v0.2.md) |
| 74 sign shapes | reference sheet | `method/sheet-v3.json` `names` |
| piece widths and enlargements of the passes | reader passes | `data/<page>/reading.json` `passes`; for the known text, method/README.md |
| byte counts in the check output | sizes of `data/<page>/plaintext.txt` and `plaintext-by-line.txt` | `sh decode/check.sh` |
| Gallica views 752–753, 212–213 | image locations | our fetch records; the links in the README |
| 19 October 2026 times (UTC) | dates of the prior-art searches | [PRIOR-ART.md](PRIOR-ART.md) |
| version 0.1 shares and counts | the comparison in "What changed since version 0.1" | `data/<page>/controls.json` and `reading/unresolved-v0.1.md` of the version 0.1 commit |
| aligned places of the stage F values | origins of the new key values | [method/other-letters.md](method/other-letters.md); `data/key-cipher2.json` `origin` |
