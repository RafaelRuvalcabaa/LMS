from models.client import Client
from models.bank import Bank


h1 = Client("Daniel", "Estrada", "Calle Pirul 123", 1)

# Ejemplo de lo que pasará:
banco1 = Bank("Mi Banco", 2000000000000000000)  # Todo bien, se crea.
print(banco1.capital) # Sigue valiendo 5000
