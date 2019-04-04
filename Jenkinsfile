pipeline {
    agent {
        dockerfile true
    }
    environment {
        COMPOSE_PROJECT_NAME = "${BUILD_TAG}"
    }
    stages {
        stage('Tests') {
            steps {
                sh 'docker-compose -f docker-compose-ci.yml up --build users_tests'
            }
            post {
                cleanup {
                    sh 'docker-compose -f docker-compose-ci.yml down --rmi local -v'
                }
            }
        }

    }
}
