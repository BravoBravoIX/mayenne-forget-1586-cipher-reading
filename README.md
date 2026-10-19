# The Mayenne–Forget cipher letter of autumn 1586 (BnF fr. 15573 f. 385): a first reading of the whole letter

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23470961.svg)](https://doi.org/10.5281/zenodo.23470961)

**BnF, Français 15573, f. 385r–v.** A letter of autumn 1586 written wholly in cipher, two pages, from the royal army in Guyenne. It uses the cipher that Satoshi Tomokiyo calls **Mayenne–Forget's Cipher-2**, the cipher of Charles de Lorraine, Duke of Mayenne, and of Forget de Fresnes, in their letters to King Henri III and to Villeroy.

> **First reading of the whole letter, version 0.2 (19 October 2026), partial in places. Version 0.1 was prepared the same day; 0.2 adds code signs learnt from other letters in this cipher deciphered at the time.**
>
> **Satoshi Tomokiyo published a fragment of the opening lines earlier**, on his page of Henri III's ciphers, and credits George Lasry with finding that this letter uses Cipher-2: <https://cryptiana.web.fc2.com/code/henryiii.htm>. His fragment reads "demain ou apresdemain et ratrape … Mons. d'Halincourt jusques … sinon qu'il le laissera advancer d'une journ… qu'il ne reste pas mil ho m es de pied qui diminue …". **Our reading of the opening agrees with it** (*… partira demain ou apres … ratrapera monsieur d'Halincourt iusques … sinon qu'il le laissera aduancer d'une iournée … de sorte qu'il ne reste pas [mil] ho[m]mes de pied qui diminuent …*), and it was made without using his text.
>
> Beyond that fragment, as far as our search found (see [PRIOR-ART.md](PRIOR-ART.md)), no reading of this letter has been published. Updates will follow.

## What changed since version 0.1

Five other letters in this cipher in the same volume carry a decipherment of the time. Read and aligned with it, they give values for code signs that version 0.1 left open: `Qh` = *armée*; `hb` = *tout*; `N` = *ée*; `17` = *tant*; `13` = *tre* (doubtful); `ub` = *droit* (doubtful). Two of these are signs the reader had folded into one name, told apart on the image (`hb`, an h with one bar, read before as `Qh`; `ub`, two uprights on a base, read before as `invT`). Every value carries its origin in [data/key-cipher2.json](data/key-cipher2.json); the alignments are in [method/other-letters.md](method/other-letters.md).

| page | share read as French, v0.1 | v0.2 |
|---|---|---|
| f. 385r | 0.912 | 0.921 |
| f. 385v | 0.923 | 0.929 |

Code signs without a value: 28 items in v0.1, 12 now. Newly read, for example: "ceste armée est desbandée", "d'une journée", "tous les jours", "ceste armée durant cest hyver", "que deviendront tant de regiments", "demeurer une armée en ceste province", "ce sera tousjours une despence de cent mil". Stretches not yet read: 34 in v0.1, 36 now (some code signs now give letters the dictionary cannot place).

## What the letter is about

The evidence weighs toward this reading of the readable stretches. The royal army in Guyenne is breaking up at the start of the winter of 1586: the foot soldiers are dwindling, men ask for leave, and there is a lack of powder. The writer weighs what to do with the regiments and the foreign troops over the winter: to keep them in garrison would be a great expense and almost useless; the landsknechts who were in Champagne might be sent; a company of light horse might be kept. "With a little help he could hold for three months." The letter names Monsieur d'Halincourt and Monsieur de Matignon, La Roche and, probably, the young Aubeterre. The sender's name is not in the cipher text; that it comes from Mayenne's side rests on the cipher and the content. See [reading/f385-english.md](reading/f385-english.md) for an English gist, labelled as such.

## Status of each page

Both pages were read the same way: five reader passes, voted, then image-checked corrections. 68 lines and 2052 signs in all.

| page | Gallica view | lines | signs | all five passes agree | share of signs read as French (reading) | shuffled controls |
|---|---|---|---|---|---|---|
| f. 385r | 752 | 34 | 1054 | 0.8463 | 0.921 | 0.621 / 0.619 / 0.624 |
| f. 385v | 753 | 34 | 998 | 0.8519 | 0.929 | 0.619 / 0.618 / 0.592 |

The known-answer lines (a letter in the same cipher whose decipherment of the time survives, read and decoded the same way) score 0.868. Both pages are above that.

Open: 89 listed items, of which 12 are code signs whose value is not known, 41 are doubtful words (each with its evidence) and **36 are short stretches not yet read** ([reading/unresolved-v0.2.md](reading/unresolved-v0.2.md)).

## What is here

| folder | contents |
|---|---|
| [reading/](reading/) | The French text of each page (Literal = exactly what the key gives; Normalised = the same letters with word breaks made by code), an English gist of the readable stretches, and the list of unresolved stretches |
| [data/](data/) | Per page: the signs as read (`signs.txt`, one manuscript line per row; `reading.json` with the votes for every sign), the key with the value chosen at every occurrence of a two-valued sign (`key.json`), the literal plaintext, corrections and controls. `key-cipher2.json` is the key with the origin of every value; `lexicon-additions.tsv` the words added to the dictionary, each with its source. `known-text/` holds the calibration material |
| [decode/](decode/) | `decode.py`, a short stand-alone script (Python 3 standard library) that applies `key.json` to `signs.txt`, and `check.sh`, which reproduces both pages byte for byte |
| [method/](method/) | How the signs were read (the prompt given to Claude, the reference sheet of signs), the vote, the corrections, the key, the controls and the measurement on known text |
| [PRIOR-ART.md](PRIOR-ART.md) | The prior-art search: what was searched, where, and every query with its result count |
| [NUMBERS.md](NUMBERS.md) | Where every number in this README comes from |

## The pages and the images

The images are on Gallica, BnF Français 15573, ark:/12148/btv1b90618780 (Source gallica.bnf.fr / BnF):

- f. 385r, view 752: <https://gallica.bnf.fr/ark:/12148/btv1b90618780/f752.item>
- f. 385v, view 753: <https://gallica.bnf.fr/ark:/12148/btv1b90618780/f753.item>

The calibration letter, in the same cipher and the same volume, is ff. 103v–104r, the Duke of Mayenne to the King from the camp of Libourne, September 1586 (views 212–213: <https://gallica.bnf.fr/ark:/12148/btv1b90618780/f212.item>, <https://gallica.bnf.fr/ark:/12148/btv1b90618780/f213.item>). Its decipherment of the time is written in the left margins and in lines under the cipher.

The page images are not copied here. The reference sheet in `method/` is made of small crops of the calibration letter and of f. 385 (see the image terms below).

## The key

The key is **Satoshi Tomokiyo's reconstruction** of Mayenne–Forget's Cipher-2, published on his page of Henri III's ciphers (<https://cryptiana.web.fc2.com/code/henryiii.htm>). We do not reproduce his key image; please see it on his page. We mapped his drawn signs to our visual names and checked the values against the decipherment of the time of the calibration letter: our reading of ff. 103v–104r was aligned by code with the decipherment, and a few values his table does not give were taken from that alignment. Every value in [data/key-cipher2.json](data/key-cipher2.json) carries its origin: `T` (Tomokiyo's table), `T?` (his table, our mapping of his sign uncertain), `E` (the alignment with the 1586 decipherment), `E-eye` (seen by eye in the calibration letter against its decipherment), `E?` (few places: doubtful), `F` (aligned places in the other letters in this cipher deciphered at the time, see [method/other-letters.md](method/other-letters.md)), `F?` (one place or a weak alignment: doubtful).

- Most signs stand for one letter; several signs share a letter (homophones).
- Some signs stand for a group of letters or a short word: for example *de*, *la*, *que*, *qui*, *est*, *et*, *pour*, *plus*, *monsieur*, and figures such as 23 = *apres*, 24 = *peu*, 31 = *pas*.
- Four signs stand for more than one value at our level of naming: `L` (a or n), `f` (i or s), `xbar` (s or ss), `rC` (s or z). For these, a word-level decoder with a period French dictionary chose one value at each place, and every choice is written in `data/<page>/key.json`.
- A slash is a word divider; it carries no letter.
- Some code signs are not identified: `14`, `15`, `30`, `invT`, `x?`. They print as `·` (or `[?name]`). Conjecture from the context (not in the key): `invT` = *vostre majesté* ("despesche devers [invT]", "ce que [invT] eust peu trouver mauvais", "supplyer [invT] de luy donner congé").

## The method in plain words

1. **A letter with a known answer.** ff. 103v–104r are in the same cipher, from the same camp, in the same volume, and their decipherment made at the time survives. We read that decipherment by eye.
2. **A reference sheet.** From the calibration pages and the target pages we cut a sheet of 74 sign shapes, named by their look only (the names say nothing about meaning). No example comes from the held-out lines.
3. **Claude reads the signs.** Each line was cut into pieces, and the pieces were shown to Claude (Anthropic, model Opus 5.5) under the reference sheet, with the instruction to name every sign from left to right. This was done five times with different cuts and magnifications.
4. **Vote.** The five readings of each line were aligned and the majority name taken at each place.
5. **Corrections, only where the image supports them.** On every unresolved stretch, two separate blind asks (never told values or words) chose among candidate names; where both agreed on a change, it was looked at on the image and applied only if the image shows that sign. 16 were applied, 12 rejected, and 13 further places were decided on the image (signs of Tomokiyo's table that the sheet lacked). The page decoder may also take another pass's name at a position, at a fixed cost; each such switch is listed.
6. **Key applied mechanically.** The key turns each sign into its value; for the two-valued signs the choice made by the word decoder is recorded. From then on the decode is a lookup that anyone can repeat with `decode/decode.py`.
7. **Word breaks by code** from a period French dictionary, for the Normalised text only. No letter is changed.
8. **Controls.** Every page was also decoded with its signs shuffled into a random order, in exactly the same way. The last fifth of each page was also decoded on its own. The known-answer lines were decoded the same way as a yardstick.
9. **Code signs from other letters (version 0.2).** Five other letters in this cipher in the same volume carry a decipherment of the time (ff. 7v–8r, 32r–33r, 97r, 149r–150r). Their cipher was read with one reader pass and decoded with the key unchanged (it reads them as French); every place of a sign without a value was looked at on the image and aligned by eye with the decipherment. Two signs the reader had folded into one name were told apart on the image and given new names (`hb`, `ub`). See [method/other-letters.md](method/other-letters.md).

Details are in [method/README.md](method/README.md).

## Measured numbers

**Reader calibrated on known text.** The reader was measured on f. 104r, cipher lines 18–24 (168 signs), held out from everything else. Nothing in the sheet or the key was tuned on these lines. The reference signs were read by eye and checked by decoding against the decipherment of the time.

| reader | sign accuracy (either name accepted where the eye cannot choose) |
|---|---|
| pass a / b / c | 0.9167 / 0.9345 / 0.9107 |
| **vote of the three passes** | **0.929** (0.917 strict, counting only the first accepted name) |

So the vote reads about **0.929 per sign** on known text: roughly one sign in fourteen is wrong. On the target pages five passes were voted; all five agree on 0.8463–0.8519 of positions.

**Share of signs read as French** (signs inside decoded dictionary words of three letters or more, or a listed short word), and bits per letter under a period French 5-gram model (lower = more like French):

| page | signs | share, reading | share, without the 6 target-prompted words | share, shuffled seeds 1 / 2 / 3 | share, held-out last fifth | bits/letter, reading | bits/letter, shuffled 1 / 2 / 3 |
|---|---|---|---|---|---|---|---|
| f. 385r | 1054 | **0.921** | 0.909 | 0.621 / 0.619 / 0.624 | 0.933 | 3.236 | 5.346 / 5.241 / 5.279 |
| f. 385v | 998 | **0.929** | 0.926 | 0.619 / 0.618 / 0.592 | 0.894 | 3.173 | 5.406 / 5.532 / 5.528 |

The readings sit at 0.921–0.929; the shuffled controls at 0.592–0.624. The last fifth of each page, decoded on its own, reads like the rest. The known-answer yardstick (f. 104r lines 18–24, three passes voted, no corrections, the same decoder) scores 0.868 (0.879 with the words only its own decipherment contributes). Caution: the measure counts any dictionary word, so some chopped sequences count as sense; the yardstick and the controls are measured the same way.

## What is unresolved

- **Code signs not identified**: `14`, `15`, `30`, `invT`, `x?`. Context conjectures for `Qh` (*armée*) and `invT` (*vostre majesté*) are not in the key.
- **Doubtful words**: abbreviations the decipherers of the time wrote out (*p[rése]nt*, *m[oye]n*, *d[eu]x*, *c[eu]x*), names, and period spellings. Each is listed with its evidence.
- **Short stretches not yet read**: misread signs, mostly. Stretches that match no dictionary word are shown in [brackets] in the Normalised text.
- **No palaeographer has checked it.** The English gist is Claude's, from our Normalised French; it is not literal plaintext.

This is version 0.2. **Updates will follow**: a second image-checked correction round on the stretches not yet read, and more passes over the other deciphered letters for the doubtful values.

## Prior art

Searched on 19 October 2026 before the work began (01:35–01:47 UTC), and repeated the same day before this write-up (04:01–04:10 UTC): GitHub (code, repositories, issues; commits, pull requests and issues of the active cipher-reading repositories), Tomokiyo's pages and blog, Lasry's survey of BnF ciphers, the Bourdeau catalogue, Cryptoole and the web. **No reading of f. 385 was found** beyond Tomokiyo's fragment of the opening lines. Every query and its result count is in [PRIOR-ART.md](PRIOR-ART.md).

## How to reproduce the decode

Needs only Python 3 (no packages):

```
sh decode/check.sh
```

Expected output:

```
f385r stream: identical to data/f385r/plaintext.txt (1404 bytes)
f385r by-line: identical to data/f385r/plaintext-by-line.txt (1544 bytes)
f385v stream: identical to data/f385v/plaintext.txt (1253 bytes)
f385v by-line: identical to data/f385v/plaintext-by-line.txt (1407 bytes)
all pages reproduced exactly
```

`plaintext.txt` and `plaintext-by-line.txt` were written by our own tools when the reading was made, so the check is a test of `decode.py` against an independent implementation. To read one page line by line: `python3 decode/decode.py data/f385r/key.json data/f385r/signs.txt --by-line`.

The measurement on known text can be recomputed with `python3 method/score_heldout.py`:

```
pass_a  154 / 168 reference signs read right -> sign accuracy 0.9167
pass_b  157 / 168 reference signs read right -> sign accuracy 0.9345
pass_c  153 / 168 reference signs read right -> sign accuracy 0.9107
vote    156 / 168 reference signs read right -> sign accuracy 0.9286
```

What cannot be repeated from this repository alone: Claude's sign readings themselves (they are recorded here, not re-run), and the dictionary and language model used for the value choice, word breaks, share read as French and bits per letter (built from our own period corpora; the additions are listed in `data/lexicon-additions.tsv`).

## Credits

- **Satoshi Tomokiyo**, for the reconstruction of Mayenne–Forget's Cipher-2, the catalogue of these letters, and the first published fragment of this letter (<https://cryptiana.web.fc2.com/code/henryiii.htm>).
- **George Lasry**, credited by Tomokiyo with finding that this letter uses Cipher-2 and with the opening fragment.
- **Bibliothèque nationale de France / Gallica**, for the manuscript images. Source gallica.bnf.fr / BnF.
- **Anthropic's Claude** (model Opus 5.5) was used as the sign reader, for the blind correction asks, for reading the calibration decipherment and the reference lines by eye, and for the English gist.

Prepared by Brett Burford, October 2026.

## Licence

- Text and data (everything except `decode/`, `method/score_heldout.py` and the image noted below): [Creative Commons Attribution 4.0 International](LICENSE) (CC BY 4.0).
- `decode/` and `method/score_heldout.py`: [MIT licence](decode/LICENSE).
- The image in `method/` (`sheet-v3.png`) is made of crops of BnF, Français 15573 (ff. 103v–104r and f. 385), from Gallica. It is not covered by CC BY: Gallica's terms allow free non-commercial reuse with the source line "Source gallica.bnf.fr / BnF"; commercial reuse needs the BnF's permission.

## How to cite

Burford, B. (2026). BnF fr. 15573 f. 385 (Mayenne-Forget Cipher-2, 1586): a first reading of the whole letter. Zenodo. https://doi.org/10.5281/zenodo.23470961 (this DOI always points to the latest version; each release has its own version DOI on Zenodo).
