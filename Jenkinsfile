pipeline {
    agent {
        dockerfile true
    }
    environment {
        AWS_ACCESS_KEY_ID = credentials('AWS_ACCESS_KEY_ID')
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY')
        AWS_ACCOUNT_ID=credentials('AWS_ACCOUNT_ID')
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
        REACT_APP_USERS_SERVICE_URL = "${env.BRANCH == "staging" ? "testdriven-staging-alb-806588837.us-west-1.elb.amazonaws.com" : "http://127.0.0.1"}"
        TAG="${BRANCH}"
        REPO="${AWS_ACCOUNT_ID}.dkr.ecr.us-west-1.amazonaws.com"
        DOCKER_ENV="${env.BRANCH == "master" ? "prod" : "stage"}"
    }
    stages {
        stage('Learning groovy') {
            steps {
                echo sh(script: 'env|sort', returnStdout: true)
            }

        }

        // stage('Configure') {
        //     steps {
        //         sh 'npm install'
        //     }
        // }

        stage('Tests') {
            steps {
                //sh 'docker-compose -f docker-compose-ci.yml up --build users_tests'
                sh 'docker-compose -f docker-compose-dev.yml up -d --build'
                sh 'docker-compose -f docker-compose-dev.yml exec -T users python manage.py test'
            }
            post {
                cleanup {
                    sh 'docker-compose -f docker-compose-ci.yml down --rmi local -v'
                }
            }

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
        // stage('Push Images') {
        //     // when {
        //     //     anyOf {
        //     //         branch "production"
        //     //         branch "staging"
        //     //     }
        //     // }
        //     steps {
        //         echo 'Login into Elastic Container Registry'
        //         sh 'set +x; eval $(aws ecr get-login --region us-west-1 --no-include-email)'

        //         echo 'Building and uploading Users Image'
        //         sh """
        //         docker build $USERS_REPO -t $USERS:$COMMIT -f Dockerfile-$DOCKER_ENV
        //         docker tag $USERS:$COMMIT $REPO/$USERS:$TAG
        //         docker push $REPO/$USERS:$TAG
        //         """

        //         echo 'Building and pushing  User DB Image'
        //         sh """
        //         docker build $USERS_DB_REPO -t $USERS_DB:$COMMIT -f Dockerfile
        //         docker tag $USERS_DB:$COMMIT $REPO/$USERS_DB:$TAG
        //         docker push $REPO/$USERS_DB:$TAG
        //         """

        //         echo "Building and pushing Client Image"
        //         sh """
        //         docker build $CLIENT_REPO -t $CLIENT:$COMMIT -f Dockerfile-$DOCKER_ENV --build-arg REACT_APP_USERS_SERVICE_URL=$REACT_APP_USERS_SERVICE_URL
        //         docker tag $CLIENT:$COMMIT $REPO/$CLIENT:$TAG
        //         docker push $REPO/$CLIENT:$TAG
        //         """

        //         echo "Building and pushing Swagger"
        //         sh """
        //         docker build $SWAGGER_REPO -t $SWAGGER:$COMMIT -f Dockerfile-$DOCKER_ENV
        //         docker tag $SWAGGER:$COMMIT $REPO/$SWAGGER:$TAG
        //         docker push $REPO/$SWAGGER:$TAG
        //         """

        //     }
        }
    }
}
