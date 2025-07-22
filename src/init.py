"""
init.py

Starting script to run NetPyNE-based models

"""
from netpyne import sim
from src.cfg import cfg
from netParams import netParams

sim.createSimulateAnalyze(netParams, cfg)
