#!/usr/bin/env python3

import random
from api import simpleapi


class UnitTest():
    def __init__(self, server_url):
        self.server_url = server_url
        self.session = simpleapi(server_url)

    def verify_all_products(self):
        resp = self.session.get_products()
        assert resp.status_code == 200

    def verify_product(self):
        resp = self.session.get_product(random.randint(0, 10))
        assert resp.status_code == 200

    def verify_invalid_url(self):
        resp = self.session.get_invalid_url()
        assert resp.status_code == 404

    def run_all_tests(self):
        self.verify_all_products()
        self.verify_product()
        self.verify_invalid_url()
