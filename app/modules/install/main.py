# -*- coding: utf-8 -*-

# Create new vhost conf for any distro
# detect web service
# add gzip

#modules
from sqlalchemy import func
from app.modules.builtins import system as s
from app.modules.builtins import resources as r


class Overview():
    def __init__(self):
        self.system = s.System()
        self.resources = r.Resources()
        self.os = self.system.getOs()
        self.hostname = self.system.getHostname()
        self.ips = self.system.getIps()
        self.kernel = self.system.getKernelRelease()
        self.disk_usage = self.resources.getDiskUsage()
        self.ram_usage = self.resources.getRamUsage()

    def getHostname(self):
        """
        Return Hostname
        """
        return self.hostname

    def getOs(self):
        """
        Return Operating System
        """
        return self.os

    def getIps(self):
        """
        Return Operating System
        """
        return self.ips

    def getKernel(self):
        """
        Return kernel version
        """
        return self.kernel

    def getDiskUsed(self):
        """
        Return Amount of Used Disk
        """
        return self.disk_usage.used / 1024 / 1024

    def getDiskFree(self):
        """
        Return Amount of Free Disk
        """
        return self.disk_usage.free / 1024 / 1024

    def getDiskTotal(self):
        """
        Return Amount of total Disk
        """
        return self.disk_usage.total / 1024 / 1024

    def getDiskPercent(self):
        """
        Return Percent of free Disk
        """
        return self.disk_usage.percent

    def getRamUsed(self):
        """
        Return Amount of Used Ram
        """
        return self.ram_usage.used / 1024 / 1024

    def getRamFree(self):
        """
        Return Amount of Free ram
        """
        return self.ram_usage.free / 1024 / 1024

    def getRamTotal(self):
        """
        Return Amount of total Ram
        """
        return self.ram_usage.total / 1024 / 1024

    def getRamPercent(self):
        """
        Return Percent of free Ram
        """
        return self.ram_usage.percent


if __name__ == '__main__':
    overview = Overview()
    overview.os
    overview.hostname
    overview.ips
    overview.kernel
