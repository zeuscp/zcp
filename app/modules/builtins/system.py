#-*- coding: utf-8 -*-

import subprocess
import sys


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
            return True
        except OSError:
            raise OSError

    def scanFile(self, file, string, array=None):
        """
        Returns True if scan finds string
        """
        self.array = []
        regex = re.compile('\\b'+string+'\\b')
        with open(file, 'r') as lines:
            for line in lines:
                match = regex.findall(line)
                if len(match) > 0:
                    if array:
                        self.array.append(line)
                    return True
        return False

    def readFile(self, file):
        """
        Reads a file
        """
        try:
            with open(file, 'r') as lines:
                return lines.read()
        except Exception, e:
            print e
            

    def writeFile(self):
        """
        Writes a file
        """
        pass

    def appendFile(self):
        """
        Appends line to a file
        """
        pass

    def findReplaceFile(self):
        """
        Find string and replace
        """
        pass

    def writeToLogFile(self):
        """
        Write line to log file
        """
        pass

    def createDirectory(self):
        """
        Create Directory
        """
        pass

if __name__ == '__main__':
    system = System()
    print system.runShellCommand('l -al hello')
    print system.runShellCommand('foo bar')
    print system.runShellCommand('ls -al hello')
    print system.runShellCommand('cas -al hello')
    #print system.readFile('/home/zeus/current/test.txt')
