# How the signs were read and measured

This folder explains how the readings in `../data/` were made, and how far they can be trusted. The full working code is not published here: it depends on our own tools and language resources. What is here is enough to see what was done, to recompute the measured numbers on the known text, and to reproduce the decode exactly (`../decode/`).

## The cipher

Mayenne–Forget's Cipher-2, as reconstructed by Satoshi Tomokiyo (<https://cryptiana.web.fc2.com/code/henryiii.htm>): a substitution of letters, figures and invented shapes, with homophones, signs for groups of letters and short words, figures for common words, and code signs for names and titles. A slash divides words. Code words are often written between dots.

## Step 1: a letter with a known answer

BnF fr. 15573 ff. 103v–104r (Mayenne to the King, camp of Libourne, September 1586) is wholly in the same cipher; its decipherment made at the time is written in the left margins and in full-width lines under each cipher block. Claude read the decipherment from the image ([../data/known-text/](../data/known-text/)). No modern reading of these leaves was used.

## Step 2: the reference sheet and the key check

The signs of the calibration and target pages were cut out by code (deskew, line tracking, connected components), grouped by shape (k-means), and the groups named by Claude from the images. The reference sheet [sheet-v3.png](sheet-v3.png) has 74 visual names ([sheet-v3.json](sheet-v3.json)). No example comes from the held-out lines (f. 104r line 18 onward). The names are labels for shapes only; the reader is never told the values.

A three-pass reading of the calibration letter was aligned by code with the decipherment. Its values agree with Tomokiyo's table; a few values his table does not give were taken from aligned places (origin `E`, `E-eye`, `E?` in `../data/key-cipher2.json`). Three of Tomokiyo's signs that the sheet lacked (a T on its side = *plus*, u, p) were added after a look at his table enlarged.

## Step 3: Claude reads the signs

Each manuscript line was straightened and cut into pieces. The pieces were shown to Claude (model `claude-opus-5-5`, effort low, 12 pieces per call) under the reference sheet, with the instruction to name every sign from left to right. The answers were treated as data only and parsed into sign names. A refused answer is never saved as a reading (no call refused here). Five passes were made over the target with different cuts and magnifications (see `passes` in `../data/<page>/reading.json`).

## Step 4: the vote

The five readings of a line are aligned by edit distance, and the majority name is taken at each place. Every position keeps the names given, most voted first (`../data/<page>/reading.json`).

## Step 5: corrections, only where the image supports them

On every stretch the decoder could not read, two blind asks (the crop shown at 2.0x and at 1.6x, with candidate names; never told values or the word wanted) chose a name. Where both agreed on a change, Claude checked it against the image and applied it only when the image shows that sign: 16 applied, 12 rejected. 13 places were decided on the image where no name on the sheet fits (signs of Tomokiyo's table missing from the sheet). The page decoder may also take another pass's name at any position for a fixed cost of 6 bits; each switch is listed. All of this is in `../data/<page>/corrections.json`.

## Step 6: from signs to letters

The key ([../data/key-cipher2.json](../data/key-cipher2.json)) is applied to the signs. For the two-valued signs, a word-level decoder (a dynamic programme over the whole page with a period French dictionary and the additions in `../data/lexicon-additions.tsv`) chose one of the listed values at each place; it can only choose among the listed values. Every choice is written in `../data/<page>/key.json` under `choices`, so the decode itself is mechanical and anyone can repeat it with [../decode/decode.py](../decode/decode.py).

## Step 7: word breaks (Normalised text)

The Normalised text in `../reading/f385-french.md` adds word breaks by the same word decoder. A stretch that matches no dictionary word is shown in [brackets]. No letter is changed, added or removed; the letters of Normalised equal the letters of Literal on every line.

## Measurement on known text

Held-out cipher lines 18–24 of f. 104r (168 signs) were read sign by sign from the image by Claude as a reference ([../data/known-text/ref-104r-l18-24.txt](../data/known-text/ref-104r-l18-24.txt)) before any reader pass with the final sheet; where the image does not decide, two names are accepted. The reference was checked by decoding it against the decipherment of the time. The three gate passes were cut as follows: a: pieces of about 900 px at 1.2x; b: pieces of about 700 px at 1.4x, first cut at 250 px; c: pieces of about 800 px at 1.3x, first cut at 450 px. Sign accuracy = reference signs read right / reference signs, after an edit-distance alignment per line. [score_heldout.py](score_heldout.py) recomputes it (Python 3, standard library):

```
$ python3 method/score_heldout.py
pass_a  154 / 168 reference signs read right -> sign accuracy 0.9167
pass_b  157 / 168 reference signs read right -> sign accuracy 0.9345
pass_c  153 / 168 reference signs read right -> sign accuracy 0.9107
vote    156 / 168 reference signs read right -> sign accuracy 0.9286
```

Strict scoring (first accepted name only) gives 0.9167 for the vote (`--strict`).

Cautions: the reference was made by Claude, the same model as the reader; its independence is the decode check against the decipherment of the time, not a second reader.

## Controls

A decoder with a dictionary makes almost anything look a little like its language. So each page was also decoded with its signs shuffled into random order (seeds 1, 2, 3), with the same key, dictionary and decoder. The readings sit at 0.921–0.929 of signs read as French, the shuffled controls at 0.592–0.624. The last fifth of each page decoded on its own reads like the rest. The known-answer lines, read and decoded the same way with no corrections, score 0.868. Numbers per page: `../data/<page>/controls.json`.

## Code signs from other letters (version 0.2)

See [other-letters.md](other-letters.md): five other letters in this cipher, deciphered at the time, read with one pass and aligned with their decipherments by Claude; the key values they give carry the origin `F` (or `F?` when doubtful).

## What this does not show

- It is a machine reading, voted; it awaits a palaeographer's reading.
- Several code signs are unidentified, and the choice of value for the two-valued signs is made by a dictionary decoder.
- Words the target itself suggested to the dictionary (6 period spellings) are reported separately; without them the shares change little (`without_target_prompted`).

## Images

`sheet-v3.png`: crops of BnF, Français 15573, ff. 103v–104r and f. 385, from Gallica (ark:/12148/btv1b90618780, views 212, 213, 752, 753). Source gallica.bnf.fr / Bibliothèque nationale de France. Free non-commercial reuse with this source line; commercial reuse needs the BnF's permission. Not under this repository's CC BY licence.
