#!/bin/bash

echo "Listing all backups..."

docker-compose run --rm wpcli ai1wm list-backups
