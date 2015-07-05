import resin
import requests
import time
import json


def log_incident(device, app=None, service_key=None):
    url = 'https://events.pagerduty.com/generic/2010-04-15/create_event.json'
    headers = {'Content-type': 'application/json'}
    data = {
        'service_key': service_key,
        'event_type': 'trigger',
        'description': 'DEVICE OFFLINE',
        'incident_key': device['id'],
        'details': {
            'is_online': device['is_online'],
            'last_seen_time': device['last_seen_time']
        },
        'client': device['name'],
        'client_url': 'https://dashboard.resin.io/dashboard/apps/' + str(app) + '/devices/' + str(device['id'] +'?tab=logs')
    }
    payload = json.dumps(data)
    r = requests.post(url, headers=headers, data=payload)

    print r.json()
