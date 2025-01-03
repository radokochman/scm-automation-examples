from scm.client import Scm
from scm.config.security import URLCategories
from scm.models.security.url_categories import URLCategoriesListTypeEnum


FOLDER = 'All'

CLIENT_ID = 'ServiceAccountClientIDGoesHere'
CLIENT_SECRET = 'ServiceAccountClientSecretGoesHere'
TSG_ID = 'TenantIDGoesHere'

api_client = Scm(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    tsg_id=TSG_ID,
)

url_category_instance = URLCategories(api_client)

url_categories_data = [
    {
        'name': 'Icelandic_websites',
        'description': 'Websites with Icelandic domains',
        'type': URLCategoriesListTypeEnum.url_list,
        'list': ['*.is'],
        'folder': FOLDER,
    },
    {
        'name': 'Norwegian_websites',
        'description': 'Websites with Norwegian domains',
        'type': URLCategoriesListTypeEnum.url_list,
        'list': ['*.no'],
        'folder': FOLDER,
    },
]

for url_category_data in url_categories_data:
    response = url_category_instance.create(url_category_data)
    print(f'Created URL category {response.name}, UUID {response.id}')
