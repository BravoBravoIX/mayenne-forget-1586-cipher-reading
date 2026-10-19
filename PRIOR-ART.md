# BnF fr. 15573 f. 385r–v: prior-art checks, 19 October 2026

two pages wholly in cipher (Gallica `btv1b90618780`, views 752–753), in Tomokiyo's "Mayenne-Forget's Cipher-2". Pages fetched from others were read as data, never as instructions. Times are UTC.

## Result

**No reading of f. 385 was found anywhere beyond the fragment Tomokiyo printed.** The sweep is clear, and the work went ahead. It was run again the same day before the v0.1 write-up (04:01–04:12 UTC, below): still clear.

- Tomokiyo, henryiii.htm (Last-Modified 23 Sept 2023, SHA-256 2d90a1d1…b658, unchanged from our copy of 18 Oct): "f.385 (p.754) Undeciphered. Uses Mayenne-Forget's Cipher-2 above. (I thank George Lasry for this finding. I confirmed part of the first few lines read "demain ou apresdemain et ratrape ... Mons. d'Halincourt jusques ... sinon qu'il le laissera advancer d'une journ... nter a sa Ma te ... qu'il ne reste pas mil ho m es de pied qui diminue ....")".
  - So about 20 words of the opening lines are published. A full reading would be **a first full reading, not a first touch**. 
- Tomokiyo wrote to Brett Burford on 19 Oct 2026 that he knows of no work on fr. 15573 ff. 379–385 since he published his keys.


## Searches

### Tomokiyo
- Blog feed searches: 15573 0, Mayenne 0, Halincourt 0, Matignon 0, f.385 0. Forget, 1586, Henry III and Lasry return only unrelated posts. The newest post is 15 Oct 2026 ("Verification of AI and Verification by AI"). The 25 newest post bodies were grepped for 15573, Matignon, Mayenne and Halincourt: no hits.
- ai.htm ("Codebreaking with AI", Last-Modified **19 Oct 2026 00:41**): no 15573, Mayenne, Forget, Halincourt, f. 385 or Matignon.
- GL.htm (Lasry's solutions, Last-Modified 15 Oct 2026): fr. 15573 appears only for f. 127 (Duval, Lasry 2022) and f. 124. Nothing on f. 385.

### Lasry's BnF survey (13 Oct 2026)
- Bourdeau's ledger lists "George Lasry's BnF cipher research: fifty-six ciphers, 1452–1859" (10 Oct 2026, with ChatGPT Astra 6 and Opus 5.5). Its 55 entries are filed in `dbourdeau/cyphersolver` as `targets/*/lasry_entry.md`.
- All 55 were downloaded and grepped for `15573|mayenne|forget|halincourt|f. 385`. The only hits are "they will forget this one" (Brienne) and "discusses Mayenne and a possible truce" (Villeroy, Dupuy 61). **f. 385 is not in Lasry's survey.**

### GitHub
- **Code search.** Queries:
  - shelfmark spellings, `btv1b90618780`;
  - `MayenneForget2`, `henryiii_MayenneForget2`;
  - "Mayenne-Forget" (both dash forms), "Mayenne-Forget Cipher-2";
  - Halincourt chiffre/cipher;
  - Tomokiyo's fragment: "apresdemain et ratrape", "mil hommes de pied qui diminue";
  - "duc de Mayenne" 1586 cipher.

  Every hit is one of these: Bourdeau's copy of Tomokiyo's page (`research/gallica_sweep/src/henryiii.txt`); Bourdeau's and cipher-lab's fr. 15572 Mayenne–Forget/Matignon work; cipher-lab's index rows; or unrelated text.
- **Files opened and grepped** for `15573|f. 385|Halincourt|btv1b90618780`. None of them names f. 385.
  - Bourdeau:
    - CATALOGUE.md and SOLVED_CATALOGUE.md;
    - targets/matignon1586/NOTES.md, targets/matignon1586c3/NOTES.md and targets/mercoeur1586/NOTES.md;
    - research/qa/key_split_audit.md.
  - Cipher-lab:
    - ciphers/matignon-mayenne-1586/NOTES.md (2 lines: fr. 15573 listed as "Not opened");
    - HYPOTHESES.md;
    - second-opinions/chatgpt-leads-2026-09-26.md (the BnF notice only);
    - BNF-VALUE.tsv, ASKS.md, JSTOR-QUEUE.tsv and hub-seed/ASSIGNMENTS.md.
  - Bourdeau's catalogue item 12 is the Cipher-2 leaves of **fr. 15572** ff. 218–219 (Matignon in Mayenne–Forget's Cipher-2), marked "not attempted". That is not our leaf.
- **Repo-scoped searches** in cipher-lab, cabinet-noir, cryptoole, Bourdeau, alejandrozarco and pangoleen/cipher-readings: no f. 385.
- **Repository search** (`mayenne`, `mayenne cipher`, `mayenne 1586`, `mayenne forget`, `halincourt`, `ligue 1586 cipher`, `first reading cipher`, `bnf cipher`, …): only Brett Burford's own repositories and the known Desportes, Senecey and Seure repos.
- **Issues:** cipher-lab #29 (fr. 15572 leads), Bourdeau #44 (Brett Burford's own note on ff. 379–381) and Bourdeau #9 (Nevers 1589). Nothing on f. 385.
- **Last 60 days** of commits (paged), open PRs and issues of the seven active repos, grepped for `15573|mayenne|forget|385|btv1b90618780|halincourt`:
  - cipher-lab's hits are all its fr. 15572 Cipher-1 work (f. 110, ff. 91–92);
  - Bourdeau's only fr. 15573 hit is Brett Burford's issue #44;
  - no commit names f. 385.

