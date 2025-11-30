import time

from clients.http.gateway.users.client import (
    CreateUserRequestDict,
    build_users_gateway_http_client
)

users_gateway_client = build_users_gateway_http_client()

create_user_request = CreateUserRequestDict(
    email=f"user.{time.time()}@example.com",
    lastName="string",
    firstName="string",
    middleName="string",
    phoneNumber="string"
)

create_user_response = users_gateway_client.create_user()
print("create user response data:", create_user_response)

get_user_response = users_gateway_client.get_user(create_user_response['user']['id'])
print(get_user_response)