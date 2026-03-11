from netpyne.batchtools.search import search
import numpy
import plotly.express as px
import pandas as pd

# Create parameter grid for search
params = {'IClamp1.amp': [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]}

# use batch_sge_config if running on a
shell_config = {'command': 'python init_fi.py',}

results = search(job_type = 'sh',
       comm_type = 'socket',
       params          = params,
       run_config      = shell_config,
       label           = "grid_search",
       output_path     = "./grid_batch",
       checkpoint_path = "./ray",
       algorithm       = "grid",
       metric          = 'rate',
       mode            = 'max',
       max_concurrent  = 5)

df = pd.read_csv('grid_search.csv')

fig = px.line(df, x='IClamp1.amp', y='rate')

fig.write_html('grid_Tim_fi.html')
