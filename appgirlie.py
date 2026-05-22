# =========================================================
# 🌴 MATERIAL WEB 2007 🌴
# Portal de Ingeniería de Materiales - Tropical Edition
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import random
import plotly.express as px

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import euclidean_distances

# =========================================================
# CONFIGURACIÓN
# =========================================================

st.set_page_config(
    page_title="Material Web 2007",
    page_icon="🌴",
    layout="wide"
)

# =========================================================
# CARGAR BASE DE DATOS
# =========================================================

@st.cache_data
def load_data():
    df = pd.read_excel("Data_convertido.xlsx")
    df.columns = df.columns.astype(str).str.strip()
    return df

df = load_data()

# =========================================================
# COLUMNAS NUMÉRICAS
# =========================================================

columnas_numericas = ["Su", "Sy", "A5", "Bhn", "E", "G"]

for col in columnas_numericas:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=columnas_numericas)

# =========================================================
# CSS ESTILO WEB 2.0 TROPICAL (2007)
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Tahoma:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Tahoma', 'Verdana', sans-serif;
}

/* FONDO TROPICAL 2007 */
.stApp {
    background: linear-gradient(135deg, #00CED1 0%, #FF1493 50%, #FFA500 100%);
    background-attachment: fixed;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.9);
    border-right: 4px solid #FF8C00;
}

/* TÍTULO PRINCIPAL */
h1 {
    color: #FFFFFF !important;
    text-align: center;
    font-size: 55px !important;
    text-shadow: 2px 2px 4px #FF1493, -2px -2px 4px #00CED1;
    background: rgba(0, 0, 0, 0.3);
    border: 4px solid #FFFFFF;
    border-radius: 15px;
    padding: 15px;
    margin-bottom: 20px;
}

/* CAJAS WEB 2.0 */
.web20-box {
    background: rgba(255, 255, 255, 0.9);
    border: 2px solid #00CED1;
    border-radius: 15px;
    padding: 20px;
    margin-bottom: 20px;
    box-shadow: 4px 4px 10px rgba(0,0,0,0.2);
    color: #333;
}

