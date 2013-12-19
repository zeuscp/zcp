#-*- coding: utf-8 -*-

import system
import platform
import socket


class Resources():
    def __init__(self):
        self.system = system.System()

    def getKernelRelease(self):
        """
        Get Kernel Release Version
        """
        return platform.release()

    def getOs(self):
        """
        Get Operating System Release
        """
        return self.system.runShellCommand("cat /etc/system-release")

    def getHostname(self):
        """
        Get Hostname
        """
        return socket.gethostname()

    def getRamUsage(self):
        """
        Get Physical Ram Usage
        """
        return psutil.phymem_usage()

    def getDiskUsage(self,path='/'):
        """
        Get Disk usage from <path>
        """
        return psutil.disk_usage(path)

if __name__ == '__main__':
    res = Resources()
    print res.getKernelRelease()
