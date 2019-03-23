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
        response_list = []
        try:
            sess_response = requests.get(
                    request_uri,
                    headers={'Accept': 'application/json'},
                    data=json.dumps(request_data))
        except Exception as ex:
            self.exit_error(400, "Error in api_get.  Cannot connect.  Check your server root address!", ex)
        if sess_response.status_code == 200 or sess_response.status_code == 201 or sess_response.status_code == 202:
            content_type = sess_response.headers.get('Content-Type')
            if (content_type and
                    content_type.lower().startswith('application/json')):
                if isinstance(sess_response.json(), list):
                    response_list = sess_response.json()
                else:
                    response_list.append(sess_response.json())
            elif (content_type and
                    content_type.lower().startswith('text/plain')):
                    response_list = sess_response
            else:
                self.exit_error(sess_response.status_code, "Error in api_get - Content type")
        else:
            print("Response: ", sess_response.json())
            self.exit_error(sess_response.status_code, "Error in api_get - HTTPS Status Code received from request.  "
                                                       "Please reference the error code with standard HTTPS error "
                                                       "responses.")
        return response_list

    def api_post(self, request_uri, request_data={}, action='post'):
        '''
        perform a RESTful POST and process the resulting json
        '''
        response_list = []
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
        if sess_response.status_code == 200 or sess_response.status_code == 201 or sess_response.status_code == 202 or sess_response.status_code == 204 or sess_response.status_code == 304:
            content_type = sess_response.headers.get('Content-Type')
            if (content_type and
                    content_type.lower().startswith('application/json')):
                if isinstance(sess_response.json(), list):
                    response_list = sess_response.json()
                else:
                    response_list.append(sess_response.json())
            else:
                if sess_response.status_code != 304 or sess_response.status_code != 204:
                    print(sess_response._content)
                    # self.exit_error(sess_response.status_code, "Error in api_post - Content type")
        else:
            print(sess_response._content)
            self.exit_error(sess_response.status_code, "Error in api_post - Status Code")
        print('Status code: ', sess_response.status_code)
        print('Response: ', sess_response)
        return sess_response

    def api_delete(self, request_uri, request_data=None):
        '''
        perform a RESTful DELETE and return the resulting json
        '''
        response_list = []
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
        if sess_response.status_code == 200 or sess_response.status_code == 201 or sess_response.status_code == 202 or sess_response.status_code == 204:
            content_type = sess_response.headers.get('Content-Type')
            if (content_type and
                    content_type.lower().startswith('application/json')):
                if isinstance(sess_response.json(), list):
                    response_list = sess_response.json()
                else:
                    response_list.append(sess_response.json())
            else:
                print('Status Code: ', sess_response.status_code)
                print('Response: ', sess_response)
                # self.exit_error(400, "Error in api_delete.", sess_response.status_code)
        else:
            self.exit_error(400, "Error in api_delete.", sess_response.status_code)
        if len(response_list) == 0:
            self.exit_error(404, "Error in api_delete.")
        return response_list

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
