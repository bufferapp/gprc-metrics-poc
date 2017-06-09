#!/bin/sh
NODE_PLUGIN=./node/node_modules/.bin/grpc_tools_node_protoc_plugin

protoc proto/collector.proto \
  --go_out=plugins=grpc:collector \
  --python_out=./python \
  --grpc_out=node \
  --js_out=import_style=commonjs:node \
  --plugin=protoc-gen-grpc=$NODE_PLUGIN

cp -R python/proto/ consumer-demo
