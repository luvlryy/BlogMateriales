# =========================================================
# 🌸 MATERIAL MATCH AI 🌸
# Pinky Matcha Latte Ultimate Edition 🐰🎀
# =========================================================

import streamlit as st
import pandas as pd
import numpy as np
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
# CSS GIRLIE ULTRA CUTE 🌸
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
        #fff0f6 30%,
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
    font-size: 65px !important;
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

/* Input */
.stTextInput>div>div>input {
    border-radius: 15px;
    border: 2px solid #ffb3c6;
}

/* Cute box */
.cute-box {
    background: rgba(255,255,255,0.75);
    border: 3px dashed #ffb3c6;
    border-radius: 25px;
    padding: 25px;
    margin-bottom: 20px;
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

### 🐰 Bienvenida al laboratorio más cute de materiales 🎀

✨ Busca materiales según propiedades mecánicas  
✨ Descubre aplicaciones reales  
✨ Explora materiales de ingeniería de forma divertida 💖

🌸 Matcha vibes + materiales + IA 🌸

</div>
""", unsafe_allow_html=True)

# =========================================================
# CARGAR EXCEL
# =========================================================

df = pd.read_excel("materiales_sin_aceros.xlsx")

# =========================================================
# LIMPIAR COLUMNAS
# =========================================================

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

tab1, tab2 = st.tabs([
    "🎀 Recomendador IA",
    "🔍 Buscar material"
])

# =========================================================
# TAB 1
# =========================================================

with tab1:

    st.header("💖 Encuentra materiales compatibles")

    # =====================================================
    # SIDEBAR
    # =====================================================

    st.sidebar.title("🎀 Propiedades deseadas")

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
        "🧁 Dureza Brinell",
        int(df["Bhn"].min()),
        int(df["Bhn"].max()),
        int(df["Bhn"].mean())
    )

    young = st.sidebar.slider(
        "📏 Módulo de Young",
        int(df["E"].min()),
        int(df["E"].max()),
        int(df["E"].mean())
    )

    corte = st.sidebar.slider(
        "🐹 Módulo de corte",
        int(df["G"].min()),
        int(df["G"].max()),
        int(df["G"].mean())
    )

    tratamiento = st.sidebar.selectbox(
        "🔥 Tratamiento térmico",
        ["Todos"] + sorted(
            df["Heat treatment"]
            .dropna()
            .astype(str)
            .unique()
        )
    )

    buscar = st.sidebar.button(
        "✨ Buscar materiales ✨"
    )

    # =====================================================
    # RECOMENDADOR
    # =====================================================

    if buscar:

        datos = df.copy()

        if tratamiento != "Todos":

            datos = datos[
                datos["Heat treatment"] == tratamiento
            ]

        features = [
            "Su",
            "Sy",
            "A5",
            "Bhn",
            "E",
            "G"
        ]

        scaler = MinMaxScaler()

        X = scaler.fit_transform(
            datos[features]
        )

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

        mejores = datos.iloc[indices].copy()

        mejores["Similitud %"] = [
            round(100 / (1 + d), 2)
            for d in distancias[0][indices]
        ]

        # =================================================
        # RESULTADOS
        # =================================================

        st.header("🎀 Materiales recomendados")

        st.dataframe(
            mejores[
                [
                    "Material",
                    "Heat treatment",
                    "Similitud %"
                ]
            ],
            use_container_width=True
        )

        # =================================================
        # TOP MATERIAL
        # =================================================

        mejor = mejores.iloc[0]

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "🌸 Material",
                mejor["Material"]
            )

        with col2:

            st.metric(
                "✨ Similitud",
                f"{mejor['Similitud %']}%"
            )

        with col3:

            st.metric(
                "🔥 Tratamiento",
                mejor["Heat treatment"]
            )

        # =================================================
        # SCATTER FUNCIONAL
        # =================================================

        st.header("📊 Comparación visual")

        fig = px.scatter(
            mejores,
            x="Bhn",
            y="Su",
            color="Material",
            size="Similitud %",
            hover_name="Material",
            text="Material"
        )

        fig.update_traces(
            textposition="top center"
        )

        fig.update_layout(
            paper_bgcolor="#fff0f5",
            plot_bgcolor="#fffafc",
            font=dict(size=14),
            height=600
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # =================================================
        # RADAR CHART
        # =================================================

        st.header("🌸 Radar de propiedades")

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
            name='Deseado'
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

        st.header("🧠 Aplicaciones sugeridas")

        aplicaciones = [

            "🚗 Componentes automotrices y ejes mecánicos",

            "✈️ Partes estructurales para aeronaves y maquinaria",

            "🏗️ Vigas, soportes y estructuras industriales",

            "⚙️ Engranes, tornillos y piezas de alto desgaste",

            "🔩 Herramientas industriales y moldes",

            "🚂 Sistemas ferroviarios y piezas sometidas a carga",

            "🏭 Tuberías industriales y recipientes de presión",

            "🛠️ Partes para maquinaria pesada",

            "🚲 Componentes metálicos para bicicletas y scooters",

            "🔧 Estructuras soldables y fabricación metálica"
        ]

        for app in aplicaciones[:5]:

            st.success(app)

# =========================================================
# TAB 2 — BUSCADOR
# =========================================================

with tab2:

    st.header("🔍 Buscar un material")

    st.info("""
    🌸 Puedes buscar materiales como:

    - Stainless steel
    - Alloy steel
    - Carbon steel
    - Titanium alloys
    - Aluminum alloys
    - Copper alloys
    """)

    busqueda = st.text_input(
        "💖 Escribe el nombre del material"
    )

    if busqueda:

        resultados = df[
            df["Material"]
            .astype(str)
            .str.contains(
                busqueda,
                case=False,
                na=False
            )
        ]

        if len(resultados) > 0:

            material = resultados.iloc[0]

            st.success(
                f"✨ Material encontrado: {material['Material']}"
            )

            # =============================================
            # INFO BREVE
            # =============================================

            st.markdown("""
            <div class="cute-box">

            🌸 Este material posee propiedades mecánicas útiles
            para aplicaciones industriales donde se requiere
            resistencia, durabilidad y estabilidad estructural.

            </div>
            """, unsafe_allow_html=True)

            # =============================================
            # PROPIEDADES
            # =============================================

            st.subheader("📋 Propiedades")

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "💪 Su",
                    material["Su"]
                )

                st.metric(
                    "⚙️ Sy",
                    material["Sy"]
                )

            with col2:

                st.metric(
                    "🌸 A5",
                    material["A5"]
                )

                st.metric(
                    "🧁 Bhn",
                    material["Bhn"]
                )

            with col3:

                st.metric(
                    "📏 E",
                    material["E"]
                )

                st.metric(
                    "🐹 G",
                    material["G"]
                )

            # =============================================
            # APLICACIÓN INDUSTRIAL
            # =============================================

            st.subheader("🏭 Aplicación industrial sugerida")

            if material["Su"] > 900:

                st.info("""
                💖 Recomendado para engranes,
                maquinaria pesada y componentes
                sometidos a esfuerzos elevados.
                """)

            elif material["A5"] > 25:

                st.info("""
                🌸 Excelente para estructuras soldables,
                fabricación metálica y piezas deformables.
                """)

            else:

                st.info("""
                🎀 Adecuado para aplicaciones
                mecánicas generales e industriales.
                """)

        else:

            st.error(
                "❌ No se encontró el material"
            )
