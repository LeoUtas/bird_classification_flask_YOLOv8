<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#introduction">Introduction</a>
    </li>
    <li><a href="#demo">Demo</a></li>
    <li><a href="#technical-tools">Technical Tools</a></li>
    <li><a href="#how-to-use-the-source-code">How to use the source code</a></li>
    <li><a href="#the-bottom-line">The Bottom Line</a></li>
  </ol>
</details>

### Introduction

This repository contains the source code for a web application that classifies bird species using a deep learning model developed from YOLOv8. It is capable of identifying 524 different bird species, the app provides a user-friendly interface for easy image uploads and rapid species identification.

### Demo

<p align="center">
  <a href="Video URL">
    <img src="/video/bird-app524.gif" width="480" alt="Alt text for the image"/>
  </a>
</p>

### Technical tools

-   Pytorch
-   YOLOv8
-   numpy
-   pandas
-   Flask
-   JavaScript (plain)
-   HTML
-   CSS (Bootstrap)
-   Docker

### How to use the source code

##### Using the source code for development

-   Fork this repository (https://github.com/LeoUtas/bird_classification_flask_YOLOv8.git)
-   Install required dependencies

    -   Run docker build (name the app whatever you want on your local machine):

    ```cmd
    docker build -t <name of the app> .
    ```

    -   Run the Docker Container

    ```cmd
    docker run -p 5000:5000 -v $(pwd):/app --name <name of the container> <name of the app>
    ```

    -   Change debug=False to True for development (if you wish)

    ```python
    # the last chunk of code in the app.py
    if __name__ == "__main__":
    port = int(
        os.environ.get("PORT", 5000)
    )  # define port so we can map container port to localhost
    app.run(host="0.0.0.0", port=port, debug=False)  # define 0.0.0.0 for Docker
    ```

    -   For windows users:

    ```cmd
    python app.py
    ```

    -   For MacOS and Linux users

    ```bash
    python3 app.py
    ```

    -   Stop running the container when you're done:

    ```cmd
    docker stop <name of the container>
    ```

### The bottom line

I'm thrilled to share it with you all! Dive in and enjoy exploring its features. A big thank you for your interest and for journeying this far with me. Wishing you a fantastic day ahead!

Best,
Hoang Ng
