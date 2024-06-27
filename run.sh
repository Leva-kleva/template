#!/bin/bash

app_name=app
version=$1


if [ "$version" == "master" ]; then
    export PORT_SERVICE=8015
#    export SECRET_KEY

#    export DB_USER=
#    export DB_PASSWORD=
#    export DB_HOST=
#    export DB_PORT=
#    export DB_NAME=
#
#    export DOCKER_NET=db-net

elif [ "$version" == "develop" ]; then
    app_name=$app_name"_test"


    export PORT_SERVICE=8020
#    export SECRET_KEY

#    export DB_USER=
#    export DB_PASSWORD=
#    export DB_HOST=
#    export DB_PORT=
#    export DB_NAME=
#
#    export DOCKER_NET=db-net-test
else
    echo "Error: no args."
    exit 1
fi


env_var=""
env_var="$env_var --env DOCKER_NET=$DOCKER_NET --env SECRET_KEY=$SECRET_KEY"
#env_var="$env_var --env DB_HOST=$DB_HOST --env DB_PORT=$DB_PORT --env DB_NAME=$DB_NAME --env DB_USER=$DB_USER --env DB_PASSWORD=$DB_PASSWORD"

build_args=""
#build_args="$build_args --build-arg http_proxy=$http_proxy --build-arg https_proxy=$https_proxy"

run_options=""
run_options="$run_options -p $PORT_SERVICE:80  --network $DOCKER_NET"
run_options="$run_options --restart=always"
run_options="$run_options $env_var"
#run_options="$run_options $FILES_VOLUME:$FILES_PATH"


# docker network create $DOCKER_NET

docker stop $app_name
docker rm $app_name
docker rmi $app_name

docker build -t $app_name $build_args .
docker run -d $run_options --name $app_name $app_name
