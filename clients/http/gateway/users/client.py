import time

from clients.http.client import HTTPClient
from httpx import Response

from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.users.schema import (
    GetUserResponseSchema,
    CreateUserRequestSchema,
    CreateUserResponseSchema
)


class UsersGatewayHTTPClient(HTTPClient):
    """
            Создание нового пользователя.

            :param request: Словарь с данными нового пользователя.
            :return: Ответ от сервера (объект httpx.Response).
    """

    def get_user_api(self, user_id: str) -> Response:
        return self.get(f"/api/v1/users/{user_id}")

    """
            Создание нового пользователя.

            :param request: Словарь с данными нового пользователя.
            :return: Ответ от сервера (объект httpx.Response).
    """

    def create_user_api(self, request: CreateUserRequestSchema) -> Response:
        return self.post("/api/v1/users", json=request.model_dump(by_alias=True))

    def get_user(self, user_id: str) -> GetUserResponseSchema:
        response = self.get_user_api(user_id)
        return GetUserResponseSchema.model_validate_json(response.text)

    def create_user(self) -> CreateUserResponseSchema:
        request = CreateUserRequestSchema(
        email= f"user.{time.time()}@example.com",
        last_name= "awd",
        first_name= "dwa",
        middle_name= "awd",
        phone_number= "fvsd"
        )
        response = self.create_user_api(request)
        return CreateUserResponseSchema.model_validate_json(response.text)

def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    return UsersGatewayHTTPClient(build_gateway_http_client())