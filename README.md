# SEN schools census data analysis

**Scripts and resources for analysing schools census data for England.**

We are interested in looking at the characteristics and placements of children with Special Educational Needs in schools in England and how they may be changing over time.

One particular interest will be looking at the characteristics and placements of children with Down syndrome, who, from 2024/25, will be identified in the school census data.

## Getting started

Requires a recent version of [Python](https://www.python.org/).

Install packages:

```
pip install -r ./requirements.txt
```

(This may be `pip3` rather than `pip` on some systems.)

Download and extract the data files:

```
python .\school-census\download_data.py
```

(This may be `python3` rather than `python` on some systems.)

Import data files into a [DuckDB](https://duckdb.org/) database.

```
python .\school-census\import_data.py
```

## Exploring the data

See [notes.ipynb](school-census\notes.ipynb) for some examples.

## Getting involved

Yes, please!
