import requests
import json
import resin


class Device(object):

    """Device Object"""

    def __init__(self, Connection, uuid=None):
        """ Gets device resource
        @parameter uuid: uuid of requested device.
        returns a dict of device
        """
        params = "/device?$filter=uuid%20eq%20'" + str(uuid) + "'"
        url = Connection.base_url + str(params)
        r = requests.get(url, headers=Connection.headers)
        d = r.json()['d'][0]

        self.uuid = uuid
