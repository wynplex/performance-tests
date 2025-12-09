from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_get_operation_pb2 import GetOperationRequest, GetOperationResponse
from contracts.services.gateway.operations.rpc_get_operation_receipt_pb2 import (
    GetOperationReceiptRequest, GetOperationReceiptResponse
)
from contracts.services.gateway.operations.rpc_get_operations_pb2 import GetOperationsRequest, GetOperationsResponse
from contracts.services.gateway.operations.rpc_get_operations_summary_pb2 import (
    GetOperationsSummaryRequest, GetOperationsSummaryResponse
)
from contracts.services.gateway.operations.rpc_make_bill_payment_operation_pb2 import (
    MakeBillPaymentOperationRequest, MakeBillPaymentOperationResponse
)
from contracts.services.gateway.operations.rpc_make_cash_withdrawal_operation_pb2 import (
    MakeCashWithdrawalOperationRequest, MakeCashWithdrawalOperationResponse
)
from contracts.services.gateway.operations.rpc_make_cashback_operation_pb2 import (
    MakeCashbackOperationRequest, MakeCashbackOperationResponse
)
from contracts.services.gateway.operations.rpc_make_fee_operation_pb2 import (
    MakeFeeOperationRequest, MakeFeeOperationResponse
)
from contracts.services.gateway.operations.rpc_make_purchase_operation_pb2 import (
    MakePurchaseOperationRequest, MakePurchaseOperationResponse
)
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (
    MakeTopUpOperationRequest, MakeTopUpOperationResponse
)
from contracts.services.gateway.operations.rpc_make_transfer_operation_pb2 import (
    MakeTransferOperationRequest, MakeTransferOperationResponse
)
from contracts.services.operations.operation_pb2 import OperationStatus
from tools.fakers import fake


