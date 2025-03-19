"""
Imports data from CSV files into a DuckDB database
"""

import duckdb
import db_utils
import config

db_name = f"{config.DATA_DIR_NAME}/data_tables.db"

print(f"Creating to database at {db_name}")

data = duckdb.connect(db_name)

if not db_utils.table_exists(data, "sen_ncyear"):
    data.sql(
        f"CREATE TABLE sen_ncyear AS SELECT * FROM '{config.DATA_DIR_NAME}/sen-2023-24/data/sen_ncyear_.csv'"
    )

if not db_utils.table_exists(data, "sen_age_sex"):
    data.sql(
        f"CREATE TABLE sen_age_sex AS SELECT * FROM '{config.DATA_DIR_NAME}/sen-2023-24/data/sen_age_sex_tidy.csv'"
    )

if not db_utils.table_exists(data, "sen_phase_type"):
    data.sql(
        f"CREATE TABLE sen_phase_type AS SELECT * FROM '{config.DATA_DIR_NAME}/sen-2023-24/data/sen_phase_type_new.csv'"
    )
