import grpc

from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub

from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import (OpenDebitCardAccountRequest,
                                                                                 OpenDebitCardAccountResponse)

from contracts.services.gateway.operations.operations_gateway_service_pb2_grpc import OperationsGatewayServiceStub
from contracts.services.gateway.operations.rpc_make_top_up_operation_pb2 import (MakeTopUpOperationRequest,
                                                                                 MakeTopUpOperationResponse)
from contracts.services.operations.operation_pb2 import OperationStatus

from tools.fakers import fake

# Установка соединения с gRPC сервером
channel = grpc.insecure_channel("localhost:9003")

# Инициализация клиентов для сервисов
users_gateway_service = UsersGatewayServiceStub(channel)
accounts_gateway_service = AccountsGatewayServiceStub(channel)
operations_gateway_service = OperationsGatewayServiceStub(channel)

# Шаг 1: Создание нового пользователя
# Формирование тела запроса с фейковыми данными пользователя
create_user_request = CreateUserRequest(
    email=fake.email(),
    last_name=fake.last_name(),
    first_name=fake.first_name(),
    middle_name=fake.middle_name(),
    phone_number=fake.phone_number()
)
# Выполнение RPC вызова для создания пользователя
create_user_response: CreateUserResponse = users_gateway_service.CreateUser(create_user_request)
print("Create user response:", create_user_response)

# Шаг 2: Открытие дебетового счета для созданного пользователя
# Формирование тела запроса с ID созданного пользователя
open_debit_card_request = OpenDebitCardAccountRequest(
    user_id=create_user_response.user.id,
)
# Выполнение RPC вызова для открытия счета с дебетовой картой
open_debit_card_response: OpenDebitCardAccountResponse = accounts_gateway_service.OpenDebitCardAccount(
    open_debit_card_request)
print("Open credit card account response:", open_debit_card_response)

#Шаг 3: Пополнение счёта на созданный аккаунт
#Формирование тела запроса со статусом "completed", рандомной суммой, card_id и account_id полученными при создании
# дебетового счёта пользователя
make_top_up_request = MakeTopUpOperationRequest(
    status=OperationStatus.OPERATION_STATUS_COMPLETED,
    amount=fake.amount(),
    card_id=open_debit_card_response.account.cards[0].id,
    account_id=open_debit_card_response.account.id,
)
#Выполнение RPC вызова для пополнения счёта
make_top_up_response = operations_gateway_service.MakeTopUpOperation(make_top_up_request)
print("Make purchase operation response:", make_top_up_response)
