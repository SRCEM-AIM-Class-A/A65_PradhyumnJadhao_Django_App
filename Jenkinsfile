pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', credentialsId: 'github-credentials', url: 'https://github.com/SRCEM-AIM-Class-A/A65_PradhyumnJadhao_Django_App.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t studentproject .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 8000:8000 studentproject'
            }
        }
    }
}
