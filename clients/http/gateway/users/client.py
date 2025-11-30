from clients.http.client import HTTPClient
from httpx import Response
from typing import TypedDict

from clients.http.gateway.client import build_gateway_http_client


class CreateUserRequestDict(TypedDict):
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


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

    def create_user_api_request(self, request: CreateUserRequestDict) -> Response:
        return self.post("/api/v1/users", json=request)

def build_users_gateway_http_client(self) -> UsersGatewayHTTPClient:
    return UsersGatewayHTTPClient(build_gateway_http_client())