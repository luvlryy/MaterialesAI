# =========================================================
# 🌸 MATERIAL MATCH AI 🌸
# Ultimate Y2K Internet Magazine Edition
# Disney + GirlSense + Materials Engineering
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import random
import plotly.express as px
import plotly.graph_objects as go
import time

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import euclidean_distances

# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="Material Match AI 🌸",
    page_icon="💖",
    layout="wide"
)

# =========================================================
# Y2K CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Fredoka', sans-serif;
}

/* BACKGROUND */

.stApp {

    background:
    linear-gradient(
        180deg,
        #ffd6ec 0%,
        #ffeaf4 35%,
        #fff4fb 70%,
        #f4fff8 100%
    );

    background-attachment: fixed;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #ff8fc7,
        #ffd4e8
    );

    border-right: 6px solid #ff5ea8;
}

/* TITLE */

h1 {

    color: #ff2f92 !important;

    text-align: center;

    font-size: 72px !important;

    text-shadow:
        3px 3px white,
        6px 6px #ffb7d5;

    background: white;

    border:
        5px solid #ff92c2;

    border-radius: 25px;

    padding: 15px;
}

/* SUBTITLES */

h2, h3 {

    color: #ff4fa1 !important;

    text-shadow: 2px 2px white;
}

/* BOXES */

.cute-box {

    background:
    linear-gradient(
        180deg,
        #fff7fb,
        #ffe8f3
    );

    border: 5px solid #ff9cc8;

    border-radius: 30px;

    padding: 25px;

    margin-bottom: 25px;

    box-shadow:
        0 0 20px rgba(255,105,180,0.3);
}

/* BUTTONS */

.stButton>button {

    background:
    linear-gradient(
        180deg,
        #ff69b4,
        #ff9ed1
    );

    color: white;

    border: 4px solid white;

    border-radius: 20px;

    font-size: 18px;

    font-weight: bold;

    height: 3.5em;

    width: 100%;

    box-shadow:
        0 4px 10px rgba(255,105,180,0.4);
}

/* INPUTS */

.stTextInput input {

    background: white;

    border:
        4px solid #ff9ed1 !important;

    border-radius: 18px !important;

    color: #ff2f92;
}

/* TABS */

.stTabs [data-baseweb="tab"] {

    background: white;

    border-radius: 20px 20px 0px 0px;

    border: 3px solid #ff9ed1;

    margin-right: 10px;

    padding: 12px;

    font-size: 18px;

    color: #ff5ea8;
}

/* DATAFRAME */

[data-testid="stDataFrame"] {

    border:
        5px solid #ff9ed1;

    border-radius: 20px;
}

/* METRICS */

[data-testid="metric-container"] {

    background: white;

    border:
        4px solid #ffb3d9;

    border-radius: 25px;
}

/* SCROLLBAR */

::-webkit-scrollbar {

    width: 12px;
}

::-webkit-scrollbar-thumb {

    background: #ff8fc7;

    border-radius: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITLE
# =========================================================

st.title("🌸 Material Match AI 🌸")

st.markdown("""
<div class="cute-box">

## 💖 Welcome to Material Match Magazine 💖

✨ Find materials  
✨ Learn engineering in a cute way  
✨ Explore heat treatments  
✨ Material gossip magazine  
✨ Play games and unlock materials  

🎀 Inspired by 2000s internet girls websites 🎀

</div>
""", unsafe_allow_html=True)

# =========================================================
# LOAD DATABASE
# =========================================================

df = pd.read_excel("Data_convertido.xlsx")

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
)

# =========================================================
# NUMERIC COLUMNS
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
    "🎀 Recommender",
    "🔍 Search",
    "📰 Material Gossip",
    "🎮 Flappy Bunny"
])

# =========================================================
# TAB 1
# =========================================================

