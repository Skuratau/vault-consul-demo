IMAGE=`docker build . | grep Successfully | awk '{print $3}'`
IMAGE=`docker build . | grep Successfully | awk '{print $3}'`
docker tag $IMAGE unlocker:latest
