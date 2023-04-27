# https://github.com/devcontainers/images/tree/main/src/python
FROM mcr.microsoft.com/devcontainers/python:3.8-bullseye

# Uninstall pre-installed formatting and linting tools
# They would conflict with our pinned versions
RUN pipx uninstall flake8
RUN pipx uninstall mypy

RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add -
RUN curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list
RUN apt update
ENV ACCEPT_EULA=Y
RUN apt-get update && apt-get install -y build-essential git libgdiplus libx11-dev python3-opencv tesseract-ocr tesseract-ocr-deu && \
    apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*