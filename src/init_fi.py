import numpy as np
import matplotlib.pyplot as plt
from netpyne import sim
from netParams import cfg, netParams
import json
sim.createSimulateAnalyze(netParams, cfg)
#from batch import params

#firing_rates = []  # List to store firing rates for each current value

# Analyze spike data and compute firing rate
#rate = sim.analysis.popAvgRates() # Get spike times
#data = json.dumps({'amp': sim.net.params.stimSourceParams['IClamp1']['amp'],
                  # 'rate': rate['PT5B']})

spike_times = sim.simData['spkt']
rate = len(spike_times)

data = json.dumps({'amp': sim.net.params.stimSourceParams['IClamp1']['amp'],
                   'rate': rate})
sim.send(data)
print(data)
