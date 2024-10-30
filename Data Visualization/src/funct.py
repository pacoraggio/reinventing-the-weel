import pandas as pd
import numpy as np

from vega_datasets import data
import json


def get_vega_colors(scheme_name='tableau10'):
    """
    Retrieve color values from a Vega color scheme.
    
    Args:
        scheme_name (str): Name of the Vega color scheme (default: 'tableau10')
        
    Returns:
        list: List of hexadecimal color values
    """
    # Load the vega color schemes data
    schemes = data.vega_schemes()
    
    # Parse the JSON string containing the schemes
    color_schemes = json.loads(schemes)
    
    # Find the requested scheme
    for scheme in color_schemes:
        if scheme['name'] == scheme_name:
            return scheme['colors']
    
    raise ValueError(f"Color scheme '{scheme_name}' not found")

def sum_and_round(x):
    if np.issubdtype(x.dtype, np.floating):
        return round(x.sum(), 0)
    else:
        return x.sum()


def mean_and_round(x):
    if np.issubdtype(x.dtype, np.floating):
        return round(x.mean(), 4)
    else:
        return x.mean()


def plot_boxplot_with_points(df, obs, value):
    obs_type = obs+':N'
    value_type = value + ':Q'
    
    points = (alt  
              .Chart(df.sort_values(value))
              .mark_point(size = 50, filled=True, opacity=0.8, color = '#953f0a')
              .encode(
                  x = alt.X(value),
                  tooltip = [obs_type, value_type]
              )
             )
    
    box = (alt
           .Chart(df.sort_values(value))
           .mark_boxplot(size = 25)
           .encode(
               x = alt.X(value_type),
           )
          )

    title = value + " by " + obs + " box plot"
    
    chart = (box + points).properties(
        title = title,
        width = 620,
        height = 180
    )
    return(chart)