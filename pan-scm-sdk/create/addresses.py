from scm.client import Scm
from scm.config.objects import Address


FOLDER = 'All'

CLIENT_ID = 'ServiceAccountClientIDGoesHere'
CLIENT_SECRET = 'ServiceAccountClientSecretGoesHere'
TSG_ID = 'TenantIDGoesHere'

api_client = Scm(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    tsg_id=TSG_ID,
)

address_instance = Address(api_client)

addresses_data = [
    {
        'name': 'Reykjavik',
        'description': 'Reykjavik IP address',
        'ip_netmask': '10.0.0.1/24',
        'folder': FOLDER,
    },
    {
        'name': 'Keflavik',
        'description': 'Keflavik IP address',
        'ip_netmask': '10.0.1.1/24',
        'folder': FOLDER,
    },
    {
        'name': 'Akureyri',
        'description': 'Akureyri IP address',
        'ip_netmask': '10.0.2.1/24',
        'folder': FOLDER,
    },
    {
        'name': 'Oslo',
        'description': 'Oslo IP address',
        'ip_netmask': '10.1.0.1/24',
        'folder': FOLDER,
    },
    {
        'name': 'Bergen',
        'description': 'Bergen IP address',
        'ip_netmask': '10.1.1.1/24',
        'folder': FOLDER,
    },
    {
        'name': 'Tromso',
        'description': 'Tromso IP address',
        'ip_netmask': '10.1.2.1/24',
        'folder': FOLDER,
    },
]

for address_data in addresses_data:
    response = address_instance.create(address_data)
    print(f'Created address {response.name}, UUID {response.id}')
