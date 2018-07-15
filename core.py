import random
from scipy.io import wavfile
import numpy as np
import os


instruments = {
    'piano':  [ 0, 'piano',  'C4', 24],
    'oboe':   [69, 'oboe',   'C4', 24],
    'guitar': [24, 'guitar', 'C3', 24],
    'base':   [34, 'base',   'C2', 24],
}


# with instrument name
def get_wave(inst, tempo, beat):
    number, filename, lo_code, ncode = instruments[inst]
    return load_instrument(filename, ncode)

# return rate, np.array(code, time, 2-channel)
def load_instrument(filename, ncode=24):
    absfname = os.path.abspath(os.path.dirname(__file__)) + '/instruments/' + filename
    rate, wave = wavfile.read(absfname)
    wave = wave[:rate*24].reshape(ncode, rate, 2)
    return rate, wave

# synthesis score
# tempo=120 beat=4 fixed
def synthesis(wave, score, tempo=120, beat=4):
    _,rate,channel = wave.shape
    output = np.zeros((int(rate * (len(score) + 1) / 2), channel))
    for i, code in enumerate(score):
        output[int(rate*i/2):int(rate*(1+i/2))] = wave[code].sum(axis=0)
    return output[:int(rate * len(score) / 2)]

# transeform score to piano roll
# return (time, key)
def piano_roll(score, ncode=24):
    roll = np.zeros((len(score),ncode))
    for i, code in enumerate(score):
        roll[i][code] = 1
    return roll

# generate random score
def random_score(length, nmin=1, nmax=3, ncode=24):
    codes = range(ncode)
    score = [random.sample(codes, random.randint(nmin, nmax)) for _ in range(length)]
    return score

def random_score_possible_melody(length, ncode=24):
    pass

def random_score_possible_chord(length, ncode=24):
    pass

