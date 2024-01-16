<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
    </li>
    <li><a href="#demo">Demo</a></li>
    <li><a href="#technical-tools">Technical Tools</a></li>
    <li><a href="#data-source">Data source</a></li>
    <li><a href="#how-to-use-the-source-code">How to use the source code</a></li>
    <li><a href="#reference">Reference</a></li>
  </ol>
</details>

### Introduction

<ul style="padding-left: 20px; list-style-type: circle;">
        <li>The project includes 4 repositories:
            <ul>                
                <li>
                <a href="https://github.com/LeoUtas/bird_classification_research.git" style="text-decoration: none; color: #3498db;">Bird classification research</a>
                </li>
                <li>
                <a href="https://github.com/LeoUtas/bird_classification_flask_MobileNet.git" style="text-decoration: none; color: #3498db;">Bird classification web application using MobileNet model</a>
                </li>
                <li>
                <a href="https://github.com/LeoUtas/bird_classification_flask_YOLOv8.git" style="text-decoration: none; color: #3498db;">Bird classification web application using YOLOv8 model</a>
                </li>
                <li>
                <a href="https://github.com/LeoUtas/bird_classification_flask_2models.git">Bird classification web app using MobileNet and YOLOv8 for better comparing model performances</a>
                </li>                                
            </ul>
        </li>
        <br>
        <li>
            I attempted to solve the task using 4 different tools (i.e., InceptionV3, MobileNetV1, MobileNetV2 and YOLOv8). After evaluating performance metrics and processing speed, MobileNetV1 was chosen as the most suitable model for this task <a href="https://bird-classification524-b310a542793a.herokuapp.com/">(visit the live demo)</a>.
        </li>        
    </ul>

This repository offers source code for a web application using YOLOv8.

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

### How to use the source code

##### use the source code

-   Fork/clone this repository (https://github.com/LeoUtas/bird_classification_flask_YOLOv8.git)
-   Get the docker container ready

    -   Run docker build (name the app whatever you want on your local machine, and please note that it might take a while for installing all the required dependencies to your local docker image)

    ```cmd
    docker build -t <name of the docker image> .
    ```

    -   Run the Docker Container (once the docker image is built, you will run a docker container, map it to the port 5000)

    ```cmd
    docker run -p 5000:5000 -v "$(PWD):/app" --name <name of the container> <name of the docker image>
    ```

I'm thrilled to share it with you all! Dive in and enjoy exploring its features. A big thank you for your interest and for journeying this far with me. Wishing you a fantastic day ahead!

Best,
Hoang Ng

### Reference

Redmon, J. et al., 2016. You Only Look Once: Unified, Real-Time Object Detection. In 2016 IEEE Conference on Computer Vision and Pattern Recognition (CVPR). pp. 779–788.
