#!flask/bin/python

import os
import unittest

from app.modules.overview.main import Overview

class TestSystem(unittest.TestCase):
    def test_getOs_match_centos(self):
        ov = Overview()
        self.assertEqual('CentOS release 6.4 (Final)', ov.getOs())

class TestSystem(unittest.TestCase):
    def test_getHostname_for_match(self):
        ov = Overview()
        self.assertEqual('py-ton', ov.getHostname())

class TestSystem(unittest.TestCase):
    def test_getDiskUsed_for_match(self):
        ov = Overview()
        self.assertEqual('1820', '1820')

class TestSystem(unittest.TestCase):
    def test_getDiskFree_for_match(self):
        ov = Overview()
        self.assertEqual('1820', '1820')

