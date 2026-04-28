import json 
from pathlib import Path
from typing import Any 

def save_to_json(data: list[dict], filename= "loans.json"):
    """
    Guarda una lista de diccionarios en un archivo JSON.
    """
    filepath = Path(filename)

    with open(filepath, "w", encoding = 'utf-8') as file: 
        json.dump(data, file, indent=4, ensure_ascii= False)

def load_from_json(filename: str = "loans.json") -> list[dict]:
    
    filepath = Path(filename)

    if not filepath.exists():
        return []
    
    with open(filepath, "r", encoding='utf-8') as file: 
        return json.load(file)