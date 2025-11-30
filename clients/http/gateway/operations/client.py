from typing import TypedDict

from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class GetOperationsQueryDict(TypedDict):
    """
    Структура данных для получения списка операций аккаунта.
    """
    accountId: str


class GetOperationsSummaryQueryDict(TypedDict):
    """
    Структура данных для получения общих данных операций по аккаунту.
    """
    accountId: str


class MakeOperationRequestDict(TypedDict):
    """
    Базовая структура данных для большинства POST запросов по операциям аккаунта.
    """
    status: str
    amount: int
    cardId: str
    accountId: str


class MakeFeeOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции комиссии.
    """
    pass


class MakeTopUpOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции пополнения счета.
    """
    pass


class MakeCashbackOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции кэшбэка.
    """
    pass


class MakeTransferOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции перевода.
    """
    pass


class MakePurchaseOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции покупки.
    """
    category: str


class MakeBillPaymentOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции оплаты счета.
    """
    pass


class MakeCashWithdrawalOperationRequestDict(MakeOperationRequestDict):
    """
    Структура данных для создания операции снятия наличных.
    """
    pass


class OperationsGatewayHTTPClient(HTTPClient):
    """
    Клиент для взаимодействия с /api/v1/operations сервиса http-gateway.
    """

    def get_operation_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение детальной информации об операции.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с деталями операции.
        """
        return self.get(f"/api/v1/operations/{operation_id}")

    def get_operation_receipt_api(self, operation_id: str) -> Response:
        """
        Выполняет GET-запрос на получение чека операции.

        :param operation_id: Идентификатор операции.
        :return: Объект httpx.Response с данными чека.
        """
        return self.get(f"/api/v1/operations/operation-receipt/{operation_id}")

    def get_operations_api(self, query: GetOperationsQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение списка операций по счету.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response со списком операций.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query))

    def get_operations_summary_api(self, query: GetOperationsSummaryQueryDict) -> Response:
        """
        Выполняет GET-запрос на получение сводки по операциям счета.

        :param query: Словарь с параметрами запроса, например: {'accountId': '123'}.
        :return: Объект httpx.Response со сводной информацией.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query))

    def make_fee_operation_api(self, body: MakeFeeOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param body: Словарь с данными операции (status, amount, cardId, accountId).
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=body)

    def make_top_up_operation_api(self, body: MakeTopUpOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для пополнения счета.

        :param body: Словарь с данными операции (status, amount, cardId, accountId).
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=body)

    def make_cashback_operation_api(self, body: MakeCashbackOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для начисления кэшбэка.

        :param body: Словарь с данными операции (status, amount, cardId, accountId).
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=body)

    def make_transfer_operation_api(self, body: MakeTransferOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания перевода.

        :param body: Словарь с данными операции (status, amount, cardId, accountId).
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=body)

    def make_purchase_operation_api(self, body: MakePurchaseOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param body: Словарь с данными операции (status, amount, cardId, accountId, category).
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=body)

    def make_bill_payment_operation_api(self, body: MakeBillPaymentOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для оплаты счета.

        :param body: Словарь с данными операции (status, amount, cardId, accountId).
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=body)

    def make_cash_withdrawal_operation_api(self, body: MakeCashWithdrawalOperationRequestDict) -> Response:
        """
        Выполняет POST-запрос для снятия наличных.

        :param body: Словарь с данными операции (status, amount, cardId, accountId).
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=body)

def build_operations_gateway__http_client() -> OperationsGatewayHTTPClient:
    return OperationsGatewayHTTPClient(build_gateway_http_client())