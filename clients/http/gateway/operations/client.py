from httpx import Response, QueryParams

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from httpx import QueryParams, Response

from clients.http.client import HTTPClient
from clients.http.gateway.client import build_gateway_http_client
from clients.http.gateway.operations.schema import (
    GetOperationReceiptResponseSchema,
    GetOperationResponseSchema,
    GetOperationsResponseSchema,
    GetOperationsSummaryResponseSchema,
    MakeBillPaymentOperationRequestSchema,
    MakeBillPaymentOperationResponseSchema,
    MakeCashWithdrawalOperationRequestSchema,
    MakeCashWithdrawalOperationResponseSchema,
    MakeCashbackOperationRequestSchema,
    MakeCashbackOperationResponseSchema,
    MakeFeeOperationRequestSchema,
    MakeFeeOperationResponseSchema,
    MakePurchaseOperationRequestSchema,
    MakePurchaseOperationResponseSchema,
    MakeTopUpOperationRequestSchema,
    MakeTopUpOperationResponseSchema,
    MakeTransferOperationRequestSchema,
    GetOperationsQuerySchema,
    GetOperationsSummaryQuerySchema,
    MakeTransferOperationResponseSchema,
    OperationStatus,
)


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

    def get_operations_api(self, query: GetOperationsQuerySchema) -> Response:
        """
        Выполняет GET-запрос на получение списка операций по счету.

        :param query: Словарь с параметрами запроса, например: {'account_id': '123'}.
        :return: Объект httpx.Response со списком операций.
        """
        return self.get("/api/v1/operations", params=QueryParams(**query.model_dump(by_alias=True)))

    def get_operations_summary_api(self, query: GetOperationsSummaryQuerySchema) -> Response:
        """
        Выполняет GET-запрос на получение сводки по операциям счета.

        :param query: Словарь с параметрами запроса, например: {'account_id': '123'}.
        :return: Объект httpx.Response со сводной информацией.
        """
        return self.get("/api/v1/operations/operations-summary", params=QueryParams(**query.model_dump(by_alias=True)))

    def make_fee_operation_api(self, body: MakeFeeOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции комиссии.

        :param body: Словарь с данными операции (status, amount, card_id, account_id).
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-fee-operation", json=body.model_dump(by_alias=True))

    def make_top_up_operation_api(self, body: MakeTopUpOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для пополнения счета.

        :param body: Словарь с данными операции (status, amount, card_id, account_id).
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-top-up-operation", json=body.model_dump(by_alias=True))

    def make_cashback_operation_api(self, body: MakeCashbackOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для начисления кэшбэка.

        :param body: Словарь с данными операции (status, amount, card_id, account_id).
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cashback-operation", json=body.model_dump(by_alias=True))

    def make_transfer_operation_api(self, body: MakeTransferOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания перевода.

        :param body: Словарь с данными операции (status, amount, card_id, account_id).
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-transfer-operation", json=body.model_dump(by_alias=True))

    def make_purchase_operation_api(self, body: MakePurchaseOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для создания операции покупки.

        :param body: Словарь с данными операции (status, amount, card_id, account_id, category).
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-purchase-operation", json=body.model_dump(by_alias=True))

    def make_bill_payment_operation_api(self, body: MakeBillPaymentOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для оплаты счета.

        :param body: Словарь с данными операции (status, amount, card_id, account_id).
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-bill-payment-operation", json=body.model_dump(by_alias=True))

    def make_cash_withdrawal_operation_api(self, body: MakeCashWithdrawalOperationRequestSchema) -> Response:
        """
        Выполняет POST-запрос для снятия наличных.

        :param body: Словарь с данными операции (status, amount, card_id, account_id).
        :return: Объект httpx.Response с результатом операции.
        """
        return self.post("/api/v1/operations/make-cash-withdrawal-operation", json=body.model_dump(by_alias=True))

    def get_operation(self, operation_id: str) -> GetOperationResponseSchema:
        """
        Получить детальную информацию об операции.

        :param operation_id: Идентификатор операции.
        :return: Словарь с данными операции.
        """
        response = self.get_operation_api(operation_id)
        return GetOperationResponseSchema.model_validate_json(response.text)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponseSchema:
        """
        Получить чек операции.

        :param operation_id: Идентификатор операции.
        :return: Словарь с данными чека.
        """
        response = self.get_operation_receipt_api(operation_id)
        return GetOperationReceiptResponseSchema.model_validate_json(response.text)

    def get_operations(self, account_id: str) -> GetOperationsResponseSchema:
        """
        Получить список операций по счету.

        :param account_id: Идентификатор счета.
        :return: Словарь со списком операций.
        """
        query = GetOperationsQuerySchema(account_id=account_id)
        response = self.get_operations_api(query)
        return GetOperationsResponseSchema.model_validate_json(response.text)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponseSchema:
        """
        Получить сводку по операциям счета.

        :param account_id: Идентификатор счета.
        :return: Словарь со сводной информацией.
        """
        query = GetOperationsSummaryQuerySchema(account_id=account_id)
        response = self.get_operations_summary_api(query)
        return GetOperationsSummaryResponseSchema.model_validate_json(response.text)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponseSchema:
        """
        Создать операцию комиссии.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с созданной операцией.
        """
        request = MakeFeeOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=55.77,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_fee_operation_api(request)
        return MakeFeeOperationResponseSchema.model_validate_json(response.text)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponseSchema:
        """
        Создать операцию пополнения счета.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с созданной операцией.
        """
        request = MakeTopUpOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=1000.00,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_top_up_operation_api(request)
        return MakeTopUpOperationResponseSchema.model_validate_json(response.text)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponseSchema:
        """
        Создать операцию начисления кэшбэка.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с созданной операцией.
        """
        request = MakeCashbackOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=25.50,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cashback_operation_api(request)
        return MakeCashbackOperationResponseSchema.model_validate_json(response.text)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponseSchema:
        """
        Создать операцию перевода.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с созданной операцией.
        """
        request = MakeTransferOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=500.00,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_transfer_operation_api(request)
        return MakeTransferOperationResponseSchema.model_validate_json(response.text)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponseSchema:
        """
        Создать операцию покупки.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с созданной операцией.
        """
        request = MakePurchaseOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=299.99,
            card_id=card_id,
            account_id=account_id,
            category="GROCERY"
        )
        response = self.make_purchase_operation_api(request)
        return MakePurchaseOperationResponseSchema.model_validate_json(response.text)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponseSchema:
        """
        Создать операцию оплаты счета.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с созданной операцией.
        """
        request = MakeBillPaymentOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=150.00,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_bill_payment_operation_api(request)
        return MakeBillPaymentOperationResponseSchema.model_validate_json(response.text)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponseSchema:
        """
        Создать операцию снятия наличных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Словарь с созданной операцией.
        """
        request = MakeCashWithdrawalOperationRequestSchema(
            status=OperationStatus.COMPLETED,
            amount=200.00,
            card_id=card_id,
            account_id=account_id
        )
        response = self.make_cash_withdrawal_operation_api(request)
        return MakeCashWithdrawalOperationResponseSchema.model_validate_json(response.text)


def build_operations_gateway_http_client() -> OperationsGatewayHTTPClient:
    return OperationsGatewayHTTPClient(build_gateway_http_client())