from scm.client import Scm
from scm.config.objects import Tag


FOLDER = 'All'

CLIENT_ID = 'ServiceAccountClientIDGoesHere'
CLIENT_SECRET = 'ServiceAccountClientSecretGoesHere'
TSG_ID = 'TenantIDGoesHere'

api_client = Scm(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    tsg_id=TSG_ID,
)

tag_instance = Tag(api_client)

tags_data = [
    {
        'name': 'Domestic',
        'color': 'Blue',
        'comments': 'Tag for domestic traffic',
        'folder': FOLDER,
    },
    {
        'name': 'International',
        'color': 'Red',
        'comments': 'Tag for international traffic',
        'folder': FOLDER,
    },
]

for tag_data in tags_data:
    response = tag_instance.create(tag_data)
    print(f'Created tag {response.name}, UUID {response.id}')
