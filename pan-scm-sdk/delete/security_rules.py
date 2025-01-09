from scm.client import Scm
from scm.config.security import SecurityRule


FOLDER = 'All'
RULEBASE = 'pre'

CLIENT_ID = 'ServiceAccountClientIDGoesHere'
CLIENT_SECRET = 'ServiceAccountClientSecretGoesHere'
TSG_ID = 'TenantIDGoesHere'

api_client = Scm(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    tsg_id=TSG_ID,
)

security_rule_instance = SecurityRule(api_client)

security_rules = security_rule_instance.list(folder=FOLDER, rulebase=RULEBASE, exact_match=True)
print(f'Number of security rules before delete actions - {len(security_rules)}')

for security_rule in security_rules:
    if 'Domestic' in security_rule.tag or 'Reykjavik' in security_rule.source:
        security_rule_instance.delete(str(security_rule.id))
        print(f'Removed security rule {security_rule.name}')

security_rules = security_rule_instance.list(folder=FOLDER, rulebase=RULEBASE, exact_match=True)
print(f'Number of security rules after delete actions - {len(security_rules)}')
