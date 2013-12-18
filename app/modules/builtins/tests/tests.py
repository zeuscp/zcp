#!flask/bin/python

import os
import unittest

from app.modules.builtins import system

class TestSystem(unittest.TestCase):
    def test_runShellCommand_returns_true(self):
        sh = system.System()
        hello = sh.runShellCommand('echo hello')
        self.assertEqual(True, hello)

    def test_runShellCommand_return_OSError_invalid_command(self):
        sh = system.System()
        self.assertRaises(OSError, sh.runShellCommand, 'foo bar')

    def test_runShellCommand_return_OSError_file_not_exists(self):
        sh = system.System()
        self.assertRaises(OSError, sh.runShellCommand, 'ls -al /var/log/fooo')

    def test_scanFile_for_IOError_file_not_exists(self):
        sh = system.System()
        self.assertRaises(IOError, sh.scanFile, 'test.txt', 'hello')

    def test_scanFile_for_return_true(self):
        sh = system.System()
        self.assertTrue(sh.scanFile('app/modules/builtins/tests/scanfile.txt',
                                    'Theres a snake in my boots'))

    def test_scanFile_for_return_false(self):
        sh = system.System()
        self.assertFalse(sh.scanFile('app/modules/builtins/tests/scanfile.txt',
                                     'Luke, I am your father'))

    def test_scanFile_for_return_true_with_array(self):
        sh = system.System()
        self.assertTrue(sh.scanFile('app/modules/builtins/tests/scanfile.txt',
                                    'I\'m a broken record',
                                    array=1))

    def test_scanFile_for_return_false_with_array(self):
        sh = system.System()
        self.assertFalse(sh.scanFile('app/modules/builtins/tests/scanfile.txt',
                                     'nooooooooooooooooooo',
                                     array=1))

    def test_readFile_for_IOError_file_not_exists(self):
        sh = system.System()
        self.assertRaises(IOError,
                          sh.readFile,
                          'app/modules/builtins/tests/readfile.t')

    def test_readFile_match_for_string(self):
        sh = system.System()
        match = sh.readFile('app/modules/builtins/tests/readfile.txt')
        self.assertEqual("I have been read!\n",
                         match)

    def test_writeFile_match_of_successful_write(self):
        sh = system.System()
        sh.writeFile('app/modules/builtins/tests/writefile.txt',
                     'Transplanted!\n')
        match = sh.readFile('app/modules/builtins/tests/writefile.txt')
        self.assertEqual("Transplanted!\n",
                         match)

    def test_writeFile_Exception_of_write(self):
        sh = system.System()
        self.assertRaises(Exception,
                          sh.writeFile,
                          'app/modules/builtins/testas/writefile.txt',
                          'I should raise an exception!\n')
