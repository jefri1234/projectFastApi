pipeline {
    agent any

    environment {
        APP_NAME = 'fastapi-app'
        DOCKER_IMAGE = 'fastapi-image'
        DOCKER_CONTAINER = 'fastapi-container'
        PORT = '8000'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Run container') {
            steps {
                script {
                    sh "docker rm -f $DOCKER_CONTAINER || true"
                    sh "docker run -d --name $DOCKER_CONTAINER -p $PORT:8000 $DOCKER_IMAGE"
                }
            }
        }
    }
}
