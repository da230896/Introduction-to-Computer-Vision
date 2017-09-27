import cv2
import numpy as np
from matplotlib import pyplot as plt

def find_template_1D(t,s):
    #need list of string for 'join' 
    t_str = ''.join(str(x) for x in t)
    s_str = ''.join(str(x) for x in s)
    #print t_str,s_str
    i = s_str.find(t_str)
    return i

s = [-1,0,0,1,1,1,0,-1,-1,0,-1,0,0,-1]
t = [1,1,0]
print(find_template_1D(t,s))    