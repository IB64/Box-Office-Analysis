"""Script to transform and clean extracted data."""
import pandas as pd


def convert_percentage(value):
    """
    Function to convert percentage strings to floats.
    """
    if value == "-":
        return 0.0
    else:
        # Remove the '%' and convert to float
        value = value.replace(",", "").replace("+", "").replace("%", "").replace("<", "")
        return float(value)


def clean(data: pd.DataFrame) -> pd.DataFrame:
    """
    Function to clean the data.
    """
    # Convert "Daily" column to an integer
    data["Daily"] = data["Daily"].str.replace("$", "")
    data["Daily"] = data["Daily"].str.replace("-", "0")
    data["Daily"] = data["Daily"].str.replace(",", "").astype(int)

    # Clean change in YD  column
    data["%± YD"] = data["%± YD"].apply(convert_percentage)

    # Clean change in LW  column
    data["%± LW"] = data["%± LW"].apply(convert_percentage)

    # Convert "Theaters" column to an integer
    data["Theaters"] = data["Theaters"].str.replace("-", "0")
    data["Theaters"] = data["Theaters"].str.replace(",", "").astype(int)

    # Convert "Avg" column to an integer
    data["Avg"] = data["Avg"].str.replace("$", "")
    data["Avg"] = data["Avg"].str.replace("-", "0")
    data["Avg"] = data["Avg"].str.replace(",", "").astype(int)

    # Convert "To Date" column to an integer
    data["To Date"] = data["To Date"].str.replace("$", "")
    data["To Date"] = data["To Date"].str.replace("-", "0")
    data["To Date"] = data["To Date"].str.replace(",", "").astype(int)

    # Clean Days  column
    data["Days"] = data["Days"].str.replace("-", "0").astype(int)

    # Clean Distributor  column
    data["Distributor"] = data["Distributor"].str.replace("-", "N/A")

    return data
