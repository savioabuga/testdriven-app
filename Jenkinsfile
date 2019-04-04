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
                sh 'docker-compose -f docker-compose-ci.yml up --build users_tests'
            }
        }
    }
}
