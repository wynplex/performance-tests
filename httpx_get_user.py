import time

import httpx

post_data = {
  "email": f"user.{time.time()}@dexample.com",
  "lastName": "awd",
  "firstName": "dwa",
  "middleName": "awd",
  "phoneNumber": "fvsd"
}

with httpx.Client(
        base_url="http://localhost:8003"
) as client:

    post_response = client.post("/api/v1/users", json = post_data)
    print(post_response.status_code)
    print(post_response.json())

    data = post_response.json()
    user_id = data["user"]["id"]

    get_response = client.get(f"/api/v1/users/{user_id}")
    print(get_response.status_code)
    print(get_response.json())

