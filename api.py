#!/usr/bin/env python3

import json
import os.path
import sys
import requests

class simpleapi():
    def __init__(self, server_root):
        self.server_root = server_root

    def api_get(self, request_uri, request_data={}):
        '''
        perform a RESTful GET and return the resulting json
        '''
        try:
            sess_response = requests.get(
                    request_uri,
                    headers={'Accept': 'application/json'},
                    data=json.dumps(request_data))
        except Exception as ex:
            self.exit_error(400, "Error in api_get.  Cannot connect.  Check your server root address!", ex)
        return sess_response

    def api_post(self, request_uri, request_data={}, action='post'):
        '''
        perform a RESTful POST and process the resulting json
        '''
        try:
            if action == "put":
                sess_response = requests.put(
                    request_uri,
                    headers={'Accept': 'application/json'},
                    data=json.dumps(request_data))
            elif action == "patch":
                sess_response = requests.patch(
                    request_uri,
                    headers={'Accept': 'application/json'},
                    data=json.dumps(request_data))
            else:
                sess_response = requests.post(
                    request_uri,
                    headers={'Accept': 'application/json'},
                    data=json.dumps(request_data))
        except Exception as ex:
            self.exit_error(400, "Error in api_post.  Cannot connect.  Check your server root address!", ex)
        return sess_response

    def api_delete(self, request_uri, request_data=None):
        '''
        perform a RESTful DELETE and return the resulting json
        '''
        try:
            if request_data:
                sess_response = requests.delete(
                        request_uri,
                        headers={'Accept': 'application/json'},
                        data=json.dumps(request_data))
            else:
                sess_response = requests.delete(
                        request_uri,
                        headers={'Accept': 'application/json'})
        except Exception as ex:
            self.exit_error(400, "Error in api_delete.  Cannot connect.  Check your server root address!", ex)
        return sess_response

    def get_products(self):
        '''
        Get all product
        '''
        uri = self.server_root + '/api/v1/products'
        return self.api_get(uri)

    def get_product(self, _id):
        '''
        Get a specific product
        '''
        uri = self.server_root + '/api/v1/products/' + str(_id)
        return self.api_get(uri)

    def get_invalid_url(self):
        '''
        Make a request to an invalid URL
        '''
        uri = self.server_root + '/api/v1/reviews/'
        return self.api_get(uri)

