from enum import StrEnum
from typing import List

from pydantic import BaseModel, ConfigDict, Field
from tools.fakers import fake


class OperationType(StrEnum):
    FEE = "FEE"
    TOP_UP = "TOP_UP"
    PURCHASE = "PURCHASE"
    CASHBACK = "CASHBACK"
    TRANSFER = "TRANSFER"
    BILL_PAYMENT = "BILL_PAYMENT"
    CASH_WITHDRAWAL = "CASH_WITHDRAWAL"


class OperationStatus(StrEnum):
    FAILED = "FAILED"
    COMPLETED = "COMPLETED"
    IN_PROGRESS = "IN_PROGRESS"
    UNSPECIFIED = "UNSPECIFIED"


class OperationSchema(BaseModel):
    """
    Структура данных операции.
    """
    model_config = ConfigDict(populate_by_name=True)

    id: str
    type: OperationType
    status: OperationStatus
    amount: float
    card_id: str = Field(alias="cardId")
    category: str
    created_at: str = Field(alias="createdAt")
    account_id: str = Field(alias="accountId")


class OperationReceiptSchema(BaseModel):
    """
    Структура данных чека операции.
    """
    url: str
    document: str


class OperationsSummarySchema(BaseModel):
    """
    Структура сводных данных по операциям.
    """
    model_config = ConfigDict(populate_by_name=True)

    spent_amount: float = Field(alias="spentAmount")
    received_amount: float = Field(alias="receivedAmount")
    cashback_amount: float = Field(alias="cashbackAmount")


class GetOperationResponseSchema(BaseModel):
    """
    Структура ответа на получение детальной информации об операции.
    """
    operation: OperationSchema


class GetOperationsResponseSchema(BaseModel):
    """
    Структура ответа на получение списка операций.
    """
    operations: List[OperationSchema]


class GetOperationsSummaryResponseSchema(BaseModel):
    """
    Структура ответа на получение сводки по операциям.
    """
    summary: OperationsSummarySchema


class GetOperationReceiptResponseSchema(BaseModel):
    """
    Структура ответа на получение чека операции.
    """
    receipt: OperationReceiptSchema


class MakeFeeOperationResponseSchema(BaseModel):
    """
    Структура ответа на создание операции комиссии.
    """
    operation: OperationSchema


class MakeTopUpOperationResponseSchema(BaseModel):
    """
    Структура ответа на создание операции пополнения.
    """
    operation: OperationSchema


class MakeCashbackOperationResponseSchema(BaseModel):
    """
    Структура ответа на создание операции кэшбэка.
    """
    operation: OperationSchema


class MakeTransferOperationResponseSchema(BaseModel):
    """
    Структура ответа на создание операции перевода.
    """
    operation: OperationSchema


class MakePurchaseOperationResponseSchema(BaseModel):
    """
    Структура ответа на создание операции покупки.
    """
    operation: OperationSchema


class MakeBillPaymentOperationResponseSchema(BaseModel):
    """
    Структура ответа на создание операции оплаты счета.
    """
    operation: OperationSchema


class MakeCashWithdrawalOperationResponseSchema(BaseModel):
    """
    Структура ответа на создание операции снятия наличных.
    """
    operation: OperationSchema


class GetOperationsQuerySchema(BaseModel):
    """
    Структура данных для получения списка операций аккаунта.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class GetOperationsSummaryQuerySchema(BaseModel):
    """
    Структура данных для получения общих данных операций по аккаунту.
    """
    model_config = ConfigDict(populate_by_name=True)

    account_id: str = Field(alias="accountId")


class MakeOperationRequestSchema(BaseModel):
    """
    Базовая структура данных для большинства POST запросов по операциям аккаунта.
    """
    model_config = ConfigDict(populate_by_name=True)

    status: str = Field(default_factory=lambda: fake.enum(OperationStatus))
    amount: float = Field(default_factory=fake.amount)
    card_id: str = Field(alias="cardId")
    account_id: str = Field(alias="accountId")


class MakeFeeOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции комиссии.
    """
    pass


class MakeTopUpOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции пополнения счета.
    """
    pass


class MakeCashbackOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции кэшбэка.
    """
    pass


class MakeTransferOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции перевода.
    """
    pass


class MakePurchaseOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции покупки.
    """
    category: str = Field(default_factory=fake.category)


class MakeBillPaymentOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции оплаты счета.
    """
    pass


class MakeCashWithdrawalOperationRequestSchema(MakeOperationRequestSchema):
    """
    Структура данных для создания операции снятия наличных.
    """
    pass
