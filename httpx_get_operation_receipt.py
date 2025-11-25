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

    response = client.post("/api/v1/accounts/open-credit-card-account",
                           json={"userId": user_id}, timeout=10)
    assert response.status_code == 200
    account_id = response.json()["account"]["id"]
    card_id = response.json()["account"]["cards"][0]["id"]

    make_purchase_payload = {
        "status": "IN_PROGRESS",
        "amount": 77.99,
        "category": "taxi",
        "cardId": f"{card_id}",
        "accountId": f"{account_id}",

    }

    response = client.post("/api/v1/operations/make-purchase-operation", json=make_purchase_payload, timeout=10)
    assert response.status_code == 200
    operation_id = response.json()["operation"]["id"]

    response = client.get(f"/api/v1/operations/operation-receipt/{operation_id}", timeout=10)
    assert response.status_code == 200
    print(response.json())
