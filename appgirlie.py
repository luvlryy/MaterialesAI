# ============================================
# 🌸 MATERIAL MATCH AI 🌸
# Pinky Matcha Latte Edition 🐰🎀
# ============================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import euclidean_distances

# ============================================
# CONFIGURACIÓN
# ============================================

st.set_page_config(
    page_title="Material Match AI 🌸",
    page_icon="🐰",
    layout="wide"
)

# ============================================
# CSS GIRLIE 🌸
# ============================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Quicksand', sans-serif;
}

/* Fondo */
.stApp {
    background: linear-gradient(
        135deg,
        #ffe4ec 0%,
        #fff0f5 40%,
        #e8fff1 100%
    );
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #fff5f8;
    border-right: 3px solid #ffc2d1;
}

/* Títulos */
h1 {
    text-align: center;
    color: #ff5fa2 !important;
    font-size: 60px !important;
}

h2, h3 {
    color: #ff85b3 !important;
}

/* Cards */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.75);
    border: 2px solid #ffc2d1;
    border-radius: 20px;
    padding: 15px;
    box-shadow: 0px 5px 15px rgba(255,182,193,0.4);
}

/* Botones */
.stButton>button {
    background: linear-gradient(
        90deg,
        #ff8fab,
        #ffb3c6
    );

    color: white;
    border: none;
    border-radius: 15px;
    height: 3em;
    font-size: 18px;
    font-weight: bold;
}

.stButton>button:hover {
    background: linear-gradient(
        90deg,
        #ff5fa2,
        #ff8fab
    );
}

/* Cute box */
.cute-box {
    background: rgba(255,255,255,0.7);
    border: 2px dashed #ffb3c6;
    border-radius: 20px;
    padding: 20px;
    margin-bottom: 20px;
}

/* Dataframe */
.stDataFrame {
    border-radius: 20px;
    overflow: hidden;
}

</style>
""", unsafe_allow_html=True)

# ============================================
# TÍTULO
# ============================================

st.title("🌸 Material Match AI 🌸")

st.markdown("""
<div class="cute-box">

### 🐰 Bienvenida al laboratorio más cute de materiales 🎀

Selecciona las propiedades mecánicas que deseas y el sistema encontrará
los materiales más compatibles de la base de datos ✨

💖 Matcha vibes + ingeniería de materiales 💖

