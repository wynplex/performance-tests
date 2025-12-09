# Импортируем фабричные функции для создания API-клиентов
from clients.grpc.gateway.accounts.client import build_accounts_gateway_grpc_client
from clients.grpc.gateway.operations.client import build_operations_gateway_grpc_client
from clients.grpc.gateway.users.client import build_users_gateway_grpc_client

# Создаём API-клиенты для работы с сервисами Users, Accounts и Operations
users_gateway_client = build_users_gateway_grpc_client()
accounts_gateway_client = build_accounts_gateway_grpc_client()
operations_gateway_client = build_operations_gateway_grpc_client()

# Шаг 1. Создаём пользователя
create_user_response = users_gateway_client.create_user()
print("Create user response:", create_user_response)

# Шаг 2. Открываем дебетовый счёт для только что созданного пользователя
open_debit_card_response = accounts_gateway_client.open_debit_card_account(create_user_response.user.id)
card_id = open_debit_card_response.account.cards[0].id
account_id = open_debit_card_response.account.id
print("Open debit card account response:", open_debit_card_response)

# Шаг 3. Пополняем только что созданную карту пользователя
make_top_up_response = operations_gateway_client.make_top_up_operation(card_id=card_id, account_id=account_id)
print("Make top up operation response:", make_top_up_response)