# Loan Management System
Python backend · In development

Sistema de gestión de préstamos bancarios construido en Python puro. Proyecto progresivo — crece con cada fase del roadmap hasta convertirse en una API REST con base de datos y Docker.

## Stack actual
- **Lenguaje:** Python 3.11
- **Testing:** pytest
- **Patrones:** OOP · Singleton · Decoradores

## Estructura
  loan_system/
  ├── models/
  │   ├── bank.py        # Singleton
  │   ├── client.py
  │   ├── loan.py
  │   └── payback.py
  ├── decorators/
  │   └── log_error.py   # @log_error_wrap
  ├── errors/
  │   └── errors_borrowed.py
  ├── test/
  │   ├── test_client.py
  │   └── test_loan.py
  └── logs/
