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

