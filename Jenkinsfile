pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/henocn/devops-part-one.git'
            }
        },
        stage('Build') {
            parallel {
                stage('Build Website') {
                    steps {
                        dir('website') {
                            sh 'python3 -m venv env'
                            sh '. env/Scripts/activate && pip install -r requirements.txt'
                        }
                    }
                }
                stage('Build API') {
                    steps {
                        dir('simple_api') {
                            sh 'python3 -m venv env'
                            sh '. env/Scripts/activate && pip install -r requirements.txt'
                        }
                    }
                }
            }
        },
        stage('Test') {
            parallel {
                stage('Test Website') {
                    steps {
                        dir('website') {
                            sh 'python -m unittest discover -s tests'
                        }
                    }
                }
                stage('Test API') {
                    steps {
                        dir('simple_api') {
                            sh '. env/Scripts/activate && python -m pytest tests/test_api.py --junitxml=api_report.xml'
                        }
                    }
                }
            }
        },
        stage('Test d\'intégration') {
            steps {
                sh '. env/Scripts/activate && pytest --junitxml=integration_report.xml'
            }
        },
        stage('Deploy') {
            parallel {
                stage('Deploy Website') {
                    steps {
                        dir('website') {
                            sh 'docker build -t devops-website .'
                            sh 'docker run -d -p 80:80 devops-website'
                        }
                    }
                }
                stage('Deploy API') {
                    steps {
                        dir('simple_api') {
                            sh 'docker build -t devops-api .'
                            sh 'docker run -d -p 5000:5000 devops-api'
                        }
                    }
                }
            }
        }
        stage('Rapport') {
            steps {
                junit '**/report.xml, **/api_report.xml, **/integration_report.xml'
            }
        }
    }
}