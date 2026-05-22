# =========================================================
# 📺 DISNEY MATERIAL CHANNEL - 2004 VIBES 📺
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
    page_title="Material Channel 📺",
    page_icon="✨",
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
    st.error(f"¡Ups! El CD-ROM está rayado: {e}")
    st.stop()

columnas_numericas = ["Su", "Sy", "A5", "Bhn", "E", "G"]

for col in columnas_numericas:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=columnas_numericas)

# =========================================================
# ESTILO DISNEY CHANNEL 2000s (CSS MAGIA)
# =========================================================

st.markdown("""
<style>
/* FUENTES DIVERTIDAS */
@import url('https://fonts.googleapis.com/css2?family=Chewy&family=Comic+Neue:wght@700&display=swap');

html, body, [class*="css"] {
    font-family: 'Comic Neue', cursive;
    color: #000080;
}

/* FONDO DISNEY BLUE CON PUNTITOS */
.stApp {
    background-color: #00BFFF;
    background-image: radial-gradient(#FFFFFF 10%, transparent 11%), radial-gradient(#FFFFFF 10%, transparent 11%);
    background-size: 60px 60px;
    background-position: 0 0, 30px 30px;
}

/* TÍTULOS GIGANTES Y DIVERTIDOS */
h1 {
    font-family: 'Chewy', cursive;
    color: #FF1493 !important;
    text-align: center;
    font-size: 70px !important;
    text-shadow: 3px 3px 0px #FFF, 6px 6px 0px #FFD700;
    letter-spacing: 3px;
    margin-bottom: 20px;
}

h2, h3 {
    font-family: 'Chewy', cursive;
    color: #FF4500 !important;
    text-shadow: 2px 2px 0px #FFF;
    letter-spacing: 1px;
}

/* CAJITAS ESTILO JUEGO FLASH */
.disney-box {
    background-color: #FFFACD; /* Amarillo clarito */
    border: 5px dashed #FF69B4;
    border-radius: 30px;
    padding: 25px;
    margin-bottom: 25px;
    box-shadow: 8px 8px 0px rgba(0,0,0,0.2);
}

/* PESTAÑAS COMO BURBUJAS */
.stTabs [data-baseweb="tab"] {
    background-color: #32CD32; /* Verde lima */
    border: 4px solid #FFF;
    border-radius: 25px 25px 0 0;
    margin-right: 10px;
    padding: 10px 25px;
    font-family: 'Chewy', cursive;
    font-size: 22px;
    color: #FFF !important;
    text-shadow: 2px 2px #000;
    box-shadow: 3px -3px 0px rgba(0,0,0,0.2);
}
.stTabs [aria-selected="true"] {
    background-color: #FF4500 !important; /* Naranja fuerte */
    transform: translateY(-5px);
}

/* BOTONES GORDITOS */
.stButton>button {
    background-color: #FFD700;
    color: #FF0000;
    font-family: 'Chewy', cursive;
    font-size: 24px;
    border: 4px solid #FFF;
    border-radius: 30px;
    box-shadow: 4px 4px 0px #FF8C00;
    transition: 0.1s;
    width: 100%;
}
.stButton>button:active {
    box-shadow: 0px 0px 0px;
    transform: translateY(4px);
}

/* --- ESTILOS EXCLUSIVOS DEL BLOG LIFESTYLE --- */
.blog-post {
    background-color: #FFFFFF;
    border: 6px solid #9370DB; /* Morado */
    border-radius: 20px;
    padding: 20px;
    margin-bottom: 30px;
    box-shadow: 10px 10px 0px #FF69B4;
}

.blog-header {
    display: flex;
    align-items: center;
    border-bottom: 3px dotted #00BFFF;
    padding-bottom: 10px;
    margin-bottom: 15px;
}

.avatar {
    width: 80px;
    height: 80px;
    background-color: #FFD700;
    border-radius: 50%;
    border: 4px solid #FF1493;
    margin-right: 15px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 40px;
}

.blog-meta {
    font-size: 14px;
    color: #666;
}

.blog-title {
    font-family: 'Chewy', cursive;
    font-size: 28px;
    color: #1E90FF;
    margin-top: 10px;
}

.blog-image-placeholder {
    width: 100%;
    height: 250px;
    background-color: #E6E6FA;
    border: 4px dashed #9370DB;
    border-radius: 15px;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #9370DB;
    font-weight: bold;
    margin: 15px 0;
}

/* ESTILOS DEL QUIZ MINIJUEGO */
.quiz-container {
    background-color: #FF7F50;
    border: 8px solid #FFF;
    border-radius: 40px;
    padding: 30px;
    color: #FFF;
    text-align: center;
    box-shadow: inset 0px 0px 20px rgba(0,0,0,0.2), 10px 10px 0px #FF4500;
}
.quiz-question {
    font-family: 'Chewy', cursive;
    font-size: 32px;
    text-shadow: 2px 2px #000;
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.markdown("<h1>✨ DISNEY MATERIAL CHANNEL ✨</h1>", unsafe_allow_html=True)

st.markdown("""
<div class="disney-box" style="text-align:center;">
<h2>🎮 ¡Bienvenida al menú principal! 🎮</h2>
<p style="font-size: 20px;">
Explora la base de datos, lee el diario secreto de las aleaciones o juega en la zona arcade. 
¡Cuidado con no trabar la computadora! 💿
</p>
</div>
""", unsafe_allow_html=True)

# LÍNEA DE BANNER PRINCIPAL
st.image("https://via.placeholder.com/1200x250/32CD32/FFFFFF?text=BANNER+PRINCIPAL+AQUI+(1200x250)", use_container_width=True)

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "⭐ Match Maker",
    "🔍 Buscador",
    "📖 Diario / Blog",
    "🕹️ Mini Juego"
])

# =========================================================
# TAB 1: RECOMENDADOR
# =========================================================

with tab1:
    st.markdown("<div class='disney-box'><h2>💖 Crea tu Aleación Perfecta 💖</h2></div>", unsafe_allow_html=True)
    st.sidebar.markdown("<h2>🛠️ Tus Herramientas</h2>", unsafe_allow_html=True)

    uts = st.sidebar.slider("Resistencia (Su)", int(df["Su"].min()), int(df["Su"].max()), int(df["Su"].mean()))
    ys = st.sidebar.slider("Límite (Sy)", int(df["Sy"].min()), int(df["Sy"].max()), int(df["Sy"].mean()))
    elong = st.sidebar.slider("Elongación (A5)", int(df["A5"].min()), int(df["A5"].max()), int(df["A5"].mean()))
    hb = st.sidebar.slider("Dureza (Bhn)", int(df["Bhn"].min()), int(df["Bhn"].max()), int(df["Bhn"].mean()))
    young = st.sidebar.slider("Módulo Young (E)", int(df["E"].min()), int(df["E"].max()), int(df["E"].mean()))
    corte = st.sidebar.slider("Módulo cortante (G)", int(df["G"].min()), int(df["G"].max()), int(df["G"].mean()))

    if st.sidebar.button("¡Hacer Magia! ✨"):
        features = ["Su", "Sy", "A5", "Bhn", "E", "G"]
        scaler = MinMaxScaler()
        X = scaler.fit_transform(df[features])
        usuario = scaler.transform([[uts, ys, elong, hb, young, corte]])
        distancias = euclidean_distances(usuario, X)
        indices = np.argsort(distancias[0])[:5]
        mejores = df.iloc[indices].copy()
        mejores["Afinidad %"] = [round(100 / (1 + d), 2) for d in distancias[0][indices]]

        st.dataframe(mejores[["Material", "Heat treatment", "Afinidad %"]], use_container_width=True)

        fig = px.scatter(mejores, x="Bhn", y="Su", color="Material", size="Afinidad %", text="Material")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=500)
        st.plotly_chart(fig, use_container_width=True)

# =========================================================
# TAB 2: BUSCADOR
# =========================================================

with tab2:
    st.markdown("""
    <div class="disney-box" style="background-color: #E0FFFF; border-color: #00CED1;">
    <h2>🕵️‍♀️ ¡Buscador Súper Secreto! 🕵️‍♀️</h2>
    Escribe cualquier palabra mágica (aleación o tratamiento) para buscar en la bóveda de datos.
    </div>
    """, unsafe_allow_html=True)
    
    busqueda = st.text_input("Escribe aquí:")

    if busqueda:
        mask = np.column_stack([df[col].astype(str).str.contains(busqueda, case=False, na=False) for col in df.columns])
        resultados = df.loc[mask.any(axis=1)]

        if len(resultados) > 0:
            st.success(f"✨ ¡Bingo! Encontré {len(resultados)} cositas.")
            for i in range(min(10, len(resultados))):
                material = resultados.iloc[i]
                st.markdown(f"""
                <div class="disney-box" style="background-color: #FFF0F5; border-color: #FF1493;">
                <h3 style="color: #FF1493 !important;">{material['Material']}</h3>
                <p><b>Tratamiento:</b> {material['Heat treatment']}</p>
                <p><b>Resistencia (Su):</b> {material['Su']} | <b>Dureza (Bhn):</b> {material['Bhn']}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error("😭 ¡Ay no! No encontré nada con esa palabra.")

# =========================================================
# TAB 3: DIARIO LIFESTYLE (BLOG)
# =========================================================

with tab3:
    st.markdown("<div class='disney-box'><h2>📖 My Secret Material Diary 📖</h2><p>Chismes, dramas y todo lo que pasa en la tabla periódica cuando nadie ve.</p></div>", unsafe_allow_html=True)

    # FUNCIÓN PARA GENERAR ENTRADAS DE BLOG
    def crear_post(titulo, avatar, mood, cancion, texto, img_placeholder):
        st.markdown(f"""
        <div class="blog-post">
            <div class="blog-header">
                <div class="avatar">{avatar}</div>
                <div class="blog-meta">
                    <b>Publicado por:</b> MaterialGurl99<br>
                    <b>Mood:</b> {mood}<br>
                    <b>🎵 Reproduciendo:</b> {cancion}
                </div>
            </div>
            <div class="blog-title">{titulo}</div>
            <img src="{img_placeholder}" style="width: 100%; border-radius: 15px; border: 4px dashed #9370DB; margin: 15px 0;">
            <p style="font-size: 16px; line-height: 1.6;">{texto}</p>
        </div>
        """, unsafe_allow_html=True)

    crear_post(
        "1. El Acero Inoxidable y la Corrosión ya NO se hablan 🙅‍♀️", 
        "💅", "Súper Tóxica 🐍", "Avril Lavigne - Complicated",
        "¡Agárrense fuerte! Se les vio en un ambiente marino y la tensión se podía cortar. Durante décadas, el Hierro y la Corrosión fueron tóxicos pero inseparables. Pero desde que el Hierro se juntó con el Cromo (mínimo un 10.5%, reina exigente), formó su famosa capa pasiva. Intentaron acercarse la semana pasada en una plataforma petrolera, y el Acero Inoxidable ni siquiera la miró. ¡Soporta!",
        "https://via.placeholder.com/800x400/FFB6C1/FFFFFF?text=FOTO+ACERO+(800x400)"
    )

    crear_post(
        "2. Robo de identidad: Bronce vs Latón 🥊", 
        "🤬", "Furiosa 🔥", "Britney Spears - Toxic",
        "El Bronce (Cobre + Estaño) salió a dar declaraciones acusando al Latón (Cobre + Zinc) de robarle su estética dorada. 'Yo soy el material de la historia, a mí me hicieron una edad entera', declaró el Bronce furioso. El Latón se defendió diciendo que al menos él no cuesta un ojo de la cara y es fácil de maquinar. ¡Drama total en los tribunales metalúrgicos!",
        "https://via.placeholder.com/800x400/FFD700/FFFFFF?text=FOTO+BRONCE+LATON+(800x400)"
    )

    crear_post(
        "3. El Glow Up del Aluminio ✨✈️", 
        "💅", "Fabulosa 💁‍♀️", "Hilary Duff - What Dreams Are Made Of",
        "¿Recuerdan cuando el Aluminio era carísimo y súper inútil en los 1800s? Pues gracias a la electrólisis, tuvo el glow up de la década. Con su bajísima densidad de 2.7 g/cm³, le robó todos los contratos aeroespaciales al Acero. Fuentes aseguran que el Acero está llorando en el gimnasio, mientras el Aluminio vuela en primera clase con Boeing.",
        "https://via.placeholder.com/800x400/87CEFA/FFFFFF?text=FOTO+ALUMINIO+(800x400)"
    )

    crear_post(
        "4. Titanio: ¿Diva Insoportable? 🙄", 
        "👑", "Cansada 🥱", "Christina Aguilera - Dirrty",
        "Sí, su relación resistencia/peso es increíble y los implantes médicos lo aman. Pero, ¿podemos hablar de lo odioso que es trabajarlo? Arruina las herramientas de corte, exige soldarse sin oxígeno y cobra carísimo. Muchos ingenieros ya no lo soportan, pero le aguantan los caprichos porque, seamos sinceros, hace un trabajo impecable.",
        "https://via.placeholder.com/800x400/DDA0DD/FFFFFF?text=FOTO+TITANIO+(800x400)"
    )

    crear_post(
        "5. La Cancelación Definitiva del Plomo 🚫", 
        "☠️", "Shockeada 😱", "My Chemical Romance - I'm Not Okay",
        "Era el rey de la plomería romana y el maquillaje del Renacimiento, pero el Plomo fue canceladísimo cuando descubrimos que es neurotóxico. Hoy en día vive aislado en baterías de autos y como escudo de radiación en hospitales. Un final trágico y oscuro para un material tan maleable. ¡Nunca confíes en los metales pesados!",
        "https://via.placeholder.com/800x400/A9A9A9/FFFFFF?text=FOTO+PLOMO+(800x400)"
    )

    crear_post(
        "6. Tungsteno: Cero Sentimientos 🧊", 
        "🥶", "Fría ❄️", "Kelly Clarkson - Since U Been Gone",
        "Con un punto de fusión de más de 3,400 °C, el Tungsteno no siente absolutamente nada. Se ríe de los hornos industriales. Cuando se junta con carbono (Carburo de Tungsteno), se dedica a romper las herramientas de otros metales por pura diversión. Es el tipo más rudo e inaccesible del barrio.",
        "https://via.placeholder.com/800x400/FFA07A/FFFFFF?text=FOTO+TUNGSTENO+(800x400)"
    )

    crear_post(
        "7. Grafeno: Puro PR y Nada de Acción 🤥", 
        "📱", "Decepcionada 😒", "Gwen Stefani - Hollaback Girl",
        "Lleva años diciendo que revolucionará el internet y la tecnología, pero el Grafeno es puro marketing. Prometió baterías infinitas y ropa inteligente, pero hasta ahora solo lo vemos en revistas de ciencia. Mientras tanto, el Silicio sigue trabajando horas extras en nuestros celulares sin quejarse.",
        "https://via.placeholder.com/800x400/98FB98/FFFFFF?text=FOTO+GRAFENO+(800x400)"
    )

    crear_post(
        "8. El Burnout del Cobre 🥵", 
        "⚡", "Estresada 🤯", "Destiny's Child - Survivor",
        "Trabaja 24/7 conduciendo electricidad en tu teléfono, tu refri y las calles de tu ciudad. El Cobre está sufriendo de un sobrecalentamiento crónico (Efecto Joule). Podría pedirle ayuda a la Plata, pero ella es demasiado 'High Maintenance'. ¡Exigimos vacaciones para el pobre Cobre!",
        "https://via.placeholder.com/800x400/CD853F/FFFFFF?text=FOTO+COBRE+(800x400)"
)
