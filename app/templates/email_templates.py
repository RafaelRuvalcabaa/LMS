from __future__ import annotations

from pathlib import Path
from string import Template


_TEMPLATES_DIR = Path(__file__).resolve().parent
_LOAN_APPROVED_PATH = _TEMPLATES_DIR / "loan_approved.html"


def loan_approved_template(name, last_name, amount, monthly, time, date) -> str:
    """
    Renders HTML from a file on disk so template edits are reflected
    immediately without restarting long-running processes.
    """
    try:
        raw_template = _LOAN_APPROVED_PATH.read_text(encoding="utf-8")
        return Template(raw_template).safe_substitute(
            name=name,
            last_name=last_name,
            amount=amount,
            monthly=monthly,
            time=time,
            date=date,
        )
    except FileNotFoundError:
        return f"""
            <p>Dear {name} {last_name},</p>
            <p>Your loan was accepted for <strong>${amount}</strong>
            Monthly payment: <strong>${monthly}</strong><br/>
            for <strong>{time} months</strong>, today {date}.</p>
            <p>Terms and conditions apply.</p>
            <p><strong>Loans Rafael by Banamex</strong></p>
        """
