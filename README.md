# earthdataDownloader

Python package to download satellite data from NASA's Earthdata portal.

## Installation

conda:
```bash
conda env create -f environment.yml
conda activate earthdata-downloader
```

pip:

```bash
pip install .
```

## Usage

To download SST satellite data (AVHRR and OSTIA) for a specified bounding box and time range using the `earthaccess` library, first modify `search.json`, then run:

```bash
download_sst
```

If you want to use a json file with a different name, run:

```bash
download_sst -f my_json_file.json
```
