# **Docker Compose para Executar uma Aplicação HTML em um Container Apache**

## **Objetivo**
Este repositório contém uma configuração simples de **Docker Compose** para executar uma aplicação **HTML** em um container **Apache**. Ele oferece uma forma prática de aprender sobre containers, Docker Compose e como configurar um ambiente de desenvolvimento básico utilizando containers para servir uma aplicação estática.


## **Estrutura do Projeto**
O repositório inclui os seguintes arquivos principais:

- **docker-compose.yml**: Arquivo de configuração do Docker Compose que define os containers Apache e a aplicação HTML.
- **index.html**: Arquivo HTML simples que é servido pelo Apache dentro do container.


## **Como Usar**

### **1. Requisitos**
Para executar este projeto, você precisa ter o **Docker** e o **Docker Compose** instalados na sua máquina. Caso ainda não tenha, siga a documentação oficial de instalação:

- [Instalar o Docker](https://docs.docker.com/get-docker/)
- [Instalar o Docker Compose](https://docs.docker.com/compose/install/)

### **2. Clonando o Repositório**

Primeiro, clone o repositório para sua máquina local:

```bash
git clone https://github.com/jacivaldocarvalho/docker-compose-projeto-1.git
cd docker-compose-projeto-1
```

### **3. Executando a Aplicação**

Com o Docker e Docker Compose instalados, basta rodar o seguinte comando para iniciar o container Apache e servir a aplicação HTML:

```bash
docker-compose up
```

Isso irá criar o container e mapear a aplicação HTML na porta `8080`. Para acessá-la, basta abrir seu navegador e acessar:

```
http://localhost:8080
```


## **Evoluções Possíveis para o Projeto**

### 1. **Adicionar Suporte a Multicontainers**
Incorpore outros containers ao projeto, como bancos de dados ou servidores de backend, utilizando o Docker Compose. Isso vai permitir a criação de um ambiente mais robusto e completo, com uma aplicação mais realista.

### 2. **Implementação de Variáveis de Ambiente**
Utilize variáveis de ambiente no `docker-compose.yml` para configurar a aplicação de maneira dinâmica e permitir uma melhor customização entre diferentes ambientes (desenvolvimento, teste, produção).

### 3. **Automatização de Build e Deploy**
Configure uma pipeline de **CI/CD** utilizando **GitHub Actions** ou **GitLab CI** para automatizar o processo de build, testes e deploy da aplicação contêinerizada.

### 4. **Adição de Testes Automatizados**
Implemente testes para verificar se a aplicação está sendo servida corretamente, tanto em termos de conectividade quanto de funcionalidade.

## Contribuições

Se você tiver sugestões de melhorias ou encontrar problemas com o script, sinta-se à vontade para abrir um **issue** ou submeter um **pull request**.

## Contatos e Network

- **LinkedIn**: [LinkedIn](https://www.linkedin.com/in/jacivaldocarvalho/) 👔
- **E-mail**: [E-mail](mailto:jacivaldocarvalho@gmail.com) 📧
- **GitHub**: [GitHub](https://github.com/jacivaldocarvalho) 🐙
- **Medium**: [Medium](https://medium.com/@jacivaldocarvalho) ✍️

Sempre aberto a novas conexões e oportunidades de aprendizado!

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

## **Referências Bibliográficas**

Para aprender mais sobre os conceitos utilizados neste projeto, consulte as seguintes fontes:

- [Documentação Oficial do Docker](https://docs.docker.com/)
- [Docker Compose - Documentação Oficial](https://docs.docker.com/compose/)
- [Guia de Introdução ao Docker Compose](https://docs.docker.com/compose/gettingstarted/)