with tab1:

    st.header("💖 Material Recommender")

    st.sidebar.title("🎀 Desired Properties")

    uts = st.sidebar.slider(
        "💪 Ultimate Strength",
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
        "🌸 Elongation",
        int(df["A5"].min()),
        int(df["A5"].max()),
        int(df["A5"].mean())
    )

    hb = st.sidebar.slider(
        "🧁 Hardness",
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
        "🐰 Shear Modulus",
        int(df["G"].min()),
        int(df["G"].max()),
        int(df["G"].mean())
    )

    buscar = st.sidebar.button(
        "✨ Find Materials ✨"
    )

    if buscar:

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

        mejores["Similarity %"] = [
            round(100 / (1 + d), 2)
            for d in distancias[0][indices]
        ]

        st.header("🌸 Suggested Materials")

        st.dataframe(
            mejores[
                [
                    "Material",
                    "Heat treatment",
                    "Similarity %"
                ]
            ],
            use_container_width=True
        )

        # GRAPH

        fig = px.scatter(
            mejores,
            x="Bhn",
            y="Su",
            color="Material",
            size="Similarity %",
            text="Material"
        )

        fig.update_layout(
            paper_bgcolor="#fff0f5",
            plot_bgcolor="#fffafc",
            height=600
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# =========================================================
# TAB 2 SEARCH
# =========================================================

with tab2:

    st.header("🔍 Smart Material Search")

    st.markdown("""
    <div class="cute-box">

    💖 Search in English or Spanish

    Examples:

    - steel
    - silver
    - aluminum
    - acero
    - cobre
    - titanio
    - alloy

    </div>
    """, unsafe_allow_html=True)

    busqueda = st.text_input(
        "✨ Search material"
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
            "aleacion": "alloy",
            "metal": "alloy",
            "resistente": "strong"
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
                f"✨ {len(resultados)} materials found!"
            )

            for i in range(
                min(8, len(resultados))
            ):

                material = resultados.iloc[i]

                st.markdown(f"""
                <div class="cute-box">

                <h3>💖 {material['Material']}</h3>

                ✨ Heat Treatment:
                {material['Heat treatment']}

                💪 Ultimate Strength:
                {material['Su']}

                ⚙️ Yield Strength:
                {material['Sy']}

                🌸 Elongation:
                {material['A5']}

                🧁 Hardness:
                {material['Bhn']}

                💅 Material Gossip:
                "She's durable, iconic and engineered to survive."

                </div>
                """, unsafe_allow_html=True)

        else:

            st.error("❌ No materials found bestie")

# =========================================================
# TAB 3 GOSSIP
# =========================================================

with tab3:

    st.header("📰 Material Gossip Magazine")

    gossip = [

        """
        💅 Stainless Steel was seen resisting corrosion
        AGAIN this week.
        Truly impossible to humble her.
        """,

        """
        ✈️ Titanium keeps dominating aerospace.
        Expensive? yes.
        Iconic? also yes.
        """,

        """
        ⚡ Copper is still carrying electronics
        on her back.
        Conductive queen behavior.
        """,

        """
        🌸 Aluminum is lightweight,
        pretty AND useful.
        Main character energy.
        """,

        """
        🔥 Heat-treated steels are becoming
        stronger than everyone's situationship.
        """
    ]

    for g in gossip:

        st.markdown(f"""
        <div class="cute-box">

        {g}

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# TAB 4 GAME
# =========================================================

with tab4:

    st.header("🎮 Flappy Bunny Materials")

    st.markdown("""
    <div class="cute-box">

    🐰 Help the bunny unlock materials!

    Click the button to fly to a random material world ✨

    </div>
    """, unsafe_allow_html=True)

    materiales_game = [

        {
            "material": "Titanium",
            "fun": "Super strong and lightweight",
            "uso": "Aerospace and implants",
            "gossip": "💅 Expensive but iconic."
        },

        {
            "material": "Copper",
            "fun": "Excellent electrical conductor",
            "uso": "Wires and electronics",
            "gossip": "⚡ Literally carrying electricity."
        },

        {
            "material": "Aluminum",
            "fun": "Very lightweight",
            "uso": "Aircraft and vehicles",
            "gossip": "✨ Skinny legend."
        },

        {
            "material": "Steel",
            "fun": "Strong and durable",
            "uso": "Buildings and machines",
            "gossip": "🏗️ Industrial queen."
        }
    ]

    if st.button("🐰 Fly Bunny ✨"):

        st.image(
            "https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif",
            width=250
        )

        with st.spinner("🌸 Bunny flying..."):

            time.sleep(2)

        elegido = random.choice(materiales_game)

        st.success(f"""
        🌸 MATERIAL UNLOCKED 🌸

        💖 {elegido['material']}

        ✨ Fun Fact:
        {elegido['fun']}

        🏭 Used in:
        {elegido['uso']}

        💅 Gossip:
        {elegido['gossip']}
        """)

        st.balloons()

# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="cute-box">

🌸 Material Match AI Magazine 🌸

Made with engineering + pink glitter + chaos 💖

</div>
""", unsafe_allow_html=True)
