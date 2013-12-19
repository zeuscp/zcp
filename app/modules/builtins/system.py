#-*- coding: utf-8 -*-

from netifaces import interfaces, ifaddresses, AF_INET
import subprocess
import fileinput
import platform
import socket
import errno
import sys
import re
import os


class System():
    def __init__(self):
        pass

    def checkRoot(self):
        """
        Return True if user execution is by root
        """
        user = os.geteuid()
        if user != 0:
            return False
        else:
            return True

    def runShellCommand(self, command):
        """
        Runs shell command via subprocess
        """
        try:
            sh = subprocess.Popen(command.split(),
                                  stdout=subprocess.PIPE,
                                  stderr=subprocess.PIPE,
                                 )
            output, error = sh.communicate()
            if sh.returncode:
                if sh.returncode == 2:
                    raise OSError
            return output
        except OSError:
            raise OSError

    def getKernelRelease(self):
        """
        Get Kernel Release Version
        """
        return platform.release()

    def getOs(self):
        """
        Get Operating System Release
        """
        return self.runShellCommand("cat /etc/system-release")

    def getHostname(self):
        """
        Get Hostname
        """
        return socket.gethostname()

    def scanFile(self, file, string, array=None):
        """
        Returns True if scan finds string
        """
        self.array = []
        try:
            regex = re.compile('\\b'+string+'\\b')
            with open(file, 'r') as lines:
                for line in lines:
                    match = regex.findall(line)
                    if len(match) > 0:
                        if array:
                            self.array.append(line)
                        return True
        except IOError:
            raise IOError
            return False

    def readFile(self, file):
        """
        Reads a file
        """
        try:
            with open(file, 'r') as lines:
                return lines.read()
        except IOError:
            raise IOError
            return False
            

    def writeFile(self, file, contents):
        """
        Writes a file
        """
        try:
            f = open(file, 'w')
            f.write(contents)
            f.close()
        except Exception, e:
            raise Exception

    def appendFile(self, file, string):
        """
        Appends line to a file
        """
        try:
            with open(file, 'a') as line:
                line.write(string)
                line.close
        except Exception:
            raise Exception

    def findReplaceFile(self, file, find, replace):
        """
        Find string and replace
        """
        try:
            for line in fileinput.FileInput(file, inplace=1):
                line = line.replace(find, replace)
                print line,
        except OSError:
            raise OSError
        except Exception, e:
            raise Exception

    def writeToLogFile(self):
        """
        Write line to log file
        """
        pass

    def createDirectory(self, path):
        """
        Create Directory
        """
        try:
            os.makedirs(path)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise OSError
        return True

    def getIps(self):
        """
        Return List of IP addresses
        """
        ip_list = []
        for interface in interfaces():
            for link in ifaddresses(interface)[AF_INET]:
                ip_list.append(link['addr'])
        return ip_list

if __name__ == '__main__':
    system = System()
    #print system.runShellCommand('l -al hello')
    #print system.runShellCommand('foo bar')
    #print system.runShellCommand('ls -al hello')
    #print system.runShellCommand('cas -al hello')
    #print system.readFile('/home/zeus/current/test.txt')
    #system.writeFile('app/modules/builtins/tests/testappendtofile.txt',
    #                 'Change: ME\n')
    #print system.readFile('app/modules/builtins/tests/testappendtofile.txt')
    #system.findReplaceFile("app/modules/builtins/tests/testappendtofile.txt",
    #                       "ME",
    #                       "I am changed",
    #                      )
    #print system.readFile('app/modules/builtins/tests/testappendtofile.txt')
    #system.findReplaceFile("app/modules/builtins/tests/testemptyappendtofile.txt",
    #                       "ME",
    #                       "I am changed",
    #                      )
    #print system.readFile('app/modules/builtins/tests/testemptyappendtofile.txt')