/* CAJAS DE CHISMES */
.gossip-box {
    background: linear-gradient(to right, #FFF0F5, #FFE4E1);
    border-left: 8px solid #FF1493;
    border-radius: 10px;
    padding: 15px;
    margin-bottom: 20px;
    box-shadow: 3px 3px 8px rgba(0,0,0,0.15);
}

.gossip-title {
    color: #FF1493;
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 10px;
    text-transform: uppercase;
}

/* TABS */
.stTabs [data-baseweb="tab"] {
    background: rgba(255, 255, 255, 0.8);
    border-radius: 10px 10px 0px 0px;
    border: 2px solid #FF8C00;
    margin-right: 5px;
    padding: 10px;
    font-weight: bold;
    color: #00CED1;
}

.stTabs [aria-selected="true"] {
    background: #FFFFFF;
    border-bottom: none;
    color: #FF1493;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER Y BANNER GENERAL
# =========================================================

st.title("🌐 MATERIAL ZONE '07 🌐")

# 📸 FOTO GENERAL AQUÍ (Tamaño: 1200 x 400 px aprox)
# Reemplaza "ruta_de_tu_banner.jpg" por el nombre de tu archivo
# st.image("ruta_de_tu_banner.jpg", use_column_width=True)

st.markdown("""
<div class="web20-box" style="text-align: center;">
<h3 style="color: #FF8C00;">Bienvenido a la red de materiales más grande de la web</h3>
<p>Explora la base de datos, encuentra materiales según sus propiedades mecánicas, 
y entérate de los últimos escándalos de la industria metalúrgica.</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "🛠️ Sistema de Recomendación",
    "🔍 Buscador de Materiales",
    "🔥 ESCÁNDALO DE LA SEMANA",
    "🕹️ Pop Quiz"
])

# =========================================================
# TAB 1: RECOMENDADOR
# =========================================================

with tab1:
    st.header("🛠️ Motor de Búsqueda por Propiedades")
    st.sidebar.title("⚙️ Parámetros")

    uts = st.sidebar.slider("Resistencia máxima (Su)", int(df["Su"].min()), int(df["Su"].max()), int(df["Su"].mean()))
    ys = st.sidebar.slider("Límite elástico (Sy)", int(df["Sy"].min()), int(df["Sy"].max()), int(df["Sy"].mean()))
    elong = st.sidebar.slider("Elongación (A5)", int(df["A5"].min()), int(df["A5"].max()), int(df["A5"].mean()))
    hb = st.sidebar.slider("Dureza (Bhn)", int(df["Bhn"].min()), int(df["Bhn"].max()), int(df["Bhn"].mean()))
    young = st.sidebar.slider("Módulo Young (E)", int(df["E"].min()), int(df["E"].max()), int(df["E"].mean()))
    corte = st.sidebar.slider("Módulo cortante (G)", int(df["G"].min()), int(df["G"].max()), int(df["G"].mean()))

    if st.sidebar.button("Buscar coincidencias"):
        features = ["Su", "Sy", "A5", "Bhn", "E", "G"]
        scaler = MinMaxScaler()
        X = scaler.fit_transform(df[features])
        usuario = scaler.transform([[uts, ys, elong, hb, young, corte]])
        distancias = euclidean_distances(usuario, X)
        indices = np.argsort(distancias[0])[:5]
        mejores = df.iloc[indices].copy()
        mejores["Compatibilidad %"] = [round(100 / (1 + d), 2) for d in distancias[0][indices]]

        st.markdown('<div class="web20-box">', unsafe_allow_html=True)
        st.subheader("Resultados de Similitud")
        st.dataframe(mejores[["Material", "Heat treatment", "Compatibilidad %"]], use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        fig = px.scatter(mejores, x="Bhn", y="Su", color="Material", size="Compatibilidad %", text="Material")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(255,255,255,0.8)", height=500)
        st.plotly_chart(fig, use_container_width=True)

# =========================================================
# TAB 2: BUSCADOR (CORREGIDO)
# =========================================================

with tab2:
    st.header("🔍 Buscador de Base de Datos")
    st.markdown('<div class="web20-box"><p>Ingresa una palabra clave o parte del nombre del material.</p></div>', unsafe_allow_html=True)
    
    busqueda = st.text_input("Palabra clave:")

    if busqueda:
        # Busca coincidencias exactas o parciales, ignorando mayúsculas/minúsculas
        mask = df["Material"].astype(str).str.contains(busqueda, case=False, na=False)
        resultados = df[mask]

        if len(resultados) > 0:
            st.success(f"Se encontraron {len(resultados)} coincidencias.")
            
            for i in range(min(5, len(resultados))):
                material = resultados.iloc[i]
                
                col_texto, col_foto = st.columns([2, 1])
                
                with col_texto:
                    st.markdown(f"""
                    <div class="web20-box">
                    <h3 style="color:#00CED1;">{material['Material']}</h3>
                    <ul>
                        <li><b>Tratamiento Térmico:</b> {material['Heat treatment']}</li>
                        <li><b>Resistencia (Su):</b> {material['Su']} MPa</li>
                        <li><b>Elongación (A5):</b> {material['A5']}%</li>
                        <li><b>Dureza (Bhn):</b> {material['Bhn']} HB</li>
                    </ul>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col_foto:
                    # 📸 FOTO PARA EL BUSCADOR AQUÍ (Tamaño: 400 x 300 px aprox)
                    # st.image("foto_resultado.jpg", caption=material['Material'])
                    st.info("Espacio para foto del material (400x300)")

        else:
            st.error("No se encontraron coincidencias en la base de datos.")

# =========================================================
# TAB 3: ESCÁNDALO DE LA SEMANA (LOS 10 CHISMES PICANTES)
# =========================================================

with tab3:
    st.header("🔥 EL ESCÁNDALO DE LA SEMANA 🔥")
    st.write("Exclusivas, toxicidad y traiciones en la tabla periódica y la industria.")

    chismes = [
        {
            "titulo": "¡EL BLOQUEO! EL ACERO INOXIDABLE Y LA CORROSIÓN NO SE HABLAN",
            "texto": "Me enteré que el Inoxidable bloqueó definitivamente a la Corrosión. Gracias a su capa pasiva de óxido de cromo (mínimo 10.5%), literalmente se volvió intocable. La Corrosión intentó acercarse en un ambiente marino, pero fue totalmente ignorada. ¡Soporta!",
            "foto_placeholder": "foto_chisme_1.jpg"
        },
        {
            "titulo": "EL TITANIO: ¿SUGAR DADDY O MATERIAL SOBREVALORADO?",
            "texto": "Todos sabemos que el Titanio es carísimo. Su biocompatibilidad lo hace el VIP de los implantes médicos, pero los ingenieros mecánicos se quejan en secreto de que es una pesadilla maquinarlo. ¿Vale la pena su ratio resistencia-peso o es pura vanidad presupuestal?",
            "foto_placeholder": "foto_chisme_2.jpg"
        },
        {
            "titulo": "CANCELADO: EL PLOMO QUEDA FUERA DE LA INDUSTRIA",
            "texto": "¡Se acabó su carrera! El Plomo, que alguna vez fue la estrella de las pinturas y gasolinas, ha sido 'cancelado' globalmente. Su toxicidad salió a la luz y su peso excesivo ya no justifica su presencia. Nadie quiere asociarse con él.",
            "foto_placeholder": "foto_chisme_3.jpg"
        },
        {
            "titulo": "EL COBRE Y SUS CONEXIONES... CON TODOS",
            "texto": "Fuentes cercanas confirman que el Cobre sigue siendo el más solicitado a altas horas de la noche para conducir corrientes. Aunque la Plata conduce mejor, es demasiado exclusiva. El Cobre no discrimina: está en todos los cables, en todas las casas.",
            "foto_placeholder": "foto_chisme_4.jpg"
        },
        {
            "titulo": "PELEA EN LA BÁSCULA: ALUMINIO HUMILLA AL ACERO",
            "texto": "¡Las comparaciones destruyen! El Aluminio anda publicando que su densidad es casi un tercio de la del Acero. Y aunque no aguanta tantos golpes, la industria aeroespacial lo coronó como su favorito. El Acero se quedó llorando en la industria automotriz.",
            "foto_placeholder": "foto_chisme_5.jpg"
        },
        {
            "titulo": "LA DOBLE VIDA DEL MERCURIO",
            "texto": "Es el único metal que se niega a madurar y solidificarse a temperatura ambiente. El Mercurio es líquido, volátil y sumamente tóxico. Se la pasa engañando a los termómetros antiguos, pero hoy en día está más que prohibido en los laboratorios modernos.",
            "foto_placeholder": "foto_chisme_6.jpg"
        },
        {
            "titulo": "DIAMANTE: LA FALSA EXCLUSIVIDAD AL DESCUBIERTO",
            "texto": "Se vende como el material más duro e invaluable, pero los ingenieros revelaron la verdad: los diamantes sintéticos hacen el mismo trabajo en las herramientas de corte y por una fracción del precio. Su marketing es excelente, pero estructuralmente, está sobrevalorado.",
            "foto_placeholder": "foto_chisme_7.jpg"
        },
        {
            "titulo": "EL OSCURO SECRETO DEL HORMIGÓN",
            "texto": "Parece fuerte y confiable, sostiene nuestras ciudades, pero su huella de carbono es escandalosa. La producción de cemento para el hormigón es responsable de casi el 8% de las emisiones globales. ¿Dejará la industria de encubrirlo?",
            "foto_placeholder": "foto_chisme_8.jpg"
        },
        {
            "titulo": "ORO: INTOCABLE PERO DEMASIADO SUAVE",
            "texto": "Mucha corona, mucha resistencia a la oxidación, pero a la hora de trabajar bajo presión, el Oro se deforma. Es tan blando que necesita mezclarse con otros metales (como el cobre) para poder usarse en joyería sin abollarse con mirarlo. Pura fachada.",
            "foto_placeholder": "foto_chisme_9.jpg"
        },
        {
            "titulo": "LOS POLÍMEROS: LOS EX QUE SE NIEGAN A DESAPARECER",
            "texto": "Terminaste con ellos, los tiraste a la basura, ¡pero los plásticos tardan cientos de años en degradarse! Prometieron ser la solución barata y ligera para los envases, y terminaron invadiendo los océanos. El nivel de apego tóxico es irreal.",
            "foto_placeholder": "foto_chisme_10.jpg"
        }
    ]

    for c in chismes:
        colA, colB = st.columns([1, 3])
        
        with colA:
            # 📸 FOTO PARA CHISMES AQUÍ (Tamaño: 300 x 300 px aprox)
            # st.image(c["foto_placeholder"])
            st.info(f"Foto aquí: {c['foto_placeholder']} (300x300)")
            
        with colB:
            st.markdown(f"""
            <div class="gossip-box">
            <div class="gossip-title">{c['titulo']}</div>
            <p>{c['texto']}</p>
            </div>
            """, unsafe_allow_html=True)

# =========================================================
# TAB 4: POP QUIZ
# =========================================================

with tab4:
    st.header("🕹️ Centro de Evaluación (Pop Quiz)")
    st.markdown('<div class="web20-box">Demuestra tus conocimientos técnicos.</div>', unsafe_allow_html=True)
    
    preguntas = [
        {"q": "¿Qué material es famoso por ser ligero y dominar la industria aeroespacial?", "op": ["Titanio", "Aluminio", "Plomo"], "ans": "Aluminio"},
        {"q": "¿Cuál es la aleación principal que forma el Acero?", "op": ["Hierro + Carbono", "Cobre + Estaño", "Aluminio + Cobre"], "ans": "Hierro + Carbono"},
        {"q": "¿Qué metal líquido a temperatura ambiente fue prohibido por tóxico?", "op": ["Mercurio", "Galio", "Bromo"], "ans": "Mercurio"},
        {"q": "Si necesitas excelente conductividad eléctrica a bajo costo, usas:", "op": ["Plata", "Cobre", "Oro"], "ans": "Cobre"},
        {"q": "¿Qué propiedad define la capacidad de un material de rayar a otro?", "op": ["Tenacidad", "Dureza", "Ductilidad"], "ans": "Dureza"}
    ]

    if 'quiz_q' not in st.session_state:
        st.session_state.quiz_q = random.choice(preguntas)

    p = st.session_state.quiz_q

    st.markdown(f"<h3 style='color:#FF1493;'>{p['q']}</h3>", unsafe_allow_html=True)
    respuesta = st.radio("Selecciona tu respuesta:", p["op"])

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Verificar Respuesta"):
            if respuesta == p["ans"]:
                st.success("¡Correcto! Respuesta exacta.")
            else:
                st.error(f"Incorrecto. La respuesta era: {p['ans']}")
    with col2:
        if st.button("Siguiente Pregunta"):
            st.session_state.quiz_q = random.choice(preguntas)
            st.rerun()
