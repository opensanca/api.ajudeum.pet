# Catchiorrineo

[![Build Status](https://travis-ci.org/opensanca/api.ajudeum.pet.svg?branch=master)](https://travis-ci.org/opensanca/api.ajudeum.pet)
[![Coverage Status](https://coveralls.io/repos/github/opensanca/api.ajudeum.pet/badge.svg?branch=master)](https://coveralls.io/github/opensanca/api.ajudeum.pet?branch=master)
[![Code Health](https://landscape.io/github/opensanca/api.ajudeum.pet/master/landscape.svg?style=flat)](https://landscape.io/github/opensanca/api.ajudeum.pet/master)
[![Maintainability](https://api.codeclimate.com/v1/badges/67158d8a92683da6a611/maintainability)](https://codeclimate.com/github/opensanca/api.ajudeum.pet/maintainability)

## Instalar:
* Python 3

## Configuração

### Virtualenv
Crie um ambiente virtual para isolar as dependências do projeto:

```sh
$ python -m venv .env
$ source .env/bin/activate
```

Para instalar os pacotes:

```sh
(.env) $ pip install -r requirements.txt
```

### Execução
Quando executar o projeto pela primeira vez, é necessário que a base seja criada. Para criar o banco de dados:

```sh
(.env) $ flask db upgrade
```

Para executar o servidor de desenvolvimento:

```sh
(.env) $ flask run
```
