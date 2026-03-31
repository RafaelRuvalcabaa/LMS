import logging  
import os 

os.makedirs("logs", exist_ok= True)

logging.basicConfig(filename="logs/prestamos.log", level = logging.DEBUG, format= "%(asctime)s  | %(levelname)s | %(message)s ")


logger = logging.getLogger(__name__)