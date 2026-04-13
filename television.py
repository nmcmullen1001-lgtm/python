import television


class Television:

    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self: television.Television):
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__status = False
        self.__channel = Television.MIN_CHANNEL
        self.__unmuted = 0
        self.__counter = 0


    def power(self: television.Television):
        #checks if power is on, if so turns off, if not turns on.
        if self.__status is False:
            self.__status = True
        elif self.__status is True:
            self.__status = False




    def mute(self: television.Television):
       if self.__status:
        #counter to make it unmute
        self.__counter += 1
        #mutes the volume
        if self.__muted is False:
            self.__muted = True
            if self.__muted is True:
                self.__unmuted = self.__volume
                self.__volume = 0
        #uses the counter to unmute the volume if mute is hit twice.
        if self.__counter == 2:
            self.__muted = False
            if self.__muted is False:
                self.__volume = self.__unmuted
                self.__counter = 0


    def channel_up(self: television.Television):
        if self.__status:
            #checks if the channel is less than the max channel, if so increases by one.
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
                #if the channel is at the max resets it to the lowest channel.
            else:
                self.__channel = Television.MIN_CHANNEL
    def channel_down(self: television.Television):
        if self.__status:
            #checks if the channel is at the lowest, if not goes down by one.
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
                #if the channel is at the lowest, it loops to the highest channel.
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self: television.Television):
        if self.__status:
            #checks if the volume is muted, and if it is it unmutes the volume and resets the counter.
            if self.__muted is True:
                self.__counter = 0
                self.__muted = False
                self.__volume = self.__unmuted
            #if the volume is lower than the maximum it increases by one.
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            #if the volume is at the maximum nothing happens.
            else:
                self.__volume = self.__volume

    def volume_down(self: television.Television):
        if self.__status:
            # checks if the volume is muted, and if it is it unmutes the volume and resets the counter.
            if self.__muted is True:
                self.__counter = 0
                self.__muted = False
                self.__volume = self.__unmuted
                #if the volume is higher than the lowest value decreases by one.
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
            else:
                pass

    def __str__(self):
        #returns the numerical or state values.
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'