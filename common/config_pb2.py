# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='config.proto',
  package='InSECTS',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x63onfig.proto\x12\x07InSECTS\"\x81\x03\n\x0c\x43onfigParams\x12\x0f\n\x07version\x18\x01 \x01(\t\x12\x17\n\x0fvirtual_machine\x18\x02 \x01(\x08\x12\x13\n\x0b\x65mulate_sdr\x18\x03 \x01(\x08\x12\x17\n\x0f\x65mulate_arduino\x18\x04 \x01(\x08\x12\x17\n\x0f\x65mulate_thermal\x18\x05 \x01(\x08\x12\x16\n\x0etelemetry_freq\x18\x06 \x01(\x01\x12\x1c\n\x14\x63ommand_multicast_ip\x18\x07 \x01(\t\x12\x1e\n\x16\x63ommand_multicast_port\x18\x08 \x01(\x05\x12\x1e\n\x16telemetry_multicast_ip\x18\t \x01(\t\x12 \n\x18telemetry_multicast_port\x18\n \x01(\x05\x12\x19\n\x11sdr_tcp_client_ip\x18\x0b \x01(\t\x12\x1b\n\x13sdr_tcp_client_port\x18\x0c \x01(\x05\x12\x17\n\x0f\x61rduino_address\x18\r \x01(\t\x12\x17\n\x0fserial_baudrate\x18\x0e \x01(\x05'
)




_CONFIGPARAMS = _descriptor.Descriptor(
  name='ConfigParams',
  full_name='InSECTS.ConfigParams',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='version', full_name='InSECTS.ConfigParams.version', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='virtual_machine', full_name='InSECTS.ConfigParams.virtual_machine', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='emulate_sdr', full_name='InSECTS.ConfigParams.emulate_sdr', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='emulate_arduino', full_name='InSECTS.ConfigParams.emulate_arduino', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='emulate_thermal', full_name='InSECTS.ConfigParams.emulate_thermal', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='telemetry_freq', full_name='InSECTS.ConfigParams.telemetry_freq', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='command_multicast_ip', full_name='InSECTS.ConfigParams.command_multicast_ip', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='command_multicast_port', full_name='InSECTS.ConfigParams.command_multicast_port', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='telemetry_multicast_ip', full_name='InSECTS.ConfigParams.telemetry_multicast_ip', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='telemetry_multicast_port', full_name='InSECTS.ConfigParams.telemetry_multicast_port', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sdr_tcp_client_ip', full_name='InSECTS.ConfigParams.sdr_tcp_client_ip', index=10,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sdr_tcp_client_port', full_name='InSECTS.ConfigParams.sdr_tcp_client_port', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='arduino_address', full_name='InSECTS.ConfigParams.arduino_address', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='serial_baudrate', full_name='InSECTS.ConfigParams.serial_baudrate', index=13,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=411,
)

DESCRIPTOR.message_types_by_name['ConfigParams'] = _CONFIGPARAMS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConfigParams = _reflection.GeneratedProtocolMessageType('ConfigParams', (_message.Message,), {
  'DESCRIPTOR' : _CONFIGPARAMS,
  '__module__' : 'config_pb2'
  # @@protoc_insertion_point(class_scope:InSECTS.ConfigParams)
  })
_sym_db.RegisterMessage(ConfigParams)


# @@protoc_insertion_point(module_scope)
