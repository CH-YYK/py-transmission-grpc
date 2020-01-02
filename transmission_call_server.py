import argparse
from concurrent import futures

import grpc
import tranmission_server
import transmission_call_pb2 as pb2
import transmission_call_pb2_grpc as pb2_grpc

transmission_host = "192.168.1.16"
transmission_port = 9091
_port = 5051

def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host")
    parser.add_argument("--port")
    parser.add_argument("--rpc_port")
    return parser.parse_args()

class TransmissionCallServicer(pb2_grpc.TransmissionCallServicer):
    """
    Provides methods that implement functionality of transmission call server
    """

    def __init__(self):
        self.client = tranmission_server.create_client(transmission_host, transmission_port)

    def GetTorrent(self, request, context):
        _torrent_id = request.torrent_id
        _torrent = self.client.get_torrent(_torrent_id)

        torrent = pb2.Torrent(
            torrent_name=_torrent._fields['name'].value,
            torrent_id=_torrent_id
        )

        return pb2.getTorrent(
            torrent=torrent,
            date_added=_torrent.date_added.strftime("%Y-%m-%d, %H:%M:%S"),
            torrent_progress=_torrent.progress,
            torrent_status=_torrent.status
        )

    def SendTorrent(self, request, context):
        _torrent_url = request.torrent_url
        _torrent = self.client.add_torrent(_torrent_url)

        torrent = pb2.Torrent(
            torrent_name=_torrent._fields['name'].value,
            torrent_id=_torrent._fields['id'].value
        )

        return pb2.sendTorrent(
            torrent=torrent
        )


def server():
    print("---- starting server at %s:%d ----" % ('localhost', _port))
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_TransmissionCallServicer_to_server(
        TransmissionCallServicer(), server
    )
    server.add_insecure_port('[::]:%d' % _port)
    server.start()
    print("---- server started ----")
    server.wait_for_termination()

if __name__ == '__main__':
    cmd_lines = make_parser()

    _port = cmd_lines.port if cmd_lines.rpc_port else _port
    transmission_host = cmd_lines.host if cmd_lines.host else transmission_host
    transmission_port = cmd_lines.port if cmd_lines.port else transmission_port

    server()
