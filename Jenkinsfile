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
                    sh 'python3 -m venv env'
                    sh '. env/Scripts/activate && pip install -r requirements.txt'
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
                sh '. env/Scripts/activate && pytest --junitxml=report.xml'
            }
        },
        stage('Deploy') {
            steps {
                sh 'docker build -t devops .'
                sh 'docker run -d -p 80:80 devops'
            }
        }
        stage('Rapport') {
            steps {
                junit 'report.xml'
            }
        }
    }
}