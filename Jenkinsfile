pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('DockerHubCredentials')
        IMAGE_NAME = 'manikirangutthula2004/ticket-booking-app'
        KUBECONFIG = credentials('kubeconfig')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
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


        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}:${env.BUILD_ID}")
                }
            }
        }

        stage('Test Docker Image') {
            steps {
                bat """
                docker run -d --name test-app ${IMAGE_NAME}:${env.BUILD_ID}
                timeout /t 20 >nul
                curl -f http://localhost:5000 || exit /b 1
                docker stop test-app
                docker rm test-app
                """
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'DockerHubCredentials') {
                        docker.image("${IMAGE_NAME}:${env.BUILD_ID}").push()
                        docker.image("${IMAGE_NAME}:latest").push()
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat """
                kubectl apply -f k8s/
                kubectl rollout status deployment/ticket-booking-app
                """
            }
        }
    }

    post {
        always {
            bat 'docker system prune -f'
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
