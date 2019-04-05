pipeline {
    agent {
        dockerfile true
    }
    environment {
        COMPOSE_PROJECT_NAME = '${BUILD_TAG}'
        COMMIT = ${GIT_COMMIT}
        BRANCH = ${GIT_BRANCH#*/}
        MAIN_REPO = 'https://github.com/savioabugah/testdriven-app.git'
        USERS = 'test-driven-users'
        USERS_REPO = '${MAIN_REPO}#${GIT_BRANCH#*/}:services/users'
        USERS_DB = 'test-driven-users_db'
        USERS_DB_REPO = '${MAIN_REPO}#${GIT_BRANCH#*/}:services/users/project/db'
        CLIENT = 'test-driven-client'
        CLIENT_REPO = '${MAIN_REPO}#${GIT_BRANCH#*/}:services/client'
        SWAGGER = 'test-driven-swagger'
        SWAGGER_REPO = '${MAIN_REPO}#${GIT_BRANCH#*/}:services/swagger'
        SECRET_KEY = 'my_precious'
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
                sh 'chmod 775 ./docker-push-jenkins.sh'
                sh './docker-push-jenkins.sh'
            }
        }
    }
}
