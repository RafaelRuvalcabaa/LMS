import pytest 
from models.bank import Bank 


@pytest.fixture(autouse=True)
def reset_bank(): 
    Bank._instancia = None
    yield
    Bank._instancia = None

@pytest.fixture
def config(): 
    name = "Banamex"
    capital = 10000
    return Bank(name, capital)

@pytest.mark.parametrize("capital", [0,-1,-1000])
def test_menor0(capital): 
    with pytest.raises(ValueError): 
        Bank("Banamex", capital)

@pytest.mark.parametrize("name", [""])
def test_name(name): 
    with pytest.raises(ValueError): 
        Bank(name, 5050050)

def test_str_(config): 
    assert "Banamex" in str(config)

def test_capital_error(config): 
    with pytest.raises(TypeError):
        config.capital = "Hola"

def test_capital_update(config): 
    config.capital = 9999
    assert config.capital == 9999

def test_amountcapital(config): 
    with pytest.raises(ValueError): 
        config.withdraw(90000000000000)

def test_withdraw(config): 
    config.withdraw(100)
    assert config.capital == 9900