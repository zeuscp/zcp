#!flask/bin/python

import os
import unittest

from app.modules.builtins import system
from app.modules.builtins import resources

class TestSystem(unittest.TestCase):
    def test_runShellCommand_returns_true(self):
        sh = system.System()
        hello = sh.runShellCommand('echo hello')
        self.assertEqual('hello\n', hello)

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

    def test_appendFile_match_of_successful_write(self):
        sh = system.System()
        sh.writeFile('app/modules/builtins/tests/appendfile.txt',
                     '')
        sh.appendFile('app/modules/builtins/tests/appendfile.txt',
                     'I\'m an appendage!\n')
        match = sh.readFile('app/modules/builtins/tests/appendfile.txt')
        self.assertEqual("I'm an appendage!\n",
                         match)

    def test_appendFile_Exception_of_write(self):
        sh = system.System()
        self.assertRaises(Exception,
                          sh.appendFile,
                          'app/modules/builtins/testas/appendfile.txt',
                          'I should raise an exception!\n')

    def test_findReplaceFile_OSError_for_exception(self):
        sh = system.System()
        self.assertRaises(OSError,
                          sh.findReplaceFile,
                          "app/modules/builtins/tests/testemptyfindreplacetofile.txt",
                          "I should be false!",
                          "I should be true!"
                         )
    def test_findReplaceFile_successfully_changed(self):
        sh = system.System()
        sh.writeFile('app/modules/builtins/tests/testfindreplacetofile.txt',
                         'Change: ME\n')
        sh.findReplaceFile("app/modules/builtins/tests/testfindreplacetofile.txt",
                               "ME",
                               "I am changed",
                              )
        match = sh.readFile('app/modules/builtins/tests/testfindreplacetofile.txt')
        self.assertEqual('Change: I am changed\n',
                         match)

    def test_findReplaceFile_exception_for_exception(self):
        sh = system.System()
        self.assertRaises(Exception,
                          sh.findReplaceFile,
                          "app/modules/builtins/tests/testfindreplaceofile.txt",
                          "I should be false!",
                          "I should be true!"
                         )

    def test_createDirectory_OSError_for_exception(self):
        sh = system.System()
        self.assertRaises(OSError,
                          sh.createDirectory,
                          '/var/www/footest',
                         )

    def test_createDirectory_success(self):
        sh = system.System()
        self.assertTrue(True,
                        sh.createDirectory(
                        'app/modules/builtins/tests/createDirectory',
                        )
                       )

    def test_getKernel(self):
        sh = system.System()
        res = resources.Resources()
        kernel = sh.runShellCommand('uname -r')
        self.assertEqual(kernel.replace('\n', ''),
                         res.getKernelRelease())

    def test_getOS(self):
        sh = system.System()
        res = resources.Resources()
        os = sh.runShellCommand('cat /etc/system-release')
        self.assertEqual(os,
                         res.getOs())

    def test_getHostName(self):
        sh = system.System()
        res = resources.Resources()
        hostname = sh.runShellCommand('hostname')
        self.assertEqual(hostname.replace('\n', ''),
                         res.getHostname())
