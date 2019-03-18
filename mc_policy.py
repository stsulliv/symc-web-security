#!/usr/bin/python

import requests
import json
import mc_config
from requests.auth import HTTPBasicAuth

# Added to disable insecure request warning
import urllib3
urllib3.disable_warnings()

###############################################################################
# Global Variables from mc_config.py
###############################################################################
user = mc_config.user
password = mc_config.password
mgmtcenter_host = mc_config.mgmtcenter_host
shared_uid = mc_config.shared_uid
policy_uid = mc_config.policy_uid
deny_urls = mc_config.deny_urls

###############################################################################
# This section demonstrates listing all policies
###############################################################################
url = 'https://' + mgmtcenter_host + ':8082/api/policies'
r = requests.get(url, auth=HTTPBasicAuth(user, password), verify=False)
json_object = json.dumps(r.json(), indent=4)
print r.status_code, "\n", json_object
# un-formatted JSON output # print r.status_code, "\n", r.json()

###############################################################################
# This section demonstrates grabbing the content from a shared object.
###############################################################################
url = 'https://' + mgmtcenter_host + ':8082/api/policies/' + shared_uid + '/content'
r = requests.get(url, auth=HTTPBasicAuth(user, password), verify=False)
json_object = json.dumps(r.json(), indent=4)
print r.status_code, "\n", json_object
# print r.status_code, "\n", r.json()

###############################################################################
# This section demonstrates pushing content to a shared object.
###############################################################################
url = 'https://' + mgmtcenter_host + ':8082/api/policies/' + shared_uid + '/content'
for i in deny_urls:
    print (i)

jsonContent = {"content": {"urls": [{"description": "", "url": "xyz123.com", "enabled": "true"},
                                    {"description": "", "url": "login.microsoftonline.com", "enabled": "true"},
                                    {"description": "", "url": "login.microsoft.net", "enabled": "true"},
                                    {"description": "", "url": "login.windows.com", "enabled": "true"},
                                    {"description": "", "url": "office365.com", "enabled": "true"},
                                    {"description": "", "url": "office.com", "enabled": "true"}]},
               "contentType": "URL_LIST", "schemaVersion": "1.0", "changeDescription": "Script Update"}
r = requests.post(url, auth=HTTPBasicAuth(user, password), json=jsonContent, verify=False)
json_object = json.dumps(r.json(), indent=4)
print r.status_code, "\n", json_object
# print r.status_code, "\n", r.json()

###############################################################################
# This section demonstrates grabbing the content from a shared object.
###############################################################################
url = 'https://' + mgmtcenter_host + ':8082/api/policies/' + shared_uid + '/content'
r = requests.get(url, auth=HTTPBasicAuth(user, password), verify=False)
json_object = json.dumps(r.json(), indent=4)
print r.status_code, "\n", json_object
# print r.status_code, "\n", r.json()

###############################################################################
# This section demonstrates installing a policy.
###############################################################################
url = 'https://' + mgmtcenter_host + ':8082/api/policies/' + policy_uid + '/install'
r = requests.post(url, auth=HTTPBasicAuth(user, password), verify=False)
json_object = json.dumps(r.json(), indent=4)
print r.status_code, "\n", json_object
# print r.status_code, "\n", r.json()
