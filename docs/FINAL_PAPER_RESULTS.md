# Results reported in the final research paper

**Paper:** *FGSM Variants in White Box Settings: A Comparative Study*  
**Authors (supplied paper):** Aarti Lad, Ruchi Bhale, Shlok Belgamwar, Madhuri Wakode

The following values are transcribed from Tables I and II on page 4 of the [supplied paper PDF](../paper/Paper_479_FGSM_Variants_in_White_Box_Settings.pdf), checked against its rendered tables. **They are historical reported measurements, not newly computed outputs.**

## Table I — Vanilla FGSM and Targeted FGSM

| Epsilon (as printed) | Vanilla FGSM predicted class | Confidence | T-FGSM predicted class | Confidence |
| ---: | --- | ---: | --- | ---: |
| 0.025 | Egyptian cat | 38.5972% | Tiger cat | 38.6791% |
| 0.05 | Egyptian cat | 39.2992% | Tiger cat | 41.6954% |
| 0.075 | Tiger cat | 40.0466% | Tiger cat | 49.3392% |
| 0.1 | Tiger cat | 47.7527% | Tiger cat | 56.1532% |

## Table II — Momentum Iterative FGSM and Iterative FGSM

| Iteration | MI-FGSM predicted class | Confidence | I-FGSM predicted class | Confidence |
| ---: | --- | ---: | --- | ---: |
| 1 | Persian cat | 99.9715% | Persian cat | 99.9715% |
| 2 | Persian cat | 99.6570% | Persian cat | 99.2843% |
| 3 | Persian cat | 96.9415% | Persian cat | 80.9636% |
| 4 | Persian cat | 82.9145% | Tiger cat | 35.9507% |
| 5 | Persian cat | 49.2908% | Persian cat | 63.5408% |
| 6 | Tabby | 30.5566% | Egyptian cat | 38.7488% |

All numerical entries and class labels match the supplied PDF's printed tables. The existing numerical entries are unchanged. See the [publication and source notes](SOURCES.md) for citations and the distinction between reported tables and saved notebook runs.
