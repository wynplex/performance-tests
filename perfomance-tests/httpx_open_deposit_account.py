import httpx
import time

create_user_payload = {
    "email": f"user.{time.time()}@example.com",
    "lastName": "awd",
    "firstName": "dwa",
    "middleName": "awd",
    "phoneNumber": "fvsd"
}

with httpx.Client(
        base_url="http://localhost:8003"
) as client:
    response = client.post("/api/v1/users", json=create_user_payload)
    assert response.status_code == 200
    user_id = response.json()["user"]["id"]

    response = client.post("/api/v1/accounts/open-deposit-account",
                           json={"userId": response.json()["user"]["id"]},
                           timeout=10)
    assert response.status_code == 200
    print(response.status_code)
    print(response.json())
