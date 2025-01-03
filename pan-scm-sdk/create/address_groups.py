from scm.client import Scm
from scm.config.objects import AddressGroup


FOLDER = 'All'

CLIENT_ID = 'ServiceAccountClientIDGoesHere'
CLIENT_SECRET = 'ServiceAccountClientSecretGoesHere'
TSG_ID = 'TenantIDGoesHere'

api_client = Scm(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    tsg_id=TSG_ID,
)

address_group_instance = AddressGroup(api_client)

address_groups_data = [
    {
        'name': 'Icelandic_addresses',
        'description': 'Addresses from Iceland',
        'static': ['Reykjavik', 'Keflavik', 'Akureyri'],
        'folder': FOLDER,
    },
    {
        'name': 'Norwegian_addresses',
        'description': 'Addresses from Norway',
        'static': ['Oslo', 'Bergen', 'Tromso'],
        'folder': FOLDER,
    },
]

for address_group_data in address_groups_data:
    response = address_group_instance.create(address_group_data)
    print(f'Created address group {response.name}, UUID {response.id}')
