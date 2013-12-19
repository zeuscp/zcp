#-*- coding: utf-8 -*-

import system
import platform
import socket
import psutil


class Resources():
    def __init__(self):
        self.system = system.System()

    def getRamUsage(self):
        """
        Get Virtual Memory Usage
        """
        return psutil.virtual_memory()

    def getDiskUsage(self,path='/'):
        """
        Get Disk usage from <path>
        """
        return psutil.disk_usage(path)

if __name__ == '__main__':
    res = Resources()
    print res.getRamUsage()
