# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/service.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14protos/service.proto\x12\x0e\x64ream_analysis\")\n\x0c\x44reamRequest\x12\x19\n\x11\x64ream_description\x18\x01 \x01(\t\")\n\x15\x44reamAnalysisResponse\x12\x10\n\x08\x61nalysis\x18\x01 \x01(\t2m\n\x14\x44reamAnalysisService\x12U\n\x0c\x41nalyzeDream\x12\x1c.dream_analysis.DreamRequest\x1a%.dream_analysis.DreamAnalysisResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_DREAMREQUEST']._serialized_start=40
  _globals['_DREAMREQUEST']._serialized_end=81
  _globals['_DREAMANALYSISRESPONSE']._serialized_start=83
  _globals['_DREAMANALYSISRESPONSE']._serialized_end=124
  _globals['_DREAMANALYSISSERVICE']._serialized_start=126
  _globals['_DREAMANALYSISSERVICE']._serialized_end=235
# @@protoc_insertion_point(module_scope)
