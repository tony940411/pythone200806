# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 09:58:54 2020

@author: user
"""

fo=open("Desert.jpg","rb")
img=fo.read()
fo.close()
fo=open("殺.jpg","wb")
fo.write(img)
fo.close()
