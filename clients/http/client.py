from httpx import Client, URL, QueryParams, Response
from typing import Any, TypedDict


class HTTPClientExtensions(TypedDict, total=False):
    route: str


class HTTPClient:
    """
        Базовый HTTP API клиент, принимающий объект httpx.Client.

        :param client: экземпляр httpx.Client для выполнения HTTP-запросов
        """

    def __init__(self, client: Client):
        self.client = client

    def get(
            self,
            url: URL | str,
            params: QueryParams | None = None,
            extentions: HTTPClientExtensions | None = None
    ) -> Response:
        """
                  Выполняет GET-запрос.

                  :param url: URL-адрес эндпоинта.
                  :param params: GET-параметры запроса (например, ?key=value).
                  :return: Объект Response с данными ответа.
                  """
        return self.client.get(url, params=params, extensions=extentions)

    def post(
            self,
            url: URL | str,
            json: Any | None = None,
            extentions: HTTPClientExtensions | None = None
    ) -> Response:
        """
                   Выполняет POST-запрос.

                   :param url: URL-адрес эндпоинта.
                   :param json: Данные в формате JSON.
                   :param extentions: Разнообразная информация
                   :return: Объект Response с данными ответа.
                   """
        return self.client.post(url, json=json, extensions=extentions)
