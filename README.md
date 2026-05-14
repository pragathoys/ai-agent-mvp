# ai-agent-mvp

## Setup

docker compose up --build

## API Usage

### GET health

curl -X GET http://localhost:8000/health

### POST agent/run

curl -X POST http://localhost:8000/agent/run

### Basic agent request example

curl -X POST "http://localhost:8000/agent/run" \
  -H "Content-Type: application/json" \
  -d '{
    "message": "Explain Docker in simple terms"
  }'