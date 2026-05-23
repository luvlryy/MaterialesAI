from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import euclidean_distances
import os

app = Flask(__name__)

# ---------------- POSTS EN MEMORIA (CHISMES + INTRO VLOG) ---------------- #
blog_posts = [
    {
        "title": "💿 BIENVENIDOS A MATERIALES VLOG 💿",
        "date": "01/01/2006",
        "content": "¡Sistema iniciado! Aquí tienes tu guía de navegación:\n\n🔌 PUBLICACIONES: Sube tus propios reportes, arrastra imágenes y cuenta el chisme del laboratorio.\n📺 VIDEOS: Tu sección informativa. Pega links de YouTube para ver documentales y tutoriales sin salir de la página.\n🔍 BASE DE DATOS: Escanea nuestra red de materiales por nombre o tratamiento.\n⚙️ MATCHMAKER: Ajusta los deslizadores y la Inteligencia Artificial encontrará tu aleación perfecta.\n🎮 POP QUIZ: Demuestra que no eres un n00b en metalurgia.\n\n¡Personaliza tu perfil a la izquierda y comienza a hackear la tabla periódica! 🌐",
        "mood": "System Online 🟢",
        "image": "https://via.placeholder.com/600x250/dbeafe/5a67d8?text=MATERIALES+VLOG+SYSTEM+ONLINE"
    },
    {
        "title": "El Grafeno es puro humo publicitario 📉",
        "date": "23/5/2006",
        "content": "Llevan 10 años prometiendo elevadores espaciales y baterías infinitas. En papel es 200 veces más fuerte que el acero, pero a nivel industrial es imposible de fabricar barato. El Silicio sigue haciendo todo el trabajo sucio en nuestras computadoras mientras el Grafeno sale en las revistas. Overrated. 🙄",
        "mood": "Escéptica 💻",
        "image": "https://via.placeholder.com/600x250/e0e7ff/4f46e5?text=Grafeno+Overrated"
    },
    {
        "title": "El Titanio: Guapo pero Inalcanzable 🙄",
        "date": "22/5/2006",
        "content": "Sí, es súper ligero, resistente y el cuerpo humano no lo rechaza en implantes. Pero intentar maquinarlo es una PESADILLA. Rompe las herramientas de corte, exige soldarse sin oxígeno y cobra carísimo. Tanta diva energy en un solo metal.",
        "mood": "Agotada 🔋",
        "image": "https://via.placeholder.com/600x250/f3e8ff/7c3aed?text=Titanio+Diva"
    },
    {
        "title": "El Cobre está súper tóxico hoy 🚩",
        "date": "21/5/2006",
        "content": "Dejé mi muestra al aire libre 5 minutos y ya se puso toda verde y oxidada (pátina de carbonato). No soporto tanto drama corrosivo. Lo único bueno es que conduce la electricidad de mi reproductor MP3.",
        "mood": "Drama Químico 🧪",
        "image": "https://via.placeholder.com/600x250/ccfbf1/0d9488?text=Cobre+Oxidado+🤢"
    },
    {
        "title": "OMG Acero Inoxidable & Corrosión",
        "date": "20/5/2006",
        "content": "El Hierro ahora sale con el Cromo (mínimo 10.5%) y formaron una capa pasiva impenetrable. Literalmente la corrosión ya no puede tocarlo. ¡Hacen match perfecto! El mayor glow up metalúrgico.",
        "mood": "Impresionada ⚡",
        "image": "https://via.placeholder.com/600x250/f1f5f9/475569?text=Acero+Inoxidable+Match"
    }
]

# ---------------- CARGAR EXCEL ---------------- #
try:
    df_full = pd.read_excel("Data_convertido.xlsx")
    df_full.columns = df_full.columns.astype(str).str.strip()
    df_search = df_full.fillna("N/A")
    df_match = df_full.copy()

    columnas_numericas = ["Su", "Sy", "A5", "Bhn", "E", "G"]

    for col in columnas_numericas:
        df_match[col] = pd.to_numeric(df_match[col], errors="coerce").fillna(0)

except Exception as e:
    print("ERROR AL CARGAR EL EXCEL:", e)

@app.route("/")
def home():
    return render_template("index.html")

# ---------------- RUTAS API ---------------- #
@app.route("/get_posts")
def get_posts():
    return jsonify(blog_posts)

@app.route("/add_post", methods=["POST"])
def add_post():
    data = request.json
    blog_posts.insert(0, data)
    return jsonify({"status": "success"})

@app.route("/buscar", methods=["POST"])
def buscar():
    query = request.json.get("query", "").lower()
    if not query:
        return jsonify([])

    mask = np.column_stack([
        df_search[col].astype(str).str.contains(query, case=False, na=False)
        for col in df_search.columns
    ])

    results = df_search.loc[mask.any(axis=1)].head(15)
    return jsonify(results.to_dict(orient="records"))

@app.route("/match", methods=["POST"])
def match():
    d = request.json
    vals = [[ float(d["su"]), float(d["sy"]), float(d["a5"]), float(d["bhn"]), float(d["e"]), float(d["g"]) ]]

    features = ["Su", "Sy", "A5", "Bhn", "E", "G"]
    scaler = MinMaxScaler()
    X = scaler.fit_transform(df_match[features])

    distancias = euclidean_distances(scaler.transform(vals), X)
    indices = np.argsort(distancias[0])[:5]

    res = df_full.iloc[indices].copy()
    res["Compatibilidad"] = [ round(100 / (1 + dist), 2) for dist in distancias[0][indices] ]

    return jsonify(res.fillna("N/A").to_dict(orient="records"))

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
