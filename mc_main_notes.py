#!/usr/bin/python

import requests
import json
import mc_config
import mc_auth
from requests.auth import HTTPBasicAuth
from Crypto.Cipher import AES

###############################################################################
# Added to disable insecure request warning
###############################################################################
import urllib3
urllib3.disable_warnings()

###############################################################################
# Loads  Global Variables from mc_config.py
###############################################################################

user = mc_config.user
password = mc_auth.password
mgmtcenter_host = mc_config.mgmtcenter_host
shared_uid = mc_config.shared_uid
policy_uid = mc_config.policy_uid

###############################################################################
# Management Center API documentation https://host:8082/help/api/
###############################################################################
url_policies = 'https://' + mgmtcenter_host + ':8082/api/policies'
url_content = 'https://' + mgmtcenter_host + ':8082/api/policies/' + shared_uid + '/content'
url_install = 'https://' + mgmtcenter_host + ':8082/api/policies/' + policy_uid + '/install'

###############################################################################
# This section demonstrates listing all policies
###############################################################################
# url_policies = 'https://' + mgmtcenter_host + ':8082/api/policies'
# r = requests.get(url_policies, auth=HTTPBasicAuth(user, password), verify=False)
# json_object = json.dumps(r.json(), indent=4)
# print r.status_code, "\n", json_object
# un-formatted JSON output
# print r.status_code, "\n", r.json()

###############################################################################
# This section demonstrates grabbing the content from a shared object.
###############################################################################

# url_content = 'https://' + mgmtcenter_host + ':8082/api/policies/' + shared_uid + '/content'
r = requests.get(url_content, auth=HTTPBasicAuth(user, password), verify=False)

# formatting JSON output
json_object = json.dumps(r.json(), indent=4)
print r.status_code, "\n", json_object

# un-formatted JSON output
# print r.status_code, "\n", r.json()

###############################################################################
# This section demonstrates pushing content to a shared object.
# data["list"].append({'b':'2'})
###############################################################################

# load Denied URLs from web TXT file
d = requests.get("https://nas.secureitquest.com/IT/denied_urls.txt")

# add .split to convert the TXT list to a Python Dictionary List
deny_urls = d.content.split()

# if you need to test without a HTTPS access able .txt file
# deny_urls = mc_config.deny_urls

print d.status_code
print deny_urls


# iterate through denied URLs to build List for Dictionary/JSON
denyList = []
for i in deny_urls:
    denyList = denyList + [{"description": "scripted entry", "url": i, "enabled": "true"}]

jsonContent = {"content": {"urls": denyList},
               "contentType": "URL_LIST", "schemaVersion": "1.0", "changeDescription": "scripted update"}

# url_content = 'https://' + mgmtcenter_host + ':8082/api/policies/' + shared_uid + '/content'
r = requests.post(url_content, auth=HTTPBasicAuth(user, password), json=jsonContent, verify=False)

# formatting JSON output
json_object = json.dumps(r.json(), indent=4)
print r.status_code, "\n", json_object

# un-formatted JSON output
# print r.status_code, "\n", r.json()

###############################################################################
# This section demonstrates grabbing the content from a shared object.
###############################################################################

# url_content = 'https://' + mgmtcenter_host + ':8082/api/policies/' + shared_uid + '/content'
r = requests.get(url_content, auth=HTTPBasicAuth(user, password), verify=False)

# formatting JSON output
json_object = json.dumps(r.json(), indent=4)
print r.status_code, "\n", json_object

# un-formatted JSON output
# print r.status_code, "\n", r.json()

###############################################################################
# This section demonstrates installing a policy.
###############################################################################

# url_install = 'https://' + mgmtcenter_host + ':8082/api/policies/' + policy_uid + '/install'
r = requests.post(url_install, auth=HTTPBasicAuth(user, password), verify=False)

# formatting JSON output
json_object = json.dumps(r.json(), indent=4)
print r.status_code, "\n", json_object

# un-formatted JSON output
# print r.status_code, "\n", r.json()
