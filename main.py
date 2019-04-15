#!/usr/bin/env python

import asyncio
import requests
import os
import json
from nats.aio.client import Client as NATS
from nats.aio.errors import ErrConnectionClosed, ErrTimeout, ErrNoServers

apiKey = os.environ["APIKEY"]
domain = os.environ["DOMAIN"]
sender = os.environ["SENDER"]
recipient = [os.environ["RECIPIENT"]]
subject = os.environ["NATSPOST"]

def send_simple_message(title):
    return requests.post(
        "https://api.mailgun.net/v3/{}/messages".format(domain),
        auth=("api", apiKey),
        data={"from": sender,
              "to": recipient,
              "subject": "Un râleur s'est exprimé !",
              "text": "Viens vite jeter un oeil à ce qu'il a bien pu raconter de beau sous le titre : {} !".format(title)})

async def run(loop):
    nc = NATS()

    await nc.connect("demo.nats.io:4222", loop=loop)

    async def message_handler(msg):
        data = json.loads(msg.data.decode())
        status = send_simple_message(data["Title"])
        print(status.text) 

    await nc.subscribe(subject, cb=message_handler)

    await asyncio.sleep(1324512000, loop=loop)

    await nc.drain()
    
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.close()