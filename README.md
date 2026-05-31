# Playwright API Automation Framework

## Overview

This project is an API Automation Framework built using Python, Pytest, and Playwright.

The framework follows a Service Object Model architecture and provides reusable components for API testing, request management, data generation, configuration management, and response validation.

The project uses the Restful Booker API as the target application for demonstrating CRUD operations and API automation best practices.

---

## Technology Stack

* Python 3.12
* Pytest
* Playwright API Testing
* Pydantic
* Faker
* Python Dotenv

---

## Framework Architecture

```text
Tests
  ↓
Services
  ↓
API Client
  ↓
Playwright Request Context
  ↓
API
```

### Project Structure

```text
API_Automation/

├── config/
│   └── config.py
│
├── core/
│   ├── api_client.py
│   └── request_builder.py
│
├── models/
│   ├── auth_model.py
│   ├── booking_model.py
│   └── partial_booking_model.py
│
├── services/
│   ├── auth_service.py
│   └── booking_service.py
│
├── test_data/
│   ├── auth_factory.py
│   └── booking_factory.py
│
├── validators/
│   └── response_validator.py
│
├── tests/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Implemented Features

### Authentication

* Token generation
* Reusable authentication service
* Environment-based credentials

### CRUD Operations

* Create Booking
* Get Booking
* Update Booking
* Partial Update Booking
* Delete Booking

### Test Data Management

* Pydantic models
* Factory Pattern
* Faker generated data

### Validation

* Status code validation
* Response validation layer

### Configuration Management

* Environment variables
* Config class
* .env support

---

## Installation

Clone repository:

```bash
git clone <repository-url>
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a .env file:

```env
BASE_URL=https://restful-booker.herokuapp.com

BOOKER_USERNAME=admin
BOOKER_PASSWORD=password123
```

---

## Execute Tests

Run all tests:

```bash
pytest
```

Run specific test:

```bash
pytest tests/test_create_booking.py
```

Run with verbose output:

```bash
pytest -v
```

---

## Future Improvements

* Docker Support
* GitHub Actions CI/CD
* Allure Reporting
* JSON Schema Validation
* Retry Mechanism
* Request/Response Logging
* Contract Testing
* Parallel Execution
