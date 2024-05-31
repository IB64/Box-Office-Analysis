"""Script to extract movie information for each day from 01/01/2000 to 01/01/2024"""
import datetime
import logging

import pandas as pd
from boxoffice_api import BoxOffice

from log_config import setup_logging

START_DATE = datetime.datetime(2023,12,1)
END_DATE = datetime.datetime(2024,1,1)


def extract_information(box_office: BoxOffice) -> pd.DataFrame:
    """
    Extracts all information.
    """
    # set up logging
    setup_logging()
    console_logger = logging.getLogger("consoleLogger")
    combined_logger = logging.getLogger("combinedLogger")

    date = START_DATE
    data_frames = []

    while date != END_DATE:
        date_as_string = date.strftime("%Y-%m-%d")

        # get information for the given day
        try:
            daily_data = box_office.get_daily(date_as_string)
        except Exception as err:
            combined_logger.error("Error for date '%s' occurred: %s", date_as_string, str(err))

        # skip if there's no data for given day
        if daily_data is not None:
            daily_data["date"] = date

            # append information to a list of dataframes to concatenate later
            console_logger.info("Information for '%s' gathered...", date_as_string)
            data_frames.append(daily_data)

        else:
            combined_logger.error("Skipped '%s' due to error...", date_as_string)

        # Go to the next day
        date += datetime.timedelta(days=1)

    # concatenate dataframes
    result = pd.concat(data_frames, ignore_index=True)

    return result
