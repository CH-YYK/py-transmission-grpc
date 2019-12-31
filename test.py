import transmissionrpc
import pytest

tc = transmissionrpc.Client("192.168.1.16", port=9091)
tc.get_torrents()


def test_add_torrent():
    torrent = tc.add_torrent("http://releases.ubuntu.com/18.04/ubuntu-18.04.3-desktop-amd64.iso.torrent?_ga=2.255141960.1388709509.1577756555-1012110682.1574224568")

def test_get_torrents():
    assert tc.get_torrents() == []

def test_get_files():
    assert tc.get_files() == []

