from typing import TypedDict

from httpx import Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client

class DocumentDict(TypedDict):
    """
    Описание структуры документа.
    """
    url: str
    document: str

class GetTariffDocumentResponseDict(TypedDict):
    """
    Описание структуры ответа получения тарифа по счёту.
    """
    tariff: DocumentDict

class GetContractDocumentResponseDict(TypedDict):
    """
    Описание структуры ответа получения контракта по счёту.
    """
    tariff: DocumentDict

class DocumentsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/documents сервиса http-gateway.
    """

    def get_tariff_document_api(self, account_id: str) -> Response:
        """
        Получить тариф по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/tariff-document/{account_id}")

    def get_contract_document_api(self, account_id: str) -> Response:
        """
        Получить контракт по счету.

        :param account_id: Идентификатор счета.
        :return: Ответ от сервера (объект httpx.Response).
        """
        return self.get(f"/api/v1/documents/contract-document/{account_id}")

    def get_tariff_document(self, account_id: str) -> GetTariffDocumentResponseDict:
        """
        Получить документ тарифа и вернуть типизированный JSON-ответ.

        :param account_id: Идентификатор счета
        :return: Словарь с документом тарифа (JSON)
        """
        response = self.get_tariff_document_api(account_id)
        return response.json()

    def get_contract_document(self, account_id: str) -> GetContractDocumentResponseDict:
        """
        Получить документ контракта и вернуть типизированный JSON-ответ.

        :param account_id: Идентификатор счета
        :return: Словарь с документом контракта (JSON)
        """
        response = self.get_contract_document_api(account_id)
        return response.json()

def build_documents_gateway_http_client() -> DocumentsGatewayHTTPClient:
    return DocumentsGatewayHTTPClient(build_gateway_http_client())