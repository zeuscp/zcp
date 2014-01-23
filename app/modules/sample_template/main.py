# -*- coding: utf-8 -*-


class SampleTemplate():
    def __init__(self, voice):
        self.voice = voice

    def yell(self, message):
        yell = "Your {0} voice yells, {1}!".format(self.voice,
                                                  message,
                                                  )
        return yell

if __name__ == '__main__':
    sc = SampleTemplate('awkward')
    print sc.yell('Yay for zeusCp!')
