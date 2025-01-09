from scm.client import Scm
from scm.config.objects import AddressGroup


CLIENT_ID = 'ServiceAccountClientIDGoesHere'
CLIENT_SECRET = 'ServiceAccountClientSecretGoesHere'
TSG_ID = 'TenantIDGoesHere'

api_client = Scm(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    tsg_id=TSG_ID,
)

address_group_instance = AddressGroup(api_client)

address_groups = address_group_instance.list(folder='All', exact_match=True)

for address_group in address_groups:
    print(
        f'Address name: {address_group.name}, static values: {address_group.static}, UUID: {address_group.id}',
    )
