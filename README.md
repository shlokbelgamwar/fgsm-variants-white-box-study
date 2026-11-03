# FGSM Variants in White Box Settings: A Comparative Study

Code and results accompanying our paper published at **ICICT 2024**.

**Aarti Lad · Ruchi Bhale · Shlok Belgamwar · Madhuri Wakode**

[Paper on IEEE Xplore](https://ieeexplore.ieee.org/document/10544606)

## Overview

We compare Vanilla, Targeted, Iterative, and Momentum Iterative FGSM attacks on ImageNet-pretrained ResNet50V2 using 224 × 224 images.

## Getting Started

Open a notebook in Google Colab or Jupyter with TensorFlow, NumPy, Matplotlib, and Pillow installed, supply an input image, and run the cells.

| Method | Notebook | Python |
| --- | --- | --- |
| Vanilla FGSM | [FGSM.ipynb](notebooks/FGSM.ipynb) | [FGSM.py](methods/FGSM.py) |
| Targeted FGSM | [T-FGSM.ipynb](notebooks/T-FGSM.ipynb) | [T-FGSM.py](methods/T-FGSM.py) |
| Iterative FGSM | [I-FGSM.ipynb](notebooks/I-FGSM.ipynb) | [I-FGSM.py](methods/I-FGSM.py) |
| Momentum Iterative FGSM | [MI-FGSM.ipynb](notebooks/MI-FGSM.ipynb) | [MI-FGSM.py](methods/MI-FGSM.py) |

T-FGSM, I-FGSM, and MI-FGSM retain the archived Colab source; the Python files are refactored method excerpts. Vanilla FGSM implements the paper’s formula; its standalone original notebook was not recovered.

Input filenames are `cat.jpg` (Vanilla/T-FGSM), `cat2.jpg` (I-FGSM), and `cat-2.JPEG` (MI-FGSM). Original photos and the full environment record are unavailable; see [source notes](docs/SOURCES.md) for saved-output and parameter differences.

## Results

Published measurements from Tables I and II, page 4:

- [Vanilla FGSM and T-FGSM](docs/final_paper_table_i.csv)
- [MI-FGSM and I-FGSM](docs/final_paper_table_ii.csv)
- [View all results](docs/FINAL_PAPER_RESULTS.md)

## Citation

A. Lad, R. Bhale, and S. Belgamwar, “Fast Gradient Sign Method (FGSM) Variants in White Box Settings: A Comparative Study,” *2024 International Conference on Inventive Computation Technologies (ICICT)*, 2024. [doi:10.1109/ICICT60155.2024.10544606](https://doi.org/10.1109/ICICT60155.2024.10544606).

*Citation follows the publication catalogue; the paper PDF credits the four authors listed above.*

