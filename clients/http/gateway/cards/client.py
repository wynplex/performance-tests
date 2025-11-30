from typing import TypedDict

from clients.http.client import HTTPClient
from httpx import Response

from clients.http.gateway.client import build_gateway_http_client


class IssueCardRequestDict(TypedDict):
    userId: str
    accountId: str


class CardsGatewayHTTPClient(HTTPClient):

    def issue_virtual_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Открытие виртуальной карты для пользователя.

        :param request: Словарь с данными пользователя.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-virtual-card", json=request)

    def issue_physical_card_api(self, request: IssueCardRequestDict) -> Response:
        """
        Открытие физической карты для пользователя.

        :param request: Словарь с данными пользователя.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.post("/api/v1/cards/issue-physical-card", json=request)

def build_cards_gateway_http_client() -> CardsGatewayHTTPClient:
    return CardsGatewayHTTPClient(build_gateway_http_client())