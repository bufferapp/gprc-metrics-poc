// GENERATED CODE -- DO NOT EDIT!

'use strict';
var grpc = require('grpc');
var proto_collector_pb = require('../proto/collector_pb.js');

function serialize_metrics_Response(arg) {
  if (!(arg instanceof proto_collector_pb.Response)) {
    throw new Error('Expected argument of type metrics.Response');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_metrics_Response(buffer_arg) {
  return proto_collector_pb.Response.deserializeBinary(new Uint8Array(buffer_arg));
}

function serialize_metrics_Visit(arg) {
  if (!(arg instanceof proto_collector_pb.Visit)) {
    throw new Error('Expected argument of type metrics.Visit');
  }
  return new Buffer(arg.serializeBinary());
}

function deserialize_metrics_Visit(buffer_arg) {
  return proto_collector_pb.Visit.deserializeBinary(new Uint8Array(buffer_arg));
}


// TODO - Figure out how to get this to work
// import "google/protobuf/timestamp.proto";
//
// The service definition
var MetricsCollectorService = exports.MetricsCollectorService = {
  trackVisit: {
    path: '/metrics.MetricsCollector/TrackVisit',
    requestStream: false,
    responseStream: false,
    requestType: proto_collector_pb.Visit,
    responseType: proto_collector_pb.Response,
    requestSerialize: serialize_metrics_Visit,
    requestDeserialize: deserialize_metrics_Visit,
    responseSerialize: serialize_metrics_Response,
    responseDeserialize: deserialize_metrics_Response,
  },
};

exports.MetricsCollectorClient = grpc.makeGenericClientConstructor(MetricsCollectorService);
