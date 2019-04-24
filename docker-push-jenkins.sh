#!/bin/sh

echo $BRANCH == "master"
echo $COMMIT

if [ -z "$CHANGE_ID" ]
then

  if [[ "$BRANCH" == "master" ]]; then
    export DOCKER_ENV=stage
    export REACT_APP_USERS_SERVICE_URL="testdriven-staging-alb-806588837.us-west-1.elb.amazonaws.com"
  elif [[ "$BRANCH" == "production" ]]; then
    export DOCKER_ENV=prod
  fi

  if [ "$BRANCH" == "master" ] || \
     [ "$BRANCH" == "production" ]
  then
    # curl "https://s3.amazonaws.com/aws-cli/awscli-bundle.zip" -o "awscli-bundle.zip"
    # unzip awscli-bundle.zip
    # ./awscli-bundle/install -b ~/bin/aws
    # export PATH=~/bin:$PATH
    # add AWS_ACCOUNT_ID, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY env vars
    eval $(aws ecr get-login --region us-west-1 --no-include-email)
    export TAG=$BRANCH
    export REPO=$AWS_ACCOUNT_ID.dkr.ecr.us-west-1.amazonaws.com
  fi

  if [ "$BRANCH" == "master" ] || \
     [ "$BRANCH" == "production" ]
  then
    echo 'Building users'
    echo $PWD
    echo "$USER
    # users
    docker build $USERS_REPO -t $USERS:$COMMIT -f Dockerfile-$DOCKER_ENV
    docker tag $USERS:$COMMIT $REPO/$USERS:$TAG
    docker push $REPO/$USERS:$TAG
    echo 'Done building user'
    # users db
    docker build $USERS_DB_REPO -t $USERS_DB:$COMMIT -f Dockerfile
    docker tag $USERS_DB:$COMMIT $REPO/$USERS_DB:$TAG
    docker push $REPO/$USERS_DB:$TAG
    # client
    docker build $CLIENT_REPO -t $CLIENT:$COMMIT -f Dockerfile-$DOCKER_ENV --build-arg REACT_APP_USERS_SERVICE_URL=$REACT_APP_USERS_SERVICE_URL
    docker tag $CLIENT:$COMMIT $REPO/$CLIENT:$TAG
    docker push $REPO/$CLIENT:$TAG
    # swagger
    docker build $SWAGGER_REPO -t $SWAGGER:$COMMIT -f Dockerfile-$DOCKER_ENV
    docker tag $SWAGGER:$COMMIT $REPO/$SWAGGER:$TAG
    docker push $REPO/$SWAGGER:$TAG
  fi
fi
