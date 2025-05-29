from netpyne import specs, sim

cfg = specs.SimConfig()  # create a SimConfig object, can be provided with a dictionary on initial call to set initial values
netParams = specs.NetParams()  # create a netParams object

sim.createSimulateAnalyze(netParams, cfg)
