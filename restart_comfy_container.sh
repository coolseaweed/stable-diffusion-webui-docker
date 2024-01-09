#!/bin/bash


docker compose --profile comfy down
docker compose --profile comfy up -d
docker logs -f webui-docker-comfy-1
