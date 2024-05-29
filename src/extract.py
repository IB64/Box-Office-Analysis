"""Script to extract movie information for each day from 01/01/2000 to 01/01/2024"""
import datetime

import pandas as pd
from boxoffice_api import BoxOffice

START_DATE = datetime.datetime(2023,12,1)
END_DATE = datetime.datetime(2024,1,1)


def extract_information(box_office: BoxOffice) -> pd.DataFrame:
    """
    Extracts all information.
    """
    date = START_DATE
    data_frames = []
    while date != END_DATE:
        # get information for the given day
        daily_data = box_office.get_daily(date.strftime("%Y-%m-%d"))
        daily_data["date"] = date

        # append information to a list of dataframes to concatenate later
        data_frames.append(daily_data)

        print(f"Information for {date} gathered...")

        # Go to the next day
        date += datetime.timedelta(days=1)
    
    # concatenate dataframes
    result = pd.concat(data_frames, ignore_index=True)

    return result
