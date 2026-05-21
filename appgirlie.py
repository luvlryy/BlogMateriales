# =========================================================
# 💖 MATERIAL GIRL ONLINE 💖
# Y2K INTERNET MATERIALS WORLD ✨
# versión ultra aesthetic 2007
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
    page_title="Material Girl Online 💖",
    page_icon="💿",
    layout="wide"
)

# =========================================================
# CARGAR BASE DE DATOS
# =========================================================

df = pd.read_excel("Data_convertido.xlsx")

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
)

# =========================================================
# COLUMNAS NUMERICAS
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
# CSS Y2K EXTREMO
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Fredoka:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Fredoka', sans-serif;
}

/* FONDO */

.stApp {

    background:
    linear-gradient(
        180deg,
        #ffd8ee 0%,
        #ffeefe 25%,
        #fff7fb 55%,
        #f2fff7 100%
    );

    background-attachment: fixed;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #ff7dbf,
        #ffc9e4
    );

    border-right: 6px solid #ff4f9a;
}

/* TITULO */

h1 {

    color: #ff2f92 !important;

    text-align: center;

    font-size: 75px !important;

    text-shadow:
        3px 3px white,
        6px 6px #ffb7d5;

    background: white;

    border:
        6px solid #ff8dc5;

    border-radius: 35px;

    padding: 20px;

    box-shadow:
        0px 0px 25px rgba(255,105,180,0.5);
}

/* SUBTITULOS */

h2, h3 {

    color: #ff4fa1 !important;

    text-shadow: 2px 2px white;
}

/* CAJAS */

.cute-box {

    background:
    linear-gradient(
        180deg,
        #fff7fb,
        #ffe3f2
    );

    border: 5px solid #ff9cc8;

    border-radius: 30px;

    padding: 25px;

    margin-bottom: 25px;

    box-shadow:
        0 0 20px rgba(255,105,180,0.35);
}

/* BOTONES */

.stButton>button {

    background:
    linear-gradient(
        180deg,
        #ff5fad,
        #ff9bd0
    );

    color: white;

    border: 4px solid white;

    border-radius: 20px;

    font-size: 18px;

    font-weight: bold;

    height: 3.5em;

    width: 100%;

    box-shadow:
        0 4px 10px rgba(255,105,180,0.4);
}

/* INPUTS */

.stTextInput input {

    background: white;

    border:
        4px solid #ff9ed1 !important;

    border-radius: 18px !important;

    color: #ff2f92;
}

/* SLIDERS */

.stSlider {

    background: rgba(255,255,255,0.3);

    padding: 10px;

    border-radius: 20px;
}

/* TABS */

.stTabs [data-baseweb="tab"] {

    background: white;

    border-radius: 20px 20px 0px 0px;

    border: 4px solid #ff9ed1;

    margin-right: 10px;

    padding: 12px;

    font-size: 18px;

    color: #ff5ea8;
}

/* DATAFRAME */

[data-testid="stDataFrame"] {

    border:
        5px solid #ff9ed1;

    border-radius: 20px;
}

/* METRICS */

[data-testid="metric-container"] {

    background: white;

    border:
        4px solid #ffb3d9;

    border-radius: 25px;
}

/* SCROLLBAR */

::-webkit-scrollbar {

    width: 12px;
}

::-webkit-scrollbar-thumb {

    background: #ff8fc7;

    border-radius: 20px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.title("💖 MATERIAL GIRL ONLINE 💖")

st.markdown("""
<div class="cute-box">

<h2>✨ Bienvenida al laboratorio más fabuloso del internet ✨</h2>

💿 Encuentra materiales  
💅 Aprende propiedades  
🧪 Descubre tratamientos térmicos  
🎮 Juega y desbloquea materiales  
📰 Lee chismecitos metalúrgicos  

</div>
""", unsafe_allow_html=True)

# =========================================================
# IMAGENES Y2K
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.image(
        "https://i.pinimg.com/736x/5d/61/5e/5d615e6d05d8fd9dc3c4b3e6e8186f9f.jpg"
    )

with col2:
    st.image(
        "https://i.pinimg.com/736x/90/6c/8e/906c8e09b9a90c859f6fd16e6fdbd2e0.jpg"
    )

with col3:
    st.image(
        "https://i.pinimg.com/736x/70/2f/79/702f79b3af8f60f8914a14e24f17f9f5.jpg"
    )

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "💖 Recomendador",
    "🔍 Buscador",
    "📰 Material Gossip",
    "🎮 Juego"
])

# =========================================================
# TAB 1
# =========================================================

