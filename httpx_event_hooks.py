from datetime import datetime

from httpx import Client, Request, Response

def log_request(request: Request):
    request.extensions['start_time'] = datetime.now()
    print(f"Request: {request.method}")

def log_response(response: Response):
    duration = datetime.now() - response.request.extensions['start_time']
    print(f"Response: {response.status_code}, duration: {duration}")

client = Client(
    base_url="http://localhost:8003",
    event_hooks= {"request": [log_request], "response": [log_response]}
)
response = client.get("/api/v1/users/6b62f114-24c8-448f-bb9c-a0524b4e902b")

print(response)
