from scm.client import Scm
from scm.config.security import SecurityRule
from scm.models.security.security_rules import SecurityRuleAction, SecurityRuleProfileSetting


FOLDER = 'All'

CLIENT_ID = 'ServiceAccountClientIDGoesHere'
CLIENT_SECRET = 'ServiceAccountClientSecretGoesHere'
TSG_ID = 'TenantIDGoesHere'

api_client = Scm(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    tsg_id=TSG_ID,
)

security_rule_instance = SecurityRule(api_client)

security_rules_data = [
    {
        'name': 'Allow-Icelandic-websites',
        'disabled': False,
        'tag': 'International',
        'from_': 'Norway',
        'source': ['Norwegian_addresses'],
        'source_user': ['any'],
        'to_': 'Iceland',
        'destination': ['Icelandic_addresses'],
        'application': ['any'],
        'service': ['service-http', 'service-https'],
        'category': ['Icelandic_websites'],
        'action': SecurityRuleAction.allow,
        'profile_setting': SecurityRuleProfileSetting(group=['best-practice']),
        'description': 'Allow websites with Icelandic domain',
        'rulebase': 'pre',
        'folder': FOLDER,
    },
    {
        'name': 'Allow-Norwegian-websites',
        'disabled': False,
        'tag': 'International',
        'from_': 'Iceland',
        'source': ['Icelandic_addresses'],
        'source_user': ['any'],
        'to_': 'Norway',
        'destination': ['Norwegian_addresses'],
        'application': ['any'],
        'service': ['service-http', 'service-https'],
        'category': ['Norwegian_websites'],
        'action': SecurityRuleAction.allow,
        'profile_setting': SecurityRuleProfileSetting(group=['best-practice']),
        'description': 'Allow websites with Norwegian domain',
        'rulebase': 'pre',
        'folder': FOLDER,
    },
    {
        'name': 'Deny-Keflavik-to-Akureyri',
        'disabled': False,
        'tag': 'Domestic',
        'from_': 'Iceland',
        'source': ['Keflavik'],
        'source_user': ['any'],
        'to_': 'Iceland',
        'destination': ['Akureyri'],
        'application': ['any'],
        'service': ['any'],
        'category': ['any'],
        'action': SecurityRuleAction.deny,
        'description': 'Deny all traffic from Keflavik to Akureyri',
        'rulebase': 'pre',
        'folder': FOLDER,
    },
    {
        'name': 'Deny-ssl-from-Bergen-to-Tromso',
        'disabled': False,
        'tag': 'Domestic',
        'from_': 'Norway',
        'source': ['Bergen'],
        'source_user': ['any'],
        'to_': 'Norway',
        'destination': ['Tromso'],
        'application': ['ssl'],
        'service': ['any'],
        'category': ['any'],
        'action': SecurityRuleAction.deny,
        'description': 'Deny ssl traffic from Bergen to Tromso',
        'rulebase': 'pre',
        'folder': FOLDER,
    },
    {
        'name': 'Allow-Oslo-to-Reykjavik',
        'disabled': False,
        'tag': 'International',
        'from_': 'Norway',
        'source': ['Oslo'],
        'source_user': ['any'],
        'to_': 'Iceland',
        'destination': ['Reykjavik'],
        'application': ['any'],
        'service': ['any'],
        'category': ['any'],
        'action': SecurityRuleAction.allow,
        'profile_setting': SecurityRuleProfileSetting(group=['best-practice']),
        'description': 'Allow traffic from Oslo to Reykjavik',
        'rulebase': 'pre',
        'folder': FOLDER,
    },
    {
        'name': 'Allow-Reykjavik-to-Oslo',
        'disabled': False,
        'tag': 'International',
        'from_': 'Iceland',
        'source': ['Reykjavik'],
        'source_user': ['any'],
        'to_': 'Norway',
        'destination': ['Oslo'],
        'application': ['any'],
        'service': ['any'],
        'category': ['any'],
        'action': SecurityRuleAction.allow,
        'profile_setting': SecurityRuleProfileSetting(group=['best-practice']),
        'description': 'Allow traffic from Reykjavik to Oslo',
        'rulebase': 'pre',
        'folder': FOLDER,
    },
]

for security_rule_data in security_rules_data:
    response = security_rule_instance.create(security_rule_data)
    print(f'Created security rule {response.name}, UUID {response.id}')
