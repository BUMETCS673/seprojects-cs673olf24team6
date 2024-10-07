# Team Blockbuster - Top Movies API

#### BU MET CS673 O1: Software Engineering, Fall 2024 - Team 6

## Project Description

Team Blockbuster is creating a microservice Data Science application which will provide the ability to query and display 
movie data based on various user inputs using the Kaggle IMDB Top 250 Movies dataset: 
<https://www.kaggle.com/datasets/rajugc/imdb-top-250-movies-dataset>

## Motivation

This application provides information for people who are curious about movie trends such as movies ratings across 
different countries, movie durations, or specific movie genres and categories, etc. This information can help people 
working in the film industry or similar industries in making important movie development choices.

## Framework

This microservice based application is built using a **Python Flask** framework where **ReactJS** will be used to create 
a frontend web-page where the user can input data points and **Python** will be used to manage backend operations that 
generate the movie data based on the input data received. **SQLite** will be used as the application's database. 

Overview:

- **Frontend:** ReactJS 
- **Backend:** Python
- **Database:** SQLite

## Tools Used

The following technologies will be used for our project:

- PyCharm Community (**2024.2.2**)
- GitHub Actions
- Python (**v3.12**)
- pip (**v24.2**)
    * Python Flask
    * PyLint
    * Pandas
- Docker (**v27.2.0**)
    * Docker Compose (**v2.29.2-desktop.2**)
- Podman (**5.2.2**)
- nodeJS (**v20.17.0**)
- SQLite (**v3**)

## Installation and Set Up

##### Please install the specific versions mentioned in the **Tools Used** section above.

**PyCharm Community**

Please follow download and installation instructions from the link: 
https://www.jetbrains.com/pycharm/download/ depending on OS.

**Docker**

Please follow download and installation instructions from the link: https://www.docker.com/ depending on OS.

**Docker Compose**

Docker Compose is part of the Docker installation process.

**nodeJS**

Please follow download and installation instructions from the link: https://nodejs.org/en depending on OS. 

**Python**

Please follow download and installation instructions from the link: https://www.python.org/ depending on OS.

**pip**

pip should be installed with the Python downloaded from https://www.python.org/.

**Python Flask**

Using the Python version installed along with pip, please follow the instructions at the link: 
https://flask.palletsprojects.com/en/3.0.x/installation/.

**Pandas**
Using the Python version that is installed along with, please use pip to install: Pandas pip3 install pandas

**SQLite**

sqlite3 is part of the Python library when Python was downloaded and installed.

For more information please refer to this link: https://docs.python.org/3/library/sqlite3.html

## How to Run Software

1. Open a command line console and clone the main branch of this repository (SSH approach) in location of choice using 
   the command below:

    `git clone git@github.com:BUMETCS673/seprojects-cs673olf24team6.git`

    Note: SSH approach was used for the command above. Please follow the appropriate GitHub guidelines to set up SSH 
    keys before cloning this repository.

2. Using either file manager or a terminal window navigate to the code directory.

3. To run this application the services must be started in the correct order or an error may occur. The first service to 
   start is Python Flask
   - `cd backend` or navigate to backend directory
   - To run the application using Python use `python3 backend.py`
   - To run the application using Docker or Podman run the commands below
     - docker build -t flask_backend .
     - docker run -p 5000:5000 -t flask_backend
   
4. To Run the frontend application you need be in the /code/frontend directory.
     - To run the application using Node use `npm start`
     - To run the application using Docker or Podman run the commands below
       - docker build -t node-frontend .
       - docker run -p 3000:3000 -t node-frontend

5. At this stage in the project you will need to allow a web-browser to open or open web-browser and navigate to 
   localhost:3000 where you will be able to view the frontend application 

## How to Run Tests

### Frontend
1. From frontend directory
2. Podman/Docker build -t node_frontend .
3. Podman/Docker run -idt --name node_frontend node_frontend
4. Podman/Docker exec -it node_frontend /bin/bash
5. ` npm test`


### Backend
1. From backend directory
2. Podman/Docker build -t flask_backend .
3. Podman/Docker run -idt --name flask_backend flask_backend
4. Podman/Docker exec -it flask_backend /bin/bash
5. `cd tests`
6. `pytest process_query_request_test.py`

### Database
1. From database directory
2. Podman/Docker build -t database .
3. Podman/Docker run -idt --name database database
4. Podman/Docker exec -it database /bin/bash
5. `cd tests`
6. `pytest movies_unit_test.py`

## Credits

**Course Instructor:** Yuting Zhang

**Facilitators:** Steve Chin, Trevor Michelson

**Tools Installation Information**
* Docker: https://www.docker.com/ 
    - Docker Compose
* Podman
* nodeJS: https://nodejs.org/en
* Python: https://www.python.org/
    - pip
    - flask
    - pandas
    - pylint
* SQLite: https://docs.python.org/3/library/sqlite3.html

**Dataset Information**
* Kaggle IMDB Top 250 Movies dataset: <https://www.kaggle.com/datasets/rajugc/imdb-top-250-movies-dataset>, 
* By Chidambara Raju G (2022)

## Meet the Team

**Team Leader:** Joshua Shilts

**Requirements Leader:** Elizabeth Tyree

**Design and Implementation Leader:** Elizabeth Tyree

**Configuration Leader:** Ricky Zheng

**QA Leader:** Alex Flinchum

**Security Leader:** James Zheng

[Contributors Information](./team.md)
