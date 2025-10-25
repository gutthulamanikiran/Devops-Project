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
                bat '''
                    REM Remove any previous test container
                    docker rm -f test-app || echo No existing container
        
                    REM Run container with port mapping
                    docker run -d -p 5000:5000 --name test-app manikirangutthula2004/ticket-booking-app:7
                    
                    REM Wait for the container to start
                    timeout /t 20
            
                    REM Test if the app is responding
                    curl -f http://localhost:5000
                    '''
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
