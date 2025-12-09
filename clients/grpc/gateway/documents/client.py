from grpc import Channel

from clients.grpc.client import GRPCClient
from clients.grpc.gateway.client import build_gateway_grpc_client
from contracts.services.gateway.documents.rpc_get_contract_document_pb2 import (GetContractDocumentRequest,
                                                                                GetContractDocumentResponse)
from contracts.services.gateway.documents.rpc_get_tariff_document_pb2 import (GetTariffDocumentRequest,
                                                                              GetTariffDocumentResponse)
from contracts.services.gateway.documents.documents_gateway_service_pb2_grpc import DocumentsGatewayServiceStub


class DocumentsGatewayGRPCClient(GRPCClient):
    def __init__(self, channel: Channel):
        super().__init__(channel)

        self.stub = DocumentsGatewayServiceStub(channel)

    def get_contract_document_api(self, request: GetContractDocumentRequest) -> GetContractDocumentResponse:
        return self.stub.GetContractDocument(request)

    def get_tariff_document_api(self, request: GetTariffDocumentRequest) -> GetContractDocumentResponse:
        return self.stub.GetTariffDocument(request)

    def get_contract(self, account_id: str) -> GetContractDocumentResponse:
        request = GetContractDocumentRequest(account_id = account_id)
        return self.get_contract_document_api(request)

    def get_tariff(self, account_id: str) -> GetTariffDocumentResponse:
        request = GetTariffDocumentRequest(account_id=account_id)
        return self.get_tariff_document_api(request)

def build_documents_gateway_grpc_client() -> DocumentsGatewayGRPCClient:
    return DocumentsGatewayGRPCClient(channel=build_gateway_grpc_client())