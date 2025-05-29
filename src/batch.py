from netpyne.batchtools.search import search
import numpy


# Create parameter grid for search
params = {'IClamp1.amp': [0.3, 0.4, 0.5, 0.6]}

# use batch_sge_config if running on a
shell_config = {'command': 'python init.py',}

search(job_type = 'sh',
       params          = params,
       run_config      = shell_config,
       label           = "grid_search",
       output_path     = "./grid_batch",
       checkpoint_path = "./ray",
       algorithm       = "grid",
       max_concurrent  = 9)
