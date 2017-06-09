# Consumer demo

This is a demo stream consumer built on [Cerone](https://github.com/bufferapp/cerone)

## Usage

The project runs using Docker Compose in development. To start, create a file
called `consumer.env` and add you AWS credentials:

```
AWS_ACCESS_KEY_ID="1234567890ASDFGHJKL"
AWS_SECRET_ACCESS_KEY="QWERTYUIOPASDFGHJKLZXCVBNM"
```

To capture logging output create a log file:

```
touch consumer.log
```

Now with those in place, start all the containers:

```
docker-compose up
```

Alternatively, you can start each individually, which may save time during
development so the database can stay running.

```
docker-compose start db
docker-compose start consumer
docker-compose logs -f consumer
```
