from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import euclidean_distances
import os

app = Flask(__name__)

# ---------------- POSTS EN MEMORIA (CON INTRO EXCLUSIVA Y SIN ACEROS) ---------------- #
blog_posts = [
    {
        "title": "💿 BIENVENIDOS A MATERIALES VLOG 💿",
        "date": "01/01/2006",
        "content": "¡Sistema iniciado! Bienvenidos al rincón más exclusivo de la metalurgia en todo el internet. 🌐\n\n¿De qué va este vlog? Aquí nos enfocamos en las aleaciones más *spicy* y exóticas del laboratorio. Hablamos de Magnesio (¡super ligero y rebelde!), Titanio, Cobre, Aluminio y otros materiales de alta gama.\n\n🚨 RULE #1: Aquí NO hablamos de aceros. Son demasiado aburridos, pesados y mainstream para nosotros. Sorry not sorry.\n\n🔌 PUBLICACIONES: Sube tus reportes y cuenta el chisme.\n📺 VIDEOS: Checa el reproductor (¡acabamos de subir un video nuevo explicativo!).\n🔍 BASE DE DATOS & MATCHMAKER: Escanea aleaciones o deja que la IA busque tu match perfecto.\n\n¡Personaliza tu perfil y comienza a hackear la tabla periódica! ✨",
        "mood": "System Online 🟢",
        "image": "https://data.textstudio.com/output/sample/animated/4/6/5/6/material-16-6564.gif"
    },
    {
        "title": "El Grafeno es puro humo publicitario 📉",
        "date": "23/5/2006",
        "content": "Llevan años prometiendo elevadores espaciales y baterías infinitas. En papel es 200 veces más fuerte que todos, pero a nivel industrial es imposible de fabricar barato. El Silicio sigue haciendo todo el trabajo sucio en nuestras computadoras mientras el Grafeno sale en las revistas. Overrated. 🙄",
        "mood": "Escéptica 💻",
        "image": "https://media4.giphy.com/media/v1.Y2lkPTZjMDliOTUyZWo1a29scHdvM2pmb2E4YTFqdm15MjhtNXp3MW5mcXVjcjc4eHZxdiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/5OEagxq0WJvmWAZqSu/200w.gif"
    },
    {
        "title": "El Titanio: Guapo pero Inalcanzable 🙄",
        "date": "22/5/2006",
        "content": "Sí, es súper ligero, resistente y el cuerpo humano no lo rechaza en implantes. Pero intentar maquinarlo es una PESADILLA. Rompe las herramientas de corte, exige soldarse sin oxígeno y cobra carísimo. Tanta diva energy en un solo metal no es normal.",
        "mood": "Agotada 🔋",
        "image": "https://images.emojiterra.com/google/noto-emoji/unicode-15/color/256px/1f612.png"
    },
    {
        "title": "El Cobre está súper tóxico hoy 🚩",
        "date": "21/5/2006",
        "content": "Dejé mi muestra al aire libre 5 minutos y ya se puso toda verde y oxidada (pátina de carbonato). No soporto tanto drama corrosivo. Lo único bueno es que conduce la electricidad de mi reproductor MP3.",
        "mood": "Drama Químico 🧪",
        "image": "https://media.tenor.com/1iFzaNAGgHIAAAAM/benjammins-red-flags.gif"
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
