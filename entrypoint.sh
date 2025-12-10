#!/bin/bash

set -e
source /opt/ros/jazzy/setup.bash
source /app/project/install/setup.bash

exec "$@"