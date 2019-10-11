from __future__ import division

import re
import sys
import os

import os
import time
import operator
from pydub import AudioSegment
from pydub.playback import _play_with_simpleaudio as play
# from google.cloud import speech
import simpleaudio as sa

from sequencer import Sequencer

kick_sample = AudioSegment.from_file('./samples/kick.wav', format='wav')
hat_sample = AudioSegment.from_file('./samples/hat.wav', format='wav')
snare_sample = AudioSegment.from_file('./samples/snare.wav', format='wav')

HAT = (hat_sample, (0, 127, 127))
KICK = (kick_sample, (127, 127, 0))
SNARE = (snare_sample, (127, 0, 127))


def LED_Action(color):

    # ss = crickit.seesaw

    # pixels.fill(OFF)
    # pixels.fill(color)

    print(color)


def play_sample(sample):
    play(sample)


def main():
    sequencer = Sequencer()

    sequencer.add_steps(KICK, [0, 3, 7])
    sequencer.add_steps(SNARE, [2, 6])
    sequencer.add_steps(HAT, [0, 1, 2, 3, 4, 5, 6, 7])

    while True:
        tempo = sequencer.get_tempo()

        step = sequencer.get_step()

        if len(step) == 0:
            LED_Action((25, 25, 25))
        elif len(step) == 1:
            play_sample(step[0][0])
            LED_Action(step[0][1])
        else:
            color = (0, 0, 0)
            i = 0
            for sample in step:
                if i == 0:
                    audio = sample[0]
                else:
                    audio = audio.overlay(sample[0])
                color = tuple(map(operator.add, color, sample[1]))
                i += 1

            play_sample(audio)
            LED_Action(color)

        time.sleep(tempo)


if __name__ == '__main__':
    main()
