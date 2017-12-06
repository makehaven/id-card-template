#!/bin/sh
exec docker run --rm -i --user="$(id -u):$(id -g)" --net=none -v "$DATA_DIR":/data blang/latex "$@"
