import plotly.graph_objects as go


amp = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0]
Tim_cell = [14, 20, 24, 28, 32, 36, 42, 47, 54, 63, 70, 68, 59, 52,46]
Original_cell = [33, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]



# Create a figure
fig = go.Figure()

# Add the first line trace
fig.add_trace(go.Scatter(x=amp, y=Tim_cell, mode='lines', name='Tim_cell'))

# Add the second line trace
fig.add_trace(go.Scatter(x=amp, y=Original_cell, mode='lines', name='Original_cell'))

# Update layout for title and labels
fig.update_layout(title='Fi Curve',
                  xaxis_title= 'nanoamps',
                  yaxis_title='rate')

# Show the plot
fig.show()