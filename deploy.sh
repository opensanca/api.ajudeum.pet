#!/bin/bash
if [ "${TRAVIS_PULL_REQUEST}" = "false" ] && [ "${TRAVIS_BRANCH}" = "master" ]; then
  docker build . -t registry.heroku.com/catiorinio/web
  docker login --username=samuel.grigolato@gmail.com --password=$(echo $HEROKU_TOKEN) registry.heroku.com
  docker push registry.heroku.com/catiorinio/web
fi
