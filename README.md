# dFFOCT — dynamic FFOCT

Data accompanying the manuscript **Label-free volumetric dynamic atlas of fresh mouse organs using full-field optical coherence tomography**.

## Dataset contents

The supplied collection contains 30 files (37,465,707,797 bytes): 10 NumPy raw-data arrays and 20 associated PNG/JPEG images. Each organ directory contains one raw array and two images.

Organs: brain, duodenum, eyeball, inguinal lymph node, kidney, liver, ovary, pancreas, testis, and thymus.

All 10 NPY files have shape `(1024, 1100, 1600)`, little-endian unsigned 16-bit values (`<u2`), and C-order storage, as read from their NPY headers. Axis meanings, acquisition intervals, pixel/voxel spacing, intensity units, and the relationship of each image to manuscript figure panels have not been supplied. Coordinate-like strings in filenames are preserved verbatim and should not be interpreted as calibrated metadata without confirmation from the authors.

## Full-resolution overview images

The overview images below are exact byte-for-byte copies of the latest files supplied by the author. Six earlier lower-resolution PNG overviews were replaced with the updated full-resolution JPEG files before release. No resizing or re-encoding is performed during preparation or upload. Download the release attachments to obtain the original files; a browser preview is not a substitute for the downloaded image.

| Organ | Original file | Width × height (pixels) |
| --- | --- | --- |
| Brain | `Brain/brain.jpg` | 26396 × 17197 |
| Duodenum | `Duodenum/Duodenum.jpg` | 19540 × 18091 |
| Eyeball | `Eyeball/Eyeball.png` | 7229 × 7598 |
| Inguinal lymph node | `Inguinal lymph node/Inguinal lymph node.jpg` | 7238 × 6097 |
| Kidney | `Kidney/kidney.jpg` | 16540 × 21077 |
| Liver | `Liver/Liver.png` | 6242 × 7605 |
| Ovary | `Ovary/ovary.jpg` | 5180 × 6101 |
| Pancreas | `Pancreas/Pancreas.jpg` | 16511 × 15058 |
| Testis | `Testis/Testis.png` | 10313 × 7600 |
| Thymus | `Thymus/Thymus.jpg` | 18566 × 15105 |

`image-quality-report.json` records image dimensions and checksums, including the comparison with the initially supplied versions. Pixel dimensions describe the supplied files; they do not independently establish the optical resolution of the imaging system.

## Download and restore

The data are distributed as GitHub Release attachments. The Git repository contains documentation, the file manifest, checksums, and the restoration script. Downloading the repository ZIP alone does not include the imaging data.

1. Download all data attachments from the dataset release into one folder named `release-assets`.
2. Download `manifest.json` and `restore_data.py` from this repository.
3. Run with Python 3.9 or later:

```shell
python restore_data.py --assets release-assets --output data
```

If GitHub CLI is installed, all release attachments can be downloaded with one command after the release is published:

```shell
gh release download data-v1.0 --repo forest1997/dffoct-dynamic-ffoct --dir release-assets
```

The script reassembles file parts in manifest order, checks SHA-256 hashes for both the individual attachments and the complete original files, and restores the exact original Unicode filenames and organ directory structure. It refuses to overwrite existing output files. If verification fails, an incomplete `.partial` file is left for inspection; remove that specific incomplete file before retrying.

Large arrays are divided into byte segments of at most 1,800,000,000 bytes, below GitHub's 2 GiB release-attachment limit. Segmentation does not alter the original data. No compression, intensity transformation, resampling, or format conversion is applied.

Allow at least 37.47 GB for downloaded attachments and an additional 37.47 GB for restored files. `manifest.json` maps every attachment to its original file and includes array-header and image-dimension metadata. `SHA256SUMS.txt` lists checksums of the restored files.

## Reading a restored raw array

Install NumPy, then open a file without loading the entire array into memory:

```python
import numpy as np
raw = np.load("data/Brain/003_+20.0μm_-0.576mm_1.642mm_raw.npy", mmap_mode="r", allow_pickle=False)
print(raw.shape, raw.dtype)
```

## Citation and reuse

The associated manuscript title is given above. Authors, publication DOI, dataset DOI, and a data reuse licence have not yet been supplied. Public download access does not by itself grant a reuse licence. This collection describes the supplied files and does not establish that every dataset underlying the manuscript is included.
