#-*- coding: utf-8 -*-

from netifaces import interfaces, ifaddresses, AF_INET
import subprocess
import datetime
import platform
import shutil
import socket
import errno
import sys
import os


class System():
    def __init__(self):
        pass

    def executeShellCommand(self, command):
        """
        Execute a shell command
        """
        if not isinstance(command, list):
            command = command.split()
        try:
            execute = subprocess.Popen(command,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE,
                                       )
            output, error = execute.communicate()
        except OSError:
            return False
        except AttributeError:
            raise TypeError
        except TypeError:
            raise TypeError
        except IndexError:
            return False

        return output.strip('\n')

    def checkIfRoot(self):
        """
        Return True if current user is root
        """
        user = os.geteuid()
        if user != 0:
            return False
        return True

    def checkPackageIsInstalled(self):
        """
        pass
        """
        pass

    def checkIfDirectory(self, path):
        """
        Return True if directory exists
        """
        return os.path.isdir(path)

    def checkIfFile(self, path):
        """
        Return True if directory exists
        """
        return os.path.isfile(path)

    def checkMount(self, path):
        """
        Return True if path is a mountpoint
        """
        return os.path.ismount(path)

    def getKernelRelease(self):
        """
        Return Kernel Release Version
        """
        return platform.release()

    def getIps(self):
        """
        Return List of IP addresses
        """
        ip_list = []
        for interface in interfaces():
            for link in ifaddresses(interface)[AF_INET]:
                ip_list.append(link['addr'])
        return ip_list

    def getOperatingSystem(self):
        """
        Returns the Operating System
        """
        return self.executeShellCommand("cat /etc/system-release")

    def getHostname(self):
        """
        Returns Hostname of current System
        """
        return socket.gethostname()

    def getTimeStamp(self):
        """
        Returns current timestamp in
        mm.dd.yyyy.hh.mm.ss
        """
        timestamp = datetime.datetime.today().strftime('%m.%d.%Y.%H.%M.%S')
        return timestamp

    def createBackupOfFile(self, file_path):
        """
        Create backup of text file
        """
        try:
            if self.checkIfFile(file_path):
                shutil.copyfile(file_path,
                                "{0}.{1}".format(file_path,
                                                 self.getTimeStamp()
                                                 )
                                )
        except:
            raise
        return True

    def createDirectory(self, path):
        """
        Create directory and return true
        """
        try:
            if not self.checkIfDirectory(path):
                os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise OSError
        return True
