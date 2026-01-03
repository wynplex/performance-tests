from locust import TaskSet, SequentialTaskSet

from clients.http.gateway.accounts.client import AccountsGatewayHTTPClient, build_accounts_gateway_locust_http_client
from clients.http.gateway.cards.client import CardsGatewayHTTPClient, build_cards_gateway_locust_http_client
from clients.http.gateway.documents.client import DocumentsGatewayHTTPClient, build_documents_gateway_locust_http_client
from clients.http.gateway.operations.client import OperationsGatewayHTTPClient, \
	build_operations_gateway_locust_http_client
from clients.http.gateway.users.client import UsersGatewayHTTPClient, build_users_gateway_locust_http_client


class GatewayHTTPTaskSet(TaskSet):
	users_gateway_client: UsersGatewayHTTPClient
	cards_gateway_client: CardsGatewayHTTPClient
	accounts_gateway_client: AccountsGatewayHTTPClient
	documents_gateway_client: DocumentsGatewayHTTPClient
	operations_gateway_client: OperationsGatewayHTTPClient

	def on_start(self) -> None:
		self.users_gateway_client = build_users_gateway_locust_http_client(self.user.environment)
		self.cards_gateway_client = build_cards_gateway_locust_http_client(self.user.environment)
		self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.user.environment)
		self.documents_gateway_client = build_documents_gateway_locust_http_client(self.user.environment)
		self.operations_gateway_client = build_operations_gateway_locust_http_client(self.user.environment)

class GatewayHTTPSequentialTaskSet(SequentialTaskSet):
	users_gateway_client: UsersGatewayHTTPClient
	cards_gateway_client: CardsGatewayHTTPClient
	accounts_gateway_client: AccountsGatewayHTTPClient
	documents_gateway_client: DocumentsGatewayHTTPClient
	operations_gateway_client: OperationsGatewayHTTPClient

	def on_start(self) -> None:
		self.users_gateway_client = build_users_gateway_locust_http_client(self.user.environment)
		self.cards_gateway_client = build_cards_gateway_locust_http_client(self.user.environment)
		self.accounts_gateway_client = build_accounts_gateway_locust_http_client(self.user.environment)
		self.documents_gateway_client = build_documents_gateway_locust_http_client(self.user.environment)
		self.operations_gateway_client = build_operations_gateway_locust_http_client(self.user.environment)