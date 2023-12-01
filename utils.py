import pandas as pd
from exception import CustomException
import os, sys


def get_classes(file_path):
    """
    This function is to read a CSV file named "birds.csv", then to parse and return a dictionary that maps class IDs to their respective labels and scientific names.

    Parameters:
    - file_path (str): The path where the "birds.csv" file is located.

    Returns:
    - dict: A dictionary where each key is a class ID (int), and each value is another      dictionary containing two key-value pairs:
        - "label" (str): The common name of the bird class.
        - "scientific_name" (str): The scientific name of the bird class.

    """

    try:
        # read in the CSV file
        birds_df = pd.read_csv(os.path.join(file_path, "birds.csv"))

        # remove all information related to the label "LOONEY BIRDS"
        birds_df = birds_df[birds_df["labels"] != "LOONEY BIRDS"]

        # get unique labels and sort them
        unique_labels = sorted(birds_df["labels"].unique())

        # create a dictionary to hold index, label, and scientific_name
        class_dict = {
            index: {
                "label": label,
                "scientific_name": birds_df[birds_df["labels"] == label][
                    "scientific name"
                ].iloc[0],
            }
            for index, label in enumerate(unique_labels)
        }

        return class_dict

    except Exception as e:
        raise CustomException(e, sys)
