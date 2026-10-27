# Mouse organ FF-OCT data

Data accompanying the manuscript **Label-free volumetric dynamic atlas of fresh mouse organs using full-field optical coherence tomography**.

## Dataset contents

The supplied collection contains 30 files (36,625,102,583 bytes): 10 NumPy raw-data arrays and 20 associated PNG/JPEG images. Each organ directory contains one raw array and two images.

Organs: brain, duodenum, eyeball, inguinal lymph node, kidney, liver, ovary, pancreas, testis, and thymus.

All 10 NPY files have shape `(1024, 1100, 1600)`, little-endian unsigned 16-bit values (`<u2`), and C-order storage, as read from their NPY headers. Axis meanings, acquisition intervals, pixel/voxel spacing, intensity units, and the relationship of each image to manuscript figure panels have not been supplied. Coordinate-like strings in filenames are preserved verbatim and should not be interpreted as calibrated metadata without confirmation from the authors.

## Download and restore

The data are distributed as GitHub Release attachments. The Git repository contains documentation, the file manifest, checksums, and the restoration script. Downloading the repository ZIP alone does not include the imaging data.

1. Download all data attachments from the dataset release into one folder named `release-assets`.
2. Download `manifest.json` and `restore_data.py` from this repository.
3. Run with Python 3.9 or later:

```shell
python restore_data.py --assets release-assets --output data
```

The script reassembles file parts in manifest order, checks SHA-256 hashes for both the individual attachments and the complete original files, and restores the exact original Unicode filenames and organ directory structure. It refuses to overwrite existing output files. If verification fails, an incomplete `.partial` file is left for inspection; remove that specific incomplete file before retrying.

Large arrays are divided into byte segments of at most 1,800,000,000 bytes, below GitHub's 2 GiB release-attachment limit. Segmentation does not alter the original data. No compression, intensity transformation, resampling, or format conversion is applied.

Allow at least 36.63 GB for downloaded attachments and an additional 36.63 GB for restored files. `manifest.json` maps every attachment to its original file and includes array-header metadata. `SHA256SUMS.txt` lists checksums of the restored files.

## Reading a restored raw array

Install NumPy, then open a file without loading the entire array into memory:

```python
import numpy as np
raw = np.load("data/Brain/003_+20.0μm_-0.576mm_1.642mm_raw.npy", mmap_mode="r", allow_pickle=False)
print(raw.shape, raw.dtype)
```

## Citation and reuse

The associated manuscript title is given above. Authors, publication DOI, dataset DOI, and a data reuse licence have not yet been supplied. Public download access does not by itself grant a reuse licence. This collection describes the supplied files and does not establish that every dataset underlying the manuscript is included.
