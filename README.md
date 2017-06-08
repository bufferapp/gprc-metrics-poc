# Buffer Metrics

A monorepo for our unified metrics collection built on
[Protobufs](https://github.com/google/protobuf)
and [gRPC](http://www.grpc.io/)

## Setup

First install the [protoc](https://github.com/google/protobuf/releases) binary
and install all of the node dependencies in the `node` package directory:

```
cd node
npm install
```

Now you can generate all the gRPC code using `protoc` and `build.sh`:

```
./build.sh
```
