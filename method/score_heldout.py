#!/usr/bin/env python3
"""Recompute the reader's sign accuracy on the held-out known text (fr. 15573 f. 104r, cipher lines 18-24).

    python3 method/score_heldout.py           # passes a, b, c and their vote
    python3 method/score_heldout.py --strict  # count only the first accepted name of the reference

Python 3 standard library only. Per line, the signs read (first name of each position) are
aligned with the reference by edit distance; a reference sign counts as right when the sign
aligned to it is one of the names accepted there (the reference gives "a|b" where the eye
cannot choose). Accuracy = reference signs read right / reference signs.
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
KT = ROOT / "data" / "known-text"


def lev_align(a, b, eq):
    n, m = len(a), len(b)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1,
                          D[i - 1][j - 1] + (0 if eq(a[i - 1], b[j - 1]) else 1))
    out, i, j = [], n, m
    while i or j:
        if i and j and D[i][j] == D[i - 1][j - 1] + (0 if eq(a[i - 1], b[j - 1]) else 1):
            out.append((i - 1, j - 1)); i, j = i - 1, j - 1
        elif i and D[i][j] == D[i - 1][j] + 1:
            out.append((i - 1, None)); i -= 1
        else:
            out.append((None, j - 1)); j -= 1
    return out[::-1]


def score(reading, ref, strict):
    tot = ok = 0
    for li, R in ref.items():
        if strict:
            R = [r[:1] for r in R]
        S = [a[0] for a in reading["lines"].get(str(li), [])]
        for i, j in lev_align(R, S, lambda r, s: s in r):
            if i is not None:
                tot += 1
                ok += j is not None and S[j] in R[i]
    return tot, ok


ref = {}
for ln in (KT / "ref-104r-l18-24.txt").read_text(encoding="utf-8").splitlines():
    if ln and not ln.startswith("#"):
        k, *toks = ln.split()
        ref[int(k)] = [t.split("|") for t in toks]
strict = "--strict" in sys.argv
for name in ("pass_a", "pass_b", "pass_c", "vote"):
    reading = json.loads((KT / "stageB" / f"f104r-{name}.json").read_text(encoding="utf-8"))
    tot, ok = score(reading, ref, strict)
    print(f"{name:7} {ok} / {tot} reference signs read right -> sign accuracy {ok / tot:.4f}")
