# =========================================================
# 🌸 MATERIAL MATCH AI 🌸
# Y2K Pinky Matcha Ultimate Edition 🐰🎀✨
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
import random
import plotly.express as px
import plotly.graph_objects as go

from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import euclidean_distances

# =========================================================
# CONFIG
# =========================================================

st.set_page_config(
    page_title="Material Match AI 🌸",
    page_icon="🐰",
    layout="wide"
)

# =========================================================
# CSS Y2K GIRLIE
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Fredoka', sans-serif;
}

/* Fondo */
.stApp {
    background:
    linear-gradient(
        135deg,
        #ffe4ec 0%,
        #fff0f5 40%,
        #e8fff1 100%
    );
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #fff5fa;
    border-right: 4px solid #ffc2d1;
}

/* Título */
h1 {
    text-align: center;
    color: #ff4f9a !important;
    font-size: 70px !important;
    text-shadow: 2px 2px white;
}

/* Subtítulos */
h2, h3 {
    color: #ff75af !important;
}

/* Cards */
[data-testid="metric-container"] {
    background: rgba(255,255,255,0.7);
    border-radius: 25px;
    border: 3px solid #ffc2d1;
    padding: 15px;
    box-shadow: 0px 6px 15px rgba(255,182,193,0.3);
}

/* Botones */
.stButton>button {
    background: linear-gradient(
        90deg,
        #ff8fab,
        #ffb3c6
    );

    color: white;
    border-radius: 18px;
    border: none;
    height: 3.2em;
    font-size: 18px;
    font-weight: bold;
}

/* Cute box */
.cute-box {
    background: rgba(255,255,255,0.75);
    border: 3px dashed #ffb3c6;
    border-radius: 25px;
    padding: 25px;
    margin-bottom: 20px;
}

/* Input */
.stTextInput input {
    border-radius: 15px !important;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    font-size: 18px;
    color: #ff75af;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TÍTULO
# =========================================================

st.title("🌸 Material Match AI 🌸")

st.markdown("""
<div class="cute-box">

### 🐰 Welcome to the cutest materials lab 🎀

✨ Busca materiales  
✨ Aprende jugando  
✨ Explora propiedades mecánicas  
✨ Matcha + Y2K + ingeniería 💖

</div>
""", unsafe_allow_html=True)

# =========================================================
# CARGAR EXCEL
# =========================================================

df = pd.read_excel("Data_convertido.xlsx")

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
)

# =========================================================
# COLUMNAS NUMÉRICAS
# =========================================================

columnas_numericas = [
    "Su",
    "Sy",
    "A5",
    "Bhn",
    "E",
    "G"
]

for col in columnas_numericas:

    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df = df.dropna(subset=columnas_numericas)

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3 = st.tabs([
    "🎀 Recomendador",
    "🔍 Buscar Material",
    "🎮 Material Game"
])

# =========================================================
# TAB 1 — RECOMENDADOR
# =========================================================

