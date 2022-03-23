"""
GreatCircleLayer
================

Plot of direct flights to and from San Francisco International Airport.

Origin is in green; destinations are in blue.

Adapted from the deck.gl documentation.
"""

import pydeck as pdk
import pandas as pd

#GREAT_CIRCLE_LAYER_DATA = "https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/flights.json"  # noqa

df = pd.read_csv('data.csv')

# RGBA value generated in Javascript by deck.gl's Javascript expression parser
GET_COLOR_JS = [
    "255 * (1 - (start[2] / 10000) * 2)",
    "128 * (start[2] / 10000)",
    "255 * (start[2] / 10000)",
    "255 * (1 - (start[2] / 10000))",
]

INITIAL_VIEW_STATE = pdk.ViewState(latitude=47.65, longitude=7, zoom=4.5, max_zoom=16, pitch=50, bearing=0)

scatterplot = pdk.Layer(
    "ScatterplotLayer",
    df,
    radius_scale=20,
    get_position=['target_longitude','target_latitude'],
    get_fill_color=[255, 140, 0],
    get_radius=60,
    pickable=True,
)

line_layer = pdk.Layer(
    "LineLayer",
    df,
    get_source_position=['longitude','latitude'],
    get_target_position=['target_longitude','target_latitude'],
    get_color=GET_COLOR_JS,
    get_width=10,
    highlight_color=[255, 255, 0],
    picking_radius=10,
    auto_highlight=True,
    pickable=True,
)
layers = [scatterplot, line_layer]

# Render
r = pdk.Deck(layers=layers, initial_view_state=INITIAL_VIEW_STATE)
r.to_html("line_layer.html")