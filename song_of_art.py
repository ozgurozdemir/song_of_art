"""
    Song of Art
    Created by Özgür Özdemir
    Uploaded /October 4 2018/

    Special thanks to Tesabob2001 for the library of piano keys
    See: https://freesound.org/people/Tesabob2001/packs/12995/
"""

import numpy as np
from math import sqrt
from scipy import misc
from scipy.io import wavfile
import wave
from random import randint
import time
import sys
import os


""" 
Progress bar
 Thanks to stackoverflow user 6502 for the code: https://stackoverflow.com/users/320726/6502
 See the topic: https://stackoverflow.com/questions/6169217/replace-console-output-in-python
"""
def startProgress(title):
    global progress_x
    sys.stdout.write(title + ": [" + "-"*40 + "]" + chr(8)*41)
    sys.stdout.flush()
    progress_x = 0

def progress(x):
    global progress_x
    x = int(x * 40 // 100)
    sys.stdout.write("#" * (x - progress_x))
    sys.stdout.flush()
    progress_x = x

def endProgress():
    sys.stdout.write("#" * (40 - progress_x) + "]\n")
    sys.stdout.flush()


def get_distance(x, y):
    return sqrt((x-y)**2)

# Find the most relevant 5 notes
def get_note(nparr, notes):

    # TODO:
    # Normalize

    #nparr /= 255.0
    knn_dict = {}
    for i in range(len(notes)):

        #notes[i] /= 255.0
        sum = 0
        leng = len(notes[i])
        if(leng > 25000): leng = 24999
        for j in range(leng):
            sum += get_distance(nparr[j], notes[i][j])
        knn_dict[i] = sum
    knn_dict = sorted(knn_dict.items(), key=lambda kv: kv[1])
    return knn_dict[:5]

# Read all notes waves
def read_notes(path):
    notes = []
    names = []
    dir = os.listdir(path)
    for file in dir:
        if ".wav" in file: names.append(file)
    for file in names:
        fs, data = wavfile.read(path + '/' + file)
        notes.append(data[:,0])
    return names, notes

# Create the output audio file corresponding to calculations
def make_audio(file_name, files):
    outfile = file_name.split('.')[0] + ".wav"
    data= []
    for i in range(len(files)):
        w = wave.open('./piano_keys/' + files[i], 'rb')
        data.append( [w.getparams(), w.readframes(w.getnframes())] )
        w.close()
    output = wave.open(outfile, 'wb')
    output.setparams(data[0][0])
    for i in range(len(data)):
        output.writeframes(data[i][1])
    output.close()

# Read image and notes
def read_image(path):
    # In order not to find image with given directory then asks again for correct
    try:
        image = misc.imread('./' + path, flatten = True)
        files, notes = read_notes('./piano_keys')

        image = image.flatten()
        chord = []
        mem = [] # Check the sequence is same or not
                 # the number of sequence can be adjusted
        leng = int(len(image)/25000)

        # TODO:
        # There is remainder corresponding to chosen sampling rate

        startProgress('Converting') # Progress Bar
        start = time.time() # Time Calculator
        for i in range(leng):
            r = i*25000
            knn = get_note(image[r:r+24999], notes)
            progress(i)
            if(len(mem)<1): # Iteration of notes can be adjusted for different sounds
                chord.append(files[knn[0][0]])
                mem.append(files[knn[0][0]])
            else:
                chord.append(files[knn[randint(1,4)][0]])
                mem = []
        endProgress()
        print('Running time: %f second' % (time.time() - start))
        return chord

    except IOError:
        inp = input('The file cannot be found, please try again:\n')
        read_image(inp)

files, notes = read_notes('./piano_keys')
files = ['./piano_keys/' + n for n in files]

file_name = input('Please give the name of picture with extension:\n')

chord = read_image(file_name)
if chord is not None:
    make_audio(file_name, chord)
