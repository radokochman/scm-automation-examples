from scm.client import Scm
from scm.config.objects import Tag


CLIENT_ID = 'ServiceAccountClientIDGoesHere'
CLIENT_SECRET = 'ServiceAccountClientSecretGoesHere'
TSG_ID = 'TenantIDGoesHere'

api_client = Scm(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    tsg_id=TSG_ID,
)

tag_instance = Tag(api_client)

tags = tag_instance.list(folder='All', exact_match=True)

for tag in tags:
    print(f'Tag name: {tag.name}, color: {tag.color.value if tag.color else None}, UUID: {tag.id}')
