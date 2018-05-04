# -*- coding: utf-8 -*-
"""
Created on Fri May  4 15:30:09 2018

@author: sujpanda
"""

import numpy as np
import matplotlib.pyplot as plot
import numpy as np

mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 10000)


np.size(s)

plot.hist(s,100)
plot.show()

