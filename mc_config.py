#!/usr/bin/python

##############################################################################
# Global Variables
###############################################################################
user = 'admin'

# moved password to mc_auth.py
# password = "xxxxxxxxxxx"

##############################################################################
# Use the following MC URL to determine the UID of the SHARED Object to edit and
# the POLICY to install https://hostname:8082/api/policies
###############################################################################

mgmtcenter_host = 'mgmtcenter.domain.com'
shared_uid = 'EECFD24A-4FEE-4D4C-9692-B90F95B407C1'
policy_uid = 'BD435D17-F97B-4A0E-94F8-6324BA82512F'

# if you need to test without a HTTPS access able .txt file
deny_urls = ['abc123.com', 'abc456.com', 'abc789.com', 'def123.com', 'def456.com', 'def789.com', 'ghi123.com',
             'ghi456.com', 'ghi789.com', 'espn8.com']
