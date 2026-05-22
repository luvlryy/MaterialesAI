from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import euclidean_distances

app = Flask(__name__)

# POSTS EN MEMORIA CON MÁS EJEMPLOS DE INICIO
blog_posts = [
    {
        "title": "El Cobre está súper tóxico hoy 🚩",
        "date": "21/5/2006",
        "content": "Dejé mi muestra al aire libre 5 minutos y ya se puso toda verde y oxidada. No soporto tanto drama corrosivo.",
        "mood": "Drama Químico 🧪",
        "image": "https://via.placeholder.com/550/bfe4ff/ff5cb8?text=Cobre+Oxidado+🤢"
    },
    {
        "title": "OMG Acero Inoxidable & Corrosión",
        "date": "20/5/2006",
        "content": "El Hierro ahora sale con el Cromo y literalmente la corrosión ya no puede tocarlo. ¡Hacen match perfecto!",
        "mood": "Impresionada ✨",
        "image": "https://via.placeholder.com/550x200/ffe4e1/ff69b4?text=Acero+Inoxidable"
    }
]

# CARGAR EXCEL
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

# ---------------- POSTS ---------------- #

@app.route("/get_posts")
def get_posts():
    return jsonify(blog_posts)

@app.route("/add_post", methods=["POST"])
def add_post():
    data = request.json
    blog_posts.insert(0, data)
    return jsonify({"status": "success"})

# ---------------- BUSCADOR ---------------- #

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

# ---------------- MATCHMAKER IA ---------------- #

@app.route("/match", methods=["POST"])
def match():
    d = request.json
    
    vals = [[
        float(d["su"]),
        float(d["sy"]),
        float(d["a5"]),
        float(d["bhn"]),
        float(d["e"]),
        float(d["g"])
    ]]

    features = ["Su", "Sy", "A5", "Bhn", "E", "G"]

    scaler = MinMaxScaler()
    X = scaler.fit_transform(df_match[features])

    distancias = euclidean_distances(scaler.transform(vals), X)
    indices = np.argsort(distancias[0])[:5]

    res = df_full.iloc[indices].copy()
    res["Compatibilidad"] = [
        round(100 / (1 + dist), 2)
        for dist in distancias[0][indices]
    ]

    return jsonify(res.fillna("N/A").to_dict(orient="records"))

import os

if __name__ == "__main__":
    # Lee el puerto que le da Render, y si no encuentra ninguno (local), usa el 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
