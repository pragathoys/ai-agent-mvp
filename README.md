# AI  agent MVP

## Setup and run

docker compose up --build

## Stop 

docker compose down


## API Usage

### GET health

curl -X GET http://localhost:8000/health

### POST agent/run

curl -X POST http://localhost:8000/agent/run

### Basic agent request example

curl -X POST "http://localhost:8000/agent/run" -H "Content-Type: application/json" -d '{ "message": "Explain Docker in simple terms" }'

### Admin requests example

curl -X GET "http://localhost:8000/admin/runs" 


curl -X GET "http://localhost:8000/admin/runs/1" 