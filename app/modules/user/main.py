#-*- coding: utf-8 -*-

from app.modules.builtins.system import System

class User():
    def __init__(self):
        self.system = System()
        self.web_service = ""
        self.shell = ""
        self.passwd = ""
        self.username = ""

    def checkDirectory(self, path):
        """
        Return True if directory exists
        """
        return self.system.validateDirectory(path)

    def checkUser(self, command=None):
        """
        Return True if user exists
        """
        if not command:
            command = "id -u root"
        try:
            grp = self.system.runShellCommand(command)
            grp = int(grp)
            if isinstance(grp, int):
                return True
            else:
                return False
        except ValueError, e:
            raise ValueError

    def checkGroup(self, group=None):
        """
        Return True if group exists
        """
        if not group:
            group = "sftpuser"
        try:
            grp = self.system.runShellCommand("id -g {0}".format(group))
            grp = int(grp)
            if isinstance(grp, int):
                return True
            else:
                return False
        except ValueError, e:
            return False

    def checkUmask(self, umask="0002"):
        """
        Return True if umask is 022 in the pam.d file
        """
        a = []
        uma = self.system.scanFile('/etc/pam.d/sshd',
                                   "session\s+optional\s+pam_umask.so\s+umask="+umask,
                                   array=1,
                                  )
        if uma:
            return True
        return False
        

    def checkFstab(self, path="/"):
        """
        Return True if mount point in fstab exists
        """
        bind_mount = self.system.checkMount(path=path)
        if bind_mount:
            return True
        return False

    def checkSubsystem(self, match=None):
        """
        Return True if sftp group subsystem is in sshd_config
        """
        if not match:
            match = "^Subsystem\s+sftp\s+/usr/libexec/openssh/sftp-server"
        ss = self.system.scanFile("/etc/ssh/sshd_config",
                                  match,
                                  array=1
                                 )
        if ss:
            return True
        return False

    def createUser(self):
        """
        Create new system user with following command:
        useradd -d /home/<username> -s </bin/nologin> -p <passwd>
        -g <apache> -G sftponly <username>
        """
        if not self.checkGroup(group="sftponly"):
            self.createGroup(group="sftponly")
        string = "useradd -g {0} -G sftponly -s {1} -p {2} \
-d /home/{3} {3}".format(self.web_service,
                         self.shell,
                         self.passwd,
                         self.username,
                        )
        try:
            cmd = self.system.runShellCommand(string)
            return cmd
        except OSError:
            raise OSError

    def createGroup(self, group="sftponly"):
        """
        Create new system group with following command:
        groupadd sftponly
        """
        string = "groupadd {0}".format(group)
        return self.system.runShellCommand(string)

    def createDirectory(self, path):
        """
        Create new directory
        """
        if not self.system.validateDirectory(path):
            return self.system.createDirectory(path)
        return True

    def appendUmask(self, umask="0002"):
        """
        Append umask line in pam.d file
        """
        file = '/etc/pam.d/sshd'
        if not self.checkUmask(umask):
            if self.system.makeBackup(file):
                self.system.appendFile(file,
                                       "session\t\toptional\tpam_umask.so\tumask="+umask+"\n",
                                      )
                return True
            else:
                return False
        return True

    def disableSubsystem(self, find=None, replace=None):
        """
        Disable Subsystem
        """
        if not find:
            find = "^Subsystem\s+sftp\s+/usr/libexec/openssh/sftp-server",
        if not replace:
            replace = "^#Subsystem\s+sftp\s+/usr/libexec/openssh/sftp-server",
        if self.system.makeBackup('/etc/ssh/sshd_config'):
            self.system.findReplaceFile("/etc/ssh/sshd_config",
                                        find,
                                        replace,
                                       )
        return True

    def appendSubSystem(self, file=None, string=None):
        """
        Append SubSystem Group to sshd_config
        """
        if self.checkSubsystem():
            self.disableSubsytem()
        if not file:
            file = '/etc/ssh/sshd_config'
        if not string:
            string = """
Subsystem   sftp    internal-sftp

UsePAM yes

Match Group sftponly
    ChrootDirectory %h
    ForceCommand internal-sftp
    AllowTcpForwarding no
"""
        if self.system.makeBackup(file):
            self.system.appendFile(file, string)


    def appendBindMount(self):
        """
        Append users bindmount point to fstab
        """
        pass

    def updateUser(self):
        """
        Updates users details: grps, pass, home dir.
        """
        pass

    def updatePasswd(self):
        """
        Updates users passwd.
        """
        pass

    def mountFstab(self):
        """
        Mount's new fstab:
        mount -a
        """
        pass

    def run(self):
        """
        Creates a user or modifies a user
        creates bindmounts
        mounts them
        """
        if self.checkRoot():
            if not self.group():
                self.createGroup()
            if not self.checkUser():
                self.createUser()
            else:
                self.updateUser()
            if not self.checkDirectory():
                self.createDirectory()
            if not self.checkUmask():
                self.appendUmask()
            if not self.checkSubSystemGroup():
                self.appendSubSystemGroup()
            if not self.checkBindMount():
                self.appendBindMount()
            self.mountFstab()

if __name__ == '__main__':
    user = User()
    user.run()
