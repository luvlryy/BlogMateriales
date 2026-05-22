# =========================================================
# 💋 MATERIAL GIRL BLOG - UPPER EAST SIDE EDITION 
# Estética Gossip Girl 2007 - Chic, Minimalista y Escandalosa
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
    page_title="Material Girl Blog",
    page_icon="💋",
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
    st.error(f"XOXO, tuvimos un problema cargando los secretos: {e}")
    st.stop()

columnas_numericas = ["Su", "Sy", "A5", "Bhn", "E", "G"]
for col in columnas_numericas:
    df[col] = pd.to_numeric(df[col], errors="coerce")
df = df.dropna(subset=columnas_numericas)

# =========================================================
# CSS GOSSIP GIRL ESTHETIC 💋🎩 (HTML INYECTADO)
# =========================================================

st.markdown("""
<style>
/* Importar tipografías elegantes (Playfair para títulos, Lora para texto, y Great Vibes para la firma) */
@import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Lora:ital,wght@0,400;0,700;1,400&family=Playfair+Display:ital,wght@0,400;0,700;1,400&display=swap');

html, body, [class*="css"] {
    font-family: 'Lora', serif;
    color: #1a1a1a;
    background-color: #fcfcfc;
}

/* FONDO CHIC MINIMALISTA */
.stApp {
    background-color: #fcfcfc;
}

/* BARRA LATERAL ELEGANTE */
section[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #e0e0e0;
}
section[data-testid="stSidebar"] * {
    font-family: 'Lora', serif;
}

/* TÍTULO PRINCIPAL GOSSIP GIRL */
.gg-header {
    text-align: center;
    border-bottom: 2px solid #1a1a1a;
    border-top: 2px solid #1a1a1a;
    padding: 20px 0;
    margin-bottom: 30px;
}
.gg-title {
    font-family: 'Playfair Display', serif;
    font-size: 65px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 5px;
    color: #1a1a1a;
    margin: 0;
}
.gg-subtitle {
    font-family: 'Lora', serif;
    font-style: italic;
    color: #8b0000; /* Rojo Borgoña */
    font-size: 20px;
    margin: 10px 0 0 0;
}

/* TABS: ESTILO NAVEGACIÓN DE REVISTA */
.stTabs [data-baseweb="tab"] {
    font-family: 'Playfair Display', serif;
    background-color: transparent;
    border: none;
    border-bottom: 2px solid transparent;
    padding: 10px 20px;
    font-size: 18px;
    color: #7a7a7a !important;
    text-transform: uppercase;
    letter-spacing: 2px;
}
.stTabs [aria-selected="true"] {
    color: #1a1a1a !important;
    border-bottom: 2px solid #8b0000 !important;
    font-weight: bold;
}

/* ENTRADAS DE BLOG (EL CHISME) */
.post-container {
    background-color: #ffffff;
    border: 1px solid #eaeaea;
    padding: 40px;
    margin-bottom: 40px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.03);
}
.post-date {
    font-family: 'Lora', serif;
    font-size: 14px;
    color: #8b0000;
    text-transform: uppercase;
    letter-spacing: 1px;
    margin-bottom: 10px;
}
.post-title {
    font-family: 'Playfair Display', serif;
    font-size: 32px;
    color: #1a1a1a;
    margin-bottom: 20px;
    line-height: 1.2;
}
.post-body {
    font-size: 18px;
    line-height: 1.8;
    color: #333333;
}
.spotted {
    font-family: 'Playfair Display', serif;
    font-weight: bold;
    font-style: italic;
    font-size: 20px;
}
.xoxo {
    font-family: 'Great Vibes', cursive;
    font-size: 35px;
    color: #8b0000;
    margin-top: 20px;
    display: block;
}

/* BOTONES ELEGANTE */
.stButton>button {
    background-color: #1a1a1a;
    color: #ffffff !important;
    font-family: 'Playfair Display', serif;
    text-transform: uppercase;
    letter-spacing: 2px;
    border: none;
    padding: 10px 20px;
    transition: all 0.3s ease;
}
.stButton>button:hover {
    background-color: #8b0000;
    color: #ffffff !important;
}

/* INPUTS DE BÚSQUEDA */
.stTextInput input {
    font-family: 'Lora', serif;
    border: none !important;
    border-bottom: 1px solid #1a1a1a !important;
    border-radius: 0 !important;
    background-color: transparent !important;
    font-size: 20px;
}
.stTextInput input:focus {
    box-shadow: none !important;
    border-bottom: 2px solid #8b0000 !important;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER GOSSIP GIRL
# =========================================================

st.markdown("""
<div class="gg-header">
    <h1 class="gg-title">Material Girl</h1>
    <p class="gg-subtitle">Tu única y mejor fuente sobre las escandalosas vidas de los metales.</p>
</div>
""", unsafe_allow_html=True)

# LÍNEA 168 - FOTO PANORÁMICA DE MANHATTAN / HIGH FASHION (1200x400)
st.image("https://via.placeholder.com/1200x400/1a1a1a/ffffff?text=FOTO+ELEGANTE+DEL+UPPER+EAST+SIDE+AQUI", use_container_width=True)

# =========================================================
# TABS (REVISTA)
# =========================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "The Matchmaker",
    "The Archives",
    "Latest Gossip",
    "Pop Quiz"
])

# =========================================================
# TAB 1: THE MATCHMAKER (RECOMENDADOR)
# =========================================================

with tab1:
    st.markdown("<h2 style='font-family:Playfair Display;'>The Perfect Match</h2>", unsafe_allow_html=True)
    st.write("Dime qué buscas en una aleación y te diré quién es tu pareja ideal. No aceptamos conformismos en el Upper East Side.")

    st.sidebar.markdown("<h3 style='font-family:Playfair Display; color:#8b0000;'>Tus Estándares</h3>", unsafe_allow_html=True)

    uts = st.sidebar.slider("Resistencia Máxima (Su)", int(df["Su"].min()), int(df["Su"].max()), int(df["Su"].mean()))
    ys = st.sidebar.slider("Límite Elástico (Sy)", int(df["Sy"].min()), int(df["Sy"].max()), int(df["Sy"].mean()))
    elong = st.sidebar.slider("Elongación (A5)", int(df["A5"].min()), int(df["A5"].max()), int(df["A5"].mean()))
    hb = st.sidebar.slider("Dureza (Bhn)", int(df["Bhn"].min()), int(df["Bhn"].max()), int(df["Bhn"].mean()))
    young = st.sidebar.slider("Módulo Young (E)", int(df["E"].min()), int(df["E"].max()), int(df["E"].mean()))
    corte = st.sidebar.slider("Módulo Cortante (G)", int(df["G"].min()), int(df["G"].max()), int(df["G"].mean()))

    if st.sidebar.button("Encontrar a mi elegido"):
        features = ["Su", "Sy", "A5", "Bhn", "E", "G"]
        scaler = MinMaxScaler()
        X = scaler.fit_transform(df[features])
        usuario = scaler.transform([[uts, ys, elong, hb, young, corte]])
        distancias = euclidean_distances(usuario, X)
        indices = np.argsort(distancias[0])[:5]
        mejores = df.iloc[indices].copy()
        mejores["Compatibilidad %"] = [round(100 / (1 + d), 2) for d in distancias[0][indices]]

        st.dataframe(mejores[["Material", "Heat treatment", "Compatibilidad %"]], use_container_width=True)

        fig = px.scatter(mejores, x="Bhn", y="Su", color="Material", size="Compatibilidad %", text="Material")
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(0,0,0,0)", height=500)
        st.plotly_chart(fig, use_container_width=True)

# =========================================================
# TAB 2: THE ARCHIVES (BUSCADOR)
# =========================================================

with tab2:
    st.markdown("<h2 style='font-family:Playfair Display;'>The Archives</h2>", unsafe_allow_html=True)
    st.write("Ningún secreto está a salvo. Busca el nombre del material o tratamiento y desenterraremos su historial.")
    
    busqueda = st.text_input("¿A quién estamos investigando hoy?")

    if busqueda:
        mask = np.column_stack([df[col].astype(str).str.contains(busqueda, case=False, na=False) for col in df.columns])
        resultados = df.loc[mask.any(axis=1)]

        if len(resultados) > 0:
            st.markdown(f"<p style='color:#8b0000;'>Encontré {len(resultados)} secretos bien guardados...</p>", unsafe_allow_html=True)
            
            for i in range(min(10, len(resultados))):
                material = resultados.iloc[i]
                
                st.markdown(f"""
                <div style="border-left: 3px solid #8b0000; padding-left: 20px; margin-bottom: 20px;">
                    <h3 style="font-family:'Playfair Display'; margin-bottom:0;">{material['Material']}</h3>
                    <p style="margin-top:5px; color:#555;">
                        <b>Tratamiento:</b> {material['Heat treatment']}<br>
                        <b>Dureza:</b> {material['Bhn']} HB | <b>Resistencia:</b> {material['Su']} MPa
                    </p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error("No hay registros. Parece que alguien borró sus huellas.")

# =========================================================
# TAB 3: LATEST GOSSIP (BLOG ESTILO GOSSIP GIRL)
# =========================================================

with tab3:
    st.markdown("<h2 style='font-family:Playfair Display;'>Latest Gossip</h2>", unsafe_allow_html=True)
    
    # GOSSIP 1
    st.markdown("""
    <div class="post-container">
        <div class="post-date">21 de Mayo, 2026</div>
        <div class="post-title">El fin de una era tóxica: Acero Inoxidable y Corrosión.</div>
        <p class="post-body"><span class="spotted">Spotted:</span> La Corrosión llorando desconsolada en las escaleras del MET. Parece que el Hierro por fin entendió su valor y se consiguió a alguien mejor: el Cromo. Bastó un 10.5% de aleación para que el Cromo le formara una capa pasiva protectora que literal lo vuelve intocable. Vimos al Acero Inoxidable pavoneándose en un yate en los Hamptons, y la sal marina ni siquiera pudo arruinarle el brillo. Sorry, Corrosión, you're officially out.</p>
        <p class="post-body">¿Podrá el ambiente salino encontrar otra víctima? Yo creo que sí.</p>
        <span class="xoxo">You know you love me. XOXO, Material Girl.</span>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x400/e0e0e0/1a1a1a?text=FOTO+PAPARAZZI+AQUI", use_container_width=True)
    
    # GOSSIP 2
    st.markdown("""
    <div class="post-container">
        <div class="post-date">19 de Mayo, 2026</div>
        <div class="post-title">Escándalo en la Alta Sociedad: ¿Bronce o Latón?</div>
        <p class="post-body"><span class="spotted">Spotted:</span> El Latón paseándose por el Upper East Side usando piezas vintage que juraríamos le pertenecen al Bronce. El Bronce (Cobre y Estaño, la verdadera realeza que definió una era histórica) está furioso de que el Latón (Cobre y Zinc, un arribista) le robe su estética dorada para colarse en las decoraciones de interiores y tuberías baratas. El Latón se defiende diciendo que él es más dócil y fácil de maquinar. But darling, we all know cheap is never chic.</p>
        <span class="xoxo">XOXO, Material Girl.</span>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x400/e0e0e0/1a1a1a?text=FOTO+PAPARAZZI+AQUI", use_container_width=True)

    # GOSSIP 3
    st.markdown("""
    <div class="post-container">
        <div class="post-date">15 de Mayo, 2026</div>
        <div class="post-title">El Ozempic de la Metalurgia: El Aluminio vuela alto.</div>
        <p class="post-body"><span class="spotted">Word on the street:</span> El Aluminio se ha vuelto el material más cotizado de la industria aeroespacial. Con un peso que humilla al acero (casi un tercio de su densidad), este material pasó de ser más caro que el oro en el siglo XIX, a ser el rey de las nubes gracias a la electrólisis. El Acero está furioso en el gimnasio tratando de perder densidad, pero querida, la genética es la genética. No intentes volar si estás hecha para los cimientos.</p>
        <span class="xoxo">XOXO, Material Girl.</span>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x400/e0e0e0/1a1a1a?text=FOTO+PAPARAZZI+AQUI", use_container_width=True)

    # GOSSIP 4
    st.markdown("""
    <div class="post-container">
        <div class="post-date">12 de Mayo, 2026</div>
        <div class="post-title">Titanio: ¿High maintenance o simplemente inalcanzable?</div>
        <p class="post-body"><span class="spotted">Spotted:</span> El Titanio arruinando herramientas de corte en un taller en Brooklyn. Tiene la relación resistencia-peso de un dios y es tan biocompatible que los médicos lo adoran, pero... ¿su actitud? Intolerable. Exige ambientes libres de oxígeno para ser soldado y destruye los tornos que intentan darle forma. Los ingenieros lo toleran porque es rico y resistente, pero todas sabemos que trabajar con él es una pesadilla de relaciones públicas.</p>
        <span class="xoxo">XOXO, Material Girl.</span>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x400/e0e0e0/1a1a1a?text=FOTO+PAPARAZZI+AQUI", use_container_width=True)

    # GOSSIP 5
    st.markdown("""
    <div class="post-container">
        <div class="post-date">10 de Mayo, 2026</div>
        <div class="post-title">Plomo: Cancelado para siempre.</div>
        <p class="post-body"><span class="spotted">Breaking News:</span> La caída en desgracia del Plomo es oficial. Quien alguna vez fue la estrella de las tuberías romanas y la pintura de las altas esferas, hoy es un exiliado. Ser neurotóxico te cuesta la carrera, darling. Hoy en día solo le permiten trabajar absorbiendo radiación en los sótanos de los hospitales. Un final muy poco glamuroso para un metal tan pesado.</p>
        <span class="xoxo">XOXO, Material Girl.</span>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x400/e0e0e0/1a1a1a?text=FOTO+PAPARAZZI+AQUI", use_container_width=True)

    # GOSSIP 6
    st.markdown("""
    <div class="post-container">
        <div class="post-date">8 de Mayo, 2026</div>
        <div class="post-title">Tungsteno, el corazón de hielo.</div>
        <p class="post-body"><span class="spotted">Spotted:</span> Tungsteno riéndose en la cara de un horno industrial. Este chico literalmente no se derrite por nadie. Con un punto de fusión superior a los 3,400 °C, es el soltero empedernido de la tabla periódica. Solo se mezcla con el Carbono para romper los corazones (y las brocas) de otros metales más débiles. Frío, duro e intocable.</p>
        <span class="xoxo">XOXO, Material Girl.</span>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x400/e0e0e0/1a1a1a?text=FOTO+PAPARAZZI+AQUI", use_container_width=True)

    # GOSSIP 7
    st.markdown("""
    <div class="post-container">
        <div class="post-date">5 de Mayo, 2026</div>
        <div class="post-title">Grafeno: El 'Nepo Baby' de los materiales.</div>
        <p class="post-body"><span class="spotted">Word is:</span> El Grafeno tiene el mejor publicista del mundo. Nos prometió elevadores espaciales, baterías infinitas y ropa inteligente. En teoría es 200 veces más fuerte que el acero, pero a la hora de producirlo a escala real, es un desastre carísimo. Mientras él sale en las portadas de Nature, el Silicio es quien hace el trabajo sucio manteniendo nuestros celulares vivos. Stop trying to make Graphene happen, it's not going to happen.</p>
        <span class="xoxo">XOXO, Material Girl.</span>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x400/e0e0e0/1a1a1a?text=FOTO+PAPARAZZI+AQUI", use_container_width=True)

    # GOSSIP 8
    st.markdown("""
    <div class="post-container">
        <div class="post-date">3 de Mayo, 2026</div>
        <div class="post-title">Cobre al borde de un colapso nervioso.</div>
        <p class="post-body"><span class="spotted">Spotted:</span> El Cobre trabajando horas extras otra vez. Conduce la electricidad de toda la ciudad, nuestros dispositivos y nuestras vidas. Es el empleado del mes desde hace un siglo. Pero el cansancio se nota: se sobrecalienta por efecto Joule y empieza a desarrollar esa famosa pátina verde cuando no puede lidiar con la presión. Alguien dele unas vacaciones antes de que sus redes cristalinas colapsen.</p>
        <span class="xoxo">XOXO, Material Girl.</span>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x400/e0e0e0/1a1a1a?text=FOTO+PAPARAZZI+AQUI", use_container_width=True)

    # GOSSIP 9
    st.markdown("""
    <div class="post-container">
        <div class="post-date">1 de Mayo, 2026</div>
        <div class="post-title">Polímeros: Las amistades tóxicas que no se van.</div>
        <p class="post-body"><span class="spotted">Scandal:</span> Los plásticos. Llegaron en los 50s prometiendo ser la solución barata a todos nuestros problemas. Pero como esos invitados incómodos en una fiesta en los Hamptons, simplemente no saben cuándo irse. Sus enlaces covalentes son tan fuertes que la naturaleza no puede degradarlos. Ahora el Océano ha emitido una orden de restricción contra ellos. Awkward.</p>
        <span class="xoxo">XOXO, Material Girl.</span>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x400/e0e0e0/1a1a1a?text=FOTO+PAPARAZZI+AQUI", use_container_width=True)

    # GOSSIP 10
    st.markdown("""
    <div class="post-container">
        <div class="post-date">28 de Abril, 2026</div>
        <div class="post-title">Oro: Complejo de superioridad.</div>
        <p class="post-body"><span class="spotted">Spotted:</span> El Oro rehusándose a mezclarse con los plebeyos. Por ser un metal noble, no se oxida ni reacciona con el ambiente. Su corona está intacta. Pero, let's be real: estructuralmente es patético. Es tan blando que para salir en público en forma de joyería, tiene que llamar a la Plata y al Cobre para que le den algo de dureza. Mucho brillo, poco soporte.</p>
        <span class="xoxo">XOXO, Material Girl.</span>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x400/e0e0e0/1a1a1a?text=FOTO+PAPARAZZI+AQUI", use_container_width=True)

# =========================================================
# TAB 4: POP QUIZ 🎩
# =========================================================

with tab4:
    st.markdown("<h2 style='font-family:Playfair Display;'>Pop Quiz, Upper East Siders.</h2>", unsafe_allow_html=True)
    st.write("Demuestra que mereces estar en la lista VIP. Falla, y todo Manhattan se enterará.")
    
    preguntas = [
        {"q": "¿Qué material es el rey absoluto de la industria aeroespacial gracias a su dieta estricta de baja densidad?", "o": ["Titanio", "Aluminio", "Cobre"], "c": "Aluminio", "r": "El aluminio tiene una densidad de 2.7 g/cm³. Perfecto para volar alto."},
        {"q": "¿Quién es el invitado secreto del hierro que lo convierte en el poderoso Acero?", "o": ["Cromo", "Carbono", "Zinc"], "c": "Carbono", "r": "El carbono entra en los intersticios del hierro y le da la fuerza que necesita para brillar."},
        {"q": "El metal que monopoliza el cableado de élite por ser un conductor de primera (y más barato que la plata):", "o": ["Cobre", "Níquel", "Estaño"], "c": "Cobre", "r": "Cobre. Nadie conecta a la élite mejor que él."},
        {"q": "¿Qué propiedad define qué tanto drama (deformación) puede soportar un material antes de romperse por completo?", "o": ["Dureza", "Elongación", "Fatiga"], "c": "Elongación", "r": "Elongación. Ser dúctil significa saber adaptarse sin quebrarse."},
        {"q": "¿Quién le regaló al acero su icónica capa pasiva para volverlo inoxidable?", "o": ["Níquel", "Vanadio", "Cromo"], "c": "Cromo", "r": "El Cromo. La mejor defensa contra los chismes y la oxidación."},
        {"q": "El Bronce, el original. ¿De quiénes es hijo?", "o": ["Cobre y Zinc", "Cobre y Estaño", "Hierro y Carbono"], "c": "Cobre y Estaño", "r": "Cobre y Estaño. La mezcla histórica más exclusiva."},
        {"q": "Si quieres saber qué tan fácil es rayar la reputación de un material, le haces una prueba de:", "o": ["Tracción", "Impacto", "Dureza"], "c": "Dureza", "r": "Dureza. Solo los más fuertes sobreviven el indentador."},
        {"q": "El metal que se ríe del calor y tiene el punto de fusión más alto de la fiesta:", "o": ["Magnesio", "Tungsteno", "Plomo"], "c": "Tungsteno", "r": "Tungsteno. Nadie derrite su corazón."},
        {"q": "Los plásticos están formados por polímeros, pero ¿quiénes son sus peones básicos?", "o": ["Cristales", "Monómeros", "Isótopos"], "c": "Monómeros", "r": "Monómeros. Se unen para formar el imperio del plástico."},
        {"q": "El metal tan exclusivo y biocompatible que el propio cuerpo humano le abre las puertas en los quirófanos:", "o": ["Titanio", "Acero al carbono", "Aluminio"], "c": "Titanio", "r": "Titanio. Caro, difícil de tratar, pero indispensable en la medicina."}
    ]

    if 'pregunta_actual' not in st.session_state:
        st.session_state.pregunta_actual = random.choice(preguntas)

    p = st.session_state.pregunta_actual

    st.markdown(f"""
    <div style="background-color: #ffffff; border: 1px solid #1a1a1a; padding: 30px; margin-bottom: 20px;">
        <h3 style="font-family:'Playfair Display'; color:#8b0000; margin-top:0;">{p['q']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    respuesta = st.radio("Tu respuesta final:", p["o"])

    colA, colB = st.columns(2)
    with colA:
        if st.button("Enviar Respuesta"):
            if respuesta == p["c"]:
                st.markdown(f"<div style='padding:15px; border-left:4px solid #8b0000; background:#f9f9f9;'><span class='spotted'>Spotted:</span> Un genio trabajando. {p['r']}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div style='padding:15px; border-left:4px solid #1a1a1a; background:#f9f9f9;'><span class='spotted'>Uh oh...</span> Alguien no hizo su tarea. Era {p['c']}. {p['r']}</div>", unsafe_allow_html=True)
                
    with colB:
        if st.button("Siguiente Escándalo"):
            st.session_state.pregunta_actual = random.choice(preguntas)
            st.rerun()
            
