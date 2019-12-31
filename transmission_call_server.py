import time
from concurrent import futures

import grpc
import tranmission_server
import transmission_call_pb2 as pb2
import transmission_call_pb2_grpc as pb2_grpc

transmission_host = "192.168.1.16"
transmission_port = 9091
_port = 5051

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
        _torrent_url = request.url
        _torrent = self.client.add_torrent(_torrent_url)

        torrent = pb2.Torrent(
            torrent_name=_torrent._fields['name'].value,
            torrent_id=_torrent._fields['id'].value
        )

        return pb2.sendTorrent(
            torrent=torrent
        )


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_TransmissionCallServicer_to_server(
        TransmissionCallServicer(), server
    )
    server.add_insecure_port('[::]:%d' % _port)
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    server()
