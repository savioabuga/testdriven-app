pipeline {
    agent {
        dockerfile true
    }
    environment {
        COMPOSE_PROJECT_NAME = "${BUILD_TAG}"
    }
    stages {
        // stage('Tests') {
        //     steps {
        //         sh 'docker-compose -f docker-compose-ci.yml up --build users_tests'
        //     }
        //     post {
        //         cleanup {
        //             sh 'docker-compose -f docker-compose-ci.yml down --rmi local -v'
        //         }
        //     }
        // }
        // stage('Flake8') {
        //     steps {
        //         sh 'docker-compose -f docker-compose-ci.yml up --build flake8'
        //     }
        //     post {
        //         cleanup {
        //             sh 'docker-compose -f docker-compose-ci.yml down --rmi local -v'
        //         }
        //     }
        // }
        // stage('Client Tests') {
        //     steps {
        //         sh 'docker-compose -f docker-compose-ci.yml up --build client_tests'
        //     }
        //     post {
        //         cleanup {
        //             sh 'docker-compose -f docker-compose-ci.yml down --rmi local -v'
        //         }
        //     }
        // }
        stage('Docker Push') {
            steps {
                sh 'chmod 775 ./docker-push.sh'
                sh './docker-push.sh'
            }
        }
    }
}
