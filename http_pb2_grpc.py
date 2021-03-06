# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import http_pb2 as http__pb2


class DuoStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetFriends = channel.unary_unary(
                '/http.Duo/GetFriends',
                request_serializer=http__pb2.User.SerializeToString,
                response_deserializer=http__pb2.Friends.FromString,
                )


class DuoServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetFriends(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DuoServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetFriends': grpc.unary_unary_rpc_method_handler(
                    servicer.GetFriends,
                    request_deserializer=http__pb2.User.FromString,
                    response_serializer=http__pb2.Friends.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'http.Duo', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Duo(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetFriends(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/http.Duo/GetFriends',
            http__pb2.User.SerializeToString,
            http__pb2.Friends.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
