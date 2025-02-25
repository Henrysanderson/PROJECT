"""
Preprocessing Script for Gaia Data

This script performs the following preprocessing steps:
1. Loads the raw Gaia dataset.
2. Handles missing values by either dropping or filling them.
3. Selects relevant features for analysis.
4. Standardizes the selected features for consistency.
5. Saves the cleaned data for further analysis or modeling.

Author: Henry Sanderson Viyuyi
Date: 19/02/2025
"""

import pandas as pd
import numpy as np

# Preprocess Gaia Data FUnction
def preprocess_gaia_data(file_path):
    df = pd.read_csv(file_path)

    # Remove entries with negative parallax
    df = df[df['parallax'] > 0]

    # Compute new features
    df['distance'] = 1 / df['parallax']
    df['pm_total'] = np.sqrt(df['pmra']**2 + df['pmdec']**2)

    # Normalize data (optional)
    df[['ra', 'dec', 'distance', 'pm_total']] = (df[['ra', 'dec', 'distance', 'pm_total']] - df[['ra', 'dec', 'distance', 'pm_total']].mean()) / df[['ra', 'dec', 'distance', 'pm_total']].std()

    df.to_csv("D:/Desktop/PROJECT/data/processed/gaia_cleaned.csv", index=False)
    return df

# Run script
if __name__ == "__main__":
    preprocess_gaia_data("D:/Desktop/PROJECT/data/raw/Gaia_DR3-2025-02-19-07-45-37-759132.csv")
