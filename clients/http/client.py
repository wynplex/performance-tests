from httpx import Client, URL, QueryParams, Response
from typing import Any


class HTTPClient:
    """
        Базовый HTTP API клиент, принимающий объект httpx.Client.

        :param client: экземпляр httpx.Client для выполнения HTTP-запросов
        """

    def __init__(self, client: Client):
        self.client = client

    """
          Выполняет GET-запрос.

          :param url: URL-адрес эндпоинта.
          :param params: GET-параметры запроса (например, ?key=value).
          :return: Объект Response с данными ответа.
          """

    def get(self, url: URL | str, params: QueryParams | None = None) -> Response:
        return self.client.get(url, params=params)

    """
           Выполняет POST-запрос.
 
           :param url: URL-адрес эндпоинта.
           :param json: Данные в формате JSON.
           :return: Объект Response с данными ответа.
           """

    def post(self, url: URL | str, json: Any | None = None) -> Response:
        return self.client.post(url, json=json)
