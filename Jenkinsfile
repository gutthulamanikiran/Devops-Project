pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials') // Replace with your Jenkins credentials ID
        DOCKER_IMAGE = "manikirangutthula2004/ticket-booking-app:5"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', credentialsId: 'Manikiran', url: 'https://github.com/gutthulamanikiran/Devops-Project.git'
            }
        }

        stage('Precheck') {
            steps {
                bat '''
                    echo Checking Docker status...
                    docker version || (echo Docker is not running! && exit /b 1)
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                    echo Running tests...
                    python --version
                    python -m ensurepip
                    python -m pip install --upgrade pip
                    python -m pip install pytest

                    echo Running pytest on tests directory...
                    python -m pytest tests/ || exit /b 1
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '''
                    echo Building Docker image...
                    docker build -t "%DOCKER_IMAGE%" .
                '''
            }
        }

        stage('Test Docker Image') {
            steps {
                bat '''
                    echo Running container for testing...
                    docker run -d -p 5000:5000 --name test-app %DOCKER_IMAGE%

                    echo Waiting for container to start...
                    powershell -Command "Start-Sleep -Seconds 10"

                    echo Checking app health...
                    curl -f http://localhost:5000 || (echo App test failed! && exit /b 1)

                    echo App is running successfully.
                    docker stop test-app
                    docker rm test-app
                '''
            }
        }

        stage('Push to Docker Hub') {
            when {
                expression { currentBuild.currentResult == 'SUCCESS' }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKERHUB_USER', passwordVariable: 'DOCKERHUB_PASS')]) {
                    bat '''
                        echo Logging in to Docker Hub...
                        echo %DOCKERHUB_PASS% | docker login -u %DOCKERHUB_USER% --password-stdin

                        echo Pushing image to Docker Hub...
                        docker push %DOCKER_IMAGE%
                    '''
                }
            }
        }

        stage('Deploy to Kubernetes') {
            when {
                expression { currentBuild.currentResult == 'SUCCESS' }
            }
            steps {
                bat '''
                    echo Deploying to Kubernetes...
                    kubectl apply -f k8s-deployment.yaml
                '''
            }
        }
    }

    post {
        always {
            bat '''
                echo Cleaning up Docker...
                docker system prune -f
            '''
            cleanWs()
        }
        failure {
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline executed successfully!'
        }
    }
}
