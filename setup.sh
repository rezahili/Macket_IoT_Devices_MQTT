#!/bin/bash

# Load environment variables from file
if [[ -f "envfile.env" ]]; then
  export $(grep -v '^#' envfile.env | xargs)
fi
#creating configfile
if [ -e mosquitto.conf ]; then
  rm mosquitto.conf
fi
echo "listener ${PORT}" > mosquitto.conf
echo 'allow_anonymous true' >> mosquitto.conf
docker compose up -d


