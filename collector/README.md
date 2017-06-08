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

Next, generate the gRPC code using `protoc`:

```
protoc buffer-metrics-proto/collector.proto \
  --go_out=plugins=grpc:. \
  --python_out=.
```

Now you should be able to run your application;

```
go run main.go
```
