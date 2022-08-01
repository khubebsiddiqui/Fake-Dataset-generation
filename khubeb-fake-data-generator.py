#####################Install the required Libraries if not available##########

#%pip install faker
#%pip install matplotlib
#%pip install pandas
#%pip install numpy
#$pip install random

# debugging and formatter
from IPython.core.debugger import set_trace
from random import choice, randint

#%load_ext nb_black

import pandas as pd
import numpy as np
import os
import random
import matplotlib.pyplot as plt
import time
import random
from random import choice, randint

################### Import faker #######3
from faker import Faker
fake = Faker()


Weather = ["sunny","rainy","cloudy"]
City = ["Sydney","Melbourne","Brisbane","Darwin","Perth","Tasmania","Bathurst","New Castle"]

###########Defining Function to generate Fake data##########################
def faker_timeseries_rows(num=1, seed=None):

    fake.seed_instance(seed)

    time_gen = fake.time_series(start_date=f"-{num}d", end_date="now", precision=3600)

    output = [
        {
          "Location": random.choice(City), 
          "Local time": next(time_gen),
         "position" : {fake.latitude(), fake.longitude(),randint(10, 1000)},  
          "condition" : random.choice(Weather),
          "humidity" : randint(1, 100),
          "Temperature" : randint(-20, +50),
          "Pressure" : randint(900, 1200),
        }
        for x in range(num)
    ]
    return output
	

df = pd.DataFrame(faker_timeseries_rows(1000, seed=0))
df.head(6)

