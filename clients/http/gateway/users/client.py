from clients.http.client import HTTPClient
from httpx import Response, Client
from typing import TypedDict


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


users_client = UsersGatewayHTTPClient(client=Client(base_url="http://localhost:8003"))
response = users_client.get_user_api("dwadaw")
print(response)
