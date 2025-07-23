pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/henocn/devops-part-one.git'
            }
        },
        stage('Build') {
            steps {
                dir('website') {
                    sh 'python student_age.py'
                }
            }
        },
        stage('Test') {
            steps {
                dir('website') {
                    sh 'python -m unittest discover -s tests'
                }
            }
        },
        stage('Test d\'intégration') {
            steps {
                sh 'python integration_test.py'
            }
        },
        stage('Deploy') {
            steps {
                sh 'docker build -t devops .'
                sh 'docker run -d -p 80:80 devops'
            }
        }
    }
}