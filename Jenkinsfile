pipeline {
    agent any
    environment {
        IMAGE_NAME = 'hello-flask'
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/MaglioccoBSI/flask-docker-customers'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }
        stage('Deploy Customers') {
            steps {
                script {
                    def customers = ['customer1', 'customer2', 'customer3']
                    for (c in customers) {
                        sh "docker run -d -p $((5000 + customers.indexOf(c))):5000 -e CUSTOMER=$c $IMAGE_NAME"
                    }
                }
            }
        }
    }
}