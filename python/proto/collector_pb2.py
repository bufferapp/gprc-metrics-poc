# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/collector.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/collector.proto',
  package='metrics',
  syntax='proto3',
  serialized_pb=_b('\n\x15proto/collector.proto\x12\x07metrics\"\x82\x01\n\x05Visit\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x03 \x01(\t\x12\n\n\x02ip\x18\x04 \x01(\t\x12\x19\n\x03utm\x18\x05 \x01(\x0b\x32\x0c.metrics.Utm\x12%\n\tuseragent\x18\x06 \x01(\x0b\x32\x12.metrics.UserAgent\x12\x12\n\nvisitor_id\x18\x07 \x01(\t\"H\n\x03Utm\x12\x0e\n\x06source\x18\x01 \x01(\t\x12\x0e\n\x06medium\x18\x02 \x01(\t\x12\x10\n\x08\x63\x61mpaign\x18\x03 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\"-\n\tUserAgent\x12\x0f\n\x07\x62rowser\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"\x1b\n\x08Response\x12\x0f\n\x07message\x18\x01 \x01(\t2E\n\x10MetricsCollector\x12\x31\n\nTrackVisit\x12\x0e.metrics.Visit\x1a\x11.metrics.Response\"\x00\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_VISIT = _descriptor.Descriptor(
  name='Visit',
  full_name='metrics.Visit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='metrics.Visit.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uri', full_name='metrics.Visit.uri', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ip', full_name='metrics.Visit.ip', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='utm', full_name='metrics.Visit.utm', index=3,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='useragent', full_name='metrics.Visit.useragent', index=4,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='visitor_id', full_name='metrics.Visit.visitor_id', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=35,
  serialized_end=165,
)


_UTM = _descriptor.Descriptor(
  name='Utm',
  full_name='metrics.Utm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='source', full_name='metrics.Utm.source', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='medium', full_name='metrics.Utm.medium', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='campaign', full_name='metrics.Utm.campaign', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='metrics.Utm.content', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=167,
  serialized_end=239,
)


_USERAGENT = _descriptor.Descriptor(
  name='UserAgent',
  full_name='metrics.UserAgent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='browser', full_name='metrics.UserAgent.browser', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='metrics.UserAgent.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=241,
  serialized_end=286,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='metrics.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='metrics.Response.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=288,
  serialized_end=315,
)

_VISIT.fields_by_name['utm'].message_type = _UTM
_VISIT.fields_by_name['useragent'].message_type = _USERAGENT
DESCRIPTOR.message_types_by_name['Visit'] = _VISIT
DESCRIPTOR.message_types_by_name['Utm'] = _UTM
DESCRIPTOR.message_types_by_name['UserAgent'] = _USERAGENT
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE

Visit = _reflection.GeneratedProtocolMessageType('Visit', (_message.Message,), dict(
  DESCRIPTOR = _VISIT,
  __module__ = 'proto.collector_pb2'
  # @@protoc_insertion_point(class_scope:metrics.Visit)
  ))
_sym_db.RegisterMessage(Visit)

Utm = _reflection.GeneratedProtocolMessageType('Utm', (_message.Message,), dict(
  DESCRIPTOR = _UTM,
  __module__ = 'proto.collector_pb2'
  # @@protoc_insertion_point(class_scope:metrics.Utm)
  ))
_sym_db.RegisterMessage(Utm)

UserAgent = _reflection.GeneratedProtocolMessageType('UserAgent', (_message.Message,), dict(
  DESCRIPTOR = _USERAGENT,
  __module__ = 'proto.collector_pb2'
  # @@protoc_insertion_point(class_scope:metrics.UserAgent)
  ))
_sym_db.RegisterMessage(UserAgent)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), dict(
  DESCRIPTOR = _RESPONSE,
  __module__ = 'proto.collector_pb2'
  # @@protoc_insertion_point(class_scope:metrics.Response)
  ))
_sym_db.RegisterMessage(Response)


# @@protoc_insertion_point(module_scope)