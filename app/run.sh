#!/bin/bash

### SET ENV VARIABLE ###
HOST="0.0.0.0"
PORT="8015"

echo "url: http://$HOST:$PORT"

export HOST_SERVICE=$HOST
export PORT_SERVICE=$PORT

export DB_USER=dbuser
export DB_PASSWORD=dbpasswd
export DB_HOST=dbhost
export DB_PORT=5432
export DB_NAME=dbname


source venv/bin/activate

if [ $? -eq 0 ]; then
  echo "source venv/bin/activate"
else
  python3 -m virtualenv venv
  source venv/bin/activate
  pip install -r requirements.txt
fi


## RUN SERVER ###
uvicorn main:app --proxy-headers --reload --port $PORT --host $HOST
