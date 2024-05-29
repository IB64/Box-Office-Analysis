"""Script to transform and clean extracted data."""
import pandas as pd

def clean(data: pd.DataFrame) -> pd.DataFrame:
    """
    Function to clean the data.
    """
    # Convert "Daily" column to an integer
    data["Daily"] = data["Daily"].str.replace("$", "")
    data["Daily"] = data["Daily"].str.replace("-", "0")
    data["Daily"] = data["Daily"].str.replace(",", "").astype(int)

    # Convert "Avg" column to an integer
    data["Avg"] = data["Avg"].str.replace("$", "")
    data["Avg"] = data["Avg"].str.replace("-", "0")
    data["Avg"] = data["Avg"].str.replace(",", "").astype(int)

    # Convert "Theaters" column to an integer
    data["Theaters"] = data["Theaters"].str.replace("-", "0")
    data["Theaters"] = data["Theaters"].str.replace(",", "").astype(int)

    # Convert "To Date" column to an integer
    data["To Date"] = data["To Date"].str.replace("$", "")
    data["To Date"] = data["To Date"].str.replace("-", "0")
    data["To Date"] = data["To Date"].str.replace(",", "").astype(int)

    return data
