LAST_STRING=`docker build . | tail -n 1`
IMAGE=`echo $LAST_STRING | grep Successfully | awk '{print $3}'`
docker tag $IMAGE unlocker:latest
