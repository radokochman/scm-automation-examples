from scm.client import Scm
from scm.config.security import URLCategories


CLIENT_ID = 'ServiceAccountClientIDGoesHere'
CLIENT_SECRET = 'ServiceAccountClientSecretGoesHere'
TSG_ID = 'TenantIDGoesHere'

api_client = Scm(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    tsg_id=TSG_ID,
)

url_category_instance = URLCategories(api_client)

url_categories = url_category_instance.list(folder='All', exact_match=True)

for url_category in url_categories:
    print(f'URL category name: {url_category.name}, URL list: {url_category.list} , UUID: {url_category.id}')
