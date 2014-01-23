#-*- coding: utf-8 -*-

from app.modules.core import system
from app.modules.core.exceptions import DoesNotExist
import psutil


class Resources():
    def __init__(self, path='/'):
        self.path = path
        self.system = system.System()
        self.ram_usage = self.getRamUsage()
        self.disk_usage = self.getDiskUsage(path=self.path)

    def getRamUsage(self):
        """
        Return dictionary of RAM usage
        """
        return psutil.virtual_memory()

    def getDiskUsage(self, path='/'):
        """
        Return usage of path
        """
        try:
            if self.system.checkIfDirectory(path):
                psu = psutil.disk_usage(path)
                self.path = path
                return psu
            else:
                raise DoesNotExist({"Error": "{0} does not exist".format(path)})
        except:
            raise
            
