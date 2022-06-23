from ape import project, Contract
import pytest


@pytest.fixture(scope="session")
def deployer(accounts):
    yield accounts[0]


@pytest.fixture(scope="session")
def user(accounts):
    yield accounts[1]


@pytest.fixture(scope="session")
def vault():
    yield Contract("0xa258C4606Ca8206D8aA700cE2143D7db854D168c")


@pytest.fixture()
def zap(project, vault, deployer):
    yield deployer.deploy(project.ZapEth, vault)
