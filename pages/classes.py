import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go




def classes_repartition(df):
    st.write("""
                Classes repartitions 
            """)
    fig = px.pie(df, values = "Nombre", names = "Classe", color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig)

def class_repartition_go(df, lvl = None):
    colors = {
        "Sadida": "#C5C5C5",      # Vert nature
        "Ouginak": "#4C5B61",     # Marron sauvage
        "Eniripsa": "#829191",    # Rose guérisseur
        "Enutrof": "#949B96",     # Or richesse
        "Osamodas": "#2C423F",    # Rouge bestial
        "Sacrieur": "#C5C5C5",    # Rouge sang
        "Xelor": "#4C5B61",       # Bleu temporel
        "Zobal": "#829191",       # Doré masque
        "Eliotrope": "#949B96",   # Violet portail
        "Huppermage": "#2C423F",  # Bleu mystique
        "Ecaflip": "#C5C5C5",     # Marron chatoyant
        "Steamer": "#4C5B61",     # Gris mécanique
        "Cra": "#829191",         # Vert forêt
        "Feca": "#949B96",        # Bleu protecteur
        "Sram": "#2C423F",        # Gris assassin
        "Pandawa": "#C5C5C5",     # Gris panda
        "Iop": "#4C5B61",         # Rouge guerrier
        "Roublard": "#829191"     # Marron roublard
    }

    if lvl != None:
        df_count = df.loc[((df['level'] <= lvl) & (df['level'] >= lvl - 14)), 'classe'].value_counts()
    else:
        df_count = df['classe'].value_counts()
    
    fig = go.Figure(data = [go.Pie(labels = df_count.index,
                                   values = df_count.values.tolist())])
    
    fig.update_traces(hoverinfo = 'label+percent', textinfo = 'value', textfont_size = 10,
                      marker = dict(colors = list(colors.values()), line = dict(color = '#000000', width = 1)))
    
    st.plotly_chart(fig)
    

def tranche_repartition(df):
    fig = px.histogram(df, x='level', category_orders={'level': LEVEL_OPTIONS})
    fig.update_layout(
        bargap=0.2
    )
    fig.update_xaxes(type='category', tickvals=LEVEL_OPTIONS, ticktext=[str(lvl) for lvl in LEVEL_OPTIONS])
    fig.update_traces(marker_color='#3a3a3a')
    st.plotly_chart(fig)
    
def clean_level(lvl):
    for lvl_it in LEVEL_OPTIONS:
        if lvl_it >= lvl:
            return lvl_it


LEVEL_OPTIONS = [20, 35, 50, 65, 80, 95, 110, 125, 140, 155, 170, 185, 200, 215, 230, 245]


st.title('Classe Information')

slider = st.select_slider("Selectionnez une tranche de niveau", options = LEVEL_OPTIONS)
df = pd.read_csv("data/info.csv")
df["level"] = df["level"].apply(clean_level)
if st.checkbox('View all level'):
    class_repartition_go(df)
else:
    class_repartition_go(df, slider)


tranche_repartition(df)