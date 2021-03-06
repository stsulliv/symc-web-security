#!/usr/bin/python

###############################################################################
# Management Center API documentation https://host:8082/help/api/
###############################################################################
import requests
import mc_config
import mc_auth
from requests.auth import HTTPBasicAuth

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

# build API URLs
url_policies = 'https://' + mgmtcenter_host + ':8082/api/policies'
url_content = 'https://' + mgmtcenter_host + ':8082/api/policies/' + shared_uid + '/content'
url_install = 'https://' + mgmtcenter_host + ':8082/api/policies/' + policy_uid + '/install'

###############################################################################
# This section demonstrates grabbing the content from a shared object.
###############################################################################

r = requests.get(url_content, auth=HTTPBasicAuth(user, password), verify=False)
print "Retrieve Shared Object status: ", r.status_code, "\n", "Original list: ", r.json()

###############################################################################
# This section demonstrates pushing content to a shared object.
###############################################################################

# load Denied URLs from web TXT file
d = requests.get("https://nas.secureitquest.com/IT/denied_urls.txt")
deny_urls = d.content.split()

print "\n", "Retrieve TXT file status: ", d.status_code, "\n", "New URLs from file: ", deny_urls

# Build Deny List with required JSON keys
denyList = []
for i in deny_urls:
    denyList = denyList + [{"description": "scripted entry", "url": i, "enabled": "true"}]

jsonContent = {"content": {"urls": denyList},
               "contentType": "URL_LIST", "schemaVersion": "1.0", "changeDescription": "scripted update"}

r = requests.post(url_content, auth=HTTPBasicAuth(user, password), json=jsonContent, verify=False)

print "\n", "Update Shared Object status: ", r.status_code, "\n", r.json()

###############################################################################
# This section demonstrates grabbing the content from a shared object.
###############################################################################

r = requests.get(url_content, auth=HTTPBasicAuth(user, password), verify=False)

print "\n", "Retrieve NEW Shared Object status: ", r.status_code, "\n", r.json()

###############################################################################
# This section demonstrates installing a policy.
###############################################################################

r = requests.post(url_install, auth=HTTPBasicAuth(user, password), verify=False)

print "\n", "Install Policy Status: ", r.status_code, "\n", r.json()
