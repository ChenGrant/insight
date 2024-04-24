# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from source_code_parser.protobuf import source_code_parser_pb2 as source__code__parser_dot_protobuf_dot_source__code__parser__pb2


class SourceCodeParserStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SyntaxParse = channel.stream_stream(
                '/SourceCodeParser/SyntaxParse',
                request_serializer=source__code__parser_dot_protobuf_dot_source__code__parser__pb2.SyntaxParseRequest.SerializeToString,
                response_deserializer=source__code__parser_dot_protobuf_dot_source__code__parser__pb2.SyntaxParseResponse.FromString,
                )


class SourceCodeParserServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SyntaxParse(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_SourceCodeParserServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SyntaxParse': grpc.stream_stream_rpc_method_handler(
                    servicer.SyntaxParse,
                    request_deserializer=source__code__parser_dot_protobuf_dot_source__code__parser__pb2.SyntaxParseRequest.FromString,
                    response_serializer=source__code__parser_dot_protobuf_dot_source__code__parser__pb2.SyntaxParseResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'SourceCodeParser', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class SourceCodeParser(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SyntaxParse(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/SourceCodeParser/SyntaxParse',
            source__code__parser_dot_protobuf_dot_source__code__parser__pb2.SyntaxParseRequest.SerializeToString,
            source__code__parser_dot_protobuf_dot_source__code__parser__pb2.SyntaxParseResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
