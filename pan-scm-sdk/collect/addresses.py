from scm.client import Scm
from scm.config.objects import Address


CLIENT_ID = 'ServiceAccountClientIDGoesHere'
CLIENT_SECRET = 'ServiceAccountClientSecretGoesHere'
TSG_ID = 'TenantIDGoesHere'

api_client = Scm(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    tsg_id=TSG_ID,
)

address_instance = Address(api_client)

addresses = address_instance.list(folder='All', exact_match=True)

for address in addresses:
    address_value = address.ip_netmask or address.ip_range or address.ip_wildcard
    print(f'Address name: {address.name}, address value: {address_value}, UUID: {address.id}')
