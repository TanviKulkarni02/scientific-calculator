pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'tanvikulkarni33/scientific-calculator:latest'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/TanviKulkarni02/scientific-calculator.git'
            }
        }

        stage('Build') {
            steps {
                sh 'gradle build'
            }
        }

        stage('Test') {
            steps {
                sh 'gradle test'
            }
        }

        stage('Containerize') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

	stage('Push to Docker Hub') {
	   steps {
		  withDockerRegistry([credentialsId: 'docker-hub-credentials', url: 'https://index.docker.io/v1/']) {
	          sh 'docker push $DOCKER_IMAGE'
        }
    }
}

        stage('Deploy using Ansible') {
            steps {
                sh 'ansible-playbook -i inventory deploy.yml'
            }
        }
    }
}
