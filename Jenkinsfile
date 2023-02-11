pipeline {
    agent any
    stages {
        stage('Building'){
            steps{
                bat 'pip install -r requirements.txt'
            }
        }
        stage('Deploying'){
            steps{
                bat 'docker pull mongo'
                bat 'docker build . --file Dockerfile --tag webscrapping_api'
                bat 'docker-compose up --build -d'
            }
        }
    }
}