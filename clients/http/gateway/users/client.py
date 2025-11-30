import time

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


class UserDict(TypedDict):
    id: str
    email: str
    lastName: str
    firstName: str
    middleName: str
    phoneNumber: str


class GetUserResponseDict(TypedDict):
    user: UserDict

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

    def create_user_api(self, request: CreateUserRequestDict) -> Response:
        return self.post("/api/v1/users", json=request)

    def get_user(self, user_id: str) -> GetUserResponseDict:
        response = self.get_user_api(user_id)
        return response.json()

    def create_user(self):
        request = CreateUserRequestDict(
        email= f"user.{time.time()}@example.com",
        lastName= "awd",
        firstName= "dwa",
        middleName= "awd",
        phoneNumber= "fvsd"
        )
        response = self.create_user_api(request)
        return response.json()

def build_users_gateway_http_client() -> UsersGatewayHTTPClient:
    return UsersGatewayHTTPClient(build_gateway_http_client())