#!flask/bin/python
#-*- coding: utf-8 -*-

from app.modules.core import textfilehandling as tfh
import unittest
import os


class TestSystem(unittest.TestCase):
    def test_writeToFile_true(self):
        th = tfh.TextFileHandling()
        write = th.writeToFile('app/modules/core/tests/tfh_test.txt',
                               'foobar',
                               )
        self.assertTrue(write)

    def test_readFile_match_foobar(self):
        th = tfh.TextFileHandling()
        match = th.readFile('app/modules/core/tests/tfh_test.txt')
        self.assertEqual('foobar', match.strip('\n'))
        
    def test_readFile_for_ioerror(self):
        th = tfh.TextFileHandling()
        self.assertRaises(IOError,
                          th.readFile,
                          'app/modules/core/tests/tfh_test.txst'
                          )
        
    def test_scanFileForString_for_true(self):
        th = tfh.TextFileHandling()
        scan = th.scanFileForString('app/modules/core/tests/tfh_test.txt',
                                    'foobar',
                                    )
        self.assertTrue(scan)

    def test_scanFileForString_for_false(self):
        th = tfh.TextFileHandling()
        scan = th.scanFileForString('app/modules/core/tests/tfh_test.txt',
                                    'food',
                                    )
        self.assertFalse(scan)

    def test_scanFileForString_for_ioerror(self):
        th = tfh.TextFileHandling()
        self.assertRaises(IOError,
                          th.scanFileForString,
                          'app/modules/core/tests/tfh_test.txst',
                          'foo',
                          )
