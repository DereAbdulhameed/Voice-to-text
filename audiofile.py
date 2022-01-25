# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 17:45:06 2021

@author: HP
"""

import speech_recognition as sr
m = sr.Microphone()
r = sr.Recognizer()
print('Pls Talk')
with m as source:
    audio_data = r.record(source, duration=10)
    print('Recognizing...')
    text = r.recognize_google(audio_data)
    print(text)
    