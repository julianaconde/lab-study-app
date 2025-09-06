# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.0/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon)
ARG VARIANT="3.10-bullseye"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

## Path to the virtualenv
ARG VENV_PATH="/home/vscode/venv"

## Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1

## Set working directory
WORKDIR /workspaces/lab-study-app

## Copy requirements and install in virtualenv
COPY requirements.txt /tmp/pip-tmp/
RUN su vscode -c "python -m venv ${VENV_PATH}" \
    && su vscode -c "${VENV_PATH}/bin/pip --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt" \
    && rm -rf /tmp/pip-tmp

## Expose the port used by the application
EXPOSE 8000

## Set default command using virtualenv
CMD ["bash", "-c", "source ${VENV_PATH}/bin/activate && python app.py"]
