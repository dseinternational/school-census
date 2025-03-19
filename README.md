# SEN schools census data analysis

SEN schools census data analysis for England.


### Getting started

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

