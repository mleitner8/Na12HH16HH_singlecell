"""
cfg.py

Simulation Configuration
"""
from netpyne import specs

cfg = specs.SimConfig() # Object of class SimConfig to store simulation configuration

#########################################################################################
#
# SIMULATION CONFIGURATION
#
#########################################################################################

#------------------------------------------------------------------------------
#  Simulation Parameters
#------------------------------------------------------------------------------
cfg.duration = 1500 # Duration of simulation in ms
cfg.dt = 0.025 # Internal integration time step (ms)
cfg.hParams = {'celsius': 34, 'v_init':-70.0432010302}
cfg.verbose = False # Show detailed messages
cfg.printPopAvgRates = True

cfg.createNEURONObj = 1
cfg.createPyStruct = 1

#------------------------------------------------------------------------------
# Recording
#------------------------------------------------------------------------------
cfg.recordStim = True
cfg.recordCells = [0]
cfg.recordTraces = {'V_soma':{'sec': 'soma', 'loc': 0.5, 'var': 'v'}}
cfg.recordStep = 0.1 #step size to save data (e.g. voltage traces, LFP, et.)


#------------------------------------------------------------------------------
# Saving
#------------------------------------------------------------------------------
cfg.simLabel = 'Na12HH16HH_TF' #File output name
cfg.saveFolder = 'data'
cfg.saveJson = True
cfg.savePickle = False
cfg.saveDataInclude = ['simData', 'simConfig', 'netParams', 'net']

#------------------------------------------------------------------------------
# Analysis and Plotting
#------------------------------------------------------------------------------
#cfg.analysis['plotRaster'] = {'saveFig': True} # Plot Raster
cfg.analysis['plotTraces'] = {'saveFig': True} # Plot Traces

#------------------------------------------------------------------------------
# Weight Normalization
#------------------------------------------------------------------------------
cfg.weightNorm = 1  # use weight normalization
cfg.weightNormThreshold = 4.0  # weight normalization factor threshold

#------------------------------------------------------------------------------
# Current Inputs
#------------------------------------------------------------------------------
cfg.addIClamp = 1 # change to 1 to add IClamps (can add multiple)

cfg.IClamp1 = {'pop': 'PT5B' ,'sec': 'soma', 'loc': 0.5, 'start': 0, 'dur': 500, 'amp': 0.4}



#------------------------------------------------------------------------------
# NetStim Inputs
#------------------------------------------------------------------------------
cfg.addNetStim = 0   # change to 1 to add NetStims (can add multiple)

cfg.NetStim1 = {'pop': 'PT5B', 'sec': 'apic_3', 'loc': 0.5, 'synMech': ['AMPA', 'NMDA'], 'synMechWeightFactor': [0.5, 0.5],
				'start': 0, 'interval': 1000.0/40.0, 'noise': 0.0, 'number': 1000.0, 'weight': 0.5, 'delay': 500}

# ------------------------------------------------------------------------------
# Load mutant params from csv
# ------------------------------------------------------------------------------
cfg.dendNa = 0.1
cfg.loadmutantParams = False
cfg.variant = 'L1666F'  # L1666F, E1211K, D195G, R853Q, K1422E, M1879T, WT
