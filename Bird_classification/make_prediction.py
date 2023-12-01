import os, sys, shutil, cv2

# ________________ HANDLE THE PATH THING ________________ #
# get the absolute path of the script's directory
script_path = os.path.dirname(os.path.abspath(__file__))
# get the parent directory of the script's directory
parent_path = os.path.dirname(script_path)
sys.path.append(parent_path)

from exception import CustomException
from Bird_classification.class_indices import Class_indices
from ultralytics import YOLO


class YOLOv8_classifier:
    """
    The core part of the project. It loads a chosen model of YOLOv8, class indices and retrieve uploaded images to use in prediction generating a series of probabilities for class indices, the class index, with the highest probability, will be chosen and mapped with its label (i.e., common name) and scientific name.

    """

    def __init__(self, path_to_images):
        """

        This initialization part is to load required items, including a chosen model, class indices, and the test image.

        """

        self.path_to_chosen_model = os.path.join(
            script_path, "models", "YOLOv8", "last.pt"
        )
        self.path_to_images = path_to_images

        Class_indices_handler = Class_indices()
        self.class_indices = Class_indices_handler.make_class_indices()

        self.detect_model = YOLO("yolov8n.pt")

        self.classify_model = YOLO(self.path_to_chosen_model)

        # remove previous detection/s
        path_to_remove = os.path.join(parent_path, "runs")
        if os.path.exists(path_to_remove):
            shutil.rmtree(path_to_remove)

    # ________________ MAKE PREDICTION IMAGES ________________ #
    def make_prediction(self):
        """

        This function handles the prediciton process.

        """

        try:
            # Process each image in the bird class folder
            for image in os.listdir(self.path_to_images):
                if image.lower().endswith((".jpg", ".jpeg", ".png")):
                    path_to_the_image = os.path.join(self.path_to_images, image)

                    image_org = cv2.imread(path_to_the_image)

                    detected_results = self.detect_model(path_to_the_image, save=True)
                    bboxes = detected_results[0].boxes.xyxy.cpu().numpy().reshape(-1, 4)

                    detection = True
                    if bboxes.size > 0:
                        for bbox in bboxes:
                            x1, y1, x2, y2 = map(int, bbox)
                            # Crop the image
                            image_to_use = image_org[y1:y2, x1:x2]
                    else:
                        detection = False
                        image_to_use = image_org

                    # prediction = self.classify_model.predict(image_to_use, device="cpu")
                    prediction = self.classify_model.predict(
                        path_to_the_image, device="cpu"
                    )
                    predicted_index = prediction[0].probs.top1
                    predicted_probability = prediction[0].probs.top1conf

                    prediction_dict = self.class_indices[predicted_index]
                    predicted_label = prediction_dict["label"]
                    predicted_scientific_name = prediction_dict["scientific_name"]

            return (
                predicted_probability,
                predicted_label,
                predicted_scientific_name,
                detection,
            )

        except Exception as e:
            # CustomException should be defined elsewhere in your code
            raise CustomException(e, sys)
