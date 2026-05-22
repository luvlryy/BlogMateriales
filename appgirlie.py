# =========================================================
# 🌐 CYBER MATERIALS LAB 2000 🌐
# Y2K WEB SURFER EDITION - V2.0
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
    page_title="Cyber Materials 2000",
    page_icon="💾",
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

df = load_data()

columnas_numericas = ["Su", "Sy", "A5", "Bhn", "E", "G"]
for col in columnas_numericas:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df = df.dropna(subset=columnas_numericas)

# =========================================================
# CSS RETRO Y2K / GEOCITIES VIBE
# =========================================================

st.markdown("""
<style>
/* Tipografía clásica de los 2000s */
html, body, [class*="css"] {
    font-family: 'Verdana', sans-serif;
}

/* Fondo oscuro cibernético */
.stApp {
    background-color: #000033;
    background-image: radial-gradient(circle, #000066 10%, transparent 11%), 
                      radial-gradient(circle, #000066 10%, transparent 11%);
    background-size: 20px 20px;
    background-position: 0 0, 10px 10px;
    color: #00FF00;
}

/* Sidebar tipo menú viejo */
section[data-testid="stSidebar"] {
    background-color: #C0C0C0;
    color: black;
    border-right: 4px outset #FFFFFF;
}
.stSidebar p, .stSidebar div, .stSidebar span, .stSidebar label {
    color: black !important;
}

/* Título de la página */
h1 {
    font-family: 'Comic Sans MS', cursive;
    color: #FFFF00 !important;
    text-align: center;
    font-size: 55px !important;
    text-shadow: 3px 3px #FF0000;
    border: 4px outset #FFFFFF;
    background-color: #000080;
    padding: 15px;
}

/* Cajas tipo Windows 95/98 */
.retro-box {
    background-color: #C0C0C0;
    color: black;
    border: 4px outset #FFFFFF;
    padding: 20px;
    margin-bottom: 25px;
    font-family: 'Tahoma', sans-serif;
}
.retro-box h2, .retro-box h3 {
    color: #000080 !important;
    border-bottom: 2px solid #000080;
    padding-bottom: 5px;
}

/* Etiquetas y expanders */
.streamlit-expanderHeader {
    background-color: #000080 !important;
    color: #FFFF00 !important;
    font-family: 'Courier New', Courier, monospace;
    font-weight: bold;
    border: 2px outset #FFFFFF !important;
}

.stTabs [data-baseweb="tab"] {
    background-color: #C0C0C0;
    border: 3px outset #FFFFFF;
    color: black;
    font-weight: bold;
}
.stTabs [aria-selected="true"] {
    background-color: #000080;
    color: #FFFF00 !important;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.title("🌐 CYBER MATERIALS LAB 2000 🌐")

# Etiqueta Marquee clásica de los 2000s
st.markdown("""
<marquee style="font-size: 20px; color: #00FF00; font-family: 'Courier New';">
+++ BIENVENIDO AL DIRECTORIO DE MATERIALES V2.0 +++ NAVEGA CON PRECAUCIÓN +++ ÚLTIMA ACTUALIZACIÓN: AÑO 2007 +++
</marquee>
""", unsafe_allow_html=True)

st.markdown("""
<div class="retro-box">
<h2 style="text-align:center;">🖥️ Portal Principal de Ingeniería</h2>
<p style="text-align:center;">
[ BUSCAR MATERIALES ] | [ CALCULAR PROPIEDADES ] | [ NOTICIAS METALÚRGICAS ] | [ FORO DE USUARIOS ]
</p>
</div>
""", unsafe_allow_html=True)

# =========================================================
# 📸 AQUI VA TU IMAGEN - SECCIÓN HEADER (3 COLUMNAS)
# TAMAÑO SUGERIDO: 300x300 px (Formato Cuadrado 1:1)
# =========================================================
col1, col2, col3 = st.columns(3)

with col1:
    # Cambia "foto_1.jpg" por el nombre de tu archivo
    st.image("https://via.placeholder.com/300x300.png?text=FOTO+AQUI", caption="💾 Base de datos online")

with col2:
    # Cambia "foto_2.jpg" por el nombre de tu archivo
    st.image("https://via.placeholder.com/300x300.png?text=FOTO+AQUI", caption="⚡ Alta tecnología")

with col3:
    # Cambia "foto_3.jpg" por el nombre de tu archivo
    st.image("https://via.placeholder.com/300x300.png?text=FOTO+AQUI", caption="🔬 Análisis estructural")

# =========================================================
# TABS PRINCIPALES
# =========================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "💻 Calculadora IA",
    "🔍 Motor de Búsqueda",
    "📰 Tech Gossip",
    "🕹️ Arcade Quiz"
])

# =========================================================
# TAB 1: RECOMENDADOR
# =========================================================

with tab1:
    st.header("💻 Calculadora de Similitud Material")
    
    st.sidebar.markdown("### 🎛️ Panel de Control")
    uts = st.sidebar.slider("Resistencia Máxima (Su)", int(df["Su"].min()), int(df["Su"].max()), int(df["Su"].mean()))
    ys = st.sidebar.slider("Límite Elástico (Sy)", int(df["Sy"].min()), int(df["Sy"].max()), int(df["Sy"].mean()))
    elong = st.sidebar.slider("Elongación % (A5)", int(df["A5"].min()), int(df["A5"].max()), int(df["A5"].mean()))
    hb = st.sidebar.slider("Dureza Brinell (Bhn)", int(df["Bhn"].min()), int(df["Bhn"].max()), int(df["Bhn"].mean()))
    young = st.sidebar.slider("Módulo Young (E)", int(df["E"].min()), int(df["E"].max()), int(df["E"].mean()))
    corte = st.sidebar.slider("Módulo Cortante (G)", int(df["G"].min()), int(df["G"].max()), int(df["G"].mean()))

    if st.sidebar.button("▶ Ejecutar Análisis"):
        features = ["Su", "Sy", "A5", "Bhn", "E", "G"]
        scaler = MinMaxScaler()
        X = scaler.fit_transform(df[features])
        usuario = scaler.transform([[uts, ys, elong, hb, young, corte]])
        distancias = euclidean_distances(usuario, X)
        indices = np.argsort(distancias[0])[:5]
        mejores = df.iloc[indices].copy()
        mejores["Similitud %"] = [round(100 / (1 + d), 2) for d in distancias[0][indices]]

        st.subheader("📊 Resultados del Sistema")
        st.dataframe(mejores[["Material", "Heat treatment", "Similitud %"]], use_container_width=True)

        # Gráfico adaptado a colores oscuros
        fig = px.scatter(mejores, x="Bhn", y="Su", color="Material", size="Similitud %", text="Material")
        fig.update_layout(paper_bgcolor="#C0C0C0", plot_bgcolor="#FFFFFF", height=500)
        st.plotly_chart(fig, use_container_width=True)

# =========================================================
# TAB 2: BUSCADOR (CORREGIDO)
# =========================================================

with tab2:
    st.header("🔍 Motor de Búsqueda Web 2.0")
    
    st.markdown("""
    <div class="retro-box">
    Ingrese su término de búsqueda (ej. Steel, Acero, Annealed, Aluminum). El motor buscará coincidencias exactas y parciales.
    </div>
    """, unsafe_allow_html=True)

    busqueda = st.text_input("Término de búsqueda:")

    traducciones = {
        "acero": "steel", "plata": "silver", "aluminio": "aluminum",
        "cobre": "copper", "titanio": "titanium", "hierro": "iron",
        "oro": "gold", "aleacion": "alloy", "laton": "brass",
        "bronce": "bronze", "polimero": "polymer", "inoxidable": "stainless"
    }

    if busqueda:
        # Limpieza de entrada
        palabra = busqueda.lower().strip()
        
        # Check de traducción
        if palabra in traducciones:
            palabra = traducciones[palabra]

        # Búsqueda robusta en las columnas de interés (ignorando mayúsculas y NaNs)
        mask_material = df["Material"].astype(str).str.lower().str.contains(palabra, na=False)
        mask_tratamiento = df["Heat treatment"].astype(str).str.lower().str.contains(palabra, na=False)
        
        resultados = df[mask_material | mask_tratamiento]

        if len(resultados) > 0:
            st.success(f"✔️ Búsqueda exitosa: Se encontraron {len(resultados)} registros.")
            
            for i in range(min(10, len(resultados))):
                material = resultados.iloc[i]

                st.markdown(f"""
                <div class="retro-box">
                <h3>📁 {material['Material']}</h3>
                <p><b>Tratamiento Térmico:</b> {material['Heat treatment']}</p>
                <ul>
                    <li><b>Resistencia (Su):</b> {material['Su']} MPa</li>
                    <li><b>Límite (Sy):</b> {material['Sy']} MPa</li>
                    <li><b>Elongación:</b> {material['A5']}%</li>
                    <li><b>Dureza:</b> {material['Bhn']} HB</li>
                </ul>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error("❌ ERROR 404: Material no encontrado en la base de datos.")

# =========================================================
# TAB 3: TECH GOSSIP (NOTICIAS / ESCÁNDALOS)
# =========================================================

with tab3:
    st.header("📰 TECH GOSSIP: El Foro de la Verdad")
    st.write("Bienvenido al foro. Haz clic en los hilos para desplegar la información.")

    # NOTICIA 1
    with st.expander("🚨 EL ESCÁNDALO DE LA SEMANA: ¿Fraude en la Industria Aeronáutica?"):
        # 📸 AQUI VA TU IMAGEN 1 - TAMAÑO: 600x400 px
        st.image("https://via.placeholder.com/600x400.png?text=FOTO+ESCANDALO+1", caption="Foros de aviación arden tras la revelación.")
        
        st.write("""
        **Posteado por: CyberEngineer99 a las 03:42 AM**
        
        Se filtraron documentos que indican que varios proveedores están sustituyendo **Aleaciones de Titanio (Ti-6Al-4V)** por grados inferiores de aluminio modificados en ciertos componentes no críticos de turbinas. 
        
        El problema es que la fatiga térmica no perdona. Mientras que el titanio mantiene sus propiedades a más de 400°C sin inmutarse, el aluminio comienza a ablandarse peligrosamente. Ingenieros de mantenimiento han reportado deformaciones anómalas (creep) en inspecciones rutinarias. ¿Estamos priorizando reducir costos de peso sobre la seguridad? La comunidad de metalurgia está furiosa.
        """)

    # NOTICIA 2
    with st.expander("⚠️ ÚLTIMA HORA: El Acero Inoxidable Serie 300 pierde su corona"):
        # 📸 AQUI VA TU IMAGEN 2 - TAMAÑO: 600x400 px
        st.image("https://via.placeholder.com/600x400.png?text=FOTO+ESCANDALO+2", caption="Corrosión intergranular detectada.")
        
        st.write("""
        **Posteado por: RustyMetal_XX a las 11:15 PM**
        
        Durante décadas nos vendieron que los aceros inoxidables austeníticos (como el famoso 304) eran invulnerables a la corrosión. Sin embargo, un nuevo reporte en ambientes marinos extremos ha dejado expuesta su gran debilidad: la corrosión por picaduras (pitting) debido a los iones de cloruro.
        
        Laboratorios independientes acaban de recomendar un cambio masivo hacia aceros Dúplex o Super Dúplex, que contienen mayor porcentaje de molibdeno y nitrógeno, haciéndolos verdaderos tanques blindados contra los cloruros. ¿Será este el fin de la era del 304 en la construcción costera?
        """)

    # NOTICIA 3
    with st.expander("📉 CAÍDA EN LA BOLSA: La crisis del Cobre"):
        # 📸 AQUI VA TU IMAGEN 3 - TAMAÑO: 600x400 px
        st.image("https://via.placeholder.com/600x400.png?text=FOTO+ESCANDALO+3", caption="Mercados de materias primas en rojo.")
        
        st.write("""
        **Posteado por: WallSt_Alchemist a las 09:30 AM**
        
        El auge de los vehículos eléctricos ha puesto al mundo al borde del abismo respecto a las reservas de Cobre. Al ser el principal conductor utilizado para bobinas de motores y cableado interno, la demanda superó en un 15% la producción minera mundial este trimestre.
        
        Rumores apuntan a que los grandes fabricantes están invirtiendo millones en I+D para utilizar **Aluminio recubierto** o incluso metamateriales basados en grafeno para puentear esta crisis. Si el aluminio logra desplazar al cobre en el cableado de potencia automotriz, estaríamos frente a la revolución de materiales más grande de la década.
        """)

# =========================================================
# TAB 4: JUEGO / ARCADE QUIZ
# =========================================================

with tab4:
    st.header("🕹️ ARCADE: TEST DE CONOCIMIENTO")
    
    st.markdown("""
    <div class="retro-box">
    Demuestra tus conocimientos técnicos. Fallar bajará tu rango en el foro.
    </div>
    """, unsafe_allow_html=True)

    preguntas = [
        {
            "pregunta": "[PREGUNTA 1]: En un tratamiento de Temple (Quenching) de acero, ¿qué estructura cristalina hiperdura se busca formar?",
            "opciones": ["Austenita", "Martensita", "Perlita", "Cementita"],
            "correcta": "Martensita",
            "dato": "CORRECTO. El enfriamiento rápido atrapa el carbono en una estructura tetragonal centrada en el cuerpo, generando Martensita, la fase más dura."
        },
        {
            "pregunta": "[PREGUNTA 2]: ¿Cuál es el límite termodinámico (aprox.) de temperatura de fusión del Tungsteno (Wolframio)?",
            "opciones": ["1,500 °C", "2,800 °C", "3,422 °C", "5,000 °C"],
            "correcta": "3,422 °C",
            "dato": "CORRECTO. El tungsteno tiene el punto de fusión más alto de todos los metales puros, ideal para filamentos incandescentes y toberas espaciales."
        },
        {
            "pregunta": "[PREGUNTA 3]: El proceso de recocido (Annealing) tiene como principal objetivo mecánico...",
            "opciones": ["Aumentar la dureza superficial", "Eliminar tensiones residuales y ablandar el material", "Proteger contra la oxidación"],
            "correcta": "Eliminar tensiones residuales y ablandar el material",
            "dato": "CORRECTO. El recocido regenera los granos del metal, aumentando su ductilidad y facilitando su mecanizado."
        }
    ]

    if 'pregunta_actual' not in st.session_state:
        st.session_state.pregunta_actual = random.choice(preguntas)

    p = st.session_state.pregunta_actual

    st.markdown(f"### {p['pregunta']}")

    respuesta = st.radio("SELECCIONE UNA OPCIÓN:", p["opciones"])

    colA, colB = st.columns(2)
    
    with colA:
        if st.button("ENVIAR RESPUESTA [ENTER]"):
            if respuesta == p["correcta"]:
                st.success(f"✅ ACCESO CONCEDIDO.\n\n{p['dato']}")
            else:
                st.error(f"❌ FALLO CRÍTICO.\n\nLa respuesta correcta es: {p['correcta']}")
    
    with colB:
        if st.button("CARGAR SIGUIENTE ARCHIVO >>"):
            st.session_state.pregunta_actual = random.choice(preguntas)
            st.rerun()
