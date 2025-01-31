# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: transmission_call.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='transmission_call.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17transmission_call.proto\"\x1f\n\tTorrentId\x12\x12\n\ntorrent_id\x18\x01 \x01(\x05\"!\n\nTorrentUrl\x12\x13\n\x0btorrent_url\x18\x01 \x01(\t\"3\n\x07Torrent\x12\x14\n\x0ctorrent_name\x18\x01 \x01(\t\x12\x12\n\ntorrent_id\x18\x02 \x01(\x05\"m\n\ngetTorrent\x12\x19\n\x07torrent\x18\x01 \x01(\x0b\x32\x08.Torrent\x12\x12\n\ndate_added\x18\x02 \x01(\t\x12\x18\n\x10torrent_progress\x18\x03 \x01(\x02\x12\x16\n\x0etorrent_status\x18\x04 \x01(\t\"(\n\x0bsendTorrent\x12\x19\n\x07torrent\x18\x01 \x01(\x0b\x32\x08.Torrent\"*\n\rremoveTorrent\x12\x19\n\x07torrent\x18\x01 \x01(\x0b\x32\x08.Torrent2\xfb\x01\n\x10TransmissionCall\x12\'\n\nGetTorrent\x12\n.TorrentId\x1a\x0b.getTorrent\"\x00\x12*\n\x0bSendTorrent\x12\x0b.TorrentUrl\x1a\x0c.sendTorrent\"\x00\x12-\n\rRemoveTorrent\x12\n.TorrentId\x1a\x0e.removeTorrent\"\x00\x12/\n\x0eGetTorrentList\x12\n.TorrentId\x1a\x0b.getTorrent\"\x00(\x01\x30\x01\x12\x32\n\x0fSendTorrentList\x12\x0b.TorrentUrl\x1a\x0c.sendTorrent\"\x00(\x01\x30\x01\x62\x06proto3')
)




_TORRENTID = _descriptor.Descriptor(
  name='TorrentId',
  full_name='TorrentId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='torrent_id', full_name='TorrentId.torrent_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=27,
  serialized_end=58,
)


_TORRENTURL = _descriptor.Descriptor(
  name='TorrentUrl',
  full_name='TorrentUrl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='torrent_url', full_name='TorrentUrl.torrent_url', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=60,
  serialized_end=93,
)


_TORRENT = _descriptor.Descriptor(
  name='Torrent',
  full_name='Torrent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='torrent_name', full_name='Torrent.torrent_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='torrent_id', full_name='Torrent.torrent_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=95,
  serialized_end=146,
)


_GETTORRENT = _descriptor.Descriptor(
  name='getTorrent',
  full_name='getTorrent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='torrent', full_name='getTorrent.torrent', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_added', full_name='getTorrent.date_added', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='torrent_progress', full_name='getTorrent.torrent_progress', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='torrent_status', full_name='getTorrent.torrent_status', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=148,
  serialized_end=257,
)


_SENDTORRENT = _descriptor.Descriptor(
  name='sendTorrent',
  full_name='sendTorrent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='torrent', full_name='sendTorrent.torrent', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=259,
  serialized_end=299,
)


_REMOVETORRENT = _descriptor.Descriptor(
  name='removeTorrent',
  full_name='removeTorrent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='torrent', full_name='removeTorrent.torrent', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=301,
  serialized_end=343,
)

_GETTORRENT.fields_by_name['torrent'].message_type = _TORRENT
_SENDTORRENT.fields_by_name['torrent'].message_type = _TORRENT
_REMOVETORRENT.fields_by_name['torrent'].message_type = _TORRENT
DESCRIPTOR.message_types_by_name['TorrentId'] = _TORRENTID
DESCRIPTOR.message_types_by_name['TorrentUrl'] = _TORRENTURL
DESCRIPTOR.message_types_by_name['Torrent'] = _TORRENT
DESCRIPTOR.message_types_by_name['getTorrent'] = _GETTORRENT
DESCRIPTOR.message_types_by_name['sendTorrent'] = _SENDTORRENT
DESCRIPTOR.message_types_by_name['removeTorrent'] = _REMOVETORRENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TorrentId = _reflection.GeneratedProtocolMessageType('TorrentId', (_message.Message,), {
  'DESCRIPTOR' : _TORRENTID,
  '__module__' : 'transmission_call_pb2'
  # @@protoc_insertion_point(class_scope:TorrentId)
  })
_sym_db.RegisterMessage(TorrentId)

TorrentUrl = _reflection.GeneratedProtocolMessageType('TorrentUrl', (_message.Message,), {
  'DESCRIPTOR' : _TORRENTURL,
  '__module__' : 'transmission_call_pb2'
  # @@protoc_insertion_point(class_scope:TorrentUrl)
  })
_sym_db.RegisterMessage(TorrentUrl)

Torrent = _reflection.GeneratedProtocolMessageType('Torrent', (_message.Message,), {
  'DESCRIPTOR' : _TORRENT,
  '__module__' : 'transmission_call_pb2'
  # @@protoc_insertion_point(class_scope:Torrent)
  })
_sym_db.RegisterMessage(Torrent)

getTorrent = _reflection.GeneratedProtocolMessageType('getTorrent', (_message.Message,), {
  'DESCRIPTOR' : _GETTORRENT,
  '__module__' : 'transmission_call_pb2'
  # @@protoc_insertion_point(class_scope:getTorrent)
  })
_sym_db.RegisterMessage(getTorrent)

sendTorrent = _reflection.GeneratedProtocolMessageType('sendTorrent', (_message.Message,), {
  'DESCRIPTOR' : _SENDTORRENT,
  '__module__' : 'transmission_call_pb2'
  # @@protoc_insertion_point(class_scope:sendTorrent)
  })
_sym_db.RegisterMessage(sendTorrent)

removeTorrent = _reflection.GeneratedProtocolMessageType('removeTorrent', (_message.Message,), {
  'DESCRIPTOR' : _REMOVETORRENT,
  '__module__' : 'transmission_call_pb2'
  # @@protoc_insertion_point(class_scope:removeTorrent)
  })
_sym_db.RegisterMessage(removeTorrent)



_TRANSMISSIONCALL = _descriptor.ServiceDescriptor(
  name='TransmissionCall',
  full_name='TransmissionCall',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=346,
  serialized_end=597,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTorrent',
    full_name='TransmissionCall.GetTorrent',
    index=0,
    containing_service=None,
    input_type=_TORRENTID,
    output_type=_GETTORRENT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendTorrent',
    full_name='TransmissionCall.SendTorrent',
    index=1,
    containing_service=None,
    input_type=_TORRENTURL,
    output_type=_SENDTORRENT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveTorrent',
    full_name='TransmissionCall.RemoveTorrent',
    index=2,
    containing_service=None,
    input_type=_TORRENTID,
    output_type=_REMOVETORRENT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTorrentList',
    full_name='TransmissionCall.GetTorrentList',
    index=3,
    containing_service=None,
    input_type=_TORRENTID,
    output_type=_GETTORRENT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendTorrentList',
    full_name='TransmissionCall.SendTorrentList',
    index=4,
    containing_service=None,
    input_type=_TORRENTURL,
    output_type=_SENDTORRENT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TRANSMISSIONCALL)

DESCRIPTOR.services_by_name['TransmissionCall'] = _TRANSMISSIONCALL

# @@protoc_insertion_point(module_scope)
