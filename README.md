# Static Website with Apache and Docker Compose

![Apache HTTP Server](https://img.shields.io/badge/Apache-HTTP%20Server-D22128?logo=apache)
![Docker Compose](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black)

A personal portfolio website served by Apache HTTP Server through Docker Compose. This project demonstrates a simple container-based environment for serving static HTML, CSS, JavaScript, and images.

## Architecture

The browser connects to Apache on host port `80`, bound to `127.0.0.1` for local access. A single container serves files mounted read-only from `website/` into `/usr/local/apache2/htdocs`.

There is no backend, database, package installation, or application build step. Google Fonts and skill icons from jsDelivr are loaded by the browser and require internet access.

## Project Structure

```text
.
├── docker-compose.yml
├── LICENSE
├── README.md
└── website/
    ├── index.html
    ├── script.js
    └── assets/
        ├── css/
        ├── icons/
        └── img/
```

## Requirements

- Docker Engine or Docker Desktop, with Docker running.
- The Docker Compose plugin (`docker compose`).
- Host port `80` available.
- Internet access to download the Apache image on the first run.

## Quick Start

Clone the repository and enter its directory:

```bash
git clone https://github.com/jacivaldocarvalho/web-dockercompose-apache-html.git
cd web-dockercompose-apache-html
```

Start Apache from the repository root:

```bash
docker compose up -d
```

Open [http://localhost](http://localhost) in your browser. The existing Compose configuration publishes host port `80`, not `8080`.

## Local Development

Edit files inside `website/` and refresh the browser. The bind mount makes local changes available to Apache without rebuilding an image. If changes are not visible, reload the page with the browser cache disabled.

No environment variables or `.env` file are required by the current configuration.

## Operations

Check the service status:

```bash
docker compose ps
```

Follow Apache logs:

```bash
docker compose logs -f apache
```

Stop and remove the Compose container and network:

```bash
docker compose down
```

The website source files remain in the local `website/` directory.

## Validation

Check the Compose configuration before starting the service:

```bash
docker compose config --quiet
```

After starting Apache, verify the HTTP response if `curl` is installed:

```bash
curl --fail --head http://localhost/
```

In the browser, check that profile images and styles load, contact links work, and the back-to-top button appears after scrolling and returns the page to the top.

There is currently no automated test suite or CI workflow. These commands describe manual validation and do not indicate a completed test run.

## Troubleshooting

| Symptom | Action |
| --- | --- |
| Docker cannot connect to the daemon | Start Docker and confirm your user has permission to access it. |
| Port `80` is already allocated | Identify the service using the port before deciding whether to stop it or change the Compose port mapping. |
| The container name is already in use | Inspect the existing `my-apache-website` container before removing or renaming anything. |
| The site does not load | Check `docker compose ps` and `docker compose logs apache`; use `http://localhost` rather than port `8080`. |
| Fonts or skill icons are missing | Check internet access and browser restrictions affecting Google Fonts or jsDelivr. |

## Current Limitations

- The Apache image uses `httpd:2.4.69`. The version tag can receive image updates; it is not pinned to an immutable digest. Review version updates explicitly.
- The website bind mount is read-only inside the container; edit source files on the host.
- Access is restricted to `127.0.0.1:80`. Access from other machines requires an explicit port-binding change.
- TLS and production deployment configuration are not included.

## Contributing

Open an issue to describe a problem or propose a focused improvement. For pull requests, explain the change and include the validation you performed.

## License

This project is licensed under the [MIT License](LICENSE).

## Author

**Jacivaldo Carvalho**

Telecommunications Engineer | DevOps Engineer | SRE | Networking

[GitHub](https://github.com/jacivaldocarvalho) | [LinkedIn](https://www.linkedin.com/in/jacivaldocarvalho) | [Website](https://www.jacivaldocarvalho.com/)
