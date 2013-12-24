#-*- coding: utf-8 -*-

from app.modules.core.system import System
import fileinput
import re


class TextFileHandling():
    def __init__(self):
        self.system = System()
        self.array = []

    def readFile(self, file_path):
        """
        Reads and returns a file
        """
        try:
            with open(file_path, 'r') as lines:
                return lines.read()
        except IOError:
            raise IOError

    def scanFileForString(self, file_path, string, array=None):
        """
        Scan File to match for a string, if array is set, append to
        self.array[]
        """
        self.array = []
        try:
            regex = re.compile('\\b{0}\\b'.format(string))
            with open(file_path, 'r') as lines:
                for line in lines:
                    match = regex.findall(line)
                    if len(match) > 0:
                        if array:
                            self.array.append(line)
                        print self.array
                        return True
        except IOError:
            raise IOError

    def appendToFile(self, file_path, content):
        """
        Append to a file
        """
        try:
            with open(file_path, 'a') as line:
                line.write(content)
                line.close()
            return True
        except:
            raise

    def writeToFile(self, file_path, content):
        """
        Write content to a file
        """
        try:
            file = open(file_path, 'w')
            file.write(content+'\n')
            file.close()
            return True
        except:
            raise

    def findReplaceString(self, file_path, find_string, replace_string):
        """
        Find and replace a string within a file
        """
        try:
            for line in fileinput.FileInput(file_path, inplace=1):
                line = line.replace(find_string, replace_string)
                print line,
            return True
        except OSError:
            raise OSError
        except:
            raise
