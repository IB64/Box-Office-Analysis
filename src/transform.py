"""Script to transform and clean extracted data."""
import logging

import pandas as pd

from log_config import setup_logging


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


def convert_to_int(value):
    """
    Function to convert comma separated or monetary values to integers.
    """
    if value == "-":
        return 0
    else:
        value = value.replace("$", "").replace(",", "")
        return int(value)


def clean(data: pd.DataFrame) -> pd.DataFrame:
    """
    Function to clean the data.
    """
    # set up logging
    setup_logging()
    console_logger = logging.getLogger("consoleLogger")
    combined_logger = logging.getLogger("combinedLogger")

    # Clean Daily column
    try:
        data["Daily"] = data["Daily"].apply(convert_to_int)
        console_logger.info("Daily columned cleaned...")
    except Exception as err:
        combined_logger.error(f"Error while cleaning Daily column: {str(err)}")

    # Clean change in YD column
    try:
        data["%± YD"] = data["%± YD"].apply(convert_percentage)
        console_logger.info("%± YD columned cleaned...")
    except Exception as err:
        combined_logger.error(f"Error while cleaning %± YD column: {str(err)}")

    # Clean change in LW column
    try:
        data["%± LW"] = data["%± LW"].apply(convert_percentage)
        console_logger.info("%± LW columned cleaned...")
    except Exception as err:
        combined_logger.error(f"Error while cleaning %± LW column: {str(err)}")

    # Convert "Theaters" column to an integer
    try:
        data["Theaters"] = data["Theaters"].apply(convert_to_int)
        console_logger.info("Theaters columned cleaned...")
    except Exception as err:
        combined_logger.error(f"Error while cleaning Theaters column: {str(err)}")

    # Convert "Avg" column to an integer
    try:
        data["Avg"] = data["Avg"].apply(convert_to_int)
        console_logger.info("Avg columned cleaned...")
    except Exception as err:
        combined_logger.error(f"Error while cleaning Avg column: {str(err)}")

    # Convert "To Date" column to an integer
    try:
        data["To Date"] = data["To Date"].apply(convert_to_int)
        console_logger.info("To Date columned cleaned...")
    except Exception as err:
        combined_logger.error(f"Error while cleaning To Date column: {str(err)}")

    # Clean Days column
    try:
        data["Days"] = data["Days"].apply(convert_to_int)
        console_logger.info("Days columned cleaned...")
    except Exception as err:
        combined_logger.error(f"Error while cleaning Days column: {str(err)}")

    # Clean Distributor  column
    try:
        data["Distributor"] = data["Distributor"].str.replace("-", "N/A")
        console_logger.info("Distributor columned cleaned...")
    except Exception as err:
        combined_logger.error(f"Error while cleaning Distributor column: {str(err)}")

    return data
