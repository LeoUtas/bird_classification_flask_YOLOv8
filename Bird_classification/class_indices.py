import os, json, sys

# ________________ HANDLE THE PATH THING ________________ #
# get the absolute path of the script's directory
script_path = os.path.dirname(os.path.abspath(__file__))
# get the parent directory of the script's directory
parent_path = os.path.dirname(script_path)
sys.path.append(parent_path)

from exception import CustomException
from utils import get_classes


class Class_indices:
    """
    Handle the classes in the bird classification data. There are 524 classes of bird (i.e., labelling their common and scientific names). Each image is listed as a record (i.e., a row) in a CSV file containing the information of class id (i.e., class index), common name, scientific name, etc.

    """

    def __init__(self):
        json_file_path = os.path.join(
            script_path, os.path.join("data", "class_indices.json")
        )

        try:
            # check if the class_indices.json already exist
            if os.path.exists(json_file_path):
                # if the JSON exist then load class_indices from JSON file
                with open(json_file_path, "r") as json_file:
                    # load the class_indices.json with str(keys) by default
                    class_indices_str_keys = json.load(json_file)
                    # convert the str(keys) back to integers
                    self.class_indices = {
                        int(k): v for k, v in class_indices_str_keys.items()
                    }

            else:  # if the classes_indices.json doesn't exist (i.e., first time code run)
                # then, make class_indices from the .csv file and save to .json
                self.class_indices = self.make_class_indices()
                with open(json_file_path, "w") as json_file:
                    json.dump(self.class_indices, json_file)

        except Exception as e:
            raise CustomException(e, sys)

    def make_class_indices(self):
        try:
            file_path = os.path.join(script_path, "data")
            class_indices = get_classes(file_path)
            return class_indices

        except Exception as e:
            raise CustomException(e, sys)


# # test execute the script
# if __name__ == "__main__":
#     class_indices_handler = Class_indices()
#     class_indices = class_indices_handler.class_indices
#     logging.info(f"class_indices was handled successfully")
