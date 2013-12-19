#-*- coding: utf-8 -*-

from app.modules.builtins.system import System

class User():
    def __init__(self):
        self.system = System()

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

    def checkGroup(self, command=None):
        """
        Return True if group exists
        """
        if not command:
            command = "id -g ftpuser"
        try:
            grp = self.system.runShellCommand(command)
            grp = int(grp)
            if isinstance(grp, int):
                return True
            else:
                return False
        except ValueError, e:
            raise ValueError

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
            match = "Subsystem\s+sftp\s+/usr/libexec/openssh/sftp-server"
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
        pass

    def createGroup(self, command="groupadd sftponly"):
        """
        Create new system group with following command:
        groupadd sftponly
        """
        string = self.system.runShellCommand(command)
        print string
        return string

    def createDirectory(self):
        """
        Create new directory
        """
        pass

    def appendUmask(self):
        """
        Append umask line in pam.d file
        """
        pass

    def appendSubSystemGroup(self):
        """
        Append SubSystem Group to sshd_config
        """
        pass

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