</div>
""", unsafe_allow_html=True)

# ============================================
# CARGAR BASE DE DATOS
# ============================================

# ⚠️ CAMBIA ESTE NOMBRE
# por el nombre de tu archivo

df = pd.read_excel("materiales_sin_aceros.xlsx")

# ============================================
# LIMPIEZA
# ============================================

columnas_numericas = [
    "Resistencia a la tracción máxima",
    "Limite elástico",
    "Elongación",
    "Dureza de Brinell",
    "Módulo de young",
    "Módulo de corte"
]

for col in columnas_numericas:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df = df.dropna()

# ============================================
# SIDEBAR
# ============================================

st.sidebar.title("🎀 Propiedades deseadas")

uts = st.sidebar.slider(
    "💪 Resistencia máxima",
    int(df["Resistencia a la tracción máxima"].min()),
    int(df["Resistencia a la tracción máxima"].max()),
    int(df["Resistencia a la tracción máxima"].mean())
)

ys = st.sidebar.slider(
    "⚙️ Límite elástico",
    int(df["Limite elástico"].min()),
    int(df["Limite elástico"].max()),
    int(df["Limite elástico"].mean())
)

elong = st.sidebar.slider(
    "🌸 Elongación",
    int(df["Elongación"].min()),
    int(df["Elongación"].max()),
    int(df["Elongación"].mean())
)

hb = st.sidebar.slider(
    "🧁 Dureza Brinell",
    int(df["Dureza de Brinell"].min()),
    int(df["Dureza de Brinell"].max()),
    int(df["Dureza de Brinell"].mean())
)

young = st.sidebar.slider(
    "📏 Módulo de Young",
    int(df["Módulo de young"].min()),
    int(df["Módulo de young"].max()),
    int(df["Módulo de young"].mean())
)

corte = st.sidebar.slider(
    "🐹 Módulo de corte",
    int(df["Módulo de corte"].min()),
    int(df["Módulo de corte"].max()),
    int(df["Módulo de corte"].mean())
)

tratamiento = st.sidebar.selectbox(
    "🔥 Tratamiento térmico",
    ["Todos"] + sorted(
        df["Tratamiento térmico"].unique()
    )
)

buscar = st.sidebar.button("✨ Buscar material ✨")

# ============================================
# RECOMENDADOR
# ============================================

if buscar:

    datos = df.copy()

    if tratamiento != "Todos":
        datos = datos[
            datos["Tratamiento térmico"] == tratamiento
        ]

    features = [
        "Resistencia a la tracción máxima",
        "Limite elástico",
        "Elongación",
        "Dureza de Brinell",
        "Módulo de young",
        "Módulo de corte"
    ]

    scaler = MinMaxScaler()

    X = scaler.fit_transform(datos[features])

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

    mejores = datos.iloc[indices].copy()

    mejores["Similitud %"] = [
        round(100 / (1 + d), 2)
        for d in distancias[0][indices]
    ]

    # ============================================
    # RESULTADOS
    # ============================================

    st.header("🎀 Materiales recomendados")

    st.dataframe(
        mejores[[
            "Material",
            "Tratamiento térmico",
            "Similitud %"
        ]],
        use_container_width=True
    )

    mejor = mejores.iloc[0]

    # ============================================
    # MÉTRICAS
    # ============================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "🌸 Material",
            mejor["Material"]
        )

    with col2:
        st.metric(
            "✨ Similitud",
            f"{mejor['Similitud %']}%"
        )

    with col3:
        st.metric(
            "🔥 Tratamiento",
            mejor["Tratamiento térmico"]
        )

    # ============================================
    # APLICACIONES
    # ============================================

    st.header("🧠 Aplicaciones sugeridas")

    def aplicaciones(uts, hb, elong):

        if uts > 900:
            return """
            💖 Excelente para:
            - Engranes
            - Ejes mecánicos
            - Componentes de alto esfuerzo
            """

        elif elong > 25:
            return """
            🌸 Ideal para:
            - Estructuras soldables
            - Componentes deformables
            - Láminas metálicas
            """

        elif hb > 250:
            return """
            🐰 Recomendado para:
            - Herramientas
            - Partes resistentes al desgaste
            - Aplicaciones industriales
            """

        else:
            return """
            🎀 Uso general:
            - Componentes mecánicos
            - Soportes estructurales
            - Aplicaciones industriales básicas
            """

    st.info(
        aplicaciones(
            mejor["Resistencia a la tracción máxima"],
            mejor["Dureza de Brinell"],
            mejor["Elongación"]
        )
    )

    # ============================================
    # SCATTER PLOT
    # ============================================

    st.header("📊 Comparación de materiales")

    fig = px.scatter(
        mejores,
        x="Dureza de Brinell",
        y="Resistencia a la tracción máxima",
        color="Material",
        size="Similitud %",
        hover_data=["Tratamiento térmico"],
        template="plotly_white"
    )

    fig.update_layout(
        paper_bgcolor="#fff0f5",
        plot_bgcolor="#fffafc"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # ============================================
    # RADAR CHART
    # ============================================

    st.header("🌸 Comparación visual")

    fig2 = go.Figure()

    fig2.add_trace(go.Scatterpolar(
        r=[
            uts,
            ys,
            elong,
            hb,
            young,
            corte
        ],
        theta=[
            "UTS",
            "YS",
            "Elong",
            "HB",
            "Young",
            "Corte"
        ],
        fill='toself',
        name='Deseado'
    ))

    fig2.add_trace(go.Scatterpolar(
        r=[
            mejor["Resistencia a la tracción máxima"],
            mejor["Limite elástico"],
            mejor["Elongación"],
            mejor["Dureza de Brinell"],
            mejor["Módulo de young"],
            mejor["Módulo de corte"]
        ],
        theta=[
            "UTS",
            "YS",
            "Elong",
            "HB",
            "Young",
            "Corte"
        ],
        fill='toself',
        name='Material'
    ))

    fig2.update_layout(
        paper_bgcolor="#fff0f5",
        polar=dict(
            bgcolor="#fffafc"
        )
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    # ============================================
    # DATASET
    # ============================================

    st.header("📋 Base de datos")

    st.dataframe(
        df,
        use_container_width=True
    )