#Python Simulation for problem
import numpy as np
import pandas as pd

s = pd.Series(list(range(24)))
number_of_trials, matches = (0,0)

while number_of_trials < 1000000:
    c1 = s[np.random.choice(24,5, replace = False)]
    c2 = s[np.random.choice(24,5, replace = False)]
    if c2.isin(c1).sum() >= 4:
        matches +=1
        
    number_of_trials +=1
    print(matches/number_of_trials)