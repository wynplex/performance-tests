import grpc

from contracts.services.gateway.users.rpc_create_user_pb2 import CreateUserRequest, CreateUserResponse
from contracts.services.gateway.users.users_gateway_service_pb2_grpc import UsersGatewayServiceStub

from contracts.services.gateway.accounts.accounts_gateway_service_pb2_grpc import AccountsGatewayServiceStub
from contracts.services.gateway.accounts.rpc_open_debit_card_account_pb2 import OpenDebitCardAccountRequest, OpenDebitCardAccountResponse

from tools.fakers import fake

# Установка соединения с gRPC сервером
channel = grpc.insecure_channel("localhost:9003")

# Инициализация клиентов для сервисов
users_gateway_service = UsersGatewayServiceStub(channel)
accounts_gateway_service = AccountsGatewayServiceStub(channel)

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
    user_id = create_user_response.user.id,
)
# Выполнение RPC вызова для открытия счета с дебетовой картой
open_debit_card_response: OpenDebitCardAccountResponse = accounts_gateway_service.OpenDebitCardAccount(
    open_debit_card_request)
print("Open debit card account response:", open_debit_card_response)