#-*- coding: utf-8 -*-

from app.modules.core import system
from app.modules.core.exceptions import DoesNotExist
import psutil


class Resources():
    def __init__(self):
        self.system = system.System()

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
                return psutil.disk_usage(path)
            else:
                raise DoesNotExist({"Error": "{0} does not exist".format(path)})
        except:
            raise
            