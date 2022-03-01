import math
import os
import random
import re
import sys


def weirdNotweird(N):
    if N % 2 == 1:
        print('Weird')
        
    elif N % 2 == 0 and N in range(2, 6):
        print('Not Weird')
    
    elif N % 2 == 0 and N in range(6, 21):
        print('Weird')
    
    elif N % 2 == 0 and N > 20:
        print('Not Weird')



weirdNotweird(100)
weirdNotweird(21)
weirdNotweird(20)
weirdNotweird(6)