with tab1:

    st.header("💖 Material Recommender")

    st.sidebar.title("🎀 Desired Properties")

    uts = st.sidebar.slider(
        "💪 Ultimate Strength",
        int(df["Su"].min()),
        int(df["Su"].max()),
        int(df["Su"].mean())
    )

    ys = st.sidebar.slider(
        "⚙️ Yield Strength",
        int(df["Sy"].min()),
        int(df["Sy"].max()),
        int(df["Sy"].mean())
    )

    elong = st.sidebar.slider(
        "🌸 Elongation",
        int(df["A5"].min()),
        int(df["A5"].max()),
        int(df["A5"].mean())
    )

    hb = st.sidebar.slider(
        "🧁 Brinell Hardness",
        int(df["Bhn"].min()),
        int(df["Bhn"].max()),
        int(df["Bhn"].mean())
    )

    young = st.sidebar.slider(
        "📏 Young Modulus",
        int(df["E"].min()),
        int(df["E"].max()),
        int(df["E"].mean())
    )

    corte = st.sidebar.slider(
        "🐹 Shear Modulus",
        int(df["G"].min()),
        int(df["G"].max()),
        int(df["G"].mean())
    )

    buscar = st.sidebar.button(
        "✨ Find Materials ✨"
    )

    if buscar:

        features = [
            "Su",
            "Sy",
            "A5",
            "Bhn",
            "E",
            "G"
        ]

        scaler = MinMaxScaler()

        X = scaler.fit_transform(df[features])

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

        mejores = df.iloc[indices].copy()

        mejores["Similarity %"] = [
            round(100 / (1 + d), 2)
            for d in distancias[0][indices]
        ]

        st.header("🎀 Suggested Materials")

        st.dataframe(
            mejores[
                [
                    "Material",
                    "Heat treatment",
                    "Similarity %"
                ]
            ],
            use_container_width=True
        )

        # =================================================
        # GRÁFICAS
        # =================================================

        st.header("📊 Interactive Comparison")

        fig = px.scatter(
            mejores,
            x="Bhn",
            y="Su",
            color="Material",
            size="Similarity %",
            text="Material"
        )

        fig.update_traces(
            textposition="top center"
        )

        fig.update_layout(
            paper_bgcolor="#fff0f5",
            plot_bgcolor="#fffafc",
            height=600
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # =================================================
        # RADAR
        # =================================================

        mejor = mejores.iloc[0]

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
            name='Desired'
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
            ),
            height=600
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

        # =================================================
        # APLICACIONES
        # =================================================

        st.header("🏭 Suggested Applications")

        aplicaciones = [

            "🚗 Automotive shafts and gears",

            "✈️ Aerospace structures",

            "🏗️ Bridges and industrial structures",

            "⚙️ High wear machine components",

            "🔩 Industrial tools and molds",

            "🚂 Railway components",

            "🏭 Pressure vessels and piping",

            "🛠️ Heavy machinery",

            "🚲 Bicycle and scooter frames",

            "🔧 Weldable structures"
        ]

        random.shuffle(aplicaciones)

        for app in aplicaciones[:5]:

            st.success(app)

# =========================================================
# TAB 2 — BUSCADOR
# =========================================================

with tab2:

    st.header("🔍 Smart Material Search")

    st.info("""
    🌸 Search in English or Spanish:

    Examples:
    - steel
    - silver
    - titanium
    - copper
    - aluminum
    - alloy
    - acero
    - aluminio
    """)

    busqueda = st.text_input(
        "💖 Search material"
    )

    if busqueda:

        traducciones = {

            "acero": "steel",
            "plata": "silver",
            "aluminio": "aluminum",
            "cobre": "copper",
            "titanio": "titanium",
            "hierro": "iron"
        }

        palabra = busqueda.lower()

        if palabra in traducciones:

            palabra = traducciones[palabra]

        resultados = df[
            df["Material"]
            .astype(str)
            .str.lower()
            .str.contains(
                palabra,
                na=False
            )
        ]

        if len(resultados) > 0:

            st.success(
                f"✨ {len(resultados)} materials found!"
            )

            for i in range(
                min(5, len(resultados))
            ):

                material = resultados.iloc[i]

                st.markdown(f"""
                <div class="cute-box">

                <h3>🌸 {material['Material']}</h3>

                💪 Ultimate Strength: {material['Su']}  
                ⚙️ Yield Strength: {material['Sy']}  
                🌸 Elongation: {material['A5']}  
                🧁 Hardness: {material['Bhn']}  

                🏭 Suggested use:
                Industrial structures, machinery,
                tools and mechanical components.

                </div>
                """, unsafe_allow_html=True)

        else:

            st.error(
                "❌ No materials found"
            )

# =========================================================
# TAB 3 — JUEGO
# =========================================================

with tab3:

    st.header("🎮 Guess The Material!")

    materiales = [

        {
            "pista":
            "✨ Lightweight and used in airplanes",
            "respuesta":
            "aluminum"
        },

        {
            "pista":
            "💎 Very resistant and corrosion resistant",
            "respuesta":
            "stainless steel"
        },

        {
            "pista":
            "⚡ Excellent electrical conductor",
            "respuesta":
            "copper"
        },

        {
            "pista":
            "🚀 Strong and lightweight aerospace metal",
            "respuesta":
            "titanium"
        }

    ]

    juego = random.choice(materiales)

    st.markdown(f"""
    <div class="cute-box">

    ### 🐰 Clue:

    {juego['pista']}

    </div>
    """, unsafe_allow_html=True)

    respuesta = st.text_input(
        "🎀 Your answer"
    )

    if st.button("✨ Check answer ✨"):

        if respuesta.lower() == juego["respuesta"]:

            st.balloons()

            st.success("""
            🌸 CORRECT 🌸

            You are officially a material science bunny engineer 🐰✨
            """)

        else:

            st.error(f"""
            ❌ Nope bestie 😭

            Correct answer:
            {juego['respuesta']}
            """)
