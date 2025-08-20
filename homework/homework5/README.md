---
## Data Storage Strategy (Homework 5)

This project uses a structured approach for data storage, managed by environment variables and utility functions.

* **Folder Structure**:
    * `data/raw/`: Stores immutable raw data, typically in CSV format.
    * `data/processed/`: Stores cleaned, processed, and optimized data, typically in Parquet format.

* **Formats Used**:
    * **CSV**: Used for raw data due to its universal readability and simplicity.
    * **Parquet**: Used for processed data because it is a columnar format that is highly efficient for storage and fast for analytical queries.

* **Configuration**:
    * File paths are not hardcoded. They are managed via a `.env` file, which defines `DATA_DIR_RAW` and `DATA_DIR_PROCESSED`. This makes the code portable and configurable.