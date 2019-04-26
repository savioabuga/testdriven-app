pipeline {
    agent {
        dockerfile true
    }
    environment {
        AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
        COMPOSE_PROJECT_NAME = "${BUILD_TAG}"
        COMMIT = "${GIT_COMMIT}"
        BRANCH = sh(script: 'echo ${GIT_BRANCH#*/}', returnStdout: true).trim()
        MAIN_REPO = 'https://github.com/savioabugah/testdriven-app.git'
        USERS = 'test-driven-users'
        USERS_REPO = "${MAIN_REPO}#${BRANCH}:services/users"
        USERS_DB = 'test-driven-users_db'
        USERS_DB_REPO = "${MAIN_REPO}#${BRANCH}:services/users/project/db"
        CLIENT = 'test-driven-client'
        CLIENT_REPO = "${MAIN_REPO}#${BRANCH}:services/client"
        SWAGGER = 'test-driven-swagger'
        SWAGGER_REPO = "${MAIN_REPO}#${BRANCH}:services/swagger"
        SECRET_KEY = 'my_precious'
        DOCKER_ENV = 'stage'
        REACT_APP_USERS_SERVICE_URL = 'testdriven-staging-alb-806588837.us-west-1.elb.amazonaws.com'
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
        // stage('Docker Push') {
        //     steps {
        //         sh 'chmod 775 ./docker-push-jenkins.sh'
        //         sh './docker-push-jenkins.sh'
        //     }
        // }
        stage('Push Image') {
            // when {
            //     anyOf {
            //         branch "develop"
            //         branch "master"
            //     }
            // }
            steps {
                echo 'Login into Elastic Container Registry'
                sh 'set +x; eval $(aws ecr get-login --region us-west-1 --no-include-email)'

                echo 'Uploading images'
                sh """
                docker build $USERS_REPO -t $USERS:$COMMIT -f Dockerfile-$DOCKER_ENV
                docker tag $USERS:$COMMIT $REPO/$USERS:$TAG
                docker push $REPO/$USERS:$TAG
                """
            }
        }
}
