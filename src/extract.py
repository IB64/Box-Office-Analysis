"""Script to extract movie information for each day from 01/01/2000 to 01/01/2024"""
import datetime
import logging

import pandas as pd
from boxoffice_api import BoxOffice

from log_config import setup_logging

START_DATE = datetime.datetime(2020,3,27)
END_DATE = datetime.datetime(2020,4,6)


def extract_information(box_office: BoxOffice) -> pd.DataFrame:
    """
    Extracts all information.
    """
    # set up logging
    setup_logging()
    logger = logging.getLogger(__name__)

    date = START_DATE
    data_frames = []

    while date != END_DATE:
        date_as_string = date.strftime("%Y-%m-%d")

        # get information for the given day
        try:
            daily_data = box_office.get_daily(date_as_string)
        except Exception as err:
            logger.error(f"Error for date '{date_as_string}' occurred: {str(err)}")

        # skip if there's no data for given day
        if daily_data is not None:
            daily_data["date"] = date

            # append information to a list of dataframes to concatenate later
            logger.info(f"Information for '{date_as_string}' gathered...")
            data_frames.append(daily_data)

        else:
            logger.error(f"Skipped '{date_as_string}' due to error...")

        # Go to the next day
        date += datetime.timedelta(days=1)
    
    # concatenate dataframes
    result = pd.concat(data_frames, ignore_index=True)

    return result
