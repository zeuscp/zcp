#!flask/bin/python
#-*- coding: utf-8 -*-

from app.modules.core import resources
from app.modules.core.exceptions import DoesNotExist
import unittest
import os


class TestSystem(unittest.TestCase):
    def test_getDiskUsage_true(self):
        res = resources.Resources()
        self.assertRaises(DoesNotExist,
                          res.getDiskUsage,
                          '/r',
                          )

