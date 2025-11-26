import httpx
import time

client = httpx.Client(
    base_url="http://localhost:8003",
    timeout = 10,
    headers = {"Authorization": "Bearer my_example_token"}
)

create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "awd",
    "firstName": "dwa",
    "middleName": "awd",
    "phoneNumber": "fvsd"
}

response = client.post("/api/v1/users", json=create_user_payload)

print(response.text)
