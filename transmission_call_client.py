import grpc

import transmission_call_pb2 as pb2
import transmission_call_pb2_grpc as pb2_grpc


def make_TorrentID(torrent_id):
    return pb2.TorrentId(torrent_id=torrent_id)


def make_TorrentUrl(torrent_url):
    return pb2.TorrentUrl(torrent_url=torrent_url)


def transmission_get_torrent(stub, torrent_id):
    response = stub.GetTorrent(
        make_TorrentID(torrent_id)
    )
    print(response)


def transmission_send_torrent(stub, torrent_url):
    response = stub.SendTorrent(
        make_TorrentUrl(torrent_url)
    )
    print(response)


def run():
    with grpc.insecure_channel('localhost:5051') as channel:
        stub = pb2_grpc.TransmissionCallStub(channel)

        print("---- get torrent ----")
        transmission_get_torrent(stub, 1)

        print("---- send torrent ----")

if __name__ == '__main__':
    run()