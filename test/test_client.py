import pytest 
from models.client import Client
from errors.errors_borrowed import NoNameClient


@pytest.fixture
def build_client(): 
    name= "Rafael"
    last_name = "Ruvalcaba"
    city = "Guadalajara"
    score = 750
    return Client(name, last_name, city, score)

def test_build_client(build_client): 
 
    assert "Rafael" in str(build_client)

def test_client_without_name():
    with pytest.raises(NoNameClient):
        Client("", "Ruvalcaba", "Guadalajara", 750)


@pytest.mark.parametrize("name, last_name",[
    ("","Ruvalcaba"),
     ("Rafael", ""),
     ("",""),
])
def test_without_names(name, last_name):
    with pytest.raises(NoNameClient): 
        Client(name, last_name, "Guadalajara", 750)