with tab1:

    st.header("💅 Material Match AI")

    st.sidebar.title("🎀 Configura tu material")

    uts = st.sidebar.slider(
        "💪 Resistencia máxima",
        int(df["Su"].min()),
        int(df["Su"].max()),
        int(df["Su"].mean())
    )

    ys = st.sidebar.slider(
        "⚙️ Límite elástico",
        int(df["Sy"].min()),
        int(df["Sy"].max()),
        int(df["Sy"].mean())
    )

    elong = st.sidebar.slider(
        "🌸 Elongación",
        int(df["A5"].min()),
        int(df["A5"].max()),
        int(df["A5"].mean())
    )

    hb = st.sidebar.slider(
        "🧁 Dureza",
        int(df["Bhn"].min()),
        int(df["Bhn"].max()),
        int(df["Bhn"].mean())
    )

    young = st.sidebar.slider(
        "📏 Módulo Young",
        int(df["E"].min()),
        int(df["E"].max()),
        int(df["E"].mean())
    )

    corte = st.sidebar.slider(
        "🐰 Módulo cortante",
        int(df["G"].min()),
        int(df["G"].max()),
        int(df["G"].mean())
    )

    buscar = st.sidebar.button(
        "✨ Encontrar materiales ✨"
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

        mejores["Compatibilidad %"] = [
            round(100 / (1 + d), 2)
            for d in distancias[0][indices]
        ]

        st.header("💖 Materiales recomendados")

        st.dataframe(
            mejores[
                [
                    "Material",
                    "Heat treatment",
                    "Compatibilidad %"
                ]
            ],
            use_container_width=True
        )

        fig = px.scatter(
            mejores,
            x="Bhn",
            y="Su",
            color="Material",
            size="Compatibilidad %",
            text="Material"
        )

        fig.update_layout(
            paper_bgcolor="#fff0f7",
            plot_bgcolor="#fff8fc",
            height=600
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# =========================================================
# TAB 2 BUSCADOR
# =========================================================

with tab2:

    st.header("🔍 Buscador inteligente")

    busqueda = st.text_input(
        "💖 Busca un material"
    )

    traducciones = {

        "acero": "steel",
        "plata": "silver",
        "aluminio": "aluminum",
        "cobre": "copper",
        "titanio": "titanium",
        "hierro": "iron",
        "oro": "gold",
        "aleacion": "alloy",
        "duro": "hard"
    }

    if busqueda:

        palabra = busqueda.lower()

        if palabra in traducciones:

            palabra = traducciones[palabra]

        materiales_texto = (
            df["Material"]
            .astype(str)
            .str.lower()
        )

        heat_texto = (
            df["Heat treatment"]
            .astype(str)
            .str.lower()
        )

        resultados = df[
            materiales_texto.str.contains(
                palabra,
                na=False
            )

            |

            heat_texto.str.contains(
                palabra,
                na=False
            )
        ]

        if len(resultados) > 0:

            st.success(
                f"✨ {len(resultados)} materiales encontrados"
            )

            for i in range(
                min(8, len(resultados))
            ):

                material = resultados.iloc[i]

                st.markdown(f"""
                <div class="cute-box">

                <h2>💖 {material['Material']}</h2>

                ⚙️ Tratamiento:
                {material['Heat treatment']}

                💪 Resistencia:
                {material['Su']}

                🌸 Elongación:
                {material['A5']}

                🧁 Dureza:
                {material['Bhn']}

                💅 Chismecito:
                Este material es fabuloso para
                componentes mecánicos y estructuras.

                </div>
                """, unsafe_allow_html=True)

        else:

            st.error("❌ No encontré nada bestie")

# =========================================================
# TAB 3 GOSSIP
# =========================================================

with tab3:

    st.header("📰 MATERIAL GOSSIP")

    chismes = [

        "💅 Stainless steel sigue siendo la reina de la corrosión.",

        "✨ Aluminum anda presumiendo que pesa menos que todos.",

        "🧪 Titanium volvió a ser visto en aplicaciones aeroespaciales.",

        "⚡ Copper literalmente no deja de conducir electricidad.",

        "🚗 Steel anda dominando automóviles otra vez."
    ]

    for c in chismes:

        st.markdown(f"""
        <div class="cute-box">

        <h3>{c}</h3>

        </div>
        """, unsafe_allow_html=True)

# =========================================================
# TAB 4 JUEGO
# =========================================================

with tab4:

    st.header("🎮 MATERIAL POP QUIZ")

    preguntas = [

        {
            "pregunta":
            "✨ ¿Qué material es famoso por ser ligero y usado en aviones?",

            "opciones":
            ["Titanium", "Aluminum", "Copper"],

            "correcta":
            "Aluminum",

            "dato":
            "💖 El aluminio es súper ligero y resistente."
        },

        {
            "pregunta":
            "⚡ ¿Cuál es excelente conductor eléctrico?",

            "opciones":
            ["Copper", "Steel", "Titanium"],

            "correcta":
            "Copper",

            "dato":
            "⚡ El cobre se usa muchísimo en cables."
        },

        {
            "pregunta":
            "💎 ¿Cuál es súper resistente a corrosión?",

            "opciones":
            ["Stainless Steel", "Lead", "Tin"],

            "correcta":
            "Stainless Steel",

            "dato":
            "✨ El acero inoxidable resiste corrosión increíblemente."
        }

    ]

    pregunta = random.choice(preguntas)

    st.markdown(f"""
    <div class="cute-box">

    <h2>{pregunta['pregunta']}</h2>

    </div>
    """, unsafe_allow_html=True)

    respuesta = st.radio(
        "💖 Escoge una opción",
        pregunta["opciones"]
    )

    if st.button("✨ Revisar respuesta ✨"):

        if respuesta == pregunta["correcta"]:

            st.balloons()

            st.success(f"""
            🌸 CORRECTO 🌸

            {pregunta['dato']}
            """)

        else:

            st.error(f"""
            ❌ Incorrecto bestie

            La respuesta era:
            {pregunta['correcta']}
            """)
