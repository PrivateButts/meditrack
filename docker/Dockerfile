FROM python:3.11-slim AS build-venv

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

# copy pipenv files
COPY ./Pipfile ./Pipfile
COPY ./Pipfile.lock ./Pipfile.lock

# install pipenv
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir pipenv

# Freeze requirements
RUN pipenv requirements > requirements.txt

# Create Virtualenv and Install
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.11-slim AS server

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

# Install dependencies
RUN apt update && apt install netcat-traditional -y

# Copy virtualenv
COPY --from=build-venv /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# copy project
COPY . .

EXPOSE 8000
ENTRYPOINT ["sh", "/usr/src/app/docker/entrypoint.sh"]
CMD [ "gunicorn", "meditrack.asgi:application", "--port", "8000", "--bind", "0.0.0.0", "-v2" ]
# HEALTHCHECK --interval=30s --timeout=30s --start-period=1m --retries=3 CMD [ "python", "manage.py", "health_check" ]
