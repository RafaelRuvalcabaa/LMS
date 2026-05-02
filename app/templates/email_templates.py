
def loan_approved_template(name, last_name,amount, time, date) -> str: 
    
    return f"""
        <p>Dear {name} {last_name},</p>
        <p>Your loan was accepted for <strong>${amount}</strong> 
        for <strong>{time} months</strong>, today {date}.</p>
        <p>Terms and conditions apply.</p>
        <p><strong>Loans Rafael by Banamex</strong></p>
    """