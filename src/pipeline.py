"""Script to run ETL pipeline to extract information, clean it and upload it as a csv file."""
import logging
import os
from time import perf_counter

from boxoffice_api import BoxOffice
import pandas as pd

import extract as ex
from log_config import setup_logging
import transform as tr


def upload(data: pd.DataFrame) -> None:
    """
    Writes data extracted to a csv file.
    """
    file_path = os.path.join("../data", "box_office_data.csv")
    data.to_csv(file_path, index=False)


if __name__ == "__main__":
    # set up logging
    setup_logging()
    combined_logger = logging.getLogger("combinedLogger")

    combined_logger.info("Starting Process...")
    start = perf_counter()
    box_office = BoxOffice(outputformat="DF")

    # Extraction
    combined_logger.info(f"Extraction Starting...")
    extraction_start_time = perf_counter()
    data = ex.extract_information(box_office)
    combined_logger.info(f"Extraction Done! Time taken: {perf_counter() - extraction_start_time} seconds | Total time elapsed: {perf_counter() - start}")

    # Cleaning
    combined_logger.info(f"Cleaning Starting...")
    cleaning_start_time = perf_counter()
    clean_data = tr.clean(data)
    combined_logger.info(f"Cleaning Done! Time taken: {perf_counter() - cleaning_start_time} seconds | Total time elapsed: {perf_counter() - start}")

    # Uploading
    combined_logger.info(f"Uploading to csv file...")
    upload(clean_data)

    combined_logger.info(f"Process Done! Total time elapsed: {perf_counter() - start} seconds.")
