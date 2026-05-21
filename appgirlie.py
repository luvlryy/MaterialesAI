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
# CONFIGURACIÓN GENERAL
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
        #fff0f5 50%,
        #e8fff1 100%
    );
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #fff5f8;
    border-right: 3px solid #ffc2d1;
}

/* Título */
h1 {
    text-align: center;
    color: #ff5fa2 !important;
    font-size: 60px !important;
}

/* Subtítulos */
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

/* Caja cute */
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

Selecciona las propiedades mecánicas deseadas y el sistema
encontrará los materiales más compatibles ✨

💖 Matcha vibes + ingeniería de materiales 💖

</div>
""", unsafe_allow_html=True)

# ============================================
# CARGAR EXCEL
# ============================================

try:

    df = pd.read_excel("materiales_sin_aceros.xlsx")

except Exception as e:

    st.error(f"❌ Error al cargar el Excel: {e}")
    st.stop()

# ============================================
# LIMPIAR COLUMNAS
# ============================================

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
    .str.replace("\n", " ")
    .str.replace("  ", " ")
)

# ============================================
# MOSTRAR COLUMNAS
# ============================================

st.write("🌸 Columnas detectadas:")
st.write(df.columns.tolist())

# ============================================
# COLUMNAS NUMÉRICAS
# ============================================

columnas_numericas = [
    "Su",
    "Sy",
    "A5",
    "Bhn",
    "E",
    "G"
]

# ============================================
# VALIDAR COLUMNAS
# ============================================

for col in columnas_numericas:

    if col not in df.columns:

        st.error(f"❌ No se encontró la columna: {col}")
        st.stop()

# ============================================
# CONVERTIR A NUMÉRICO
# ============================================

for col in columnas_numericas:

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

# ============================================
# ELIMINAR NaN
# ============================================

df = df.dropna(subset=columnas_numericas)

# ============================================
# SIDEBAR
# ============================================

st.sidebar.title("🎀 Propiedades deseadas")

# ============================================
# SLIDERS
# ============================================

uts = st.sidebar.slider(
    "💪 Resistencia máxima (Su)",
    int(df["Su"].min()),
    int(df["Su"].max()),
    int(df["Su"].mean())
)

ys = st.sidebar.slider(
    "⚙️ Límite elástico (Sy)",
    int(df["Sy"].min()),
    int(df["Sy"].max()),
    int(df["Sy"].mean())
)

elong = st.sidebar.slider(
    "🌸 Elongación (A5)",
    int(df["A5"].min()),
    int(df["A5"].max()),
    int(df["A5"].mean())
)

hb = st.sidebar.slider(
    "🧁 Dureza Brinell (Bhn)",
    int(df["Bhn"].min()),
    int(df["Bhn"].max()),
    int(df["Bhn"].mean())
)

young = st.sidebar.slider(
    "📏 Módulo de Young (E)",
    int(df["E"].min()),
    int(df["E"].max()),
    int(df["E"].mean())
)

corte = st.sidebar.slider(
    "🐹 Módulo de corte (G)",
    int(df["G"].min()),
    int(df["G"].max()),
    int(df["G"].mean())
)

# ============================================
# TRATAMIENTO
# ============================================

if "Heat treatment" in df.columns:

    tratamientos = sorted(
        df["Heat treatment"]
        .dropna()
        .astype(str)
        .unique()
    )

else:

    tratamientos = ["Todos"]

tratamiento = st.sidebar.selectbox(
    "🔥 Tratamiento térmico",
    ["Todos"] + tratamientos
)

# ============================================
# BOTÓN
# ============================================

buscar = st.sidebar.button(
    "✨ Buscar material ✨"
)

# ============================================
# RECOMENDADOR
# ============================================

if buscar:

    datos = df.copy()

    if (
        tratamiento != "Todos"
        and "Heat treatment" in datos.columns
    ):

        datos = datos[
            datos["Heat treatment"] == tratamiento
        ]

    # ============================================
    # FEATURES
    # ============================================

    features = [
        "Su",
        "Sy",
        "A5",
        "Bhn",
        "E",
        "G"
    ]

    # ============================================
    # NORMALIZAR
    # ============================================

    scaler = MinMaxScaler()

    X = scaler.fit_transform(
        datos[features]
    )

    usuario = scaler.transform([[
        uts,
        ys,
        elong,
        hb,
        young,
        corte
    ]])

    # ============================================
    # DISTANCIAS
    # ============================================

    distancias = euclidean_distances(
        usuario,
        X
    )

    # ============================================
    # TOP 5
    # ============================================

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

    columnas_mostrar = ["Material", "Similitud %"]

    if "Heat treatment" in mejores.columns:

        columnas_mostrar.insert(
            1,
            "Heat treatment"
        )

    st.dataframe(
        mejores[columnas_mostrar],
        use_container_width=True
    )

    # ============================================
    # MEJOR MATERIAL
    # ============================================

    mejor = mejores.iloc[0]

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "🌸 Material",
            str(mejor["Material"])
        )

    with col2:

        st.metric(
            "✨ Similitud",
            f"{mejor['Similitud %']}%"
        )

    with col3:

        if "Heat treatment" in mejor.index:

            st.metric(
                "🔥 Tratamiento",
                str(mejor["Heat treatment"])
            )

    # ============================================
    # APLICACIONES
    # ============================================

    st.header("🧠 Aplicaciones sugeridas")

    def aplicaciones(su, hb, a5):

        if su > 900:

            return """
            💖 Excelente para:
            - Engranes
            - Ejes mecánicos
            - Componentes de alto esfuerzo
            """

        elif a5 > 25:

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
            - Piezas resistentes al desgaste
            """

        else:

            return """
            🎀 Uso general:
            - Componentes mecánicos
            - Soportes
            - Aplicaciones industriales
            """

    st.info(
        aplicaciones(
            mejor["Su"],
            mejor["Bhn"],
            mejor["A5"]
        )
    )

    # ============================================
    # SCATTER PLOT
    # ============================================

    st.header("📊 Comparación de materiales")

    fig = px.scatter(
        mejores,
        x="Bhn",
        y="Su",
        color="Material",
        size="Similitud %",
        hover_data=["Heat treatment"]
        if "Heat treatment" in mejores.columns
        else None,
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
            "Su",
            "Sy",
            "A5",
            "Bhn",
            "E",
            "G"
        ],
        fill='toself',
        name='Deseado'
    ))

    fig2.add_trace(go.Scatterpolar(
        r=[
            mejor["Su"],
            mejor["Sy"],
            mejor["A5"],
            mejor["Bhn"],
            mejor["E"],
            mejor["G"]
        ],
        theta=[
            "Su",
            "Sy",
            "A5",
            "Bhn",
            "E",
            "G"
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
