# 🏫 StudentProject - Django Multi-App with Docker & Jenkins  

## 📖 Project Overview  
StudentProject is a Django-based web application that contains multiple apps demonstrating fundamental Django functionalities, including navigation, routing, and templates. The project is containerized using **Docker** and is set up for **CI/CD automation** using **Jenkins**.  

## 🚀 Features  
- **Multi-App Structure**: Separate apps (`app1`, `app2`, etc.) with individual static pages.  
- **Navigation Links**: Home, About, and App2 pages with Django templates.  
- **Dockerized**: Runs as a containerized application with `Docker`.  
- **Jenkins Integration**: Automates deployment using a Jenkins pipeline.   

Install Dependencies
pip install -r requirements.txt

Apply Migrations
python manage.py migrate

Run the Django Server
python manage.py runserver

🐳 Run Using Docker

Build the Docker Image
docker build -t studentproject .

Run the Container
docker run -p 8000:8000 studentproject

🏗 Jenkins Pipeline Setup

1️⃣ Start Jenkins Container

docker run -d --name myjenkins -p 8080:8080 -p 50000:50000 \
-v /var/run/docker.sock:/var/run/docker.sock \
-v jenkins_home:/var/jenkins_home jenkins/jenkins:lts

2️⃣ Unlock Jenkins

Find the admin password using:
docker exec -it myjenkins cat /var/jenkins_home/secrets/initialAdminPassword
Access Jenkins and enter the password.

3️⃣ Create a New Pipeline

In Jenkins, create a new Pipeline Job.
Use your GitHub repo URL in the SCM (Source Code Management) section.
Jenkins will automatically build and deploy the project.

