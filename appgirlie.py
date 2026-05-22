# =========================================================
# MATERIAL WORLD - 2026 NEO-Y2K EDITION 💿
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
    page_title="Material World",
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
# ESTILO NEO-BRUTALISTA Y2K (MODERNIDAD 2026)
# Colores: Turquesa mate (#4ECDC4), Naranja/Salmón (#F4A261), Rosa polvo (#FFB5A7)
# =========================================================

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Inter:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: #2B2D42;
}

/* FONDO LIMPIO 2026 CON PATRÓN SUTIL */
.stApp {
    background-color: #F7F7F2;
    background-image: radial-gradient(#d1d1d1 1px, transparent 1px);
    background-size: 20px 20px;
}

/* BARRA LATERAL */
section[data-testid="stSidebar"] {
    background-color: #FFB5A7;
    border-right: 4px solid #2B2D42;
}

/* TÍTULO PRINCIPAL */
h1 {
    font-family: 'Space Mono', monospace;
    color: #F7F7F2 !important;
    text-align: center;
    background-color: #2B2D42;
    border: 4px solid #2B2D42;
    padding: 20px;
    box-shadow: 8px 8px 0px #4ECDC4;
    text-transform: uppercase;
}

/* CAJAS DE CONTENIDO (NEO-BRUTALISM) */
.retro-box {
    background-color: #FFFFFF;
    border: 4px solid #2B2D42;
    padding: 25px;
    margin-bottom: 30px;
    box-shadow: 6px 6px 0px #F4A261;
    transition: transform 0.2s ease;
}
.retro-box:hover {
    transform: translate(-2px, -2px);
    box-shadow: 8px 8px 0px #4ECDC4;
}

/* SUBTÍTULOS */
h2, h3 {
    font-family: 'Space Mono', monospace;
    color: #2B2D42 !important;
    background-color: #4ECDC4;
    display: inline-block;
    padding: 5px 15px;
    border: 3px solid #2B2D42;
    margin-bottom: 15px;
}

/* TABS (PESTAÑAS) */
.stTabs [data-baseweb="tab"] {
    font-family: 'Space Mono', monospace;
    background-color: #FFB5A7;
    border: 3px solid #2B2D42;
    margin-right: 10px;
    padding: 10px 20px;
    font-weight: bold;
    color: #2B2D42 !important;
    border-bottom: none;
}
.stTabs [aria-selected="true"] {
    background-color: #F4A261 !important;
    box-shadow: inset 0px 4px 0px #2B2D42;
}

/* BOTONES */
.stButton>button {
    background-color: #4ECDC4;
    color: #2B2D42;
    font-family: 'Space Mono', monospace;
    font-weight: bold;
    border: 3px solid #2B2D42;
    box-shadow: 4px 4px 0px #2B2D42;
    transition: all 0.1s;
}
.stButton>button:active {
    box-shadow: 0px 0px 0px #2B2D42;
    transform: translate(4px, 4px);
}

/* EXPANDERS (CHISMES) */
.streamlit-expanderHeader {
    font-family: 'Space Mono', monospace !important;
    font-weight: bold !important;
    background-color: #F4A261 !important;
    color: #2B2D42 !important;
    border: 3px solid #2B2D42 !important;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.title("MATERIAL WORLD _ 2007.exe")

st.markdown("""
<div class="retro-box">
<p style="text-align:center; font-size:18px;">
<strong>> INICIANDO SISTEMA...</strong><br>
Bienvenido al portal definitivo de ingeniería y chismes metalúrgicos.<br>
Navega por las pestañas para explorar la base de datos o leer nuestro blog.
</p>
</div>
""", unsafe_allow_html=True)

# LÍNEA DE BANNER PRINCIPAL (TAMAÑO: 1200 x 300)
st.image("https://via.placeholder.com/1200x300/FFB5A7/2B2D42?text=BANNER+PRINCIPAL+(1200x300)", use_container_width=True)

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "RECOMENDADOR",
    "BUSCADOR",
    "VLOG / GOSSIP",
    "TEST ZONE"
])

