import settings as s
import sqlite3
import pandas as pd


def dataframe_to_sql():
    csv_folder = s.data_root_path / "csv"

    # Connect to SQLite
    conn = sqlite3.connect(s.db_path)

    # Load each CSV as a table
    for csv_file in csv_folder.glob("*.csv"):
        table_name = csv_file.stem  # filename = table name
        df = pd.read_csv(csv_file)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        print(f"Loaded {csv_file.name} → table {table_name}")

    conn.close()
