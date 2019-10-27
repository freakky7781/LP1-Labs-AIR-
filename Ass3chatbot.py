# -*- coding: utf-8 -*-
"""
Created on Fri Oct 25 14:39:00 2019

@author: Freakky7781_VRikk
"""

from nltk.chat.util import Chat,reflections
pairs=[
          [
              r"how are you doing (.*)?",
              ["i am doing all fine buddy %1",]
          ], 
       
          [
              r"what is your name (.*)...my name is (.*)?",
              ["My name is Chatty %2 %1",]
          ]
      ]
          
def chatty():
    print("high you are talkig to chaty")
    chat=Chat(pairs,reflections)
    chat.converse()


chatty()