# =========================================================
# TAB 1: RECOMENDADOR
# =========================================================

with tab1:
    st.header("MATCH_MAKER_AI")
    st.sidebar.title("PARÁMETROS")

    uts = st.sidebar.slider("Resistencia máxima (Su)", int(df["Su"].min()), int(df["Su"].max()), int(df["Su"].mean()))
    ys = st.sidebar.slider("Límite elástico (Sy)", int(df["Sy"].min()), int(df["Sy"].max()), int(df["Sy"].mean()))
    elong = st.sidebar.slider("Elongación (A5)", int(df["A5"].min()), int(df["A5"].max()), int(df["A5"].mean()))
    hb = st.sidebar.slider("Dureza (Bhn)", int(df["Bhn"].min()), int(df["Bhn"].max()), int(df["Bhn"].mean()))
    young = st.sidebar.slider("Módulo Young (E)", int(df["E"].min()), int(df["E"].max()), int(df["E"].mean()))
    corte = st.sidebar.slider("Módulo cortante (G)", int(df["G"].min()), int(df["G"].max()), int(df["G"].mean()))

    if st.sidebar.button("CALCULAR ALGORITMO"):
        features = ["Su", "Sy", "A5", "Bhn", "E", "G"]
        scaler = MinMaxScaler()
        X = scaler.fit_transform(df[features])
        usuario = scaler.transform([[uts, ys, elong, hb, young, corte]])
        distancias = euclidean_distances(usuario, X)
        indices = np.argsort(distancias[0])[:5]
        mejores = df.iloc[indices].copy()
        mejores["Afinidad %"] = [round(100 / (1 + d), 2) for d in distancias[0][indices]]

        st.markdown("### RESULTADOS_")
        st.dataframe(mejores[["Material", "Heat treatment", "Afinidad %"]], use_container_width=True)

        fig = px.scatter(mejores, x="Bhn", y="Su", color="Material", size="Afinidad %", text="Material")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=500)
        st.plotly_chart(fig, use_container_width=True)

# =========================================================
# TAB 2: BUSCADOR
# =========================================================

