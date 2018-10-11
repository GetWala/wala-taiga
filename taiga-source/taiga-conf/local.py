# Please modify this file as needed, see the local.py.example for details:
# https://github.com/taigaio/taiga-back/blob/master/settings/local.py.example
#
# Importing docker provides common settings, see:
# https://github.com/benhutchins/docker-taiga/blob/master/docker-settings.py
# https://github.com/taigaio/taiga-back/blob/master/settings/common.py
from .docker import *

import os

PUBLIC_REGISTER_ENABLED = False
DEBUG = False
TEMPLATE_DEBUG = False

## Slack
# https://github.com/taigaio/taiga-contrib-slack
INSTALLED_APPS += ["taiga_contrib_slack"]

## LDAP
# see https://github.com/ensky/taiga-contrib-ldap-auth
# INSTALLED_APPS += ["taiga_contrib_ldap_auth"]

## For additional configuration options, look at:
# https://github.com/taigaio/taiga-back/blob/master/settings/local.py.example

#GMAIL SETTINGS EXAMPLE
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

IMPORTERS["trello"] = {
   "active": True, # Enable or disable the importer
   "api_key": os.getenv("TRELLO_API_KEY"),
   "secret_key": os.getenv("TRELLO_API_SECRET_KEY")
}