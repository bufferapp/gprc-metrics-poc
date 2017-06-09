# gRPC Collector Service

A [gRPC](http://www.grpc.io) service that collects metrics from services and
forwards them to the Kinesis data stream for consumption.

## Setup

First install the dependencies:

- [Golang](https://golang.org/)
- [Glide](https://github.com/Masterminds/glide)
- [protoc](https://github.com/google/protobuf/releases)

Install all the golang dependencies. Be sure to have you GOPATH set up before.

```
glide install
```

To run the collector service, use your AWS credentials and run this command (or save as a shell script for easy re-use):

```
#!/bin/sh

KINESIS_STREAM="dev_buffermetrics" \
  AWS_ACCESS_KEY_ID="1234567890ASDFGHJKL" \
  AWS_SECRET_ACCESS_KEY="dfghjk567890fghjk567890fghj" \
  go run main.go
```
