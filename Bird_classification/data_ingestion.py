import os, sys, shutil


# ________________ HANDLE THE PATH THING ________________ #
# get the absolute path of the script's directory
script_path = os.path.dirname(os.path.abspath(__file__))
# get the parent directory of the script's directory
parent_path = os.path.dirname(script_path)
sys.path.append(parent_path)


from exception import CustomException
from dataclasses import dataclass
from tensorflow.keras.preprocessing import image
import numpy as np
from ultralytics import YOLO


@dataclass
class Data_ingestion_path_config:
    """

    This class is to handle the path directing to where the images located.

    """

    data_ingestion_path: str = os.path.join(
        parent_path, os.path.join("static", "images")
    )


class Data_ingestion:
    """

    This class is to make a pipeline to the location where uploaded images are located and retrieved them, then preprocess making them ready as input going to the prediction.

    """

    def __init__(self, file_name):
        self.data_ingestion_path = Data_ingestion_path_config()
        self.file_name = file_name

        self.detect_model = YOLO("yolov8n.pt")

        # remove previous detection/s
        path_to_runs = os.path.join(parent_path, "runs")
        if os.path.exists(path_to_runs):
            shutil.rmtree(path_to_runs)

    def make_data_in(self):
        """

        This function goes to the location of uploaded images, get the image and preprocess it making it ready for using in prediction.

        """

        try:
            # make the image ready for prediction
            image_name = self.file_name
            image_path = self.data_ingestion_path.data_ingestion_path

            if image_name.lower().endswith((".jpg", ".jpeg", ".png")):
                full_image_path = os.path.join(image_path, image_name)
            detected_results = self.detect_model(full_image_path, save=True)

            test_image = image.load_img(full_image_path, target_size=(224, 224))
            test_image = image.img_to_array(test_image) / 255.0
            test_image = np.expand_dims(test_image, axis=0)

            return test_image

        except Exception as e:
            raise CustomException(e, sys)


# test execute the script
# if __name__ == "__main__":
#     image_name = "1.jpg"
#     Data_ingestion = Data_ingestion(image_name)
#     image = Data_ingestion.make_data_in
#     logging.info(f"{image_name} is ready for prediction")
