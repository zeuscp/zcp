#-*- coding: utf-8 -*-


class User():
    def __init__(self):
        pass

    def checkRoot(self):
        """
        Return True if script executioner is root
        """
        pass

    def checkDirectory(self):
        """
        Return True if directory exists
        """
        pass

    def checkUser(self):
        """
        Return True if user exists
        """
        pass

    def checkGroup(self):
        """
        Return True if group exists
        """
        pass

    def checkUmask(self):
        """
        Return True if umask is 022 in the pam.d file
        """
        pass

    def checkFstab(self):
        """
        Return True if mount point in fstab exists
        """
        pass

    def checkMatchGroup(self):
        """
        Return True if sftp group subsystem is in sshd_config
        """
        pass

    def createUser(self):
        """
        Create new system user with following command:
        useradd -d /home/<username> -s </bin/nologin> -p <passwd> \\
        -g <apache> -G sftponly <username>
        """
        pass

    def createGroup(self):
        """
        Create new system group with following command:
        grpadd sftponly
        """
        pass

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
                self.createGroup():
            if not self.checkUser():
                self.createUser():
            else:
                self.updateUser():
            if not self.checkDirectory():
                self.createDirectory():
            if not self.checkUmask():
                self.appendUmask()
            if not self.checkSubSystemGroup():
                self.appendSubSystemGroup()
            if not self.checkBindMount():
                self.appendBindMount():
            self.mountFstab()

if __name__ == '__main__':
    user = User()
    user.run()
