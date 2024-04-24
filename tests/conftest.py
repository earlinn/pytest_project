import datetime
import pytest


@pytest.fixture
def return_10():
    return 10


# Параметр scope для @pytest.fixture() может иметь следующие значения:
# function, class, module, package, session. По умолчанию scope='function'.

# Параметр autouse=True говорит о том, что фикстура вызывается автоматически,
# ее не нужно передавать как параметр теста


@pytest.fixture(scope="session", autouse=True)
def session_fixture():
    print("\nTest setup")
    yield
    print("\nTest teardown")
    print(datetime.datetime.now())
