install:
	pip3 install -r requirements.txt

build: docker/Dockerfile
	docker build --no-cache -t transmission_grpc:latest ./

run: transmission_call_server.py
	docker run -p 5051:5051 transmission_grpc:latest

test: transmission_call_client.py
	python3 transmission_call_client.py --host localhost --port 5051
