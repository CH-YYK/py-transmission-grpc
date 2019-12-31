import transmissionrpc

HOST = "192.168.1.16"
PORT = 9091

def create_client(host, port):
    return transmissionrpc.Client(host, port)

def get_torrent_id(
        client: transmissionrpc.client.Client,
        torrent_id: int
):
    torrent = client.get_torrent(torrent_id)

