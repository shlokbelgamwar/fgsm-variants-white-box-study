# Sources and experiment notes

## Paper and publication

- [Supplied paper PDF](https://doi.org/10.1109/ICICT60155.2024.10544606), *FGSM Variants in White Box Settings: A Comparative Study*. Page 1 credits Aarti Lad, Ruchi Bhale, Shlok Belgamwar, and Madhuri Wakode. Tables I and II are on page 4; Figure 1 is on page 2.
- [Published paper — IEEE Xplore](https://ieeexplore.ieee.org/document/10544606), DOI [10.1109/ICICT60155.2024.10544606](https://doi.org/10.1109/ICICT60155.2024.10544606).
- [Conference proceedings contents](https://www.proceedings.com/content/074/074902webtoc.pdf) lists Aarti Lad, Ruchi Bhale, and Shlok Belgamwar under the published title.
- [Research Paper.pdf in STC 2023](https://drive.google.com/file/d/1oYYLR46nL3zTf43uNz_97W_CxalTleHK/view) is the earlier manuscript, uploaded November 6, 2023. It differs from the supplied paper PDF in authorship, figures, and results presentation.
- [STC 2023 research folder](https://drive.google.com/drive/folders/1x-BVBnlrAentNk9BOnVNnqchud52ZIfo).
- [Historical Images folder](https://drive.google.com/drive/folders/1UqoxOXQVN9AdhHzkPGn2GEFw0Xv2gAdu) contains algorithm and architecture graphics, not the missing input photographs.

The CSV files and readable result tables were checked against both the extracted text and the rendered page 4 of the supplied paper PDF. All class labels, epsilon/iteration entries, and confidence values match; no numerical entries were changed. CSV numeric serialization omits the trailing zero in 99.6570, without changing its value.

The supplied PDF is retained byte-for-byte (SHA-256: `dc8362355d4dc84b42043f9526901d5c701d21992e7a7adaa51303e8a4add4c1`). Its embedded creation/modification timestamp is February 27, 2024; that metadata does not establish publisher-version identity. The paper copy credits four authors, while the proceedings catalogue lists three and the publication uses an expanded title. The README credits all four authors of the supplied copy and keeps the catalogue citation distinct.

Two printed inconsistencies are retained as source notes: the results paragraph says epsilon 0.75 while Table I prints 0.075; the T-FGSM discussion calls target index 281 “Tiger cat,” while the archived notebook identifies it as tabby. The tables follow the printed tables rather than silently correcting either record.

## Notebook snapshots

The T-FGSM, I-FGSM, and MI-FGSM files in `notebooks/` are byte-preserving copies of the current archived Drive files, including saved outputs. The files were created in 2023; Drive reports later modification dates of November 6, 2025. These are snapshots of the available archive, not a claim that the files remained untouched since creation.

| Snapshot | Drive source | Created | Recorded settings |
| --- | --- | --- | --- |
| [T-FGSM](../notebooks/T-FGSM.ipynb) | [Colab](https://colab.research.google.com/drive/1aZ0KbOuC1hG-5A5lHyjW4tEPxs35Z9vA) | November 6, 2023 | target index 281; epsilon [0.005, 0.01, 0.05, 0.1] |
| [I-FGSM](../notebooks/I-FGSM.ipynb) | [Colab](https://colab.research.google.com/drive/1ujiHNES0NChZwqZiic1SD2dWp8hXMese) | November 6, 2023 | epsilon 0.005; six iterations |
| [MI-FGSM](../notebooks/MI-FGSM.ipynb) | [Colab](https://colab.research.google.com/drive/1Xw75zdLYlw59gdu-3QNy4rH_TzgzFX1A) | October 21, 2023 | epsilon 0.01; six iterations; decay 1.2 |

The saved outputs are archival records, not newly executed results. For example, T-FGSM's saved output starts from an Egyptian cat and targets tabby, while Table I reports tiger cat; I-FGSM's saved run also differs from Table II. MI-FGSM's saved run ends at tabby with approximately 30.5566% confidence. Preserve each record independently rather than replacing either with tuned values.

The README's Figure 1 is extracted directly from the image embedded on page 2 of the supplied paper PDF, including its labels, without rerunning an attack. `assets/mi-fgsm-archived-output.png` is separately retained from a saved PNG output in MI-FGSM.ipynb. Neither figure establishes recovery of an original full-resolution input photograph.

## Method provenance

The Python files retain the archived attack choices: I-FGSM updates the predicted label each iteration; MI-FGSM uses the current predicted label but differentiates the original image and normalizes the first image's gradient with a global L1 norm. These details should be considered when interpreting the code alongside the paper's equations.

[`notebooks/FGSM.ipynb`](../notebooks/FGSM.ipynb) is a companion notebook derived from the paper's one-step formula and `methods/FGSM.py`. It includes image loading/upload, ResNet50V2 setup, Table I epsilon settings, and perturbation visualization. The original standalone Vanilla notebook has not been recovered. The companion contains no saved run outputs; the paper's reported table is explicitly identified as reference data.

## Inputs and execution

The referenced `cat.jpg`, `cat2.jpg`, and `cat-2.JPEG` are absent from the inspected research folder. Notebook display images do not establish recovery of those original files. The full TensorFlow, model-weight, image-decoding, and preprocessing environment is not preserved. Running the code with replacement images or a different environment does not establish the origin of the published measurements.