with tab2:
    st.header("DATABASE_SEARCH")
    
    st.markdown("""
    <div class="retro-box" style="box-shadow: 6px 6px 0px #FFB5A7;">
    Ingresa cualquier fragmento de texto (aleación, tratamiento, número) para escanear los registros.
    </div>
    """, unsafe_allow_html=True)
    
    busqueda = st.text_input("QUERY:")

    if busqueda:
        mask = np.column_stack([df[col].astype(str).str.contains(busqueda, case=False, na=False) for col in df.columns])
        resultados = df.loc[mask.any(axis=1)]

        if len(resultados) > 0:
            st.success(f"> {len(resultados)} REGISTROS ENCONTRADOS.")
            
            for i in range(min(10, len(resultados))):
                material = resultados.iloc[i]
                
                st.markdown(f"""
                <div class="retro-box" style="border-left: 10px solid #4ECDC4;">
                <h3 style="background-color: transparent; border: none; margin: 0; padding: 0;">{material['Material']}</h3>
                <hr style="border: 1px solid #2B2D42;">
                <p><b>Tratamiento:</b> {material['Heat treatment']}</p>
                <p><b>Su (Resistencia):</b> {material['Su']} MPa | <b>Bhn (Dureza):</b> {material['Bhn']} HB</p>
                <p><b>E (Módulo de Young):</b> {material['E']} GPa | <b>Elongación:</b> {material['A5']}%</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error("> ERROR 404: NO HAY COINCIDENCIAS.")

# =========================================================
# TAB 3: VLOG / GOSSIP (ARTÍCULOS LARGOS)
# =========================================================

with tab3:
    st.header("THE_VLOG_ARCHIVES")
    st.write("Análisis profundo, dramas estructurales y secretos de la tabla periódica.")

    with st.expander("1. ACERO INOXIDABLE Y CORROSIÓN: EL BLOQUEO DEFINITIVO"):
        st.image("https://via.placeholder.com/800x400/4ECDC4/2B2D42?text=FOTO+ACERO+(800x400)", use_container_width=True)
        st.write("""
        **Posteado a las 02:34 AM** Por años, el hierro y la corrosión mantuvieron una de las relaciones termodinámicas más tóxicas de la industria. Era inevitable: dejabas hierro a la intemperie y la oxidación comenzaba su trabajo destructivo, devorando la estructura desde adentro. Pero todo cambió cuando el hierro conoció al cromo. 
        
        Al alearse con al menos un 10.5% de cromo, el acero sufre una transformación radical. El cromo, siendo altamente reactivo al oxígeno, se sacrifica primero para formar una capa invisible, continua y ultra resistente de óxido de cromo en la superficie. Esta capa pasiva sella el material por completo. La semana pasada vimos al acero inoxidable sumergido en un ambiente marino severo, y la corrosión literalmente no pudo ni tocarlo. Lo mejor de todo es que si esta capa se raya, se regenera sola si hay oxígeno presente. Es el sistema de defensa perfecto y el mayor "glow up" de la historia metalúrgica.
        """)

    with st.expander("2. ROBO DE IDENTIDAD: EL BRONCE DEMANDA AL LATÓN"):
        st.image("https://via.placeholder.com/800x400/F4A261/2B2D42?text=FOTO+BRONCE+LATON+(800x400)", use_container_width=True)
        st.write("""
        **Posteado a las 14:15 PM** Las aleaciones basadas en cobre están en una guerra civil. El Bronce, la aleación histórica de cobre y estaño que definió toda una era de la humanidad (la Edad de Bronce), ha emitido un comunicado oficial acusando al Latón (cobre y zinc) de suplantación de identidad en aplicaciones modernas.
        
        "Tengo una excelente resistencia al desgaste, a la corrosión marina y una fricción bajísima. Yo soy el material de las estatuas, de los engranajes navales y de la historia", declaró el Bronce. Sin embargo, el Latón, aprovechando su color dorado similar, su menor costo y su increíble facilidad para ser maquinado, ha acaparado el mercado de la decoración, cerraduras, válvulas y tuberías. Los ingenieros de costos defienden al Latón por su ductilidad, pero los puristas estructurales insisten en que nada supera la resistencia a la fatiga del Bronce auténtico.
        """)

    with st.expander("3. TITANIO: COMPLEJO DE DIVA O GENIO INCOMPRENDIDO"):
        st.image("https://via.placeholder.com/800x400/FFB5A7/2B2D42?text=FOTO+TITANIO+(800x400)", use_container_width=True)
        st.write("""
        **Posteado a las 11:20 AM** El titanio es el material que todos quieren en su currículum, pero nadie quiere en su línea de ensamblaje. Su relación resistencia/peso es legendaria (tan fuerte como el acero, pero un 45% más ligero) y su biocompatibilidad lo hace el rey absoluto de los implantes médicos. 
        
        Pero hablemos de su lado oscuro: el maquinado. El titanio tiene un módulo de elasticidad bajo, lo que significa que "rebota" cuando intentas cortarlo, destruyendo las herramientas de corte por fricción y calor acumulado. Además, es tan reactivo a altas temperaturas que si lo sueldas sin gas inerte protector, se contamina con el oxígeno y el nitrógeno del aire, volviéndose quebradizo como vidrio. Cobra carísimo, exige condiciones de laboratorio para manufacturarse, pero cuando entrega resultados en un motor de jet aeroespacial, nos recuerda por qué le aguantamos tantos caprichos.
        """)

    with st.expander("4. POLÍMEROS VS EL OCÉANO: UN JUICIO MILENARIO"):
        st.image("https://via.placeholder.com/800x400/4ECDC4/2B2D42?text=FOTO+POLIMEROS+(800x400)", use_container_width=True)
        st.write("""
        **Posteado a las 09:00 AM** Fueron aclamados como el milagro del siglo XX. Cadenas infinitas de monómeros unidos por enlaces covalentes fuertes. Polímeros como el PET, PVC y el Polietileno ofrecieron impermeabilidad, aislamiento eléctrico y un costo de producción cercano a cero. 
        
        Pero su mayor ventaja resultó ser su peor condena: su resistencia a la degradación biológica. Al no existir bacterias naturales capaces de romper eficientemente estos enlaces sintéticos a gran escala, los plásticos comenzaron a acumularse. Hoy enfrentan la demanda ambiental más grande de la historia. Aunque intentan lavar su imagen desarrollando polímeros bioplásticos (como el PLA, derivado del ácido láctico del maíz), la industria pesada sabe que los polímeros termoplásticos convencionales seguirán dominando por sus insuperables propiedades mecánicas a bajo costo.
        """)

    with st.expander("5. ALUMINIO: EL REY DE LOS CIELOS"):
        st.image("https://via.placeholder.com/800x400/F4A261/2B2D42?text=FOTO+ALUMINIO+(800x400)", use_container_width=True)
        st.write("""
        **Posteado a las 16:45 PM** En el siglo XIX, el aluminio era considerado un metal precioso, más caro que el oro, porque separarlo de la bauxita era energéticamente imposible. Hoy, gracias a la electrólisis, es el pilar de la aviación moderna. 
        
        Su densidad de 2.7 g/cm³ humilla a los 7.8 g/cm³ del acero. Y aunque en su estado puro el aluminio es blando y débil, cuando se alea con cobre, zinc o magnesio (y se somete a tratamientos de envejecimiento como en la serie 7000), alcanza resistencias mecánicas comparables a ciertos aceros estructurales. Los ingenieros de Boeing lo adoran. El Acero lo odia por haberle robado el protagonismo en el aire.
        """)

    with st.expander("6. LA CANCELACIÓN DEL PLOMO"):
        st.image("https://via.placeholder.com/800x400/FFB5A7/2B2D42?text=FOTO+PLOMO+(800x400)", use_container_width=True)
        st.write("""
        **Posteado a las 18:30 PM** Si hay un material que ha sufrido la cancelación más severa y justificada, es el plomo. Fue la estrella de la fontanería en el Imperio Romano, el pigmento blanco más codiciado del Renacimiento y el aditivo antidetonante mágico de la gasolina en los años 50.
        
        ¿El problema? Es altamente neurotóxico. Al entrar al torrente sanguíneo, el plomo imita al calcio, cruzando la barrera hematoencefálica y causando daños cerebrales irreversibles. Tras décadas de encubrimiento, finalmente fue desterrado de pinturas, tuberías y combustibles. Hoy, su alta densidad y capacidad para absorber radiación lo mantienen confinado trabajando en el departamento de radiología de los hospitales, donde nadie quiere acercarse a él.
        """)

    with st.expander("7. EL GRAFENO: PROMESAS ROTAS Y PR"):
        st.image("https://via.placeholder.com/800x400/4ECDC4/2B2D42?text=FOTO+GRAFENO+(800x400)", use_container_width=True)
        st.write("""
        **Posteado a las 10:15 AM** Lleva dos décadas siendo "el material del futuro", pero parece que el futuro nunca llega. Una sola capa de átomos de carbono dispuestos en una red hexagonal bidimensional. En el papel, el grafeno es 200 veces más fuerte que el acero, excelente conductor eléctrico y casi transparente.
        
        Pero fuera del laboratorio, la historia es otra. Fabricarlo a escala industrial sin defectos, en áreas grandes y a un costo razonable ha sido un fracaso espectacular. Mientras el grafeno sigue publicando artículos científicos y llevándose premios Nobel, el viejo y confiable Silicio sigue sosteniendo toda la industria de los semiconductores y la electrónica mundial trabajando horas extras.
        """)

    with st.expander("8. COBRE: FATIGA CRÓNICA Y BURNOUT"):
        st.image("https://via.placeholder.com/800x400/F4A261/2B2D42?text=FOTO+COBRE+(800x400)", use_container_width=True)
        st.write("""
        **Posteado a las 20:00 PM** Pobre Cobre. Con una estructura cristalina Cúbica Centrada en las Caras (FCC), tiene electrones libres que lo convierten en un excelente conductor eléctrico y térmico. Y debido a esto, la humanidad lo ha esclavizado para cablear literalmente el planeta entero.
        
        A diferencia de la plata (que es mejor conductora pero excesivamente cara), el cobre ofrece el balance perfecto. Sin embargo, sufre de constantes sobrecalentamientos (efecto Joule) y, cuando se expone a los elementos, desarrolla una pátina verde (carbonato de cobre) que, aunque protege el interior y se ve muy "aesthetic" en la Estatua de la Libertad, demuestra el agotamiento del material. ¡Merece un descanso!
        """)

    with st.expander("9. TUNGSTENO: EL CORAZÓN INQUEBRANTABLE"):
        st.image("https://via.placeholder.com/800x400/FFB5A7/2B2D42?text=FOTO+TUNGSTENO+(800x400)", use_container_width=True)
        st.write("""
        **Posteado a las 07:45 AM** Con un punto de fusión superior a los 3,400 °C, el tungsteno (o wolframio) es el metal que se ríe de las calderas del infierno. Es tan resistente al calor que se usó como filamento en las clásicas bombillas incandescentes durante un siglo sin derretirse.
        
        Su otra faceta famosa es cuando se mezcla con carbono para formar Carburo de Tungsteno. Esta cerámica metálica es tan brutalmente dura que se utiliza para fabricar las herramientas de corte que mecanizan al acero o al titanio. El tungsteno no socializa, no se funde fácilmente y su densidad es comparable a la del oro. Es el "tipo duro" definitivo de la tabla periódica.
        """)

    with st.expander("10. EL ORO Y SU COMPLEJO DE SUPERIORIDAD"):
        st.image("https://via.placeholder.com/800x400/4ECDC4/2B2D42?text=FOTO+ORO+(800x400)", use_container_width=True)
        st.write("""
        **Posteado a las 22:10 PM** El oro pertenece a la clase de los metales nobles. Termodinámicamente hablando, esto significa que la energía necesaria para oxidarlo es tan alta que simplemente prefiere no reaccionar con el ambiente. Puedes enterrarlo mil años bajo el agua, y saldrá brillando igual.
        
        Esta estabilidad química lo hizo la base de la economía mundial. Pero estructuralmente, el oro es un fraude: es tan blando que lo puedes deformar con los dientes. Para poder usarlo en joyería, literalmente tiene que rogarle al cobre o a la plata que se aleen con él para ganar algo de rigidez y dureza (de ahí nacen los quilates; 18k significa 75% oro y 25% otros metales que hacen el trabajo sucio).
        """)

# =========================================================
# TAB 4: QUIZ ZONE (10 PREGUNTAS)
# =========================================================

with tab4:
    st.header("KNOWLEDGE_EVALUATION")
    st.write("Demuestra tu nivel técnico. El sistema elegirá preguntas aleatorias.")
    
    preguntas = [
        {"q": "¿Qué material es el favorito de la industria aeroespacial por su baja densidad (2.7 g/cm³)?", "o": ["Titanio", "Aluminio", "Cobre"], "c": "Aluminio", "r": "El aluminio ligero permite que los aviones comerciales no gasten combustible en exceso."},
        {"q": "¿Qué elemento se añade al hierro para transformarlo en acero y aumentar su resistencia?", "o": ["Cromo", "Carbono", "Zinc"], "c": "Carbono", "r": "El carbono bloquea el movimiento de dislocaciones en el hierro, endureciéndolo."},
        {"q": "¿Qué material destaca por su conductividad y se usa en el 90% del cableado eléctrico mundial?", "o": ["Cobre", "Níquel", "Estaño"], "c": "Cobre", "r": "El cobre ofrece la mejor conductividad eléctrica después de la plata, pero a una fracción de su costo."},
        {"q": "En ensayos de tensión, ¿qué propiedad nos dice qué tanto se puede deformar un material antes de romperse?", "o": ["Dureza", "Elongación", "Fatiga"], "c": "Elongación", "r": "La elongación (ductilidad) permite moldear y doblar metales sin fracturarlos."},
        {"q": "¿Qué aleante es responsable de crear la capa pasiva que hace al acero 'inoxidable'?", "o": ["Níquel", "Vanadio", "Cromo"], "c": "Cromo", "r": "Se necesita un mínimo de 10.5% de Cromo para crear la película de óxido protectora."},
        {"q": "¿Qué aleación histórica está formada principalmente por Cobre y Estaño?", "o": ["Latón", "Bronce", "Alpaca"], "c": "Bronce", "r": "El bronce es la mezcla de Cobre y Estaño, mientras que el latón es Cobre y Zinc."},
        {"q": "¿Qué prueba mecánica utiliza una pequeña bola de acero o un cono de diamante para dejar una marca en el material?", "o": ["Ensayo de Tracción", "Prueba de Impacto Charpy", "Prueba de Dureza"], "c": "Prueba de Dureza", "r": "Las pruebas de dureza (como Brinell o Rockwell) miden la resistencia a la indentación plástica."},
        {"q": "¿Qué metal tiene una resistencia extrema a altas temperaturas y se usa para fabricar filamentos o herramientas de corte?", "o": ["Magnesio", "Tungsteno", "Plomo"], "c": "Tungsteno", "r": "El tungsteno funde a más de 3,400 °C, siendo el metal con el punto de fusión más alto."},
        {"q": "A nivel molecular, ¿cómo se denominan las unidades básicas que se encadenan para formar un plástico?", "o": ["Cristales", "Monómeros", "Isótopos"], "c": "Monómeros", "r": "Miles de monómeros se unen en un proceso llamado polimerización para formar el polímero."},
        {"q": "¿Qué metal es famoso por su biocompatibilidad extrema, permitiendo que el hueso humano crezca a su alrededor?", "o": ["Titanio", "Acero al carbono", "Aluminio"], "c": "Titanio", "r": "El titanio se integra tan bien al cuerpo (osteointegración) que no genera rechazo inmunológico."}
    ]

    if 'pregunta_actual' not in st.session_state:
        st.session_state.pregunta_actual = random.choice(preguntas)

    p = st.session_state.pregunta_actual

    st.markdown(f"<div class='retro-box' style='background-color:#F7F7F2;'><h3>> PREGUNTA:</h3><p style='font-size:18px;'>{p['q']}</p></div>", unsafe_allow_html=True)
    
    respuesta = st.radio("SELECCIONA TU RESPUESTA:", p["o"])

    colA, colB = st.columns(2)
    with colA:
        if st.button("ENVIAR RESPUESTA"):
            if respuesta == p["c"]:
                st.success(f"> CORRECTO. {p['r']}")
                st.balloons()
            else:
                st.error(f"> INCORRECTO. La respuesta era {p['c']}. {p['r']}")
                
    with colB:
        if st.button("CARGAR NUEVA PREGUNTA"):
            st.session_state.pregunta_actual = random.choice(preguntas)
            st.rerun()
