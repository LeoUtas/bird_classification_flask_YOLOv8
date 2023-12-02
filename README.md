<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
    </li>
    <li><a href="#demo">Demo</a></li>
    <li><a href="#technical-tools">Technical Tools</a></li>
    <li><a href="#data-source">Data source</a></li>
    <li><a href="#the-design">The design</a></li>
    <li><a href="#how-to-use-the-source-code">How to use the source code</a></li>
    <li><a href="#the-bottom-line">The Bottom Line</a></li>
    <li><a href="#reference">Reference</a></li>
  </ol>
</details>

### Introduction

This repository contains the source code for a web application that classifies bird species using a deep learning model developed from the architecture of You Only Look Once framework (i.e., YOLOv8). It is capable of identifying 524 different bird species, the app provides a user-friendly interface for easy image uploads and rapid species identification.

### Demo

<p align="center">
  <a href="GIF">
    <img src="/video/bird-app-yolov8.gif" width="480" alt=""/>
  </a>
</p>

### Technical tools

The orginal paper of You Only Look Once YOLO architecture <a href="https://arxiv.org/pdf/1506.02640.pdf">(Redmon, J. et al., 2016)</a>.

The application documentation of <a href="https://docs.ultralytics.com/"> YOLOv8 </a> by Ultralytics.

-   Pytorch
-   YOLOv8
-   numpy
-   pandas
-   Flask
-   JavaScript (plain)
-   HTML
-   CSS (Bootstrap)
-   Docker

### Data source

This project utilizes a bird species dataset provided by <a href="https://www.kaggle.com/gpiosenka">Gerry</a>, available on Kaggle. For detailed information, visit <a href="https://www.kaggle.com/datasets/gpiosenka/100-bird-species/data"> birds 525 species- image classification </a>.

### The design

This project is a 2-stage model application:

-   Stage 1: Using an object detection model (i.e., YOLO8n) to detect the bird in a given image;
-   Stage 2: Using a customized classification model built upon the YOLOv8 classification framework (i.e., YOLOv8n-cls) to classify the bird species.

I developed a bird classification web application with three distinct approaches:

-   A 2-stage model using YOLOv8 architecture, <a href="https://github.com/LeoUtas/bird_classification_flask_YOLOv8.git">(source code)</a>;
-   A 1-stage model using MobileNet architectures, <a href="https://github.com/LeoUtas/bird_classification_flask_MobileNet.git">(source code)</a>; and
-   A combination of the YOLOv8 and MobileNet architectures, <a href="https://github.com/LeoUtas/bird_classification_flask_2models.git">(source code)</a>

After evaluating these models, I decided to use only the MobileNet architecture for the <a href="https://bird-classification524-b310a542793a.herokuapp.com/"> final web application </a>. While the YOLO8n object detection adds functionality, it's not essential for this task and may slow down performance. However, in scenarios where object measurement is crucial, such as detecting and measuring fish samples, incorporating an object detector like YOLO8n is highly beneficial.

### How to use the source code

##### Using the source code for development

-   Fork this repository (https://github.com/LeoUtas/bird_classification_flask_YOLOv8.git)
-   Get the docker container ready

    -   Run docker build (name the app whatever you want on your local machine, and please note that it might take a while for installing all the required dependencies to your local docker image)

    ```cmd
    docker build -t <name of the app> .
    ```

    -   Run the Docker Container (once the docker image is built, you will run a docker container, map it to the port 5000)

    ```cmd
    docker run -p 5000:5000 -v "$(PWD):/app" --name <name of the container> <name of the app>
    ```

-   Run the app.py on the docker container

    -   For windows users

    ```cmd
    python app.py
    ```

    -   For MacOS and Linux users

    ```bash
    python3 app.py
    ```

    -   Change debug=False to True in app.py for development (it's crucial to asign debug=True for the ease of tracking bugs when customizing the code)

    ```python
    # the last chunk of code in the app.py
    if __name__ == "__main__":
    port = int(
        os.environ.get("PORT", 5000)
    )  # define port so we can map container port to localhost
    app.run(host="0.0.0.0", port=port, debug=False)  # define 0.0.0.0 for Docker
    ```

-   Stop running the container when you're done:

    ```cmd
    docker stop <name of the container>
    ```

### The bottom line

I'm thrilled to share it with you all! Dive in and enjoy exploring its features. A big thank you for your interest and for journeying this far with me. Wishing you a fantastic day ahead!

Best,
Hoang Ng

### Reference

Redmon, J. et al., 2016. You Only Look Once: Unified, Real-Time Object Detection. In 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR). pp. 779–788.
