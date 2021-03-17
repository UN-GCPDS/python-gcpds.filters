# from gcpds.utils import loaddb
from matplotlib import pyplot as plt
import numpy as np
from scipy.fftpack import fft, fftfreq, fftshift
from scipy.signal import welch
from datetime import datetime, timedelta

# db = loaddb.BCI_CIV_2a('BCI2a_database')
# db.load_subject(1)
# data, _ = db.get_data()
# fs = db.metadata['sampling_rate']
# data.shape

data = np.random.random(1000)

from gcpds.filters import frequency as flt

flt.alpha(data, timestamp=[0, 15.2]).shape