class OperationsGatewayGRPCClient(GRPCClient):
    """
    gRPC-клиент для взаимодействия с OperationsGatewayService.
    Предоставляет методы для работы с операциями: получение информации,
    создание различных типов операций (платежи, переводы, кэшбэк и т.д.).
    """

    def __init__(self, channel: Channel):
        """
        Инициализация клиента с указанным gRPC-каналом.

        :param channel: gRPC-канал для подключения к OperationsGatewayService.
        """
        super().__init__(channel)  # ИСПРАВЛЕНО: добавлены скобки
        self.stub = OperationsGatewayServiceStub(channel)

    # ========== НИЗКОУРОВНЕВЫЕ API МЕТОДЫ ==========

    def get_operation_api(self, request: GetOperationRequest) -> GetOperationResponse:
        """
        Низкоуровневый вызов метода GetOperation через gRPC.
        Получение информации об операции по её ID.

        :param request: gRPC-запрос с ID операции.
        :return: Ответ с информацией об операции.
        """
        return self.stub.GetOperation(request)

    def get_operation_receipt_api(self, request: GetOperationReceiptRequest) -> GetOperationReceiptResponse:
        """
        Низкоуровневый вызов метода GetOperationReceipt через gRPC.
        Получение чека по операции.

        :param request: gRPC-запрос с ID операции для получения чека.
        :return: Ответ с данными чека операции.
        """
        return self.stub.GetOperationReceipt(request)

    def get_operations_api(self, request: GetOperationsRequest) -> GetOperationsResponse:
        """
        Низкоуровневый вызов метода GetOperations через gRPC.
        Получение списка операций для определенного счета.

        :param request: gRPC-запрос с ID счета.
        :return: Ответ со списком операций.
        """
        return self.stub.GetOperations(request)  # ИСПРАВЛЕНО: был GetOperationReceipt

    def get_operations_summary_api(self, request: GetOperationsSummaryRequest) -> GetOperationsSummaryResponse:
        """
        Низкоуровневый вызов метода GetOperationsSummary через gRPC.
        Получение статистики по операциям для определенного счета.

        :param request: gRPC-запрос с ID счета.
        :return: Ответ со статистикой по операциям.
        """
        return self.stub.GetOperationsSummary(request)

    def make_fee_operation_api(self, request: MakeFeeOperationRequest) -> MakeFeeOperationResponse:
        """
        Низкоуровневый вызов метода MakeFeeOperation через gRPC.
        Создание операции комиссии.

        :param request: gRPC-запрос с данными для создания операции комиссии.
        :return: Ответ с информацией о созданной операции комиссии.
        """
        return self.stub.MakeFeeOperation(request)

    def make_top_up_operation_api(self, request: MakeTopUpOperationRequest) -> MakeTopUpOperationResponse:
        """
        Низкоуровневый вызов метода MakeTopUpOperation через gRPC.
        Создание операции пополнения.

        :param request: gRPC-запрос с данными для создания операции пополнения.
        :return: Ответ с информацией о созданной операции пополнения.
        """
        return self.stub.MakeTopUpOperation(request)

    def make_cashback_operation_api(self, request: MakeCashbackOperationRequest) -> MakeCashbackOperationResponse:
        """
        Низкоуровневый вызов метода MakeCashbackOperation через gRPC.
        Создание операции кэшбэка.

        :param request: gRPC-запрос с данными для создания операции кэшбэка.
        :return: Ответ с информацией о созданной операции кэшбэка.
        """
        return self.stub.MakeCashbackOperation(request)

    def make_transfer_operation_api(self, request: MakeTransferOperationRequest) -> MakeTransferOperationResponse:
        """
        Низкоуровневый вызов метода MakeTransferOperation через gRPC.
        Создание операции перевода.

        :param request: gRPC-запрос с данными для создания операции перевода.
        :return: Ответ с информацией о созданной операции перевода.
        """
        return self.stub.MakeTransferOperation(request)

    def make_purchase_operation_api(self, request: MakePurchaseOperationRequest) -> MakePurchaseOperationResponse:
        """
        Низкоуровневый вызов метода MakePurchaseOperation через gRPC.
        Создание операции покупки.

        :param request: gRPC-запрос с данными для создания операции покупки.
        :return: Ответ с информацией о созданной операции покупки.
        """
        return self.stub.MakePurchaseOperation(request)

    def make_bill_payment_operation_api(self,
                                        request: MakeBillPaymentOperationRequest) -> MakeBillPaymentOperationResponse:
        """
        Низкоуровневый вызов метода MakeBillPaymentOperation через gRPC.
        Создание операции оплаты по счету.

        :param request: gRPC-запрос с данными для создания операции оплаты по счету.
        :return: Ответ с информацией о созданной операции оплаты.
        """
        return self.stub.MakeBillPaymentOperation(request)

    def make_cash_withdrawal_operation_api(self,
                                           request: MakeCashWithdrawalOperationRequest) -> MakeCashWithdrawalOperationResponse:
        """
        Низкоуровневый вызов метода MakeCashWithdrawalOperation через gRPC.
        Создание операции снятия наличных денег.

        :param request: gRPC-запрос с данными для создания операции снятия наличных.
        :return: Ответ с информацией о созданной операции снятия наличных.
        """
        return self.stub.MakeCashWithdrawalOperation(request)

    # ========== ВЫСОКОУРОВНЕВЫЕ МЕТОДЫ-ОБЁРТКИ ==========

    def get_operation(self, operation_id: str) -> GetOperationResponse:
        """
        Получение информации об операции по её идентификатору.
        Высокоуровневая обёртка над get_operation_api.

        :param operation_id: Идентификатор операции.
        :return: Ответ с полной информацией об операции.
        """
        request = GetOperationRequest(id=operation_id)
        return self.get_operation_api(request)

    def get_operation_receipt(self, operation_id: str) -> GetOperationReceiptResponse:
        """
        Получение чека по операции.
        Высокоуровневая обёртка над get_operation_receipt_api.

        :param operation_id: Идентификатор операции для получения чека.
        :return: Ответ с данными чека операции.
        """
        request = GetOperationReceiptRequest(operation_id=operation_id)
        return self.get_operation_receipt_api(request)

    def get_operations(self, account_id: str) -> GetOperationsResponse:
        """
        Получение списка операций для указанного счета.
        Высокоуровневая обёртка над get_operations_api.

        :param account_id: Идентификатор счета.
        :return: Ответ со списком операций по счету.
        """
        request = GetOperationsRequest(account_id=account_id)  # ИСПРАВЛЕНО: был GetOperationRequest
        return self.get_operations_api(request)

    def get_operations_summary(self, account_id: str) -> GetOperationsSummaryResponse:
        """
        Получение статистики по операциям для указанного счета.
        Высокоуровневая обёртка над get_operations_summary_api.

        :param account_id: Идентификатор счета.
        :return: Ответ со сводной статистикой по операциям.
        """
        request = GetOperationsSummaryRequest(account_id=account_id)
        return self.get_operations_summary_api(request)

    def make_fee_operation(self, card_id: str, account_id: str) -> MakeFeeOperationResponse:
        """
        Создание операции комиссии.
        Высокоуровневая обёртка над make_fee_operation_api с автогенерацией данных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Ответ с информацией о созданной операции комиссии.
        """
        request = MakeFeeOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_fee_operation_api(request)

    def make_top_up_operation(self, card_id: str, account_id: str) -> MakeTopUpOperationResponse:
        """
        Создание операции пополнения счета.
        Высокоуровневая обёртка над make_top_up_operation_api с автогенерацией данных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Ответ с информацией о созданной операции пополнения.
        """
        request = MakeTopUpOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_top_up_operation_api(request)

    def make_cashback_operation(self, card_id: str, account_id: str) -> MakeCashbackOperationResponse:
        """
        Создание операции кэшбэка.
        Высокоуровневая обёртка над make_cashback_operation_api с автогенерацией данных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Ответ с информацией о созданной операции кэшбэка.
        """
        request = MakeCashbackOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_cashback_operation_api(request)

    def make_transfer_operation(self, card_id: str, account_id: str) -> MakeTransferOperationResponse:
        """
        Создание операции перевода.
        Высокоуровневая обёртка над make_transfer_operation_api с автогенерацией данных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Ответ с информацией о созданной операции перевода.
        """
        request = MakeTransferOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_transfer_operation_api(request)

    def make_purchase_operation(self, card_id: str, account_id: str) -> MakePurchaseOperationResponse:
        """
        Создание операции покупки.
        Высокоуровневая обёртка над make_purchase_operation_api с автогенерацией данных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Ответ с информацией о созданной операции покупки.
        """
        request = MakePurchaseOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id,
            category=fake.category()
        )
        return self.make_purchase_operation_api(request)

    def make_bill_payment_operation(self, card_id: str, account_id: str) -> MakeBillPaymentOperationResponse:
        """
        Создание операции оплаты по счету.
        Высокоуровневая обёртка над make_bill_payment_operation_api с автогенерацией данных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Ответ с информацией о созданной операции оплаты.
        """
        request = MakeBillPaymentOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_bill_payment_operation_api(request)

    def make_cash_withdrawal_operation(self, card_id: str, account_id: str) -> MakeCashWithdrawalOperationResponse:
        """
        Создание операции снятия наличных.
        Высокоуровневая обёртка над make_cash_withdrawal_operation_api с автогенерацией данных.

        :param card_id: Идентификатор карты.
        :param account_id: Идентификатор счета.
        :return: Ответ с информацией о созданной операции снятия наличных.
        """
        request = MakeCashWithdrawalOperationRequest(
            status=fake.proto_enum(OperationStatus),
            amount=fake.amount(),
            card_id=card_id,
            account_id=account_id
        )
        return self.make_cash_withdrawal_operation_api(request)


def build_operations_gateway_grpc_client() -> OperationsGatewayGRPCClient:
    """
    Фабрика для создания экземпляра OperationsGatewayGRPCClient.

    :return: Инициализированный клиент для OperationsGatewayService.
    """
    return OperationsGatewayGRPCClient(channel=build_gateway_grpc_client())