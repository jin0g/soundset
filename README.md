# Instruments synthesized source generator for Machine-Learning (ALPHA)

# Set up
- $ cd project-directory
- $ git clone https://github.com/jin0g/soundset.git
- $ cp /your/path/of/soundfont.sf2 soundset/fonts/soundfont.sf2

# REQUIRES
- numpy

# How to use
## BASIC
- import soundset
- score = soundset.random_score(length=10,tempo=120,beat=16,chord=3,range=('C3','C5')) # 10seconds
- piano = score.generate_piano_roll # Two-dimensional binary array(length*beat/4, 88)
- mono_wave = score.generate_wave(font='soundfont.sf2',stereo=False,rate=44100) # float array(times*rate), in [-1,1]
- stereo_wave = score.generate_wave(font='soundfont.sf2',stereo=True,rate=44100) # float array(times*rate,2), in [-1,1]

## TWO INSTRUMENTS
- wave1 = socre1.generate_wave(font='font1.sf2')
- wave2 = socre2.generate_wave(font='font2.sf2')
- wave = soundset.mix( wave1 + wave2 )

# TODO
- import soundfont data

# LICENCE
Only My PRIVATE!!
DONT USE THIS
