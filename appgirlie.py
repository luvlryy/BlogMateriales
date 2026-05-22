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

@st.cache_data
def load_data():
    # Usamos el archivo que nos mencionaste
    df = pd.read_excel("Data_convertido.xlsx")
    df.columns = df.columns.astype(str).str.strip()
    return df

df = load_data()

# =========================================================
# COLUMNAS NUMERICAS
# =========================================================

columnas_numericas = ["Su", "Sy", "A5", "Bhn", "E", "G"]

for col in columnas_numericas:
    df[col] = pd.to_numeric(df[col], errors="coerce")

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
    background: linear-gradient(180deg, #ffd8ee 0%, #ffeefe 25%, #fff7fb 55%, #f2fff7 100%);
    background-attachment: fixed;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #ff7dbf, #ffc9e4);
    border-right: 6px solid #ff4f9a;
}

/* TITULO */
h1 {
    color: #ff2f92 !important;
    text-align: center;
    font-size: 65px !important;
    text-shadow: 3px 3px white, 6px 6px #ffb7d5;
    background: white;
    border: 6px solid #ff8dc5;
    border-radius: 35px;
    padding: 20px;
    box-shadow: 0px 0px 25px rgba(255,105,180,0.5);
}

/* CAJAS */
.cute-box {
    background: linear-gradient(180deg, #fff7fb, #ffe3f2);
    border: 5px solid #ff9cc8;
    border-radius: 30px;
    padding: 25px;
    margin-bottom: 25px;
    box-shadow: 0 0 20px rgba(255,105,180,0.35);
}

/* EXPANDERS (BLOG GOSSIP) */
.streamlit-expanderHeader {
    font-size: 20px !important;
    color: #ff2f92 !important;
    background-color: #ffe3f2 !important;
    border-radius: 15px !important;
    border: 3px solid #ff9cc8 !important;
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
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.title("💖 MATERIAL GIRL ONLINE 💖")

st.markdown("""
<div class="cute-box">
<h2 style="text-align:center; color:#ff4fa1;">✨ Bienvenida al laboratorio más fabuloso del internet ✨</h2>
<p style="text-align:center; font-size:18px;">
💿 Encuentra materiales | 💅 Aprende propiedades | 🧪 Descubre tratamientos térmicos <br> 🎮 Juega y desbloquea | 📰 Lee chismecitos metalúrgicos 
</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# IMAGENES Y2K (TUS IMÁGENES)
# =========================================================

col1, col2, col3 = st.columns(3)

with col1:
    try:
        st.image("IMG_6304.JPG", caption="💖 That's hot")
    except:
        st.error("Falta IMG_6304.JPG")

with col2:
    try:
        st.image("IMG_6305.JPG", caption="✨ Aesthetic vibes")
    except:
        st.error("Falta IMG_6305.JPG")

with col3:
    st.image("https://i.pinimg.com/736x/70/2f/79/702f79b3af8f60f8914a14e24f17f9f5.jpg", caption="💅 Material World")

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "💖 Recomendador",
    "🔍 Buscador bilingüe",
    "📰 Material Gossip",
    "🎮 Juego"
])

# =========================================================
# TAB 1: RECOMENDADOR (Intacto, solo ajusté diseño)
# =========================================================

with tab1:
    st.header("💅 Material Match AI")
    st.sidebar.title("🎀 Configura tu material")

    uts = st.sidebar.slider("💪 Resistencia máxima (Su)", int(df["Su"].min()), int(df["Su"].max()), int(df["Su"].mean()))
    ys = st.sidebar.slider("⚙️ Límite elástico (Sy)", int(df["Sy"].min()), int(df["Sy"].max()), int(df["Sy"].mean()))
    elong = st.sidebar.slider("🌸 Elongación (A5)", int(df["A5"].min()), int(df["A5"].max()), int(df["A5"].mean()))
    hb = st.sidebar.slider("🧁 Dureza (Bhn)", int(df["Bhn"].min()), int(df["Bhn"].max()), int(df["Bhn"].mean()))
    young = st.sidebar.slider("📏 Módulo Young (E)", int(df["E"].min()), int(df["E"].max()), int(df["E"].mean()))
    corte = st.sidebar.slider("🐰 Módulo cortante (G)", int(df["G"].min()), int(df["G"].max()), int(df["G"].mean()))

    if st.sidebar.button("✨ Encontrar materiales ✨"):
        features = ["Su", "Sy", "A5", "Bhn", "E", "G"]
        scaler = MinMaxScaler()
        X = scaler.fit_transform(df[features])
        usuario = scaler.transform([[uts, ys, elong, hb, young, corte]])
        distancias = euclidean_distances(usuario, X)
        indices = np.argsort(distancias[0])[:5]
        mejores = df.iloc[indices].copy()
        mejores["Compatibilidad %"] = [round(100 / (1 + d), 2) for d in distancias[0][indices]]

        st.subheader("💖 Materiales que hacen 'Match' contigo")
        st.dataframe(mejores[["Material", "Heat treatment", "Compatibilidad %"]], use_container_width=True)

        fig = px.scatter(mejores, x="Bhn", y="Su", color="Material", size="Compatibilidad %", text="Material")
        fig.update_layout(paper_bgcolor="#fff0f7", plot_bgcolor="#fff8fc", height=500)
        st.plotly_chart(fig, use_container_width=True)

# =========================================================
# TAB 2: BUSCADOR BILINGÜE
# =========================================================

with tab2:
    st.header("🔍 Buscador / Search Engine")
    busqueda = st.text_input("💖 Busca un material (Ej: Acero, Steel, Cobre, Copper)")

    traducciones = {
        "acero": "steel", "plata": "silver", "aluminio": "aluminum",
        "cobre": "copper", "titanio": "titanium", "hierro": "iron",
        "oro": "gold", "aleacion": "alloy", "laton": "brass",
        "bronce": "bronze", "polimero": "polymer", "inoxidable": "stainless"
    }

    if busqueda:
        palabra = busqueda.lower().strip()
        if palabra in traducciones:
            palabra = traducciones[palabra]

        materiales_texto = df["Material"].astype(str).str.lower()
        resultados = df[materiales_texto.str.contains(palabra, na=False)]

        if len(resultados) > 0:
            st.success(f"✨ ¡OMG! Encontré {len(resultados)} materiales / Found {len(resultados)} materials")
            
            for i in range(min(5, len(resultados))):
                material = resultados.iloc[i]
                
                # Chisme dinámico según propiedades
                if material['Bhn'] > 200:
                    chisme = "¡Este material es súper duro! Literalmente impenetrable, cero red flags estructurales. 💅"
                elif material['A5'] > 20:
                    chisme = "Súper flexible y aesthetic. Se estira un montón sin romperse, ideal para cuando necesitas adaptabilidad. 🧘‍♀️"
                else:
                    chisme = "Un clásico. No le gusta llamar la atención pero hace el trabajo perfectamente. Muy demure, muy mindful. ✨"

                st.markdown(f"""
                <div class="cute-box">
                <h3 style="color:#ff2f92;">💖 {material['Material']}</h3>
                <p><b>⚙️ Tratamiento / Treatment:</b> {material['Heat treatment']}</p>
                <p><b>💪 Resistencia / Tensile Strength (Su):</b> {material['Su']} MPa</p>
                <p><b>🌸 Elongación / Elongation (A5):</b> {material['A5']}%</p>
                <p><b>🧁 Dureza / Hardness (Bhn):</b> {material['Bhn']} HB</p>
                <p><b>💅 Chismecito técnico:</b> {chisme}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error("❌ No encontré nada bestie. Try another word! 😭")

# =========================================================
# TAB 3: MATERIAL GOSSIP (ESTILO BLOG)
# =========================================================

with tab3:
    st.header("📰 MATERIAL GOSSIP")
    st.write("¡Dale click a los titulares para leer el chisme completo!")

    with st.expander("💅 ¡ESCÁNDALO! El Acero Inoxidable y la Corrosión ya NO se hablan"):
        st.write("""
        **XOXO, Gossip Girl.** Me enteré que el *Stainless Steel* bloqueó definitivamente a la Corrosión. 
        Gracias a su capa pasiva de óxido de cromo (mínimo 10.5%, reina), el acero inoxidable literalmente se volvió intocable. 
        La Corrosión intentó acercarse en un ambiente marino, pero fue totalmente ignorada. ¡Soporta! 💋
        """)

    with st.expander("✨ El Aluminio humilla al Acero en la báscula"):
        st.write("""
        ¡Las comparaciones son odiosas! Pero el *Aluminum* no para de presumir que su densidad (2.7 g/cm³) es casi un tercio 
        de la del Acero (7.8 g/cm³). Y aunque no es tan fuerte, el Aluminio dice que "la que es ligera, es ligera" y por eso 
        la industria aeroespacial lo prefiere. ¿Será que el Acero está *cancelled* para volar? ✈️
        """)

    with st.expander("⚡ El Cobre fue visto conduciendo altas corrientes a deshoras..."):
        st.write("""
        Fuentes cercanas confirman que el *Copper* sigue siendo el material más solicitado para conexiones eléctricas. 
        Aunque la Plata es técnicamente mejor conductora, resulta que es demasiado *high maintenance* y costosa. 
        Así que el Cobre se queda con el monopolio de los cables. ¡Mentalidad de tiburón! 🦈
        """)

    with st.expander("🧪 El Titanio: ¿Material exclusivo o simplemente sobrevalorado?"):
        st.write("""
        Todos sabemos que el *Titanium* es carísimo de procesar. Su biocompatibilidad lo hace el *sugar daddy* de 
        los implantes médicos, pero muchos ingenieros se quejan de que es un dolor de cabeza maquinarlo. 
        ¿Vale la pena su alto ratio resistencia-peso o solo lo usamos para presumir presupuesto? 💅💸
        """)

# =========================================================
# TAB 4: JUEGO (MÁS LARGO Y DIVERTIDO)
# =========================================================

with tab4:
    st.header("🎮 Y2K MATERIAL POP QUIZ")
    
    preguntas = [
        {
            "pregunta": "✨ ¿Qué material es famoso por ser súper ligero y tener pase VIP en la industria aeroespacial?",
            "opciones": ["Titanio", "Aluminio", "Plomo"],
            "correcta": "Aluminio",
            "dato": "💖 ¡Slay! El aluminio es súper ligero (densidad baja) y por eso los aviones lo aman."
        },
        {
            "pregunta": "⚡ Si tienes que hacer una instalación eléctrica y no eres millonaria para usar plata, ¿a quién llamas?",
            "opciones": ["Cobre", "Acero", "Madera"],
            "correcta": "Cobre",
            "dato": "⚡ ¡Obvio! El cobre es el bestie indiscutible de la conductividad eléctrica y el presupuesto."
        },
        {
            "pregunta": "💎 ¿Cuál es el material con la 'red flag' de ser súper pesado y hasta tóxico, al punto que lo cancelaron de las pinturas y gasolinas?",
            "opciones": ["Plomo", "Estaño", "Zinc"],
            "correcta": "Plomo",
            "dato": "☠️ ¡Canceladísimo! El plomo es densísimo y tóxico. Cero aesthetic hoy en día."
        },
        {
            "pregunta": "💅 ¿Qué material tiene un 'glow up' térmico al agregarle carbono, pasando de hierro aburrido a una estructura súper resistente?",
            "opciones": ["Acero", "Bronce", "Latón"],
            "correcta": "Acero",
            "dato": "🔥 ¡Yass! El hierro + carbono = Acero. El verdadero glow up de la metalurgia."
        },
        {
            "pregunta": "🛡️ ¿Cuál es la propiedad mecánica que mide si un material es 'flexible' y aguanta estirarse sin romperse (como tus excusas)?",
            "opciones": ["Dureza", "Elongación / Ductilidad", "Fatiga"],
            "correcta": "Elongación / Ductilidad",
            "dato": "🧘‍♀️ Correcto. Los metales dúctiles se pueden deformar plásticamente antes de fracturarse. ¡Aesthetic y funcional!"
        }
    ]

    # Estado para la pregunta actual
    if 'pregunta_actual' not in st.session_state:
        st.session_state.pregunta_actual = random.choice(preguntas)

    p = st.session_state.pregunta_actual

    st.markdown(f"""
    <div class="cute-box">
    <h3 style="color:#ff2f92;">{p['pregunta']}</h3>
    </div>
    """, unsafe_allow_html=True)

    respuesta = st.radio("💖 Selecciona la respuesta correcta:", p["opciones"])

    colA, colB = st.columns(2)
    
    with colA:
        if st.button("✨ Revisar respuesta ✨"):
            if respuesta == p["correcta"]:
                st.balloons()
                st.success(f"🌸 ¡CORRECTO REINA! 🌸\n\n{p['dato']}")
            else:
                st.error(f"❌ ¡No bestie, te equivocaste!\n\nLa respuesta era: {p['correcta']}")
    
    with colB:
        if st.button("🔄 Siguiente pregunta"):
            st.session_state.pregunta_actual = random.choice(preguntas)
            st.rerun()
