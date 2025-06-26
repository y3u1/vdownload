
import transmissionrpc
import utils
import random


class TC:
    def __init__(self, host='127.0.0.1', port=9090, username="admin", password="qpalzm1234"):
        self.client = transmissionrpc.Client(host, port)

    def add_torrents(self,url,download_dir="./"):
        n = self.get_torrents_file(url)
        if n is None:
            return None
        try:
            task = self.client.add_torrent(torrent=n)
            task.set_location(download_dir)
        except Exception as e:
            print(f"Error adding torrent: {e}")
            return None
        finally:
            import os
            if os.path.exists(n):
                os.remove(n)
        return task
    def get_torrents_file(self,u):
        r = utils.vreq(url=u)
        if r is None:
            return None
        name = str(random.randrange(1231,12312124) + ".torrents")
        with open("temp.torrent", name) as f:
            f.write(r)
        return name