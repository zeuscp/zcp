#!flask/bin/python

import os
import unittest

from app.modules.user import main as user

class TestSystem(unittest.TestCase):
    def test_checkGroup_returns_true(self):
        u = user.User()
        grp = u.checkGroup('root')
        self.assertTrue(grp)

    def test_checkUser_returns_true(self):
        u = user.User()
        us = u.checkUser()
        self.assertTrue(us)
        
    def test_appendUmask_return_true(self):
        us = user.User()
        self.assertTrue(us.appendUmask(umask='0002'))

    def test_checkUser_returns_False(self):
        u = user.User()
        self.assertRaises(ValueError,
                          u.checkUser,
                          'id -u ifail')

    def test_checkDirectory_returns_true(self):
        u = user.User()
        dir = u.checkDirectory('/root')
        self.assertTrue(dir)

    def test_checkDirectory_returns_false(self):
        u = user.User()
        dir = u.checkDirectory('/ifail')
        self.assertFalse(dir)

    def test_checkUmask_returns_true(self):
        u = user.User()
        umask = u.checkUmask()
        self.assertTrue(umask)

    def test_checkUmask_returns_false(self):
        u = user.User()
        umask = u.checkUmask(umask="0222")
        self.assertFalse(umask)

    def test_checkMounts_returns_true(self):
        u = user.User()
        fstab = u.checkMounts()
        self.assertTrue(fstab)

    def test_checkMounts_returns_false(self):
        u = user.User()
        fstab = u.checkMounts(path='/root')
        self.assertFalse(fstab)

    def test_checkSubsytem_returns_true(self):
        u = user.User()
        ss = u.checkSubsystem()
        self.assertTrue(ss)

    def test_checkSubsytem_returns_false(self):
        u = user.User()
        ss = u.checkSubsystem(match="foobar")
        self.assertFalse(ss)

    def test_createGroup_matches_string(self):
        u = user.User()
        grp = u.createGroup()
        self.assertEquals("", grp)

    def test_createUser_matches_string(self):
        us = user.User()
        us.web_service = 'ftponly'
        us.shell = '/bin/false'
        us.passwd = 'foobar'
        us.username = 'rawrgar'
        create = us.createUser()
        print create
        self.assertEquals("", create)
        
    def test_createUser_matches_fail(self):
        us = user.User()
        us.web_service = 'ftponly'
        us.shell = '/bin/false'
        us.passwd = 'foobar'
        us.username = ''
        self.assertRaises(OSError,
                          us.createUser)
        
    def test_createDirectory_return_true_for_exists(self):
        us = user.User()
        self.assertTrue(us.createDirectory('/home/zeus'))
        
    def test_appendSubsystem_return_true(self):
        us = user.User()
        self.assertTrue(us.appendSftpSubsystem())

    def test_checkFstab_returns_true(self):
        us = user.User()
        self.assertTrue(us.checkFstab("/var/www/vhosts/ohaiworld.com\s+/home/foobard/ohaiworld.com\s+none\s+bind\s+0\s+0"))
