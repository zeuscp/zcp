#!flask/bin/python
#-*- coding: utf-8 -*-

from app.modules.core import system
import unittest
import os


class TestSystem(unittest.TestCase):
    def test_executeShellCommand_match_output(self):
        sys = system.System()
        hello = sys.executeShellCommand('echo hello')
        self.assertEqual('hello', hello)

    def test_executeShellCommand_match_output_with_list(self):
        sys = system.System()
        hello = sys.executeShellCommand(['echo', 'hello'])
        self.assertEqual('hello', hello)

    def test_executeShellCommand_match_OSError_false(self):
        sys = system.System()
        hello = sys.executeShellCommand('inva com')
        self.assertFalse(hello)

    def test_executeShellCommand_raise_AttributeError(self):
        sys = system.System()
        self.assertRaises(AttributeError,
                          sys.executeShellCommand,
                          None,
                         )

    def test_executeShellCommand_raise_TypeError(self):
        sys = system.System()
        self.assertRaises(TypeError,
                          sys.executeShellCommand,
                         )

    def test_executeShellCommand_match_IndexError_false(self):
        sys = system.System()
        hello = sys.executeShellCommand([])
        self.assertFalse(hello)

    def test_checkIfRoot_is_true(self):
        sys = system.System()
        self.assertTrue(sys.checkIfRoot())

    def test_checkIfDirectory_is_true(self):
        sys = system.System()
        self.assertTrue(sys.checkIfDirectory('/var'))

    def test_checkIfDirectory_is_false(self):
        sys = system.System()
        self.assertFalse(sys.checkIfDirectory('/false'))

    def test_checkMount_is_true(self):
        sys = system.System()
        self.assertTrue(sys.checkMount('/'))

    def test_checkMount_is_false(self):
        sys = system.System()
        self.assertFalse(sys.checkMount('/false'))

    def test_checkOperatingSystem_match(self):
        sys = system.System()
        os = sys.getOperatingSystem()
        self.assertEqual("CentOS release 6.4 (Final)", os)

    def test_checkHostname_match(self):
        sys = system.System()
        host_name = sys.getHostname()
        match = sys.executeShellCommand("hostname")
        self.assertEqual(match, host_name)

    def test_getKernelRelease_match(self):
        sys = system.System()
        kernel = sys.getKernelRelease()
        match = sys.executeShellCommand("uname -r")
        self.assertEqual(match, kernel)

    def test_checkIfFile_true(self):
        sys = system.System()
        self.assertTrue(sys.checkIfFile('/etc/fstab'))
