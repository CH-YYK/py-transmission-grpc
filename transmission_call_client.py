import argparse
import grpc

import transmission_call_pb2 as pb2
import transmission_call_pb2_grpc as pb2_grpc

_host = "192.168.1.6"
_port = 5051
_torrent_url = ""


def make_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--host",
                        help="The host of grpc server")

    parser.add_argument("-p", "--port",
                        help="The port listened by the server",
                        type=int)

    parser.add_argument("-t", "--torrent_url")

    parser.add_argument("-i", "--id")

    return parser

def make_TorrentID(torrent_id:int):
    """make TorrentID object"""
    return pb2.TorrentId(torrent_id=torrent_id)


def make_TorrentUrl(torrent_url: str):
    """make TorrentUrl object"""
    return pb2.TorrentUrl(torrent_url=torrent_url)


def transmission_get_torrent(stub, torrent_id):
    """GetTorrent method"""
    response = stub.GetTorrent(
        make_TorrentID(torrent_id)
    )
    print(response)


def transmission_send_torrent(stub: pb2_grpc.TransmissionCallStub, torrent_url: str):
    """SendTorrent method"""
    response = stub.SendTorrent(
        make_TorrentUrl(torrent_url)
    )
    print(response)


def run():
    """run the stub"""
    with grpc.insecure_channel('%s:%d' % (_host, _port)) as channel:
        print("---- start communicating with %s at %d ---- " % (_host, _port))
        stub = pb2_grpc.TransmissionCallStub(channel)

        print("---- get torrent ----")
        transmission_get_torrent(stub, 3)

        print("---- send torrent ----")
        transmission_send_torrent(stub, _torrent_url)

if __name__ == '__main__':
    cmdlines = make_parser().parse_args()

    if cmdlines.host:
        _host = cmdlines.host
    if cmdlines.port:
        _port = cmdlines.port
    if cmdlines.torrent_url:
        _torrent_url = cmdlines.torrent_url

    run()