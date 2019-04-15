# hs-micro-email

## Overview

This is a educational purpose app: a simple bloging like platform.

## Architecture

```
             ---------
             | EMAIL |
             ---------
                 ^
                 |
---------     --------     --------     -----------
| FRONT | --> | NATS | --> | BACK | --> | MariaDB |
---------     --------     --------     -----------
```

 - Front: a go frontend (gorilla, html/templatesn go-nats)
 - Back: a go backend (go-nats, database/sql)
 - Email: a python notification service

## Run

This script use [mailgun API](https://www.mailgun.com/) to send email.

### Binary

```
$ python -m pip install asyncio-nats-client
$ python -m pip install requests
$ export APIKEY="your_mailgun_apiKey"
$ export DOMAIN="your_mailgun_domain"
$ export RECIPIENT="your_recipient"
$ export SENDER="your_sender"                  // eg. "bot@leraleur.12monkey.fr"
$ export NATSPOST="your_nats_post_channel"     // the channel used for posts
$ python main.py
```

### Docker

```
$ export APIKEY="your_mailgun_apiKey"
$ export DOMAIN="your_mailgun_domain"
$ export RECIPIENT="your_recipient"
$ export SENDER="your_sender"                  // eg. "bot@leraleur.12monkey.fr"
$ export NATSPOST="your_nats_post_channel"     // the channel used for posts
$ docker run -d -e APIKEY=${APIKEY} -e DOMAIN=${DOMAIN} -e RECIPIENT=${RECIPIENT} \ 
    -e SENDER=${SENDER} -e NATSPOST=${NATSPOST} \
    jblaskowich/hs-micro-email:$release
```
