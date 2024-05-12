import streamlit as st
import pandas as pd
import numpy as np

st.write("Hello world")
#movie = st.text_input('Favorite Movie?')
#st.write(movie)

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a","b","c"]
)

st.bar_chart(chart_data)
st.line_chart(chart_data)


