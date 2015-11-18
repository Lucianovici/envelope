#!/bin/bash

_NAME=${NAME:-"Envelope"}
_IP=${IP:-"127.0.0.1"}
_PORT=${PORT:-"4000"}
_USER=${USER:-"www-data"}
_GROUP=${GROUP:-"www-data"}
_NUM_WORKERS=${NUM_WORKERS:-"3"}
_HOME_DIR=${HOME_DIR:-"/home/vagrant"}

VENV_NAME=virtualenv
VENV_DIR=${_HOME_DIR}/${VENV_NAME}
APP_ROOT_DIR=${_HOME_DIR}/envelope/app

GUNICORN_DIR=${_HOME_DIR}/gunicorn
SOCKET_FILE=${GUNICORN_DIR}/envelope.sock
RUN_DIR=$(dirname ${SOCKET_FILE})
# Create the run directory if it doesn't exist
test -d ${RUN_DIR} || mkdir -p ${RUN_DIR}

WSGI_MODULE=index
WSGI_APP_VAR=wsgi_app

echo "Starting $_NAME as `whoami`"

# Activate the virtual environment
cd ${APP_ROOT_DIR}
source ${VENV_DIR}/bin/activate

# Starting the app with guinicorn.
# Meant to be run under supervisor. Should NOT daemonize themselves (do not use --daemon)
exec ${VENV_DIR}/bin/gunicorn ${WSGI_MODULE}:${WSGI_APP_VAR} \
  --name ${_NAME} \
  --bind ${_IP}:${_PORT} \
  --workers ${_NUM_WORKERS} \
  --user=${_USER} --group=${_GROUP} \
  --log-level=info \
  --bind=unix:${SOCKET_FILE}