# temp-racatao

Project Description

## Qual o objetivo deste repositório?

## Quais são os outros repositórios desta solução?

---

<p align="center">
    Adicione aqui badges de qualidade do código
</p>

---


## Urls
| Environment  |  Url  |
| - | - |
| Sandbox | xxx |
| Produção | xxx |
| Sonar |  xxx |
| CI/CD  |  xxx |


## Setup

1 - Para gerenciar as versões de python e a criação de virtualenvs, instale essas duas ferramentas:

- [pyenv](https://github.com/pyenv/pyenv)
- [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv)


2 - Verifique a versão corrente do projeto no arquivo .python-version e instale caso necessário

```bash
pyenv install <version>
```

3 - Crie um virtualenv para o projeto

```bash
pyenv virtualenv <python-version> tempracatao
```

4 - Ative o virtualenv

```bash
pyenv activate tempracatao
```

5 - Instale as dependencias do projeto

```
make dev-dependencies
```


## Gerando uma nova versão de projeto.

1 - Instale o [nvm](https://github.com/nvm-sh/nvm)

2 - Habilite a versão de node para o projeto com o comando `nvm`

3 - Instale as dependências de node para o projeto

```
npm install
```

4 - Gere uma nova versão do projeto seguindo os passos do `release-it` e o padrão do [semver](https://semver.org/)

```
npx release-it
```
