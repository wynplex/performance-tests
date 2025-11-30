from typing import TypedDict, List

from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client


class OperationDict(TypedDict):
    """
    Структура данных операции.
    """
    id: str
    type: str  # FEE, TOP_UP, PURCHASE, CASHBACK, TRANSFER, BILL_PAYMENT, CASH_WITHDRAWAL
    status: str  # FAILED, COMPLETED, IN_PROGRESS, UNSPECIFIED
    amount: float
    cardId: str
    category: str
    createdAt: str
    accountId: str


class OperationReceiptDict(TypedDict):
    """
    Структура данных чека операции.
    """
    url: str
    document: str


class OperationsSummaryDict(TypedDict):
    """
    Структура сводных данных по операциям.
    """
    spentAmount: float
    receivedAmount: float
    cashbackAmount: float


class GetOperationResponseDict(TypedDict):
    """
    Структура ответа на получение детальной информации об операции.
    """
    operation: OperationDict


class GetOperationsResponseDict(TypedDict):
    """
    Структура ответа на получение списка операций.
    """
    operations: List[OperationDict]


class GetOperationsSummaryResponseDict(TypedDict):
    """
    Структура ответа на получение сводки по операциям.
    """
    summary: OperationsSummaryDict


class GetOperationReceiptResponseDict(TypedDict):
    """
    Структура ответа на получение чека операции.
    """
    receipt: OperationReceiptDict


class MakeFeeOperationResponseDict(TypedDict):
    """
    Структура ответа на создание операции комиссии.
    """
    operation: OperationDict


class MakeTopUpOperationResponseDict(TypedDict):
    """
    Структура ответа на создание операции пополнения.
    """
    operation: OperationDict


class MakeCashbackOperationResponseDict(TypedDict):
    """
    Структура ответа на создание операции кэшбэка.
    """
    operation: OperationDict


class MakeTransferOperationResponseDict(TypedDict):
    """
    Структура ответа на создание операции перевода.
    """
    operation: OperationDict


class MakePurchaseOperationResponseDict(TypedDict):
    """
    Структура ответа на создание операции покупки.
    """
    operation: OperationDict


class MakeBillPaymentOperationResponseDict(TypedDict):
    """
    Структура ответа на создание операции оплаты счета.
    """
    operation: OperationDict


class MakeCashWithdrawalOperationResponseDict(TypedDict):
    """
    Структура ответа на создание операции снятия наличных.
    """
    operation: OperationDict


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
    amount: float
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

    def get_operation(self, operation_id: str) -> GetOperationResponseDict:
        """
        Получить детальную информацию об операции.

        :param operation_id: Идентификатор операции.
        :return: Словарь с данными операции.
        """
        response = self.get_operation_api(operation_id)
        return response.json()

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseDict:
        """
        Получить чек операции.

        :param operation_id: Идентификатор операции.
        :return: Словарь с данными чека.
        """
        response = self.get_operation_receipt_api(operation_id)
        return response.json()

    def get_operations(self, account_id: str) -> GetOperationsResponseDict:
        """
        Получить список операций по счету.

        :param account_id: Идентификатор счета.
        :return: Словарь со списком операций.
        """
        query = GetOperationsQueryDict(accountId=account_id)
        response = self.get_operations_api(query)
        return response.json()

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseDict:
        """
        Получить сводку по операциям счета.

        :param account_id: Идентификатор счета.
        :return: Словарь со сводной информацией.
        """
        query = GetOperationsSummaryQueryDict(accountId=account_id)
        response = self.get_operations_summary_api(query)
        return response.json()

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseDict:
        """
        Создать операцию комиссии.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с созданной операцией.
        """
        request = MakeFeeOperationRequestDict(
            status="COMPLETED",
            amount=55.77,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_fee_operation_api(request)
        return response.json()

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseDict:
        """
        Создать операцию пополнения счета.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с созданной операцией.
        """
        request = MakeTopUpOperationRequestDict(
            status="COMPLETED",
            amount=1000.00,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_top_up_operation_api(request)
        return response.json()

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseDict:
        """
        Создать операцию начисления кэшбэка.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с созданной операцией.
        """
        request = MakeCashbackOperationRequestDict(
            status="COMPLETED",
            amount=25.50,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cashback_operation_api(request)
        return response.json()

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseDict:
        """
        Создать операцию перевода.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с созданной операцией.
        """
        request = MakeTransferOperationRequestDict(
            status="COMPLETED",
            amount=500.00,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_transfer_operation_api(request)
        return response.json()

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseDict:
        """
        Создать операцию покупки.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с созданной операцией.
        """
        request = MakePurchaseOperationRequestDict(
            status="COMPLETED",
            amount=299.99,
            cardId=card_id,
            accountId=account_id,
            category="GROCERY"
        )
        response = self.make_purchase_operation_api(request)
        return response.json()

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseDict:
        """
        Создать операцию оплаты счета.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с созданной операцией.
        """
        request = MakeBillPaymentOperationRequestDict(
            status="COMPLETED",
            amount=150.00,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return response.json()

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseDict:
        """
        Создать операцию снятия наличных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с созданной операцией.
        """
        request = MakeCashWithdrawalOperationRequestDict(
            status="COMPLETED",
            amount=200.00,
            cardId=card_id,
            accountId=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return response.json()


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    return OperationsGatewayHTTPClient(build_gateway_http_client())