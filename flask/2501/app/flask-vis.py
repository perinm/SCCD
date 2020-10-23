import streamlit as st
#import matplotlib.pyplot as plt
import pandas as pd

#st.write("Authors:")
#images = ["/root/ryuk.jpg","/root/waru.jpg","/root/peregoso.jpg"]
#st.image(images, width=200, caption=images)

def display_dataframe_quickly(df, max_rows=2000, **st_dataframe_kwargs):
    """Display a subset of a DataFrame or Numpy Array to speed up app renders.
    Parameters
    ----------
    df : DataFrame | ndarray
        The DataFrame or NumpyArray to render.
    max_rows : int
        The number of rows to display.
    st_dataframe_kwargs : Dict[Any, Any]
        Keyword arguments to the st.dataframe method.
    """
    n_rows = len(df)
    if n_rows <= max_rows:
        # As a special case, display small dataframe directly.
        st.dataframe(df)

    else:
        # Slice the DataFrame to display less information.
        start_row = st.slider('Linha inicial', 0, n_rows - max_rows)
        end_row = start_row + max_rows
        df = df[start_row:end_row]

        # Reindex Numpy arrays to make them more understandable.
        if type(df) == np.ndarray:
            df = pd.DataFrame(df)
            df.index = range(start_row, end_row)

        # Display everything.
        st.dataframe(df, **st_dataframe_kwargs)
        st.text('Mostando linhas %i até %i de %i.' % (start_row, end_row - 1, n_rows))


# @st.cache
# def ler_df():
# 	pass

df = pd.read_csv("texto.csv", sep=",", parse_dates={"teste":[1,2]}, index_col='teste')

display_dataframe_quickly(df)

st.line_chart(df[['T (ºC)']])
#plt.plot( 'teste', 'T (ºC)', data=df)
