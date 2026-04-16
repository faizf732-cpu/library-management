Run cm as administrator 
-   cd "\Program Files\Jenkins"
-   Java -jar jenkins.war
-   Java -jar jenkins.war --httpPort=8080/9090





Maven

dir

git remote -v
git remote remove origin
git remote add origin https://github.com/yourusername/maven-project.git
git remote -v (if error means)

git add .
git commit -m "Initial commit"
git branch -M main
git remote remove origin
git remote add origin https://github.com/yourusername/maven-project.git

Docker
kubectl get nodes


I don’t see your PDF attached here. Please upload it so I can extract exact commands from your file.

Meanwhile, based on your setup (GitHub + Jenkins + Docker pipeline), here are the standard commands you’re using, written exactly how you asked:


---

🧾 Git Commands

git init
# initialize new git repository (if starting fresh)

git clone <repo_url>
# clone project from GitHub to local

git status
# check current changes / untracked files

git add .
# add all files to staging area

git commit -m "message"
# save changes locally with message

git branch
# check current branch

git branch -M main
# rename branch to main (fix branch issue)

git remote add origin <repo_url>
# connect local repo to GitHub (fix 'origin not found' error)

git remote -v
# verify remote URL added correctly

git push -u origin main
# push code to GitHub (first time setup)

git pull origin main
# pull latest code from GitHub


---

🧾 Maven Commands

mvn clean
# delete previous build files (target folder)

mvn compile
# compile project source code

mvn test
# run test cases

mvn package
# create .jar/.war file

mvn clean install
# full build + install into local repository (most used)


---

🧾 Docker Commands

docker version
# check docker installed and running

docker info
# check docker engine status (debug errors like yours)

docker build -t <image_name> .
# build docker image from Dockerfile

docker images
# list all docker images

docker run -d -p 8080:80 <image_name>
# run container in background and map port

docker ps
# show running containers

docker ps -a
# show all containers

docker stop <container_id>
# stop running container

docker rm <container_id>
# remove container

docker rmi <image_name>
# remove docker image

docker login
# login to Docker Hub

docker tag <image> <username>/<repo>:latest
# tag image for push

docker push <username>/<repo>
# push image to Docker Hub


---

🧾 Jenkins (Pipeline related commands inside script)

git 'https://github.com/username/repo.git'
# clone repo in Jenkins pipeline

bat 'mvn clean install'
# run maven build in Windows Jenkins

bat 'docker build -t image_name .'
# build docker image in pipeline

bat 'docker push username/repo'
# push image to Docker Hub


---

🧾 WSL / Docker Fix Commands (for your error)

wsl --shutdown
# stop all WSL processes (fix docker stuck loading)

wsl --update
# update WSL backend

wsl --unregister docker-desktop
# reset docker backend (fix serious errors)

wsl --unregister docker-desktop-data
# clear docker data


---

🚀 IMPORTANT (your mistake reminder)

git remote add origin <repo_url>
# FIX: origin not found error

docker info
# FIX: check docker 500 error

wsl --shutdown
# FIX: docker loading issue


Jenkins -- Username : Faiz_jen
bd4dfe1014cc4c13a7055342b4204237

git push -u origin main




Pipelines:

pipeline {
    agent any
    # runs pipeline on any available agent/node

    stages {

        stage('Build') {
            # Build stage
            steps {
                echo 'Build Stage Running'
                # prints message to console (used for testing pipeline)
            }
        }

        stage('Test') {
            # Test stage
            steps {
                echo 'Test Stage Running'
                # prints message to console (used to simulate testing)
            }
        }

        stage('Deploy') {
            # Deploy stage
            steps {
                echo 'Deploy Stage Running'
                # prints message to console (used to simulate deployment)
            }
        }

    }
}
