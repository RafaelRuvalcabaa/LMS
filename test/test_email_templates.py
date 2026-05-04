from app.templates.email_templates import loan_approved_template


def test_loan_approved_template_substitutes_values():
    html = loan_approved_template("Ada", "Lovelace", 1200, 200, 6, "2026-05-03")
    assert "Ada Lovelace" in html
    assert "$1200" in html
    assert "$200" in html
    assert "6 months" in html
    assert "2026-05-03" in html
