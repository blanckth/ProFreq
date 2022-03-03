#!/usr/bin/env python3

# Author : Salar Muhammadi

# DateTime : Fri, 26 March 2021

# Proffesional Frequency Waves Sound

# LIBRARY

#MATH LIB

import math

#Audio Tools LIB : sudo install python-pyaudio

import pyaudio

# Struct LIB

import struct

FORMAT = pyaudio.paInt16

PyAudio = pyaudio.PyAudio  #initialize pyaudio 

BITRATE = 44444  # Number of frames per second/frameset

FREQUENCY = 6119.666 #Hz , Waves per second , 261.63=C4-note

LENGTH = 0.222 #seconds to play sound 

CHANNELS = 2 # 1 for mono and 2 for sterio

PURENUMBER = 8
# ADDITION NUMERICAL MUTIPLICATION

def ANM (NUMBER : int) :
	if NUMBER == 0 :
		return 0
	ANMNUMBER = 0
	for D in str(NUMBER) :
		ANMNUMBER += int(D)
	return int(ANMNUMBER)

# ADDITIONAL PURE NUMBER

def APN (NUMBER : int) :
	if NUMBER == 0 :
		return 0
	ADDPURENUM = NUMBER
	while int(ADDPURENUM) > 9 :
		ADDPURENUM = ANM(ADDPURENUM)
	return ADDPURENUM

# Absoloute NUMBER

def AON (NUMBER : int) :
	if NUMBER < 0 :
		return NUMBER * int(-1)
	else :
		return NUMBER

# Usually Sample rate is Double Frequency

if FREQUENCY > BITRATE:
	BITRATE = FREQUENCY+100

p = PyAudio()

#Generating waves

def data_for_freq(FREQUENCY: float, LENGTH: float = None):
	# Get frames for a fixed Frequency for a specified time or number of frames ,
	#  if NUMBEROFFRAMES is specified time is ignored

	NUMBEROFFRAMES = int(BITRATE * LENGTH)

	RESTFRAMES = NUMBEROFFRAMES % BITRATE

	WAVEDATA=[]

	for x in range(NUMBEROFFRAMES):

		a = BITRATE / FREQUENCY #number of frames per wave

		b = x / a # part of wave in graph

		px2 = 2 * math.pi

		c = b * px2

		d = math.sin(c) * 32767

		e = int(d)
		WAVEDATA.append(e)

		#WAVEDATA = WAVEDATA+chr(int(math.sin(x/((BITRATE/FREQUENCY)/math.pi))*127+128))

	for x in range(RESTFRAMES):
		WAVEDATA.append(0)

	NUMBEROFBYTES = str(len(WAVEDATA))
	WAVEDATA = struct.pack(NUMBEROFBYTES + 'h', *WAVEDATA)

	return WAVEDATA

def play(FREQUENCY: float , LENGTH: float):

	# play a frequency for a fixed time!
##
	frames = data_for_freq(FREQUENCY,LENGTH)

	stream = p.open(format=FORMAT, channels=CHANNELS, rate=BITRATE, output=True)

	stream.write(frames)

	stream.stop_stream()

	stream.close()

	#p.terminate()

def ANMRYTHM() :

	MINfreq = 17
	MAXfreq = 32767
	nmfreq = MINfreq
	backanmfreq = 1
	BACKW = False
	while nmfreq < MAXfreq :
		
		print (nmfreq)

		FREQUENCY = nmfreq

		play (FREQUENCY,LENGTH)

		anmFrq = APN (int(FREQUENCY))
		if BACKW :
			nmfreq -= APN (anmFrq * backanmfreq) 
			nmfreq = AON (nmfreq)
			BACKW = False
		else :
			nmfreq += anmFrq * backanmfreq + backanmfreq
			BACKW = True
		
		backanmfreq = anmFrq
		
		print (anmFrq)

#stream = p.open(format = p.get_format_from_width(1),channels = CHANNELS, rate = BITRATE,output = True)
def main():
	#ANMRYTHM()
	#play(35.666,6.21)
	freqMedList= [174,285,396,417,432,528,639,741,852,963]
	while True:
		for x in freqMedList:
			play(float(x),0.2)
if __name__ == "__main__":
	main()
