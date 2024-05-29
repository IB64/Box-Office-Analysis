"""Script to run ETL pipeline to extract information, clean it and upload it as a csv file."""
import os

from boxoffice_api import BoxOffice
import pandas as pd

import extract as ex
import transform as tr


def upload(data: pd.DataFrame) -> None:
    """
    Writes data extracted to a csv file.
    """
    file_path = os.path.join("../data", "box_office_data.csv")
    data.to_csv(file_path, index=False)


if __name__ == "__main__":
    box_office = BoxOffice(outputformat="DF")
    data = ex.extract_information(box_office)
    clean_data = tr.clean(data)
    upload(clean_data)
