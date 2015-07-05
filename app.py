from pager import log_incident
import resin
from config import RESIN_JWT, PD_SERVICE_KEY, RESIN_APP
import time

# Connect to resin API
connection = resin.Connection(JWT=RESIN_JWT)


def devices_update():
	'''grabs list of resin devices and checks if they are online
	if they aren't it will create an incident on pagerduty'''

	# Get all devices associated with app
	devices = connection.device_getAll(app_id=RESIN_APP)
	for d in devices:
		print d['name'] + " : " + d['is_online']
		if d['is_online'] == False:
			# device is not online log incident on PD
			log_incident(d, app=RESIN_APP, service_key=PD_SERVICE_KEY)

devices_update()
