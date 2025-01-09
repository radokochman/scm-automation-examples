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

print(f'All security rules from the "{RULEBASE}" rulebase:')
security_rules = security_rule_instance.list(folder=FOLDER, rulebase=RULEBASE, exact_match=True)
print(f'Number of security rules - {len(security_rules)}')
for security_rule in security_rules:
    print(f'Name - {security_rule.name}')


print('\n\nFiltered security rules with tag "International":')
filters = {
    'tag': ['International'],
}
security_rules = security_rule_instance.list(folder=FOLDER, rulebase=RULEBASE, exact_match=True, **filters)
print(f'Number of security rules - {len(security_rules)}')
for security_rule in security_rules:
    print(f'Name - {security_rule.name}')


print('\n\nFiltered security rules with tag "International" and source "Oslo":')
filters = {
    'tag': ['International'],
    'source': ['Oslo'],
}
security_rules = security_rule_instance.list(folder=FOLDER, rulebase=RULEBASE, exact_match=True, **filters)
print(f'Number of security rules - {len(security_rules)}')
for security_rule in security_rules:
    print(f'Name - {security_rule.name}')


print('\n\nFiltered security rules with service set to "service-http":')
security_rules = security_rule_instance.list(
    folder=FOLDER,
    rulebase=RULEBASE,
    exact_match=True,
    service=['service-http'],
)
print(f'Number of security rules - {len(security_rules)}')
for security_rule in security_rules:
    print(f'Name - {security_rule.name}')
