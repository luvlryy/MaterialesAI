# =========================================================
# 🌐 CYBER MATERIALS 2000 🌐
# Y2K TROPICAL EDITION 🌴
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import random
import plotly.express as px
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import euclidean_distances

# =========================================================
# CONFIGURACIÓN DE PÁGINA
# =========================================================

st.set_page_config(
    page_title="Cyber Materials 2000",
    page_icon="💿",
    layout="wide"
)

# =========================================================
# CARGA DE BASE DE DATOS
# =========================================================

@st.cache_data
def load_data():
    df = pd.read_excel("Data_convertido.xlsx")
    df.columns = df.columns.astype(str).str.strip()
    return df

df = load_data()

columnas_numericas = ["Su", "Sy", "A5", "Bhn", "E", "G"]
for col in columnas_numericas:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df = df.dropna(subset=columnas_numericas)

# =========================================================
# CSS Y2K TROPICAL (Turquesa, Naranja, Rosa)
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Verdana:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Verdana', sans-serif;
}

/* FONDO TROPICAL Y2K */
.stApp {
    background: linear-gradient(135deg, #E0FFFF 0%, #FFE4B5 50%, #FFB6C1 100%);
    background-attachment: fixed;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #40E0D0, #FFA500);
    border-right: 5px dashed #FF69B4;
}

/* TITULO PRINCIPAL */
h1 {
    color: #FF8C00 !important;
    text-align: center;
    font-size: 55px !important;
    font-weight: bold;
    text-shadow: 2px 2px #40E0D0, 4px 4px #FF69B4;
    background: white;
    border: 4px solid #40E0D0;
    border-radius: 15px;
    padding: 15px;
    box-shadow: 5px 5px 0px #FF69B4;
}

/* CAJAS ESTILO WEB 2000s */
.cyber-box {
    background: rgba(255, 255, 255, 0.85);
    border: 3px solid #40E0D0;
    border-radius: 10px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 4px 4px 0px #FFA500;
}

/* TITULOS DE SECCION */
h2, h3 {
    color: #FF69B4 !important;
    text-shadow: 1px 1px white;
}

/* EXPANDERS (CHISMES) */
.streamlit-expanderHeader {
    font-size: 18px !important;
    font-weight: bold !important;
    color: white !important;
    background-color: #FF69B4 !important;
    border: 2px solid #FFA500 !important;
    border-radius: 5px !important;
}

/* TABS */
.stTabs [data-baseweb="tab"] {
    background: white;
    border: 3px solid #40E0D0;
    border-radius: 10px 10px 0px 0px;
    margin-right: 5px;
    padding: 10px;
    font-size: 16px;
    font-weight: bold;
    color: #FF8C00;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.title("🌐 CYBER MATERIALS 2000 🌐")

st.markdown("""
<div class="cyber-box">
<h2 style="text-align:center; color:#40E0D0 !important;">Bienvenido al portal definitivo de materiales</h2>
<p style="text-align:center; font-size:16px;">
Hardware de recomendación | Motor de búsqueda | Archivos clasificados | Simulador de pruebas
</p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# 📸 FOTO 1: IMAGEN GENERAL (Línea ~106)
# Tamaño recomendado: Banner ancho (ej. 800x250 píxeles)
# ---------------------------------------------------------
# st.image("tu_imagen_general.jpg", use_container_width=True)

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "⚙️ Recomendador",
    "🔍 Buscador",
    "🔥 Revista: EL ESCÁNDALO",
    "🕹️ Simulador"
])

# =========================================================
# TAB 1: RECOMENDADOR
# =========================================================

with tab1:
    st.header("⚙️ Motor de Recomendación Algorítmica")
    
    # ---------------------------------------------------------
    # 📸 FOTO 2: IMAGEN RECOMENDADOR (Línea ~127)
    # Tamaño recomendado: Cuadrada o rectangular pequeña (ej. 400x300 píxeles)
    # ---------------------------------------------------------
    # st.image("tu_imagen_recomendador.jpg", width=400)

    st.sidebar.title("Parámetros de Búsqueda")

    uts = st.sidebar.slider("Resistencia máxima (Su)", int(df["Su"].min()), int(df["Su"].max()), int(df["Su"].mean()))
    ys = st.sidebar.slider("Límite elástico (Sy)", int(df["Sy"].min()), int(df["Sy"].max()), int(df["Sy"].mean()))
    elong = st.sidebar.slider("Elongación (A5)", int(df["A5"].min()), int(df["A5"].max()), int(df["A5"].mean()))
    hb = st.sidebar.slider("Dureza (Bhn)", int(df["Bhn"].min()), int(df["Bhn"].max()), int(df["Bhn"].mean()))
    young = st.sidebar.slider("Módulo Young (E)", int(df["E"].min()), int(df["E"].max()), int(df["E"].mean()))
    corte = st.sidebar.slider("Módulo cortante (G)", int(df["G"].min()), int(df["G"].max()), int(df["G"].mean()))

    if st.sidebar.button("Procesar Datos 💿"):
        features = ["Su", "Sy", "A5", "Bhn", "E", "G"]
        scaler = MinMaxScaler()
        X = scaler.fit_transform(df[features])
        usuario = scaler.transform([[uts, ys, elong, hb, young, corte]])
        distancias = euclidean_distances(usuario, X)
        indices = np.argsort(distancias[0])[:5]
        mejores = df.iloc[indices].copy()
        mejores["Match %"] = [round(100 / (1 + d), 2) for d in distancias[0][indices]]

        st.subheader("Resultados del análisis:")
        st.dataframe(mejores[["Material", "Heat treatment", "Match %"]], use_container_width=True)

        fig = px.scatter(mejores, x="Bhn", y="Su", color="Material", size="Match %", text="Material")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(255,255,255,0.5)", height=400)
        st.plotly_chart(fig, use_container_width=True)

# =========================================================
# TAB 2: BUSCADOR ARREGLADO
# =========================================================

with tab2:
    st.header("🔍 Buscador de Materiales")
    
    # ---------------------------------------------------------
    # 📸 FOTO 3: IMAGEN BUSCADOR (Línea ~164)
    # Tamaño recomendado: Estilo banner delgado (ej. 600x150 píxeles)
    # ---------------------------------------------------------
    # st.image("tu_imagen_buscador.jpg", use_container_width=True)

    busqueda = st.text_input("Ingresa el nombre del material, aleación o tratamiento (ej: 1020, Annealed, Q&T):")

    if busqueda:
        # Se elimina el diccionario. Ahora busca coincidencias parciales exactas en toda la base.
        palabra = busqueda.lower().strip()
        
        mask_material = df["Material"].astype(str).str.lower().str.contains(palabra, na=False)
        mask_heat = df["Heat treatment"].astype(str).str.lower().str.contains(palabra, na=False)
        
        resultados = df[mask_material | mask_heat]

        if len(resultados) > 0:
            st.success(f"Sistema: Se encontraron {len(resultados)} coincidencias.")
            
            for i in range(min(10, len(resultados))):
                material = resultados.iloc[i]

                st.markdown(f"""
                <div class="cyber-box">
                <h3 style="color:#FFA500 !important;">{material['Material']}</h3>
                <p><b>Tratamiento:</b> {material['Heat treatment']}</p>
                <p><b>Resistencia (Su):</b> {material['Su']} MPa | <b>Elongación:</b> {material['A5']}% | <b>Dureza:</b> {material['Bhn']} HB</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Error 404: Material no encontrado en la base de datos.")

# =========================================================
# TAB 3: LA REVISTA (PURO CHISME)
# =========================================================

with tab3:
    st.header("🔥 EL ESCÁNDALO DE LA SEMANA 🔥")
    st.write("Exclusivas, secretos y las verdades incómodas de la tabla periódica.")

    # ---------------------------------------------------------
    # 📸 FOTO 4: IMAGEN REVISTA/CHISMES (Línea ~201)
    # Tamaño recomendado: Foto estilo "paparazzi" o portada de revista (ej. 500x500 píxeles)
    # ---------------------------------------------------------
    # st.image("tu_imagen_revista.jpg", width=500)

    with st.expander("😱 EL TRIÁNGULO AMOROSO: Carbono, Hierro y los Tratamientos Térmicos"):
        st.write("""
        **Lo que todos sospechaban pero nadie quería admitir.** Fuentes cercanas al horno industrial nos confirman que el Hierro Base estaba completamente aburrido y sin propósito, 
        hasta que el Carbono entró en escena. La química fue innegable, formaron Acero y juraron lealtad eterna... 
        Pero el drama no terminó ahí. 
        
        Resulta que el *Templado* (Quenching) los sorprendió con un enfriamiento tan brusco que los dejó atrapados en 
        una estructura martensítica, tensos y a punto de colapsar. Tuvieron que llamar de emergencia al *Revenido* (Tempering) 
        para calmar las aguas y devolverles la flexibilidad. ¡Una relación verdaderamente tóxica que solo sobrevive a base de estrés térmico!
        """)

    with st.expander("💸 TITANIO AL DESCUBIERTO: ¿Exclusivo o simplemente un caprichoso sobrevalorado?"):
        st.write("""
        **Nos destaparon la verdad sobre el material más "aesthetic" de la ingeniería.**
        El Titanio se pasea por las alfombras rojas de la industria aeroespacial y médica exigiendo presupuestos millonarios. 
        "Soy biocompatible", "Mi relación resistencia-peso es inigualable", dice en sus entrevistas. 
        
        Pero, ¿qué pasa a puerta cerrada? Mecánicos y torneros afirman que trabajar con él es una pesadilla absoluta. 
        Desgasta las herramientas de corte en tiempo récord y si no lo bañas en refrigerante, hace un berrinche y se arruina la pieza. 
        ¿Es realmente un supermaterial o solo un divo con buena campaña de marketing? El Acero Inoxidable ya dejó de seguirlo en redes.
        """)

    with st.expander("🚨 POLÍMEROS EN CRISIS: El Termoplástico que se derritió bajo presión"):
        st.write("""
        **Un papelón en la línea de ensamblaje.**
        Todo iba de maravilla para el Polietileno de Alta Densidad. Estaba presumiendo su resistencia química y su bajo costo frente 
        a los metales pesados. Sin embargo, testigos presenciales afirman que cuando el ambiente superó los 120°C, el supuesto 
        "material del futuro" perdió por completo la compostura y se volvió una masa inestable. 
        
        Los Termoestables, desde la otra esquina del laboratorio, no paraban de reírse: *"Eso te pasa por no tener enlaces cruzados, cariño"*. 
        ¡El escarnio público fue total!
        """)

# =========================================================
# TAB 4: SIMULADOR (JUEGO NEUTRAL)
# =========================================================

with tab4:
    st.header("🕹️ Simulador de Conocimientos")
    
    # ---------------------------------------------------------
    # 📸 FOTO 5: IMAGEN JUEGO/SIMULADOR (Línea ~240)
    # Tamaño recomendado: Estilo retro gaming o píxel art (ej. 400x300 píxeles)
    # ---------------------------------------------------------
    # st.image("tu_imagen_juego.jpg", width=400)

    preguntas = [
        {
            "pregunta": "Identifica el material: Baja densidad, alta resistencia a la corrosión, utilizado frecuentemente en la industria aeronáutica.",
            "opciones": ["Titanio", "Aluminio", "Plomo"],
            "correcta": "Aluminio",
            "dato": "El aluminio tiene una densidad de aprox. 2.7 g/cm³, ideal para aplicaciones donde el peso es crítico."
        },
        {
            "pregunta": "¿Qué propiedad mecánica evalúa la capacidad de un material para absorber energía y deformarse plásticamente antes de fracturarse?",
            "opciones": ["Tenacidad", "Dureza", "Resiliencia"],
            "correcta": "Tenacidad",
            "dato": "La tenacidad es clave para evitar fallas catastróficas en estructuras bajo impacto."
        },
        {
            "pregunta": "En los aceros, ¿qué tratamiento térmico se utiliza inmediatamente después del temple para reducir la fragilidad?",
            "opciones": ["Recocido", "Revenido", "Normalizado"],
            "correcta": "Revenido",
            "dato": "El revenido (tempering) alivia las tensiones internas dejadas por la formación de martensita durante el temple."
        }
    ]

    if 'pregunta_actual' not in st.session_state:
        st.session_state.pregunta_actual = random.choice(preguntas)

    p = st.session_state.pregunta_actual

    st.markdown(f"""
    <div class="cyber-box">
    <h3 style="color:#40E0D0 !important;">{p['pregunta']}</h3>
    </div>
    """, unsafe_allow_html=True)

    respuesta = st.radio("Selecciona el parámetro correcto:", p["opciones"])

    colA, colB = st.columns(2)
    
    with colA:
        if st.button("Ejecutar Análisis 👾"):
            if respuesta == p["correcta"]:
                st.success(f"✔️ Sistema: Respuesta confirmada.\n\nDatos adicionales: {p['dato']}")
            else:
                st.error(f"❌ Error en el sistema.\n\nParámetro correcto requerido: {p['correcta']}")
    
    with colB:
        if st.button("Cargar nueva secuencia 🔄"):
            st.session_state.pregunta_actual = random.choice(preguntas)
            st.rerun()
