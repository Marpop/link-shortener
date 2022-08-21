# link shortener

Simple link shortening django app

[![Built with Cookiecutter Django](https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter)](https://github.com/cookiecutter/cookiecutter-django/)
[![Black code style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

### Prerequisites

- Docker
- docker-compose

## Basic Commands

### Setting up super user

      make manage createsuperuser

### Type checks and linting (flake8 and pylint)

     make lint

### Test and coverage

     make test
     make coverage

### Running locally

     docker-compose up

- API: http://0.0.0.0:8000/api/
- API docs: http://0.0.0.0:8000/api/docs/
- API schema: http://0.0.0.0:8000/api/schema/
