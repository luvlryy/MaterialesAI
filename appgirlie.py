# =========================================================
# MATERIAL WORLD - 2007 TROPICAL EDITION 🌴💿
# Interfaz Y2K / Blog de Ingeniería
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
    page_title="Material World 2007",
    page_icon="🌴",
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

try:
    df = load_data()
except Exception as e:
    st.error(f"Error al cargar la base de datos: {e}")
    st.stop()

columnas_numericas = ["Su", "Sy", "A5", "Bhn", "E", "G"]

for col in columnas_numericas:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=columnas_numericas)

# =========================================================
# ESTILO Y2K TROPICAL 2007 (CSS)
# =========================================================

st.markdown("""
<style>
/* Importar tipografía retro (Verdana/Tahoma vibes) */
@import url('https://fonts.googleapis.com/css2?family=VT323&family=Work+Sans:wght@400;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Work Sans', sans-serif;
}

/* FONDO TROPICAL 2007 */
.stApp {
    background: linear-gradient(135deg, #00CED1 0%, #40E0D0 25%, #FFA500 70%, #FF69B4 100%);
    background-attachment: fixed;
}

/* BARRA LATERAL */
section[data-testid="stSidebar"] {
    background: rgba(255, 255, 255, 0.85);
    border-right: 5px dashed #FF8C00;
}

/* TÍTULO PRINCIPAL */
h1 {
    font-family: 'VT323', monospace;
    color: #FFFFFF !important;
    text-align: center;
    font-size: 70px !important;
    text-shadow: 4px 4px #FF69B4, -4px -4px #00CED1;
    background: rgba(0, 0, 0, 0.2);
    border: 4px solid #FFA500;
    border-radius: 0px;
    padding: 15px;
    box-shadow: 10px 10px 0px #FF1493;
    letter-spacing: 2px;
}

/* CAJAS DE CONTENIDO (ESTILO BLOG ANTIGUO) */
.retro-box {
    background: rgba(255, 255, 255, 0.95);
    border: 3px solid #00CED1;
    border-top: 15px solid #FF8C00;
    padding: 20px;
    margin-bottom: 25px;
    box-shadow: 5px 5px 15px rgba(0,0,0,0.2);
    color: #333;
}

/* SUBTÍTULOS */
h2, h3 {
    color: #FF8C00 !important;
    text-transform: uppercase;
    font-weight: bold;
    border-bottom: 2px dotted #00CED1;
    padding-bottom: 5px;
}

/* TABS */
.stTabs [data-baseweb="tab"] {
    background: #00CED1;
    border: 2px solid #FFFFFF;
    margin-right: 5px;
    padding: 10px 20px;
    font-family: 'VT323', monospace;
    font-size: 24px;
    color: #FFFFFF !important;
    text-shadow: 1px 1px #333;
}
.stTabs [aria-selected="true"] {
    background: #FF8C00 !important;
    border-bottom: none;
}

/* BOTONES */
.stButton>button {
    background: #FF69B4;
    color: white;
    border: 2px solid #FFFFFF;
    font-family: 'VT323', monospace;
    font-size: 24px;
    width: 100%;
    box-shadow: 3px 3px 0px #00CED1;
    transition: 0.1s;
}
.stButton>button:active {
    box-shadow: 0px 0px 0px;
    transform: translateY(3px) translateX(3px);
}

/* EXPANDERS (CHISMES) */
.streamlit-expanderHeader {
    font-weight: bold !important;
    font-size: 18px !important;
    color: #FFFFFF !important;
    background-color: #FF1493 !important;
    border: 2px solid #FFA500 !important;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.title("🌴 MATERIAL WORLD // 2007 🌴")

st.markdown("""
<div class="retro-box">
<p style="text-align:center; font-size:18px; font-weight:bold;">
Bienvenido al portal definitivo de ciencia de materiales.<br>
[Buscador de Aleaciones] | [Calculadora de Propiedades] | [Blog de Noticias] | [Foro]
</p>
</div>
""", unsafe_allow_html=True)

# LÍNEA 149 - IMAGEN PRINCIPAL (TAMAÑO RECOMENDADO: 1200 x 300)
st.image("https://via.placeholder.com/1200x300/40E0D0/FFFFFF?text=Tu+Banner+Principal+Aqui+(1200x300)", use_container_width=True)

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "⚙️ Recomendador",
    "🔍 Buscador",
    "📰 EL ESCÁNDALO DE LA SEMANA",
    "🕹️ Quiz Zone"
])

# =========================================================
# TAB 1: RECOMENDADOR
# =========================================================

with tab1:
    st.header("Análisis de Propiedades")
    st.sidebar.title("Parámetros de Entrada")

    uts = st.sidebar.slider("Resistencia máxima (Su)", int(df["Su"].min()), int(df["Su"].max()), int(df["Su"].mean()))
    ys = st.sidebar.slider("Límite elástico (Sy)", int(df["Sy"].min()), int(df["Sy"].max()), int(df["Sy"].mean()))
    elong = st.sidebar.slider("Elongación (A5)", int(df["A5"].min()), int(df["A5"].max()), int(df["A5"].mean()))
    hb = st.sidebar.slider("Dureza (Bhn)", int(df["Bhn"].min()), int(df["Bhn"].max()), int(df["Bhn"].mean()))
    young = st.sidebar.slider("Módulo Young (E)", int(df["E"].min()), int(df["E"].max()), int(df["E"].mean()))
    corte = st.sidebar.slider("Módulo cortante (G)", int(df["G"].min()), int(df["G"].max()), int(df["G"].mean()))

    if st.sidebar.button("Ejecutar Análisis"):
        features = ["Su", "Sy", "A5", "Bhn", "E", "G"]
        scaler = MinMaxScaler()
        X = scaler.fit_transform(df[features])
        usuario = scaler.transform([[uts, ys, elong, hb, young, corte]])
        distancias = euclidean_distances(usuario, X)
        indices = np.argsort(distancias[0])[:5]
        mejores = df.iloc[indices].copy()
        mejores["Match %"] = [round(100 / (1 + d), 2) for d in distancias[0][indices]]

        st.subheader("Resultados del algoritmo")
        st.dataframe(mejores[["Material", "Heat treatment", "Match %"]], use_container_width=True)

        fig = px.scatter(mejores, x="Bhn", y="Su", color="Material", size="Match %", text="Material")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(255,255,255,0.8)", height=500)
        st.plotly_chart(fig, use_container_width=True)

# =========================================================
# TAB 2: BUSCADOR (CORREGIDO)
# =========================================================

with tab2:
    st.header("Buscador de Base de Datos")
    
    st.markdown("""
    <div class="retro-box">
    Ingresa cualquier término (nombre del material, tratamiento térmico, o número) para buscar en nuestra base.
    </div>
    """, unsafe_allow_html=True)
    
    busqueda = st.text_input("Buscar material:")

    if busqueda:
        # Buscador 100% efectivo: busca el texto en cualquier columna, sin importar mayúsculas/minúsculas
        mask = np.column_stack([df[col].astype(str).str.contains(busqueda, case=False, na=False) for col in df.columns])
        resultados = df.loc[mask.any(axis=1)]

        if len(resultados) > 0:
            st.success(f"Búsqueda finalizada. {len(resultados)} coincidencias encontradas.")
            
            for i in range(min(10, len(resultados))):
                material = resultados.iloc[i]
                
                st.markdown(f"""
                <div class="retro-box" style="border-top: 5px solid #00CED1;">
                <h3>{material['Material']}</h3>
                <p><b>Tratamiento:</b> {material['Heat treatment']}</p>
                <p><b>Resistencia (Su):</b> {material['Su']} MPa | <b>Dureza:</b> {material['Bhn']} HB</p>
                <p><b>Elongación:</b> {material['A5']}%</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error("Error 404: Material no encontrado en la base de datos.")

# =========================================================
# TAB 3: EL ESCÁNDALO DE LA SEMANA (VLOG)
# =========================================================

with tab3:
    st.header("📰 EL ESCÁNDALO DE LA SEMANA")
    st.write("Exclusivas, traiciones químicas y el lado oscuro de la tabla periódica.")

    # CHISME 1
    with st.expander("🚨 1. EL ACERO INOXIDABLE Y LA CORROSIÓN: LA RUPTURA DEL AÑO"):
        # LÍNEA 252 - TAMAÑO: 600x400
        st.image("https://via.placeholder.com/600x400/FF69B4/FFFFFF?text=Foto+Acero+vs+Corrosion", use_container_width=False)
        st.write("""
        ¡Agárrense fuerte! Se les vio en un ambiente marino y la tensión se podía cortar con un cuchillo. 
        Durante décadas, el Hierro y la Corrosión fueron tóxicos pero inseparables (literalmente se oxidaban juntos todo el día). 
        Pero desde que el Hierro se juntó con el Cromo (mínimo un 10.5%, ya saben cómo es de exigente), formó su famosa capa pasiva 
        y ahora actúa como si no conociera a la Corrosión. Intentaron acercarse la semana pasada en una plataforma petrolera, 
        y el Acero Inoxidable ni siquiera parpadeó. ¡El mayor bloqueo en la historia de la metalurgia!
        """)

    # CHISME 2
    with st.expander("🚨 2. ROBO DE IDENTIDAD: EL BRONCE DEMANDA AL LATÓN"):
        # LÍNEA 263 - TAMAÑO: 600x400
        st.image("https://via.placeholder.com/600x400/FFA500/FFFFFF?text=Foto+Bronce+Latón", use_container_width=False)
        st.write("""
        Las aleaciones de Cobre están en los tribunales. El Bronce (Cobre + Estaño) salió a dar declaraciones fortísimas 
        acusando al Latón (Cobre + Zinc) de robarle su estética dorada para colarse en aplicaciones arquitectónicas y de plomería 
        donde no pertenece. "Yo soy el material de la historia, a mí me hicieron una edad entera (La Edad de Bronce). 
        El Latón es solo una aleación barata que se hace pasar por mí en las cerraduras de las puertas", declaró el Bronce furioso. 
        El Latón se defendió diciendo que al menos él es más fácil de maquinar. ¡Zafarrancho!
        """)

    # CHISME 3
    with st.expander("🚨 3. EL GLOW UP DEL ALUMINIO: DE PATITO FEO A CHICO AEROESPACIAL"):
        # LÍNEA 275 - TAMAÑO: 600x400
        st.image("https://via.placeholder.com/600x400/00CED1/FFFFFF?text=Foto+GlowUp+Aluminio", use_container_width=False)
        st.write("""
        Recordemos los 1800s, cuando el Aluminio era más caro que el oro y nadie sabía qué hacer con él. 
        Hoy, gracias al proceso Hall-Héroult, el Aluminio es el rey de la pista. Su reciente pérdida de densidad 
        (pesando un tercio de lo que pesa el acero) lo llevó directo a firmar contratos millonarios con Boeing y Airbus. 
        Fuentes aseguran que el Acero está furioso, llorando en el gimnasio tratando de bajar su densidad, 
        mientras el Aluminio simplemente pasea por los cielos tomando mimosas.
        """)

    # CHISME 4
    with st.expander("🚨 4. TITANIO: ¿EL MATERIAL MÁS SOBREVALORADO DE LA DÉCADA?"):
        # LÍNEA 287 - TAMAÑO: 600x400
        st.image("https://via.placeholder.com/600x400/FF1493/FFFFFF?text=Foto+Diva+Titanio", use_container_width=False)
        st.write("""
        Todos quieren trabajar con él, pero nadie lo soporta. El Titanio exige temperaturas de fusión ridículas, 
        arruina las herramientas de corte en los talleres por su bajo módulo de elasticidad y encima cobra carísimo. 
        Sí, es biocompatible y los implantes médicos lo aman, pero los ingenieros de manufactura confesaron en un foro anónimo: 
        "Es un dolor de cabeza. Se cree indispensable solo porque tiene una relación resistencia-peso increíble". 
        ¿Acaso estamos aguantando actitudes tóxicas solo por sus propiedades mecánicas? Sí, probablemente.
        """)

    # CHISME 5
    with st.expander("🚨 5. LA CAÍDA EN DESGRACIA DEL PLOMO"):
        # LÍNEA 298 - TAMAÑO: 600x400
        st.image("https://via.placeholder.com/600x400/40E0D0/FFFFFF?text=Foto+Cancelacion+Plomo", use_container_width=False)
        st.write("""
        De ser el invitado de honor en tuberías romanas, pinturas renacentistas y hasta en la gasolina, el Plomo hoy 
        está más cancelado que nadie. La revelación de que es neurotóxico destruyó su carrera por completo. 
        Hoy en día solo se le ve en aplicaciones súper marginadas, escondido dentro de baterías de autos o como escudo 
        contra radiación en hospitales (donde literalmente nadie quiere acercarse a él). Un final trágico para un material 
        tan maleable.
        """)

    # CHISME 6
    with st.expander("🚨 6. TUNGSTENO: EL CORAZÓN MÁS FRÍO DEL BARRIO"):
        # LÍNEA 310 - TAMAÑO: 600x400
        st.image("https://via.placeholder.com/600x400/FFA500/FFFFFF?text=Foto+Tungsteno", use_container_width=False)
        st.write("""
        ¡Nadie puede derretir el corazón del Tungsteno! Con el punto de fusión más alto de todos los metales (más de 3,400 °C), 
        este tipo se ríe en la cara de los hornos industriales. Hace poco lo invitaron a una fiesta de aleaciones ligeras 
        y arruinó el ambiente porque no quiso interactuar termodinámicamente con nadie. Ahora solo se junta con el carbono 
        para formar Carburo de Tungsteno y romper herramientas por diversión. Insoportable pero necesario.
        """)

    # CHISME 7
    with st.expander("🚨 7. GRAFENO: EL NEPO BABY QUE NO CUMPLE SUS PROMESAS"):
        # LÍNEA 321 - TAMAÑO: 600x400
        st.image("https://via.placeholder.com/600x400/00CED1/FFFFFF?text=Foto+Grafeno", use_container_width=False)
        st.write("""
        Lleva 15 años prometiendo revolucionar las baterías, el internet, la construcción y hasta la ropa. 
        Todos los laboratorios le han dado presupuesto infinito. ¿Y qué nos ha entregado a nivel masivo? 
        Algunas raquetas de tenis caras y un par de artículos de revistas. El Grafeno es puro PR y marketing científico. 
        El Silicio, que lleva décadas haciendo el trabajo pesado en nuestros celulares, está a punto de convocar a una huelga.
        """)

    # CHISME 8
    with st.expander("🚨 8. COBRE, A PUNTO DEL BURNOUT"):
        # LÍNEA 331 - TAMAÑO: 600x400
        st.image("https://via.placeholder.com/600x400/FF69B4/FFFFFF?text=Foto+Cobre+Burnout", use_container_width=False)
        st.write("""
        Trabaja de lunes a domingo. Conduce electricidad en tu celular, en tu refrigerador, en las redes eléctricas de toda la ciudad. 
        El Cobre no descansa, y se le nota: últimamente se calienta demasiado rápido (efecto Joule, le dicen sus terapeutas). 
        Le sugirieron delegar responsabilidades a la Plata, pero ella cobra carísimo por hora, así que el Cobre sigue 
        esclavizado. ¡Exigimos vacaciones para las redes cristalinas FCC!
        """)

    # CHISME 9
    with st.expander("🚨 9. POLÍMEROS (PLÁSTICOS): LA DEMANDA DEL MILENIO"):
        # LÍNEA 342 - TAMAÑO: 600x400
        st.image("https://via.placeholder.com/600x400/FF8C00/FFFFFF?text=Foto+Polimeros", use_container_width=False)
        st.write("""
        Fueron la sensación de los años 50. Versátiles, baratos y moldeables. Parecían perfectos, hasta que el Océano 
        presentó una demanda colectiva por ocupación ilegal de espacio. Ahora, materiales como el PET y el PVC están en medio 
        de un escándalo de relaciones públicas intentando lavar su imagen con campañas de "biodegradabilidad" que nadie les cree. 
        Se espera un juicio de miles de años (literalmente, lo que tardan en degradarse).
        """)

    # CHISME 10
    with st.expander("🚨 10. EL ORO SE NIEGA A SOCIALIZAR"):
        # LÍNEA 352 - TAMAÑO: 600x400
        st.image("https://via.placeholder.com/600x400/FF1493/FFFFFF?text=Foto+Oro+Noble", use_container_width=False)
        st.write("""
        "Soy un metal noble. No me oxido, no reacciono, no me mezclo con plebeyos", fue la última declaración del Oro 
        antes de encerrarse en una caja fuerte. A diferencia de metales reactivos que arman fiestas químicas con el oxígeno 
        y el agua (¡hola Sodio, sabemos que te encanta explotar!), el Oro mantiene su estructura inalterable. 
        Mucha arrogancia, pero al final del día todos sabemos que es demasiado suave para el trabajo pesado industrial y 
        depende del Cobre o la Plata para tener algo de dureza. ¡Atrapada!
        """)

# =========================================================
# TAB 4: QUIZ ZONE
# =========================================================

with tab4:
    st.header("Test de Conocimientos")
    
    preguntas = [
        {"q": "¿Qué material es la estrella principal en la industria aeroespacial por su baja densidad?", "o": ["Titanio", "Aluminio", "Cobre"], "c": "Aluminio", "r": "El aluminio tiene una densidad aproximada de 2.7 g/cm³, perfecto para volar."},
        {"q": "¿Qué adición principal convierte al hierro en acero?", "o": ["Cromo", "Carbono", "Zinc"], "c": "Carbono", "r": "El carbono se aloja en los intersticios del hierro, aumentando drástastically su resistencia mecánica."},
        {"q": "Material conocido por su excelente conductividad, usado masivamente en cableado:", "o": ["Cobre", "Níquel", "Estaño"], "c": "Cobre", "r": "Aunque la plata es mejor, el cobre ofrece el mejor balance costo/beneficio en conductividad."},
        {"q": "¿Qué propiedad indica la capacidad de un material de deformarse antes de romperse?", "o": ["Dureza", "Elongación", "Resiliencia"], "c": "Elongación", "r": "A mayor elongación (ductilidad), más 'estirable' es el material antes de la fractura."},
        {"q": "¿Qué elemento hace al acero 'inoxidable'?", "o": ["Níquel", "Vanadio", "Cromo"], "c": "Cromo", "r": "El cromo forma una fina capa pasiva de óxido de cromo que detiene la oxidación del hierro."}
    ]

    if 'pregunta_actual' not in st.session_state:
        st.session_state.pregunta_actual = random.choice(preguntas)

    p = st.session_state.pregunta_actual

    st.markdown(f"<div class='retro-box'><h3>{p['q']}</h3></div>", unsafe_allow_html=True)
    respuesta = st.radio("Selecciona tu respuesta:", p["o"])

    if st.button("Verificar respuesta"):
        if respuesta == p["c"]:
            st.success(f"¡Correcto! {p['r']}")
        else:
            st.error(f"Error. La respuesta era {p['c']}. {p['r']}")
            
    if st.button("Generar otra pregunta"):
        st.session_state.pregunta_actual = random.choice(preguntas)
        st.rerun()
