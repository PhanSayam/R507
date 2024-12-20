pipeline {
    agent any
    environment {
        DOCKER_IMAGE = "phandamien/devops-app"
    }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/PhanSayam/R507.git'
            }
        }
        stage('Start ngrok') {
            steps {
                sh 'ngrok http 5000 & sleep 5'
            }
        }
        stage('Get ngrok URL') {
            steps {
                script {
                    def url = sh(script: "curl -s http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url'", returnStdout: true).trim()
                    echo "Ngrok URL: ${url}"
                }
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'python -m unittest discover tests'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }
        stage('Security Scan') {
            steps {
                sh 'trivy image $DOCKER_IMAGE || exit 1'
            }
        }
        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    sh 'docker push $DOCKER_IMAGE'
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment/deployment.yaml'
                sh 'kubectl apply -f deployment/service.yaml'
            }
        }
        stage('Canary Deployment') {
            steps {
                sh 'kubectl apply -f deployment/canary-deployment.yaml'
            }
        }
    }
}
