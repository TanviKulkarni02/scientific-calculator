pipeline {
    agent any

    environment {
        // Docker Hub credentials (store these in Jenkins credentials)
        DOCKER_HUB_CREDENTIALS = credentials('docker-hub-credentials')
        DOCKER_IMAGE = "tanvikulkarni33/scientific-calculator:latest"
    }

    stages {
        // Stage 1: Pull code from GitHub
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/TanviKulkarni02/scientific-calculator.git'
            }
        }

        // Stage 2: Run unit tests
        stage('Run Unit Tests') {
            steps {
                sh 'python3 -m unittest test_calculator.py'
            }
        }

        // Stage 3: Build Docker image
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t tanvikulkarni33/scientific-calculator .'
                }
            }
        }

        // Stage 4: Push Docker image to Docker Hub
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
			docker.image("${DOCKER_IMAGE}").push()                     
                    }
                }
            }
        }

        // Stage 5: Deploy using Ansible
        stage('Deploy with Ansible') {
            steps {
                ansiblePlaybook(
                    playbook: 'ansible/deploy.yml',
                    inventory: 'ansible/inventory',
                    credentialsId: 'ansible-ssh-credentials' // Store SSH credentials in Jenkins
                )
            }
        }
    }

    post {
        // Actions to perform after the pipeline completes
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the logs for details.'
        }
    }
}
