pipeline {
    agent any
    
    environment {
        DOCKERHUB_CREDENTIALS = credentials('Docker')
        IMAGE_NAME = 'your-dockerhub-username/ticket-booking-app'
        KUBECONFIG = credentials('kubeconfig')
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
                // Add your actual test commands here
                sh 'python -m pytest tests/ || true'
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
                sh """
                docker run -d --name test-app ${IMAGE_NAME}:${env.BUILD_ID}
                sleep 10
                curl -f http://localhost:5000 || exit 1
                docker stop test-app
                docker rm test-app
                """
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        docker.image("${IMAGE_NAME}:${env.BUILD_ID}").push()
                        docker.image("${IMAGE_NAME}:latest").push()
                    }
                }
            }
        }
        
        stage('Deploy to Kubernetes') {
            steps {
                sh """
                kubectl apply -f k8s/
                kubectl rollout status deployment/ticket-booking-app
                """
            }
        }
    }
    
    post {
        always {
            sh 'docker system prune -f'
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