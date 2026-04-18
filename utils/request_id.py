import uuid 
from logs import logger

def generate_request_id(): 
    try: 
        return str(uuid.uuid4())
    except Exception as e: 
        logger.error("Error generating request_i")
        raise ValueError ("Error generating request_i") from e 


print(generate_request_id())