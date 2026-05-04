# 🏦 Loan System API

REST API para gestión de préstamos bancarios construida con **FastAPI** y arquitectura limpia. Proyecto personal desarrollado para aprender backend profesional y preparación para entrevistas técnicas.

---

## 🚀 Tech Stack

- **Python 3.11**
- **FastAPI** — framework web
- **Pydantic v2** — validación de datos y settings
- **Resend** — envío de emails transaccionales
- **Pytest** — testing con 32+ tests
- **GitHub Actions** — CI/CD automático

---

## 📌 Features

- `POST /loans/bulk` — Crear un préstamo con validaciones de negocio
- `GET /loans/all` — Obtener todos los préstamos registrados
- Validación de credit score (300–850), monto y tiempo de pago
- Notificación por email al cliente cuando el préstamo es aprobado
- Persistencia automática en JSON
- Headers dinámicos (`x-user-id`) para trazabilidad
- Metadata completa por request (`created_at`, `created_by`, `request_id`)
- Variables de entorno con `pydantic-settings`
- CI/CD con GitHub Actions en cada push

---

## 🏗️ Arquitectura

```
├── app/
│   ├── config.py          # Variables de entorno (pydantic-settings)
│   ├── services/
│   │   ├── loan_service.py    # Lógica de negocio
│   │   └── email_service.py   # Servicio de email con Resend
│   ├── templates/
│   │   └── email_templates.py # Templates HTML de emails
│   └── dependencies/
├── models/
│   ├── loan.py            # Modelo Loan con to_response() y to_dict()
│   ├── client.py          # Modelo Client
│   └── bank.py            # Singleton Bank
├── routers/
│   └── loan_post.py       # Endpoints con manejo de errores
├── schemas/
│   └── schemas.py         # LoanCreate, LoanResponse, LoanFinalResponse
├── tests/                 # 32+ tests unitarios
├── .env.example           # Plantilla de variables de entorno
└── main.py                # Entry point minimalista
```

---

## ⚙️ Instalación local

```bash
# 1. Clonar el repo
git clone https://github.com/tuusuario/loan-system-api.git
cd loan-system-api

# 2. Crear entorno virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Mac/Linux

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env
# Edita .env con tus valores

# 5. Correr el servidor
uvicorn main:app --reload
```

Abre `http://localhost:8000/docs` para ver el Swagger.

---

## 🧪 Tests

```bash
pytest --cov
```

---

## 🔑 Variables de entorno


| Variable | Descripción | Default |
|---|---|---|
| `APP_NAME` | Nombre de la app | Loan System API |
| `DEBUG` | Modo debug | False |
| `EMAIL_ENABLED` | Activar emails reales | False |
| `EMAIL_FROM` | Remitente | onboarding@resend.dev |
| `RESEND_API_KEY` | API key de Resend | — |
| `SECRET_KEY` | Clave JWT (Fase 07) | — |

---

## 📈 Roadmap

- [x] Arquitectura limpia (router / service / schemas)
- [x] Singleton pattern (Bank)
- [x] Pydantic models y validaciones
- [x] Persistencia en JSON
- [x] CI/CD con GitHub Actions
- [x] Variables de entorno con pydantic-settings
- [x] Email service con Resend


---

## 👤 Autor

**Rafael Ruvalcaba** — México  
Proyecto personal de preparación para entrevistas backend.