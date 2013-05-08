#!/usr/bin/env python2

from stormpath.client import ClientBuilder

api_key_file = 'apikey.yml'
client = ClientBuilder().set_api_key_file_location(api_key_file).build()`
