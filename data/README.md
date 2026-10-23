# Data

Per page (`f385r` = f. 385 recto, `f385v` = f. 385 verso):

| file | contents |
|---|---|
| `signs.txt` | the sign names as read, one manuscript line per row: line number, a tab, the signs separated by spaces. Names are visual names from the reference sheet (`../method/sheet-v3.png`); `x?` = a sign on no row of the sheet; numbers are written as numbers; `/` is a word divider (no letter, not counted as a sign) |
| `key.json` | the key as a table (`pipeline[0].table`: each name's value, `type`, confidence and origin), and under `pipeline[0].choices` the value taken at every occurrence of the two-valued signs `L`, `f`, `xbar` and `rC`, in reading order |
| `plaintext.txt` | the literal plaintext as one stream (signs without a value as `[?name]`), as written by our tool when the reading was made |
| `plaintext-by-line.txt` | the same, one manuscript line per row (signs without a value as `·`), as written by our word decoder |
| `reading.json` | per position: the names given by the five reader passes, most voted first (after image-checked corrections); the passes |
| `corrections.json` | the rule for corrections; the changes applied, decided on the image, and rejected (line from 1, 0-based position in `reading.json`); the decoder's switches to another pass's name |
| `controls.json` | the page decoded as read, with its signs shuffled (seeds 1-3), its last fifth on its own, and without the target-prompted words: share read as French and bits per letter |

`key-cipher2.json`: the key with the origin of every value (`T` Tomokiyo's table, `T?` our mapping of his sign uncertain, `E` alignment with the 1586 decipherment, `E-eye` seen on the image by Claude, `E?` doubtful).

`lexicon-additions.tsv`: words added to the period French dictionary for this letter, each with its source (`dec103v`/`dec104r` = the calibration decipherment; `m1586-*` = names, places and period words of the 1586 Guyenne campaign; `period-target-prompted` = period spellings added after the target suggested them, reported separately). They apply to the controls and the yardstick too.

`known-text/`: the calibration material. `f103v-decipherment.txt`, `f104r-decipherment.txt` are readings of the decipherment made at the time (fr. 15573 ff. 103v–104r), read from the image by Claude; `ref-104r-l18-24.txt` the reference signs of the held-out lines; `stageB/` the three passes and the vote on f. 104r lines 18–24; `scores/` the recorded scores.
