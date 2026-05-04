from logs import logger 
from models.loan import Loan 
from app.config import get_settings
import resend 
from app.templates.email_templates import loan_approved_template

settings = get_settings()
resend.api_key = settings.resend_api_key

class EmailService:

    def send_loan_email(self, loan: Loan): 
        if loan.prestamo == False:
           logger.info("Loan was refused")
        elif settings.email_enabled and loan.prestamo == True: 
            monthly_payment = loan.amount / loan.time
            resend.Emails.send({
                "from": settings.email_from, 
                "to": loan.cliente._email, 
                "subject": "Your loan was accepted", 
                "html": loan_approved_template( loan.cliente._name,
    loan.cliente._last_name,
    loan.amount,
    monthly_payment,
    loan.time,
    loan.created_at.strftime("%Y-%m-%d"))
            })
            logger.info(f"Dear.{loan.cliente._name}, Your loan was accepted for {loan.amount}, your have {loan.time} to pay. Atte. Loans Rafael by Banamex. Date: {loan.created_at}, Email was sent to {loan.cliente._email}")
        else: 
            logger.info(f"Dear.{loan.cliente._name}, Your loan was accepted for {loan.amount}, your have {loan.time} to pay. Atte. Loans Rafael by Banamex. Date: {loan.created_at}")





           
        
