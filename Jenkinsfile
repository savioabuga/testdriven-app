pipeline {
    agent {
        dockerfile true
    }
    environment {
        COMPOSE_PROJECT_NAME = "${BUILD_TAG}"
    }
    stages {
        stage('checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[url: 'https://github.com/savioabugah/testdriven-app']]])
            }
        }
        stage('Tests') {
            steps {
                sh 'docker-compose -f docker-compose-dev.yml up -d --build'
                sh 'docker ps'
                sh 'docker-compose -f docker-compose-dev.yml exec ${BUILD_TAG}_users flake8 project'
                sh 'docker-compose -f docker-compose-dev.yml exec ${BUILD_TAG}_client npm test -- --coverage'
                sh 'docker-compose -f docker-compose-dev.yml down'
            }
        }
    }
}
