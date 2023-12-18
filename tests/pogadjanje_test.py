import pytest
from algokit_utils import (
    ApplicationClient,
    ApplicationSpecification,
    get_localnet_default_account,
)
from algosdk.v2client.algod import AlgodClient

from smart_contracts.pogadjanje import contract as pogadjanje_contract


@pytest.fixture(scope="session")
def pogadjanje_app_spec(algod_client: AlgodClient) -> ApplicationSpecification:
    return pogadjanje_contract.app.build(algod_client)


@pytest.fixture(scope="session")
def pogadjanje_client(
    algod_client: AlgodClient, pogadjanje_app_spec: ApplicationSpecification
) -> ApplicationClient:
    client = ApplicationClient(
        algod_client,
        app_spec=pogadjanje_app_spec,
        signer=get_localnet_default_account(algod_client),
    )
    client.create()
    return client


def test_says_hello(pogadjanje_client: ApplicationClient) -> None:
    result = pogadjanje_client.call(pogadjanje_contract.hello, name="World")

    assert result.return_value == "Hello, World"
