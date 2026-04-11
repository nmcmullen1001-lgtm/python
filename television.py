
class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__status = False
        self.__channel = Television.MIN_CHANNEL
        self.__unmuted = 0
        self.__counter = 0


    def power(self):
        if self.__status is False:
            self.__status = True
        elif self.__status is True:
            self.__status = False




    def mute(self):
       if self.__status:
        self.__counter += 1
        if self.__muted is False:
            self.__muted = True
            if self.__muted is True:
                self.__unmuted = self.__volume
                self.__volume = 0
        if self.__counter is 2:
            self.__muted = False
            if self.__muted is False:
                self.__volume = self.__unmuted
                self.__counter = 0


    def channel_up(self):
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL
    def channel_down(self):
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.__status:
            if self.__muted is True:
                self.__counter = 0
                self.__muted = False
                self.__volume = self.__unmuted
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            else:
                self.__volume = self.__volume

    def volume_down(self):
        if self.__status:
            if self.__muted is True:
                self.__counter = 0
                self.__muted = False
                self.__volume = self.__unmuted
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                pass

    def __str__(self):

        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'