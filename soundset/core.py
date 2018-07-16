import numpy as np
import random

# from .helper import default_path

def default_path(filename):
    import os
    return os.path.dirname(os.path.abspath(__file__)) + '/' + filename

center = 60

class score:
    # generator
    @classmethod
    def random(cls,length,tempo=80,beat=8,chord=1,pitch=3,register=25,random_state=None,minnote=None,maxnote=None):
        # minnote <= note < maxnote
        if minnote is None: minnote = 12 + 12*pitch
        if maxnote is None: maxnote = minnote + register
        # note candidates in register
        candidates = list( range(minnote, maxnote) )
        # generate notes
        random.seed(random_state)
        notes = [sorted(random.sample(candidates, chord)) for _ in range(length)]
        # create class and return
        return cls(notes,base=minnote,high=maxnote,tempo=tempo,beat=beat)

    def __init__(self, notes, base, high, tempo, beat):
        self.notes = notes
        self.base = base # including
        self.high = high # excluding
        self.tempo = tempo
        self.beat = beat

    def to_roll(self, ignore_out_of_range=False):
        # zero array
        roll = np.zeros((len(self.notes), 128), int)
        # pin flg to roll
        for i, ns in enumerate(self.notes):
           roll[i][ns] = 1
        # mask
        if ignore_out_of_range:
            roll = roll[:, self.base:self.high]
        # return
        return roll

    # create wave data
    # policy: notes -prettymidi-> midi -fluidsynth-> wav -scipy.waveform-> numpy array
    def to_wave(self, instrument,font=None,stereo=False,rate=44100,mono_dim2=False,clip=True):
        # find default soundfont if needed
        if font is None: font = default_path('TimGM6mb.sf2')
        assert 0<=instrument and instrument<128
        # 1.create midi file
        from pretty_midi import PrettyMIDI, Instrument, Note
        midi = PrettyMIDI(resolution=960, initial_tempo=self.tempo)
        inst = Instrument(instrument)
        reso = 60/self.tempo*4/self.beat
        for i,ns in enumerate(self.notes):
            for n in ns:
                inst.notes.append(Note(velocity=100, pitch=n, start=i*reso, end=i*reso+reso))
        midi.instruments.append(inst)
        midi.write('temp.mid')
        # 2.create wave file
        from midi2audio import FluidSynth
        fs = FluidSynth(font,sample_rate=rate)
        fs.midi_to_audio('temp.mid', 'temp.wav')
        # 3.import wav file
        from scipy.io import wavfile
        _, wave = wavfile.read('temp.wav')
        # clip
        if clip:
            le = len(self.notes)
            wave = wave[:int(rate*reso*le)]
        wave = wave.astype(float) / abs(wave).max() * 0.9
        return wave










# import random
# from scipy.io import wavfile
# import numpy as np
# import os


# class score

# instruments = {
    # 'piano':  [ 0, 'piano',  'C4', 24],
    # 'oboe':   [69, 'oboe',   'C4', 24],
    # 'guitar': [24, 'guitar', 'C3', 24],
    # 'base':   [34, 'base',   'C2', 24],
# }


# # with instrument name
# def get_wave(inst, tempo, beat):
    # number, filename, lo_code, ncode = instruments[inst]
    # return load_instrument(filename, ncode)

# # return rate, np.array(code, time, 2-channel)
# def load_instrument(filename, ncode=24):
    # absfname = os.path.abspath(os.path.dirname(__file__)) + '/instruments/' + filename
    # rate, wave = wavfile.read(absfname)
    # wave = wave[:rate*24].reshape(ncode, rate, 2)
    # return rate, wave

# # synthesis score
# # tempo=120 beat=4 fixed
# def synthesis(wave, score, tempo=120, beat=4):
    # _,rate,channel = wave.shape
    # output = np.zeros((int(rate * (len(score) + 1) / 2), channel))
    # for i, code in enumerate(score):
        # output[int(rate*i/2):int(rate*(1+i/2))] = wave[code].sum(axis=0)
    # return output[:int(rate * len(score) / 2)]

# # transeform score to piano roll
# # return (time, key)
# def piano_roll(score, ncode=24):
    # roll = np.zeros((len(score),ncode))
    # for i, code in enumerate(score):
        # roll[i][code] = 1
    # return roll

# # generate random score
# def random_score(length, nmin=1, nmax=3, ncode=24):
    # codes = range(ncode)
    # score = [random.sample(codes, random.randint(nmin, nmax)) for _ in range(length)]
    # return score

# def random_score_possible_melody(length, ncode=24):
    # pass

# def random_score_possible_chord(length, ncode=24):
    # pass

