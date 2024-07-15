pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/vikasmyself/selenium-docker.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest --json=pytest_config.json --alluredir=reports/allure-results'
            }
        }
        stage('Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: '/Users/vmata/Documents/New_Sess/selenium-docker/reports/allure-results']]
            }
        }
    }
}