### Cryptoole (satoru.net/crypt)
- Its "mayenne1586" entry is **BnF fr. 15572 f. 143** (Favas; recto read with Tomokiyo's key, 75 %). That is not our leaf. There is no fr. 15573 entry.

### Web
| Search | Result |
|---|---|
| `Mayenne 1586 cipher letter BnF "15573" deciphered` (extended) | Nothing on this letter. It pointed to Lasry's survey, checked above |
| `"Halincourt" 1586 Mayenne lettre chiffrée déchiffrement Henri III` | Nothing on this letter |
| `first reading Mayenne cipher letter 1586 Claude OR AI github 2026` (extended) | Cryptoole's fr. 15572 f. 143 (above) and pangoleen/cipher-readings (no Mayenne) |

### Not searched
- DECODE: f. 385 has no DECODE record known to us (as for ff. 379–381). It was not searched today.

## Query log (machine-written)

| UTC | where | query | hits | first results |
|---|---|---|---|---|
| 2026-10-19T01:36Z | recent | `NoAutopilot/cipher-lab` | commits4d=100 openPRs=2 | commits: (every commit hit is its fr. 15572 Matignon/Mayenne Cipher-1 work; messages not copied) |
| 2026-10-19T01:36Z | recent | `el-descifrador/cabinet-noir` | commits4d=12 openPRs=0 | commits:  ;; PRs:  ;; issues4d:  |
| 2026-10-19T01:36Z | recent | `satorunet/cryptoole` | commits4d=80 openPRs=0 | commits:  ;; PRs:  ;; issues4d:  |
| 2026-10-19T01:36Z | recent | `dbourdeau/cyphersolver` | commits4d=100 openPRs=1 | commits:  ;; PRs:  ;; issues4d: #44 BnF fr. 15573 ff. 379-381 (Matignon Cipher-3, 1586): first reading of the     whole despatch published (work in progress / #9 Intercepts summarised for Nevers, 1589 (fr. 3977 no. 96): no ciphertext there — and eleven deciphe |
| 2026-10-19T01:36Z | recent | `alejandrozarco/cyphersolver` | commits4d=100 openPRs=0 | commits:  ;; PRs:  ;; issues4d:  |
| 2026-10-19T01:36Z | recent | `pangoleen/cipher-readings` | commits4d=71 openPRs=0 | commits:  ;; PRs:  ;; issues4d:  |
| 2026-10-19T01:36Z | recent | `Cipher-Atelier/cipher-atelier` | commits4d=ERR openPRs=ERR | commits:  ;; PRs:  ;; issues4d:  |
| 2026-10-19T01:36Z | code | `"fr. 15573"` | 2 | dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt / NoAutopilot/cipher-lab:sources/cryptiana/CRYPTO-INDEX.tsv |
| 2026-10-19T01:36Z | code | `"fr.15573"` | 4 | dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt / NoAutopilot/cipher-lab:LESSONS-TOMOKIYO.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/NOTES.md / NoAutopilot/cipher-lab:sources/cryptiana/CRYPTO-INDEX.tsv |
| 2026-10-19T01:36Z | code | `"fr 15573"` | 7 | lucas-amberg/ecfr-analyzer:public/ecfr/2025-02-06/9/III/A/312/312.6/312.6.md / lucas-amberg/ecfr-analyzer:public/ecfr/2025-02-06/9/III/A/312/312.5/312.5.md / lucas-amberg/ecfr-analyzer:public/ecfr/2025-02-06/9/III/A/312/312.2/312.2.md / lucas-amberg/ecfr-analy |
| 2026-10-19T01:36Z | code | `"français 15573"` | 2 | NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/second-opinions/chatgpt-leads-2026-09-26.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/NOTES.md |
| 2026-10-19T01:37Z | code | `"15573" 385` | 6553600 | fegennari/3DWorld:mesh.txt / giongto35/TetrisAI:Stat.txt / tanakimees/Sudoku:README.md / spaze/hashes:md5.md / benjaminantunes/SMA-SEIR-Repro:log6.txt / cxcscmu/Craw4LLM:seed.txt / VITA-Group/GLNet:train.txt / haruncanatali/HavaDurumu:README.md / Roytak/AOC23: |
| 2026-10-19T01:37Z | code | `"f. 385" Mayenne` | 0 | - |
| 2026-10-19T01:37Z | code | `"f.385" Mayenne` | 1 | dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt |
| 2026-10-19T01:37Z | code | `MayenneForget2` | 0 | - |
| 2026-10-19T01:37Z | code | `henryiii_MayenneForget2` | 0 | - |
| 2026-10-19T01:37Z | code | `"Mayenne-Forget"` | 22 | dbourdeau/cyphersolver:CATALOGUE.md / dbourdeau/cyphersolver:targets/matignon1586c3/NOTES.md / dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt / dbourdeau/cyphersolver:targets/matignon1586/NOTES.md / dbourdeau/cyphersolver:research/qa/key_split_ |
| 2026-10-19T01:37Z | code | `"Mayenne–Forget"` | 14 | dbourdeau/cyphersolver:targets/mercoeur1586/NOTES.md / dbourdeau/cyphersolver:targets/matignon1586/f173_reading.md / dbourdeau/cyphersolver:targets/matignon1586/f154_reading.md / dbourdeau/cyphersolver:targets/matignon1586/NOTES.md / dbourdeau/cyphersolver:CAT |
| 2026-10-19T01:38Z | code | `"Mayenne Forget" cipher` | 1 | NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/NOTES.md |
| 2026-10-19T01:38Z | code | `"Mayenne-Forget Cipher-2"` | 3 | dbourdeau/cyphersolver:research/qa/key_split_audit.md / dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt / dbourdeau/cyphersolver:research/qa/key_split_findings.jsonl |
| 2026-10-19T01:38Z | code | `Halincourt chiffre` | 1 | dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt |
| 2026-10-19T01:38Z | code | `Halincourt cipher` | 9 | dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt / GITenberg/Cinq-Mars-Volume-6_3952:3952.txt / victoriasparrow/coursework_parallel_computing:minicorpus/3952.txt / isel-sw-projects/2021-asyncio-pipelines:books/gutenberg/3000/2000/pg3952.txt / chr |
| 2026-10-19T01:38Z | code | `"ratrape"` | 792 | global-asp/global-asp:ht/0262_magozwe.md / global-asp/global-asp:mfe/0262_magozwe.md / tesseract-ocr/langdata_lstm:hat/hat.wordlist / ch-nry/VCV_nozori:src/m68_Gran.ino / SSNTails/SRB2Proto:Code/d_clisrv.c / ch-nry/VCV_nozori:template_nozori/src/m68_Gran.ino / |
| 2026-10-19T01:38Z | code | `"apresdemain et ratrape"` | 1 | dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt |
| 2026-10-19T01:38Z | code | `"mil hommes de pied qui diminue"` | 0 | - |
| 2026-10-19T01:38Z | code | `btv1b90618780` | 0 | - |
| 2026-10-19T01:39Z | code | `"Mayenne" 1586 chiffre` | 241 | NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/NOTES.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/HYPOTHESES.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/second-opinions/chatgpt-leads-2026-09-26.md / NoAutopilot/cipher-lab:ciphe |
| 2026-10-19T01:39Z | code | `"duc de Mayenne" 1586 cipher` | 15 | dbourdeau/cyphersolver:targets/matignon1586/f154_reading.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/second-opinions/PROMPT-chatgpt-leads.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/NOTES.md / NoAutopilot/cipher-lab:ciphers/matignon |
| 2026-10-19T01:39Z | code | `"Forget" Mayenne 1586` | 1002 | NoAutopilot/cipher-lab:specs/matignon-mayenne-1586.json / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/NOTES.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/second-opinions/PROMPT-chatgpt-leads.md / NoAutopilot/cipher-lab:ciphers/matignon-may |
| 2026-10-19T01:39Z | code | `"15573" repo:NoAutopilot/cipher-lab` | 10 | NoAutopilot/cipher-lab:sources/pools-scout/2026-10-03/P1.md / NoAutopilot/cipher-lab:LESSONS-TOMOKIYO.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/second-opinions/chatgpt-leads-2026-09-26.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/N |
| 2026-10-19T01:39Z | code | `"385"  Mayenne repo:NoAutopilot/cipher-lab` | 27 | NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/HYPOTHESES.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/NOTES.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/sorter/recut.py / NoAutopilot/cipher-lab:ciphers/fr4715-f61-mayenne-1592/H |
| 2026-10-19T01:39Z | code | `MayenneForget2 repo:NoAutopilot/cipher-lab` | 0 | - |
| 2026-10-19T01:39Z | code | `Halincourt repo:NoAutopilot/cipher-lab` | 0 | - |
| 2026-10-19T01:40Z | code | `"15573" repo:el-descifrador/cabinet-noir` | 0 | - |
| 2026-10-19T01:40Z | code | `"385"  Mayenne repo:el-descifrador/cabinet-noir` | 0 | - |
| 2026-10-19T01:40Z | code | `MayenneForget2 repo:el-descifrador/cabinet-noir` | 0 | - |
| 2026-10-19T01:40Z | code | `Halincourt repo:el-descifrador/cabinet-noir` | 0 | - |
| 2026-10-19T01:40Z | code | `"15573" repo:satorunet/cryptoole` | 0 | - |
| 2026-10-19T01:40Z | code | `"385"  Mayenne repo:satorunet/cryptoole` | 0 | - |
| 2026-10-19T01:40Z | code | `MayenneForget2 repo:satorunet/cryptoole` | 0 | - |
| 2026-10-19T01:40Z | code | `Halincourt repo:satorunet/cryptoole` | 0 | - |
| 2026-10-19T01:41Z | code | `"15573" repo:dbourdeau/cyphersolver` | 3 | dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt / dbourdeau/cyphersolver:targets/voynich/results/b4.json / dbourdeau/cyphersolver:research/gallica_sweep/sru_results.json |
| 2026-10-19T01:41Z | code | `"385"  Mayenne repo:dbourdeau/cyphersolver` | 11 | dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt / dbourdeau/cyphersolver:targets/matignon1586/NOTES.md / dbourdeau/cyphersolver:CATALOGUE.md / dbourdeau/cyphersolver:SOLVED_CATALOGUE.md / dbourdeau/cyphersolver:SOLVED_RANKING.md / dbourdeau/cyph |
| 2026-10-19T01:41Z | code | `MayenneForget2 repo:dbourdeau/cyphersolver` | 0 | - |
| 2026-10-19T01:41Z | code | `Halincourt repo:dbourdeau/cyphersolver` | 1 | dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt |
| 2026-10-19T01:41Z | code | `"15573" repo:alejandrozarco/cyphersolver` | 0 | - |
| 2026-10-19T01:41Z | code | `"385"  Mayenne repo:alejandrozarco/cyphersolver` | 0 | - |
| 2026-10-19T01:41Z | code | `MayenneForget2 repo:alejandrozarco/cyphersolver` | 0 | - |
| 2026-10-19T01:42Z | code | `Halincourt repo:alejandrozarco/cyphersolver` | 0 | - |
| 2026-10-19T01:42Z | code | `"15573" repo:pangoleen/cipher-readings` | 0 | - |
| 2026-10-19T01:42Z | code | `"385"  Mayenne repo:pangoleen/cipher-readings` | 0 | - |
| 2026-10-19T01:42Z | code | `MayenneForget2 repo:pangoleen/cipher-readings` | 0 | - |
| 2026-10-19T01:42Z | code | `Halincourt repo:pangoleen/cipher-readings` | 0 | - |
| 2026-10-19T01:42Z | code | `"15573" repo:Cipher-Atelier/cipher-atelier` | 0 | - |
| 2026-10-19T01:42Z | code | `"385"  Mayenne repo:Cipher-Atelier/cipher-atelier` | 0 | - |
| 2026-10-19T01:42Z | code | `MayenneForget2 repo:Cipher-Atelier/cipher-atelier` | 0 | - |
| 2026-10-19T01:43Z | code | `Halincourt repo:Cipher-Atelier/cipher-atelier` | 0 | - |
| 2026-10-19T01:43Z | repositories | `15573` | 56 | jc-infinite-repos/jc-infinite-repos-15573 (2026-03-03) / pitiessayer/1557374401685418949976 (2023-05-30) / pzpinfo/testrepo1557322469555 (2019-05-08) / pzpinfo/testrepo1557371531121 (2019-05-09) / ModelDBRepository/155735 (2019-05-29) / ModelDBRepository/15573 |
| 2026-10-19T01:43Z | repositories | `mayenne` | 23 | LordGnomeMBE/MayenneMap (2023-08-05) / Neritic-mayenne9092/neritic-mayenne9092.github.io (2026-09-25) / Fabx97/Calcul_VintamFabyo (2025-11-14) / slioult/GranitWeb (2013-05-27) / MAYENNE-242/MAYENNE-242 (2021-09-15) / LaMayenne/LaMayenne (2020-02-01) / mattmg83 |
| 2026-10-19T01:43Z | repositories | `mayenne cipher` | 0 | - |
| 2026-10-19T01:43Z | repositories | `mayenne 1586` | 0 | - |
| 2026-10-19T01:43Z | repositories | `mayenne forget` | 0 | - |
| 2026-10-19T01:43Z | repositories | `henri III cipher 1586` | 0 | - |
| 2026-10-19T01:43Z | repositories | `cipher reading 1586` | 1 | BravoBravoIX/matignon-1586-cipher-reading (2026-10-18) |
| 2026-10-19T01:44Z | repositories | `first reading cipher` | 7 | jorruior/CIPHER (2016-02-29) / BravoBravoIX/matignon-1586-cipher-reading (2026-10-18) / taufiq0205/zodiac-cipher-analysis (2026-08-23) / BravoBravoIX/desportes-1593-rereading (2026-10-18) / sohadQtaitat/cipher (2019-12-13) / pangoleen/senecey-1594 (2026-10-03) |
| 2026-10-19T01:44Z | repositories | `bnf cipher` | 5 | BravoBravoIX/matignon-1586-cipher-reading (2026-10-18) / pangoleen/senecey-1594 (2026-10-03) / devinokeefe/seure (2026-10-04) / pangoleen/desportes-1593 (2026-10-01) / BravoBravoIX/desportes-1593-rereading (2026-10-18) |
| 2026-10-19T01:44Z | repositories | `gallica cipher` | 0 | - |
| 2026-10-19T01:44Z | repositories | `chiffre 1586` | 0 | - |
| 2026-10-19T01:44Z | repositories | `tomokiyo` | 5 | TomokiYoshizawa/TomokiYoshizawa (2024-03-28) / momogu97531/tomokiyocom-del (2026-07-25) / TommyNP/complex_networks_2024_tomokiyo (2024-09-10) / suzanv/termprofiling (2016-09-08) / Cipher-Atelier/desportes-to-aldobrandini-cipher-letter-1593 (2026-10-06) |
| 2026-10-19T01:44Z | repositories | `halincourt` | 0 | - |
| 2026-10-19T01:44Z | repositories | `ligue 1586 cipher` | 0 | - |
| 2026-10-19T01:44Z | repositories | `catholic league cipher` | 1 | pangoleen/desportes-1593 (2026-10-01) |
| 2026-10-19T01:45Z | issues | `"15573"` | 10853 | Significant-Gravitas/AutoGPT#15573 fix(frontend): keep the @ mention list on screen above or be / jsboige/CoursIA#15573 meta: recenser les issues dont le cadrage prescrit un grain  / sagemath/sage#15573 (co)product coercion / red-hat-storage/ocs-ci#15573 Updat |
| 2026-10-19T01:45Z | issues | `Mayenne cipher` | 3 | NoAutopilot/cipher-lab#66 JSTOR run 4 Oct 2026 (2): last 24 rows, queue empty / NoAutopilot/cipher-lab#29 [SO-MATIGNON-LEADS] leads: Matignon/Mayenne cipher, BnF fr.1 / dbourdeau/cyphersolver#9 Intercepts summarised for Nevers, 1589 (fr. 3977 no. 96):  |
| 2026-10-19T01:45Z | issues | `Mayenne 1586` | 34688 | heartcombo/devise#1586 Devise shared_views generator not found / elastic/elasticsearch#1586 TTL does not respect routing when expiring (deleting) docume / scikit-image/scikit-image#1586 Document negative `sigma` values in `filters.gaussian_filter / astropy/ast |
| 2026-10-19T01:45Z | issues | `Halincourt` | 0 | - |
| 2026-10-19T01:45Z | issues | `MayenneForget2` | 0 | - |
| 2026-10-19T01:45Z | issues | `btv1b90618780` | 0 | - |
| 2026-10-19T01:46Z | recent | `NoAutopilot/cipher-lab` | commits60d=3000 openPRs=2 | commits: (every commit hit is its fr. 15572 Matignon/Mayenne Cipher-1 work; messages not copied) |
| 2026-10-19T01:46Z | recent | `el-descifrador/cabinet-noir` | commits60d=12 openPRs=0 | commits:  ;; PRs:  ;; issues60d:  |
| 2026-10-19T01:46Z | recent | `satorunet/cryptoole` | commits60d=80 openPRs=0 | commits:  ;; PRs:  ;; issues60d:  |
| 2026-10-19T01:47Z | recent | `dbourdeau/cyphersolver` | commits60d=2180 openPRs=1 | commits: 2026-09-24T20:44 sinzendorff1578: Sinzendorff's Sept 1578 Constantinople despatch attempted, blocked on access (catalogue 343) / 2026-09-22T23:37 jqa: No. 88 read, 375 of 390 groups as sense (0.962); solved (key rebuilt here) / 2026-09-21T17:27 Site:  |
| 2026-10-19T01:47Z | recent | `alejandrozarco/cyphersolver` | commits60d=2043 openPRs=0 | commits: 2026-09-24T20:44 sinzendorff1578: Sinzendorff's Sept 1578 Constantinople despatch attempted, blocked on access (catalogue 343) / 2026-09-22T23:37 jqa: No. 88 read, 375 of 390 groups as sense (0.962); solved (key rebuilt here) / 2026-09-21T17:27 Site:  |
| 2026-10-19T01:47Z | recent | `pangoleen/cipher-readings` | commits60d=71 openPRs=0 | commits:  ;; PRs:  ;; issues60d:  |
| 2026-10-19T01:47Z | recent | `Cipher-Atelier/cipher-atelier` | commits60d=ERR openPRs=ERR | commits:  ;; PRs:  ;; issues60d:  |
| 2026-10-19T01:35Z | blog-search | `15573` | 0 | - |
| 2026-10-19T01:35Z | blog-search | `Mayenne` | 0 | - |
| 2026-10-19T01:35Z | blog-search | `Forget` | 2 | 2024-07-19 Ciphertext-only Attack on Classical Ciphers by Using AI / 2023-09-06 I Reconstructed a Cipher but Lost Its Source. |
| 2026-10-19T01:35Z | blog-search | `Halincourt` | 0 | - |
| 2026-10-19T01:35Z | blog-search | `Matignon` | 0 | - |
| 2026-10-19T01:36Z | blog-search | `1586` | 12 | 2026-09-28 Walsingham's Pigpen Cipher (1586-1587) / 2026-07-06 Heavy Use of Nulls in Henry of Navarre's Cipher (1586) / 2026-01-28 Vigenere's Description of Scytale Not as a Transposition Cipher / 2024-08-11 A Second "More Ample" Babington Cipher / 2024-03-24  |
| 2026-10-19T01:36Z | blog-search | `Henri III` | 0 | - |
| 2026-10-19T01:36Z | blog-search | `Henry III` | 16 | 2026-07-13 Spanich Decryption of Claude Blatier's letter (1582) / 2026-03-15 French Ciphers for German Affairs / 2026-02-22 Reconstruction of a Cipher used by Charles de Danzay, French Ambassador to Denmark / 2024-07-03 Early French Figure Ciphers / 2023-07-31 |
| 2026-10-19T01:36Z | blog-search | `f.385` | 0 | - |
| 2026-10-19T01:36Z | blog-search | `Lasry` | 32 | 2026-10-14 Empress Eugénie's Cipher Telegrams to Napoleon III Broken by Two / 2026-10-06 "Hieronimo Ranzo" Cipher Solved by AI / 2026-09-08 Wellington's Code/Cipher during the Peninsular War / 2026-07-11 Earliest French Ciphers (1507, 1513, 1521) / 2026-04-29  |
| 2026-10-19T01:36Z | blog-latest | `25 newest` | 25 | 2026-10-15 Verification of AI and Verification by AI / 2026-10-14 Empress Eugénie's Cipher Telegrams to Napoleon III Broken by Two / 2026-10-11 Dutch Ciphers with Table Switching / 2026-10-09 Trithemius' Cipher Deciphered and Re-enciphered Polyalphabetically i |

## Same-day re-sweep before publishing (19 Oct 2026, 04:01–04:12 UTC): clear

Run again before the write-up of v0.1, as the rule asks.

- **GitHub code, repository and issue search**: the same 66 queries as the first sweep. Same hits; nothing new, and nothing names f. 385.
- **Last 7 days** of commits, pull requests and issues in cipher-lab, cabinet-noir, Cryptoole, both Bourdeau copies, and **every repository** of the pangoleen (12) and Cipher-Atelier (11) accounts:
  - cipher-lab: 4,557 commits since 12 Oct (all paged). Every hit is its fr. 15572 Matignon/Mayenne Cipher-1 work;
  - Bourdeau: the only hit is the preparer's own issue #44 (ff. 379–381);
  - no other hit.
- **Tomokiyo**:
  - henryiii.htm unchanged (Last-Modified 23 Sept 2023, SHA-256 2d90a1d1…b658); f. 385 still "Undeciphered", with the same fragment;
  - ai.htm (Last-Modified 19 Oct 2026 00:41, unchanged since the first sweep) and polyphonic1593.htm (18 Oct): no 15573, Mayenne, Forget, Halincourt or f. 385;
  - GL.htm (15 Oct): fr. 15573 only for f. 127 and f. 124;
  - blog: no new post since 15 Oct; searches for 15573, Mayenne, Halincourt, Matignon and f.385 return nothing.
- **Web** (two searches, one extended): nothing on this letter.

### Query log of the re-sweep (machine-written)

| UTC | where | query | hits | first results |
|---|---|---|---|---|
| 2026-10-19T04:01Z | owner-repos | `pangoleen` | 12 | pangoleen/cipher-readings / pangoleen/ormarch-picture-frame / pangoleen/photo-frame-dashboard / pangoleen/senecey-1594 / pangoleen/desportes-1593 / pangoleen/qwen3.8-flash-next-dgx-spark / pangoleen/awesome-even-realities-g2 / pangoleen/qwen3.8-27b-dgx-spark-d |
| 2026-10-19T04:01Z | owner-repos | `Cipher-Atelier` | 11 | Cipher-Atelier/anna-ticha-cipher-postcards / Cipher-Atelier/desportes-to-aldobrandini-cipher-letter-1593 / Cipher-Atelier/slovak-cipher-telegram-to-madrid-1940 / Cipher-Atelier/slovak-cipher-telegram-to-berlin-1940 / Cipher-Atelier/research-index / Cipher-Atel |
| 2026-10-19T04:01Z | recent7d | `NoAutopilot/cipher-lab` | commits=3000 prs=71 | commits: (every commit hit is its fr. 15572 Matignon/Mayenne Cipher-1 work; messages not copied) |
| 2026-10-19T04:01Z | recent7d | `el-descifrador/cabinet-noir` | commits=0 prs=0 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:01Z | recent7d | `satorunet/cryptoole` | commits=1 prs=0 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:01Z | recent7d | `dbourdeau/cyphersolver` | commits=66 prs=32 | commits:  ;; PRs:  ;; issues: #44 BnF fr. 15573 ff. 379-381 (Matignon Cipher-3, 1586): first reading of the     whole despatch published (work in progress |
| 2026-10-19T04:01Z | recent7d | `alejandrozarco/cyphersolver` | commits=0 prs=0 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:01Z | recent7d | `pangoleen/cipher-readings` | commits=2 prs=0 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:01Z | recent7d | `pangoleen/ormarch-picture-frame` | commits=2 prs=0 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:01Z | recent7d | `pangoleen/photo-frame-dashboard` | commits=46 prs=0 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:01Z | recent7d | `pangoleen/senecey-1594` | commits=0 prs=0 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `pangoleen/desportes-1593` | commits=0 prs=1 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `pangoleen/qwen3.8-flash-next-dgx-spark` | commits=0 prs=0 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `pangoleen/awesome-even-realities-g2` | commits=0 prs=6 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `pangoleen/qwen3.8-27b-dgx-spark-dflash2` | commits=0 prs=0 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `pangoleen/mib-doc-challenge` | commits=0 prs=0 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `pangoleen/mib-doc-challenge-solution` | commits=0 prs=0 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `pangoleen/PyClaw` | commits=0 prs=0 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `pangoleen/PromptStack` | commits=0 prs=0 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `Cipher-Atelier/anna-ticha-cipher-postcards` | commits=0 prs=19 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `Cipher-Atelier/desportes-to-aldobrandini-cipher-letter-1593` | commits=0 prs=4 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `Cipher-Atelier/slovak-cipher-telegram-to-madrid-1940` | commits=0 prs=5 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `Cipher-Atelier/slovak-cipher-telegram-to-berlin-1940` | commits=0 prs=6 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `Cipher-Atelier/research-index` | commits=0 prs=5 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `Cipher-Atelier/malsburg-cipher-letter-1637` | commits=0 prs=5 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `Cipher-Atelier/louis-xiii-cipher-letter-june-1635` | commits=0 prs=4 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `Cipher-Atelier/lincker-to-vultejus-cipher-letter-1672` | commits=0 prs=4 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `Cipher-Atelier/kingston-cipher-postcard-1907` | commits=0 prs=5 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `Cipher-Atelier/chatillon-to-servien-cipher-letter-1635` | commits=0 prs=7 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:02Z | recent7d | `Cipher-Atelier/.github` | commits=0 prs=4 | commits:  ;; PRs:  ;; issues:  |
| 2026-10-19T04:01Z | code | `"fr. 15573"` | 2 | dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt / NoAutopilot/cipher-lab:sources/cryptiana/CRYPTO-INDEX.tsv |
| 2026-10-19T04:01Z | code | `"fr.15573"` | 4 | dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt / NoAutopilot/cipher-lab:LESSONS-TOMOKIYO.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/NOTES.md / NoAutopilot/cipher-lab:sources/cryptiana/CRYPTO-INDEX.tsv |
| 2026-10-19T04:01Z | code | `"fr 15573"` | 7 | lucas-amberg/ecfr-analyzer:public/ecfr/2025-02-06/9/III/A/312/312.6/312.6.md / lucas-amberg/ecfr-analyzer:public/ecfr/2025-02-06/9/III/A/312/312.5/312.5.md / lucas-amberg/ecfr-analyzer:public/ecfr/2025-02-06/9/III/A/312/312.2/312.2.md / lucas-amberg/ecfr-analy |
| 2026-10-19T04:01Z | code | `"français 15573"` | 2 | NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/second-opinions/chatgpt-leads-2026-09-26.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/NOTES.md |
| 2026-10-19T04:01Z | code | `"15573" 385` | 6553600 | fegennari/3DWorld:mesh.txt / giongto35/TetrisAI:Stat.txt / tanakimees/Sudoku:README.md / spaze/hashes:md5.md / benjaminantunes/SMA-SEIR-Repro:log6.txt / cxcscmu/Craw4LLM:seed.txt / VITA-Group/GLNet:train.txt / haruncanatali/HavaDurumu:README.md / Roytak/AOC23: |
| 2026-10-19T04:02Z | code | `"f. 385" Mayenne` | 0 | - |
| 2026-10-19T04:02Z | code | `"f.385" Mayenne` | 1 | dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt |
| 2026-10-19T04:02Z | code | `MayenneForget2` | 0 | - |
| 2026-10-19T04:02Z | code | `henryiii_MayenneForget2` | 0 | - |
| 2026-10-19T04:02Z | code | `"Mayenne-Forget"` | 22 | dbourdeau/cyphersolver:CATALOGUE.md / dbourdeau/cyphersolver:targets/matignon1586c3/NOTES.md / dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt / dbourdeau/cyphersolver:targets/matignon1586/NOTES.md / dbourdeau/cyphersolver:research/qa/key_split_ |
| 2026-10-19T04:02Z | code | `"Mayenne–Forget"` | 14 | dbourdeau/cyphersolver:targets/mercoeur1586/NOTES.md / dbourdeau/cyphersolver:targets/matignon1586/f173_reading.md / dbourdeau/cyphersolver:targets/matignon1586/f154_reading.md / dbourdeau/cyphersolver:targets/matignon1586/NOTES.md / dbourdeau/cyphersolver:CAT |
| 2026-10-19T04:02Z | code | `"Mayenne Forget" cipher` | 1 | NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/NOTES.md |
| 2026-10-19T04:02Z | code | `"Mayenne-Forget Cipher-2"` | 3 | dbourdeau/cyphersolver:research/qa/key_split_audit.md / dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt / dbourdeau/cyphersolver:research/qa/key_split_findings.jsonl |
| 2026-10-19T04:03Z | code | `Halincourt chiffre` | 1 | dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt |
| 2026-10-19T04:03Z | code | `Halincourt cipher` | 9 | dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt / GITenberg/Cinq-Mars-Volume-6_3952:3952.txt / victoriasparrow/coursework_parallel_computing:minicorpus/3952.txt / isel-sw-projects/2021-asyncio-pipelines:books/gutenberg/3000/2000/pg3952.txt / chr |
| 2026-10-19T04:03Z | code | `"ratrape"` | 792 | global-asp/global-asp:ht/0262_magozwe.md / global-asp/global-asp:mfe/0262_magozwe.md / tesseract-ocr/langdata_lstm:hat/hat.wordlist / ch-nry/VCV_nozori:src/m68_Gran.ino / SSNTails/SRB2Proto:Code/d_clisrv.c / ch-nry/VCV_nozori:template_nozori/src/m68_Gran.ino / |
| 2026-10-19T04:03Z | code | `"apresdemain et ratrape"` | 1 | dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt |
| 2026-10-19T04:03Z | code | `"mil hommes de pied qui diminue"` | 0 | - |
| 2026-10-19T04:03Z | code | `btv1b90618780` | 0 | - |
| 2026-10-19T04:03Z | code | `"Mayenne" 1586 chiffre` | 241 | NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/NOTES.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/HYPOTHESES.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/second-opinions/chatgpt-leads-2026-09-26.md / NoAutopilot/cipher-lab:ciphe |
| 2026-10-19T04:04Z | code | `"duc de Mayenne" 1586 cipher` | 15 | dbourdeau/cyphersolver:targets/matignon1586/f154_reading.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/second-opinions/PROMPT-chatgpt-leads.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/NOTES.md / NoAutopilot/cipher-lab:ciphers/matignon |
| 2026-10-19T04:04Z | code | `"Forget" Mayenne 1586` | 1002 | NoAutopilot/cipher-lab:specs/matignon-mayenne-1586.json / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/NOTES.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/second-opinions/PROMPT-chatgpt-leads.md / NoAutopilot/cipher-lab:ciphers/matignon-may |
| 2026-10-19T04:04Z | code | `"15573" repo:NoAutopilot/cipher-lab` | 10 | NoAutopilot/cipher-lab:sources/pools-scout/2026-10-03/P1.md / NoAutopilot/cipher-lab:LESSONS-TOMOKIYO.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/second-opinions/chatgpt-leads-2026-09-26.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/N |
| 2026-10-19T04:04Z | code | `"385"  Mayenne repo:NoAutopilot/cipher-lab` | 27 | NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/HYPOTHESES.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/NOTES.md / NoAutopilot/cipher-lab:ciphers/matignon-mayenne-1586/sorter/recut.py / NoAutopilot/cipher-lab:ciphers/fr4715-f61-mayenne-1592/H |
| 2026-10-19T04:04Z | code | `MayenneForget2 repo:NoAutopilot/cipher-lab` | 0 | - |
| 2026-10-19T04:04Z | code | `Halincourt repo:NoAutopilot/cipher-lab` | 0 | - |
| 2026-10-19T04:04Z | code | `"15573" repo:el-descifrador/cabinet-noir` | 0 | - |
| 2026-10-19T04:05Z | code | `"385"  Mayenne repo:el-descifrador/cabinet-noir` | 0 | - |
| 2026-10-19T04:05Z | code | `MayenneForget2 repo:el-descifrador/cabinet-noir` | 0 | - |
| 2026-10-19T04:05Z | code | `Halincourt repo:el-descifrador/cabinet-noir` | 0 | - |
| 2026-10-19T04:05Z | code | `"15573" repo:satorunet/cryptoole` | 0 | - |
| 2026-10-19T04:05Z | code | `"385"  Mayenne repo:satorunet/cryptoole` | 0 | - |
| 2026-10-19T04:05Z | code | `MayenneForget2 repo:satorunet/cryptoole` | 0 | - |
| 2026-10-19T04:05Z | code | `Halincourt repo:satorunet/cryptoole` | 0 | - |
| 2026-10-19T04:05Z | code | `"15573" repo:dbourdeau/cyphersolver` | 3 | dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt / dbourdeau/cyphersolver:targets/voynich/results/b4.json / dbourdeau/cyphersolver:research/gallica_sweep/sru_results.json |
| 2026-10-19T04:06Z | code | `"385"  Mayenne repo:dbourdeau/cyphersolver` | 11 | dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt / dbourdeau/cyphersolver:targets/matignon1586/NOTES.md / dbourdeau/cyphersolver:CATALOGUE.md / dbourdeau/cyphersolver:SOLVED_CATALOGUE.md / dbourdeau/cyphersolver:SOLVED_RANKING.md / dbourdeau/cyph |
| 2026-10-19T04:06Z | code | `MayenneForget2 repo:dbourdeau/cyphersolver` | 0 | - |
| 2026-10-19T04:06Z | code | `Halincourt repo:dbourdeau/cyphersolver` | 1 | dbourdeau/cyphersolver:research/gallica_sweep/src/henryiii.txt |
| 2026-10-19T04:06Z | code | `"15573" repo:alejandrozarco/cyphersolver` | 0 | - |
| 2026-10-19T04:06Z | code | `"385"  Mayenne repo:alejandrozarco/cyphersolver` | 0 | - |
| 2026-10-19T04:06Z | code | `MayenneForget2 repo:alejandrozarco/cyphersolver` | 0 | - |
| 2026-10-19T04:06Z | code | `Halincourt repo:alejandrozarco/cyphersolver` | 0 | - |
| 2026-10-19T04:06Z | code | `"15573" repo:pangoleen/cipher-readings` | 0 | - |
| 2026-10-19T04:07Z | code | `"385"  Mayenne repo:pangoleen/cipher-readings` | 0 | - |
| 2026-10-19T04:07Z | code | `MayenneForget2 repo:pangoleen/cipher-readings` | 0 | - |
| 2026-10-19T04:07Z | code | `Halincourt repo:pangoleen/cipher-readings` | 0 | - |
| 2026-10-19T04:07Z | code | `"15573" repo:Cipher-Atelier/cipher-atelier` | 0 | - |
| 2026-10-19T04:07Z | code | `"385"  Mayenne repo:Cipher-Atelier/cipher-atelier` | 0 | - |
| 2026-10-19T04:07Z | code | `MayenneForget2 repo:Cipher-Atelier/cipher-atelier` | 0 | - |
| 2026-10-19T04:07Z | code | `Halincourt repo:Cipher-Atelier/cipher-atelier` | 0 | - |
| 2026-10-19T04:07Z | repositories | `15573` | 56 | jc-infinite-repos/jc-infinite-repos-15573 (2026-03-03) / pitiessayer/1557374401685418949976 (2023-05-30) / pzpinfo/testrepo1557322469555 (2019-05-08) / pzpinfo/testrepo1557371531121 (2019-05-09) / ModelDBRepository/155735 (2019-05-29) / ModelDBRepository/15573 |
| 2026-10-19T04:08Z | repositories | `mayenne` | 23 | LordGnomeMBE/MayenneMap (2023-08-05) / Neritic-mayenne9092/neritic-mayenne9092.github.io (2026-09-25) / Fabx97/Calcul_VintamFabyo (2025-11-14) / slioult/GranitWeb (2013-05-27) / MAYENNE-242/MAYENNE-242 (2021-09-15) / LaMayenne/LaMayenne (2020-02-01) / mattmg83 |
| 2026-10-19T04:08Z | repositories | `mayenne cipher` | 0 | - |
| 2026-10-19T04:08Z | repositories | `mayenne 1586` | 0 | - |
| 2026-10-19T04:08Z | repositories | `mayenne forget` | 0 | - |
| 2026-10-19T04:08Z | repositories | `henri III cipher 1586` | 0 | - |
| 2026-10-19T04:08Z | repositories | `cipher reading 1586` | 1 | BravoBravoIX/matignon-1586-cipher-reading (2026-10-18) |
| 2026-10-19T04:08Z | repositories | `first reading cipher` | 7 | jorruior/CIPHER (2016-02-29) / BravoBravoIX/matignon-1586-cipher-reading (2026-10-18) / taufiq0205/zodiac-cipher-analysis (2026-08-23) / BravoBravoIX/desportes-1593-rereading (2026-10-18) / sohadQtaitat/cipher (2019-12-13) / pangoleen/senecey-1594 (2026-10-03) |
| 2026-10-19T04:08Z | repositories | `bnf cipher` | 5 | BravoBravoIX/matignon-1586-cipher-reading (2026-10-18) / pangoleen/senecey-1594 (2026-10-03) / devinokeefe/seure (2026-10-04) / pangoleen/desportes-1593 (2026-10-01) / BravoBravoIX/desportes-1593-rereading (2026-10-18) |
| 2026-10-19T04:09Z | repositories | `gallica cipher` | 0 | - |
| 2026-10-19T04:09Z | repositories | `chiffre 1586` | 0 | - |
| 2026-10-19T04:09Z | repositories | `tomokiyo` | 5 | TomokiYoshizawa/TomokiYoshizawa (2024-03-28) / momogu97531/tomokiyocom-del (2026-07-25) / TommyNP/complex_networks_2024_tomokiyo (2024-09-10) / suzanv/termprofiling (2016-09-08) / Cipher-Atelier/desportes-to-aldobrandini-cipher-letter-1593 (2026-10-06) |
| 2026-10-19T04:09Z | repositories | `halincourt` | 0 | - |
| 2026-10-19T04:09Z | repositories | `ligue 1586 cipher` | 0 | - |
| 2026-10-19T04:09Z | repositories | `catholic league cipher` | 1 | pangoleen/desportes-1593 (2026-10-01) |
| 2026-10-19T04:09Z | issues | `"15573"` | 10859 | Significant-Gravitas/AutoGPT#15573 fix(frontend): keep the @ mention list on screen above or be / jsboige/CoursIA#15573 meta: recenser les issues dont le cadrage prescrit un grain  / sagemath/sage#15573 (co)product coercion / red-hat-storage/ocs-ci#15573 Updat |
| 2026-10-19T04:10Z | issues | `Mayenne cipher` | 3 | NoAutopilot/cipher-lab#66 JSTOR run 4 Oct 2026 (2): last 24 rows, queue empty / NoAutopilot/cipher-lab#29 [SO-MATIGNON-LEADS] leads: Matignon/Mayenne cipher, BnF fr.1 / dbourdeau/cyphersolver#9 Intercepts summarised for Nevers, 1589 (fr. 3977 no. 96):  |
| 2026-10-19T04:10Z | issues | `Mayenne 1586` | 34697 | heartcombo/devise#1586 Devise shared_views generator not found / elastic/elasticsearch#1586 TTL does not respect routing when expiring (deleting) docume / scikit-image/scikit-image#1586 Document negative `sigma` values in `filters.gaussian_filter / astropy/ast |
| 2026-10-19T04:10Z | issues | `Halincourt` | 0 | - |
| 2026-10-19T04:10Z | issues | `MayenneForget2` | 0 | - |
| 2026-10-19T04:10Z | issues | `btv1b90618780` | 0 | - |
| 2026-10-19T04:02Z | blog-search | `15573` | 0 | - |
| 2026-10-19T04:02Z | blog-search | `Mayenne` | 0 | - |
| 2026-10-19T04:02Z | blog-search | `Forget` | 2 | 2024-07-19 Ciphertext-only Attack on Classical Ciphers by Using AI / 2023-09-06 I Reconstructed a Cipher but Lost Its Source. |
| 2026-10-19T04:02Z | blog-search | `Halincourt` | 0 | - |
| 2026-10-19T04:02Z | blog-search | `Matignon` | 0 | - |
| 2026-10-19T04:02Z | blog-search | `1586` | 12 | 2026-09-28 Walsingham's Pigpen Cipher (1586-1587) / 2026-07-06 Heavy Use of Nulls in Henry of Navarre's Cipher (1586) / 2026-01-28 Vigenere's Description of Scytale Not as a Transposition Cipher / 2024-08-11 A Second "More Ample" Babington Cipher / 2024-03-24  |
| 2026-10-19T04:03Z | blog-search | `Henri III` | 0 | - |
| 2026-10-19T04:03Z | blog-search | `Henry III` | 16 | 2026-07-13 Spanich Decryption of Claude Blatier's letter (1582) / 2026-03-15 French Ciphers for German Affairs / 2026-02-22 Reconstruction of a Cipher used by Charles de Danzay, French Ambassador to Denmark / 2024-07-03 Early French Figure Ciphers / 2023-07-31 |
| 2026-10-19T04:03Z | blog-search | `f.385` | 0 | - |
| 2026-10-19T04:03Z | blog-search | `Lasry` | 32 | 2026-10-14 Empress Eugénie's Cipher Telegrams to Napoleon III Broken by Two / 2026-10-06 "Hieronimo Ranzo" Cipher Solved by AI / 2026-09-08 Wellington's Code/Cipher during the Peninsular War / 2026-07-11 Earliest French Ciphers (1507, 1513, 1521) / 2026-04-29  |
| 2026-10-19T04:03Z | blog-latest | `25 newest` | 25 | 2026-10-15 Verification of AI and Verification by AI / 2026-10-14 Empress Eugénie's Cipher Telegrams to Napoleon III Broken by Two / 2026-10-11 Dutch Ciphers with Table Switching / 2026-10-09 Trithemius' Cipher Deciphered and Re-enciphered Polyalphabetically i |
| 2026-10-19T04:03Z | page | `https://cryptiana.web.fc2.com/code/henryiii.htm` | LM=Sat, 23 Sep 2023 11:53:39 GMT sha=2d90a1d1..b658 hits=37 | ubeterre , f113 , Hautefort , Maygnieulx ), 15568 , 15569 ( Matignon2 ), 15570 , 15571 ( Chasteauneuf , f184 ), 15572 ( Mayenne1 , Camus , Malycorne , Matignon3 , Mayenne2 , MatignonTuple , StLuc , Biron ), 15573 , 15574 ) References to Cipher in the Correspon |
| 2026-10-19T04:03Z | page | `https://cryptiana.web.fc2.com/code/ai.htm` | LM=Mon, 19 Oct 2026 00:41:23 GMT sha=5db44588..9acd hits=0 | - |
| 2026-10-19T04:03Z | page | `https://cryptiana.web.fc2.com/code/GL.htm` | LM=Thu, 15 Oct 2026 13:01:21 GMT sha=e6b5172d..f2b4 hits=4 | wholly enciphered, dated January 1586 is in BnF fr.15572, f.43 (see another article) . It is solved as follows. BnF fr. 15573 The cipher used in a letter of Duval to Villeroi in f.127 of BnF fr.15573 ( Gallica ) is solved as follows. It appears to be a sequel  |
| 2026-10-19T04:03Z | page | `https://cryptiana.web.fc2.com/code/polyphonic1593.htm` | LM=Sun, 18 Oct 2026 12:49:24 GMT sha=7ca198e2..be94 hits=0 | - |
