# Homework 6: Data Preprocessing

This project demonstrates a modular workflow for cleaning the raw `sample_data.csv`.

The entire process is executed in `notebooks/preprocessing_notebook.ipynb` using reusable functions from `src/cleaning.py`. The cleaning strategy involves three main steps:

-   Dropping columns with over 50% missing values.
-   Filling remaining missing values in numeric columns (`age`, `income`, `score`) with the median.
-   Scaling these numeric columns to a [0, 1] range using a Min-Max scaler.

The final, analysis-ready dataset is saved to the `data/processed/` directory.