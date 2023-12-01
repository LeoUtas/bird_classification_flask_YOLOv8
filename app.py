import os, sys, json, shutil

# ________________ HANDLE THE PATH THING ________________ #
# get the absolute path of the script's directory
script_path = os.path.dirname(os.path.abspath(__file__))
# get the parent directory of the script's directory
parent_path = os.path.dirname(script_path)
sys.path.append(parent_path)

from flask import Flask, render_template, request, redirect, flash, session
from Bird_classification.make_prediction import (
    YOLOv8_classifier,
    Class_indices,
)
from Bird_classification.data_ingestion import Data_ingestion
from exception import CustomException
from time import time
from datetime import datetime


UPLOAD_FOLDER = os.path.join("static", "images")
DETECT_FOLDER = os.path.join("runs", "detect", "predict")


app = Flask(__name__, static_folder="static")

class_indices_handler = Class_indices()

app.secret_key = "secret key"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["DETECT_FOLDER"] = DETECT_FOLDER


@app.route("/")
def render_index():
    return render_template("index.html", current_year=datetime.now().year)


@app.route("/YOLOv8")
def render_YOLOv8():
    return render_template("YOLOv8.html", current_year=datetime.now().year)


@app.route("/YOLOv8", methods=["POST"])
def upload_image_YOLOv8():
    try:
        if request.method == "POST":
            if "image" not in request.files:
                flash("There is no file")
                return redirect(request.url)

            image = request.files["image"]

            if image.filename == "":
                flash("No image uploaded")
                return redirect(request.url)

            if image:
                start_time = time()

                """
                The following code is to work around a bug occuring when the current image saved in the static/images has the same name with a already-uploaded one. Therefore, using time() to generate unique_image_name.
                """

                # remove previous detection/s
                path_to_remove = os.path.join(app.config["UPLOAD_FOLDER"], "detect")
                if os.path.exists(path_to_remove):
                    shutil.rmtree(path_to_remove)

                # get the original file extension (e.g., .jpg, .png)
                file_ext = os.path.splitext(image.filename)[1]
                # generate a unique filename by appending a timestamp to the original filename
                unique_image_name = f"{int(time())}{file_ext}"

                full_image_path = os.path.join(
                    app.config["UPLOAD_FOLDER"], unique_image_name
                )
                image.save(full_image_path)

                # delete the previous image if there is one
                previous_image_path = session.get("last_image_path")
                if previous_image_path and os.path.exists(previous_image_path):
                    os.remove(previous_image_path)

                # save the path of the current image for next time
                session["last_image_path"] = full_image_path

                classifier = YOLOv8_classifier(
                    app.config["UPLOAD_FOLDER"],
                )

                (
                    predicted_probability,
                    predicted_label,
                    predicted_scientific_name,
                    detection,
                ) = classifier.make_prediction()

                if detection == False:
                    full_path_to_the_image = os.path.join(
                        app.config["UPLOAD_FOLDER"], unique_image_name
                    )

                else:
                    path_to_image_source = os.path.join(
                        app.config["DETECT_FOLDER"], unique_image_name
                    )
                    path_to_image_destination = os.path.join(
                        app.config["UPLOAD_FOLDER"], "detect"
                    )

                    if not os.path.exists(path_to_image_destination):
                        os.makedirs(path_to_image_destination)

                    shutil.move(path_to_image_source, path_to_image_destination)

                    full_path_to_the_image = os.path.join(
                        path_to_image_destination,
                        unique_image_name,
                    )

                print(full_path_to_the_image)

                predicted_label = predicted_label.capitalize()
                # to handle the scientific name styling
                predicted_scientific_name = (
                    predicted_scientific_name[0].capitalize()
                    + predicted_scientific_name[1:].lower()
                )

                execution_time = round(time() - start_time, 2)

                flash(full_path_to_the_image)
                flash(round(float(predicted_probability), 4))
                flash(predicted_label)
                flash(predicted_scientific_name)
                flash(execution_time)

                return redirect("/YOLOv8")

    except Exception as e:
        raise CustomException(e, sys)


@app.route("/bird-classes")
def render_bird_classes():
    # load the class_indices.json file
    json_file_path = os.path.join(
        script_path, os.path.join("Bird_classification", "data", "class_indices.json")
    )

    with open(
        json_file_path,
        "r",
    ) as json_file:
        class_indices = json.load(json_file)

    # convert to a list of tuples
    bird_classes_list = [
        (index, info["label"], info["scientific_name"])
        for index, info in class_indices.items()
    ]

    return render_template(
        "bird_classes.html",
        bird_classes=bird_classes_list,
        current_year=datetime.now().year,
    )


@app.route("/test-imgs")
def render_test_imgs():
    image_dir = os.path.join(script_path, os.path.join("static", "test_imgs"))
    image_files = [
        file
        for file in os.listdir(image_dir)
        if file.lower().endswith((".jpg", ".jpeg"))
    ]
    image_files.sort()  # ensure files are sorted by name
    return render_template(
        "test_imgs.html", image_files=image_files, current_year=datetime.now().year
    )


if __name__ == "__main__":
    port = int(
        os.environ.get("PORT", 5000)
    )  # define port so we can map container port to localhost
    app.run(host="0.0.0.0", port=port, debug=False)  # define 0.0.0.0 for Docker
