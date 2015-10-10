#!/bin/bash

NAME="Envelope"
IP=127.0.0.1
PORT=4000
USER=www-data
GROUP=www-data
NUM_WORKERS=3

HOME_DIR=/home/vagrant

VENV_NAME=virtualenv
VENV_DIR=${HOME_DIR}/${VENV_NAME}
APP_ROOT_DIR=${HOME_DIR}/envelope/app

GUNICORN_DIR=${HOME_DIR}/gunicorn
SOCKET_FILE=${GUNICORN_DIR}/envelope.sock
RUN_DIR=$(dirname ${SOCKET_FILE})
# Create the run directory if it doesn't exist
test -d ${RUN_DIR} || mkdir -p ${RUN_DIR}

WSGI_MODULE=index
WSGI_APP_VAR=wsgi_app

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd ${APP_ROOT_DIR}
source ${VENV_DIR}/bin/activate

# Starting the app with guinicorn.
# Meant to be run under supervisor. Should NOT daemonize themselves (do not use --daemon)
exec ${VENV_DIR}/bin/gunicorn ${WSGI_MODULE}:${WSGI_APP_VAR} \
  --name ${NAME} \
  --bind ${IP}:${PORT} \
  --workers ${NUM_WORKERS} \
  --user=${USER} --group=${GROUP} \
  --log-level=info \
  --bind=unix:${SOCKET_FILE}