# =========================================================
# 💖 MATERIAL GOSSIP AI 💖
# Y2K INTERNET MAGAZINE EDITION ✨
# Inspirado en Disney/GirlSense/2008 internet
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import random
import time
import plotly.express as px
import plotly.graph_objects as go

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import euclidean_distances

# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="💖 Material Gossip AI 💖",
    page_icon="🎀",
    layout="wide"
)

# =========================================================
# CSS Y2K EXTREMO
# =========================================================

st.markdown("""

<style>

@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Fredoka', sans-serif;
}

/* =========================================================
FONDO PRINCIPAL
========================================================= */

.stApp {

    background:
    linear-gradient(
        180deg,
        #ffb7da 0%,
        #ffd6ea 20%,
        #fff0f7 45%,
        #ffe3f4 70%,
        #f1fff8 100%
    );

    background-attachment: fixed;
}

/* =========================================================
TOP HEADER
========================================================= */

.top-banner {

    background:
    linear-gradient(
        90deg,
        #ff4fa1,
        #ff89c5,
        #ffb6d9
    );

    padding: 18px;

    border-radius: 25px;

    border: 6px solid white;

    text-align: center;

    color: white;

    font-size: 40px;

    font-weight: bold;

    box-shadow:
        0 0 25px rgba(255,20,147,0.5);

    margin-bottom: 20px;
}

/* =========================================================
SIDEBAR
========================================================= */

section[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #ff7bbb,
        #ffd0e8
    );

    border-right: 8px solid #ff4fa1;
}

/* =========================================================
TITULOS
========================================================= */

h1 {

    color: #ff2f92 !important;

    text-align: center;

    font-size: 70px !important;

    text-shadow:
        3px 3px white,
        5px 5px #ffb7da;

    background: white;

    border:
        6px solid #ff8fc7;

    border-radius: 25px;

    padding: 15px;
}

h2, h3 {

    color: #ff4fa1 !important;

    text-shadow:
        2px 2px white;
}

/* =========================================================
CAJAS
========================================================= */

.cute-box {

    background:
    linear-gradient(
        180deg,
        #fff8fc,
        #ffe7f4
    );

    border:
        5px solid #ff9ed1;

    border-radius: 30px;

    padding: 25px;

    margin-bottom: 25px;

    box-shadow:
        0 0 25px rgba(255,105,180,0.3);
}

/* =========================================================
BOTONES
========================================================= */

.stButton>button {

    background:
    linear-gradient(
        180deg,
        #ff5cad,
        #ff9ed1
    );

    color: white;

    border:
        4px solid white;

    border-radius: 20px;

    font-size: 18px;

    font-weight: bold;

    height: 3.5em;

    width: 100%;

    box-shadow:
        0 4px 15px rgba(255,20,147,0.4);
}

/* =========================================================
INPUTS
========================================================= */

.stTextInput input {

    background: white;

    border:
        4px solid #ff9ed1 !important;

    border-radius: 18px !important;

    color: #ff2f92;

    font-size: 18px;
}

/* =========================================================
SLIDERS
========================================================= */

.stSlider {

    background: rgba(255,255,255,0.3);

    padding: 10px;

    border-radius: 15px;
}

/* =========================================================
TABS
========================================================= */

.stTabs [data-baseweb="tab"] {

    background: white;

    border-radius: 20px 20px 0px 0px;

    border:
        4px solid #ff9ed1;

    margin-right: 10px;

    padding: 15px;

    font-size: 18px;

    color: #ff4fa1;
}

/* =========================================================
DATAFRAME
========================================================= */

[data-testid="stDataFrame"] {

    border:
        5px solid #ff9ed1;

    border-radius: 25px;
}

/* =========================================================
SCROLL
========================================================= */

::-webkit-scrollbar {

    width: 12px;
}

::-webkit-scrollbar-thumb {

    background: #ff7bbb;

    border-radius: 20px;
}

/* =========================================================
MARCOS
========================================================= */

.y2k-card {

    background: white;

    border:
        5px solid #ff9ed1;

    border-radius: 30px;

    padding: 20px;

    text-align: center;

    box-shadow:
        0 0 20px rgba(255,105,180,0.25);
}

</style>

""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown("""
<div class='top-banner'>
💖 MATERIAL GOSSIP AI 💖<br>
✨ la revista más chismosa de ingeniería ✨
</div>
""", unsafe_allow_html=True)

# =========================================================
# TITULO
# =========================================================

st.title("🎀 MATERIAL MATCH MAGAZINE 🎀")

# =========================================================
# IMAGENES Y2K
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.image(
        "https://i.pinimg.com/736x/4b/51/8c/4b518ce4dc0d7e1c0d48cb4e8b42c06d.jpg"
    )

with col2:
    st.image(
        "https://i.pinimg.com/736x/e4/66/17/e466174fefcb31b8d02cbd7a1fdfe91b.jpg"
    )

with col3:
    st.image(
        "https://i.pinimg.com/736x/f2/72/70/f272708da7d9c6e8f1d09d4aefbde6d9.jpg"
    )

# =========================================================
# INTRO
# =========================================================

st.markdown("""
<div class='cute-box'>

## 🌸 Bienvenida bestie 🌸

Aquí puedes:

✨ Buscar materiales  
✨ Encontrar el mejor material con IA  
✨ Leer chismes metalúrgicos  
✨ Jugar Flappy Bunny Materials  
✨ Aprender ingeniería de materiales de manera cute 💅

</div>
""", unsafe_allow_html=True)

# =========================================================
# CARGAR EXCEL
# =========================================================

df = pd.read_excel("Data_convertido.xlsx")

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
)

# =========================================================
# COLUMNAS
# =========================================================

columnas_numericas = [
    "Su",
    "Sy",
    "A5",
    "Bhn",
    "E",
    "G"
]

for col in columnas_numericas:

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df = df.dropna(subset=columnas_numericas)

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "💖 Match IA",
    "🔍 Buscar",
    "📰 Chismes",
    "🎮 Flappy Bunny"
])

# =========================================================
# TAB 1
# =========================================================

with tab1:

    st.header("💅 Encuentra tu material ideal")

    st.sidebar.title("🎀 Propiedades deseadas")

    uts = st.sidebar.slider(
        "💪 Resistencia última",
        int(df["Su"].min()),
        int(df["Su"].max()),
        int(df["Su"].mean())
    )

    ys = st.sidebar.slider(
        "⚙️ Yield Strength",
        int(df["Sy"].min()),
        int(df["Sy"].max()),
        int(df["Sy"].mean())
    )

    elong = st.sidebar.slider(
        "🌸 Elongación",
        int(df["A5"].min()),
        int(df["A5"].max()),
        int(df["A5"].mean())
    )

    hb = st.sidebar.slider(
        "🧁 Dureza",
        int(df["Bhn"].min()),
        int(df["Bhn"].max()),
        int(df["Bhn"].mean())
    )

    young = st.sidebar.slider(
        "📏 Young Modulus",
        int(df["E"].min()),
        int(df["E"].max()),
        int(df["E"].mean())
    )

    corte = st.sidebar.slider(
        "✨ Shear Modulus",
        int(df["G"].min()),
        int(df["G"].max()),
        int(df["G"].mean())
    )

    if st.sidebar.button("💖 ENCONTRAR 💖"):

        features = [
            "Su",
            "Sy",
            "A5",
            "Bhn",
            "E",
            "G"
        ]

        scaler = MinMaxScaler()

        X = scaler.fit_transform(df[features])

        usuario = scaler.transform([[
            uts,
            ys,
            elong,
            hb,
            young,
            corte
        ]])

        distancias = euclidean_distances(
            usuario,
            X
        )

        indices = np.argsort(
            distancias[0]
        )[:5]

        mejores = df.iloc[indices].copy()

        mejores["Compatibilidad"] = [
            round(100 / (1 + d), 2)
            for d in distancias[0][indices]
        ]

        st.success("✨ materiales encontrados bestie ✨")

        st.dataframe(
            mejores[
                [
                    "Material",
                    "Heat treatment",
                    "Compatibilidad"
                ]
            ],
            use_container_width=True
        )

        fig = px.scatter(
            mejores,
            x="Bhn",
            y="Su",
            size="Compatibilidad",
            color="Material",
            text="Material"
        )

        fig.update_layout(
            paper_bgcolor="#fff0f7",
            plot_bgcolor="#fff7fb"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# =========================================================
# TAB 2 BUSCADOR
# =========================================================

with tab2:

    st.header("🔍 Busca materiales")

    busqueda = st.text_input(
        "🎀 escribe algo"
    )

    if busqueda:

        traducciones = {

            "acero": "steel",
            "plata": "silver",
            "aluminio": "aluminum",
            "cobre": "copper",
            "titanio": "titanium",
            "hierro": "iron",
            "oro": "gold",
            "aleacion": "alloy"
        }

        palabra = busqueda.lower()

        if palabra in traducciones:

            palabra = traducciones[palabra]

        materiales_texto = (
            df["Material"]
            .astype(str)
            .str.lower()
        )

        heat_texto = (
            df["Heat treatment"]
            .astype(str)
            .str.lower()
        )

        resultados = df[
            materiales_texto.str.contains(
                palabra,
                na=False
            )

            |

            heat_texto.str.contains(
                palabra,
                na=False
            )
        ]

        if len(resultados) > 0:

            st.success(
                f"💖 {len(resultados)} resultados encontrados"
            )

            for i in range(
                min(8, len(resultados))
            ):

                material = resultados.iloc[i]

                st.markdown(f"""
                <div class='cute-box'>

                <h2>✨ {material['Material']}</h2>

                💪 Resistencia: {material['Su']}<br>
                ⚙️ Yield: {material['Sy']}<br>
                🌸 Elongación: {material['A5']}<br>
                🧁 Dureza: {material['Bhn']}<br>

                💅 Gossip:
                "este material anda siendo icónico en aplicaciones industriales"

                </div>
                """, unsafe_allow_html=True)

        else:

            st.error("😭 no encontré nada bestie")

# =========================================================
# TAB 3 CHISMES
# =========================================================

with tab3:

    st.header("📰 Material Gossip")

    chismes = [

        """
        💅 Stainless Steel volvió a humillar
        a todos en corrosión.
        Sigue siendo la reina.
        """,

        """
        ✈️ Titanium fue visto
        en aplicaciones aeroespaciales
        porque pesa poquito pero aguanta TODO.
        """,

        """
        ⚡ Copper sigue siendo
        el conductor eléctrico favorito.
        literalmente una diva.
        """,

        """
        🧁 Aluminum anda presumiendo
        que es ligero y bonito
        pero le falta fuerza 😭
        """
    ]

    for c in chismes:

        st.markdown(f"""
        <div class='cute-box'>
        <h3>{c}</h3>
        </div>
        """, unsafe_allow_html=True)

# =========================================================
# TAB 4 JUEGO
# =========================================================

with tab4:

    st.header("🎮 Flappy Bunny Materials")

    st.markdown("""
    <div class='cute-box'>

    🐰 Ayuda al bunny a caer en un material.

    Dependiendo del material desbloqueas:
    ✨ propiedades
    ✨ datos curiosos
    ✨ aplicaciones

    </div>
    """, unsafe_allow_html=True)

    materiales_juego = [

        {
            "nombre": "Titanium",
            "emoji": "🚀",
            "dato": "Muy ligero y super resistente",
            "uso": "Aeroespacial"
        },

        {
            "nombre": "Copper",
            "emoji": "⚡",
            "dato": "Excelente conductor",
            "uso": "Electrónica"
        },

        {
            "nombre": "Steel",
            "emoji": "🏗️",
            "dato": "Muy fuerte y barato",
            "uso": "Construcción"
        },

        {
            "nombre": "Aluminum",
            "emoji": "✨",
            "dato": "Ligero y resistente",
            "uso": "Aviones y autos"
        }
    ]

    st.markdown("## 🐰")
    st.progress(30)

    if st.button("💖 VOLAR 💖"):

        st.balloons()

        elegido = random.choice(materiales_juego)

        st.success(f"""
        🌸 Bunny cayó en:

        {elegido['emoji']} {elegido['nombre']}

        ✨ Dato:
        {elegido['dato']}

        🏭 Uso:
        {elegido['uso']}

        💅 Chismecito:
        "todo mundo quiere trabajar con este material"
        """)

        st.image(
            "https://media.tenor.com/JhQ8tMUz6v8AAAAC/pink-glitter.gif"
        )

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class='cute-box'>

<center>

💖 MATERIAL GOSSIP AI 💖<br>

✨ ingeniería de materiales pero fashion ✨

</center>

</div>
""", unsafe_allow_html=True)
