import requests, json
import resin

class Connection(object):

	"""
	This is a python library for accessing the resin api
	http://github.com/craig-mulligan/resin-api-python
	Usage:
	    import resin_io
	    c = resin_io.Connection('{{JWT}}')
	"""

	def __init__(self, JWT=None):
	    self.base_url = 'https://api.resin.io/ewa'
	    self.headers = {'Content-type': 'application/json',
               'Authorization': 'Bearer ' + str(JWT)}

	def device_getAll(self, app_id=None):
		""" Gets all devices resources
		@parameter appname: appname of requested devices, if None, will return all devices from all apps.
		returns a dict of devices
		"""
		if app_id:
		    params = "/device?$filter=application%20eq%20'" + str(app_id) + "'"

		else:
		    params = "/device"

		url = self.base_url + str(params)
		r = requests.get(url, headers=self.headers)
		return r.json()['d']

	def get_device(self, uuid=None):
		""" Gets device resource
		@parameter uuid: uuid of requested device.
		returns device object
		"""
		return resin.Device(self, uuid=uuid)
		
from resin.device import *  # noqa
