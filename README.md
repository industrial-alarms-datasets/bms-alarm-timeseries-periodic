# BMS alarm timeseries with periodicity labels

## Overview

This repository is a companion to the
[BMS alarm timeseries with periodicity labels](https://doi.org/10.5281/zenodo.19855611) dataset.
It hosts some code associated with exploration of the data, and may serve at opening issues related with the dataset.

Before using this repository, place the 4 data files from Zenodo into the `data/` folder.

## Executing the code

The code provided in this repository requires python `>=3.12`, `uv` and `nox`.

```bash
> pip install uv
> pip install nox
```

Simply run `nox` create a local virtual environment with the right dependencies to execute the code:

```bash
> nox
nox > Running session dev
nox > uv sync --all-extras --all-groups --python=3.13
Resolved 113 packages in 56ms
Audited 109 packages in 41ms
nox > Session dev was successful.
```

Now your virtual environment is created, located at `.venv`. You can run the notebook like this:

```bash
> jupyter notebook 1.dataset_walkthrough.ipynb
```
