

run:
	python -m playapp

docker_build:
	docker-compose -f docker-compose.yml build 
	
docker_up:
	docker-compose -f docker-compose.yml up
docker_start_mongo:
	docker-compose -f docker-compose.yml up -d mongo

docker_stop_mongo:
	docker-compose -f docker-compose.yml stop mongo
