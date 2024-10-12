#!/bin/bash

source .venv/bin/activate

args=("$@")

if [ "$1" == "--preprocess" ]; then
  echo "Running preprocessing..."
  shift
  python3 preprocess.py "$@"
fi

echo "Processing data..."
python3 data_parse.py "$@"
