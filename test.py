import soundset


# create random score for C3~C5note == 130.8~523.3hz
#-> score object
s1 = soundset.score.random(length=32,tempo=120,beat=16,chord=3,pitch=3,register=25,random_state=None)

# create score piano roll
#-> 2-dim binaly numpy array, size of (length, 128)
roll = s1.to_roll(ignore_out_of_range=False)
assert roll.dtype==int, 'it is binaly array but dtype is int'
assert roll.shape==(32,128), 'shape is to (32,128)'
assert roll.min()==0 and roll.max()==1, 'binaly array'
assert all( roll.sum(axis=1)==3 ), 'each line has 3 notes'

roll = s1.to_roll(ignore_out_of_range=True)
assert roll.shape == (32,25), 'the roll shape is to (32,25) when ignore_out_of_range is True'

# synthesize score
#-> 1 or 2-dim float on [-1,1] numpy array, size of (length):mono or (length, 2):stereo
wave = s1.to_wave(instrument=0,stereo=True,rate=44100) # inst0=piano
assert wave.dtype==float
assert wave.shape==(44100*32*4/16*60/120, 2)
assert -1<=wave.min() and wave.max()<=1

# synthesize score with system soundfont
wave = s1.to_wave(instrument=40) # synthesize violin with default font



# refaences

## score
## you can generate specific score with pianoroll
# s2 = soundset.score.generate(roll=roll) # the size must be (length, 128)

## (in future) you can generate score from midi file
# s2 = soundset.score.load(filename='midi/file/name.midi')

## (in future) you can save score as midi file
# s2.save(filename='midifilename.midi')


## synthesize
## (in future) wave is Periodic function which period is 2 pi, and range is [-1,1]
# s2.to_wave(wave=np.sin)

print('')
print('all tests pass.')
print('done.')
