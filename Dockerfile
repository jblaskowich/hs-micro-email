FROM python:3.8.0a3-alpine3.9

RUN python -m pip install asyncio-nats-client

RUN python -m pip install requests

COPY main.py .

ENTRYPOINT [ "python", "-u", "main.py" ]