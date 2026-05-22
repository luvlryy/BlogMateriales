# =========================================================
# ✨ MATERIAL CHANNEL - 2004 EDITION ✨
# La página más cool del internet 💖
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
    page_title="Material Channel 🌟",
    page_icon="📺",
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
    st.error(f"¡Ups! Ocurrió un error al cargar los datos: {e}")
    st.stop()

columnas_numericas = ["Su", "Sy", "A5", "Bhn", "E", "G"]

for col in columnas_numericas:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df = df.dropna(subset=columnas_numericas)

# =========================================================
# CSS DISNEY CHANNEL 2000s VIBES 📺🌸
# =========================================================

st.markdown("""
<style>
/* Fuentes divertidas: Chewy para títulos, Nunito para texto */
@import url('https://fonts.googleapis.com/css2?family=Chewy&family=Nunito:wght@400;700&family=Comic+Neue:wght@700&display=swap');

html, body, [class*="css"] {
    font-family: 'Nunito', sans-serif;
    color: #4a4a4a;
}

/* FONDO AZUL CIELO CON BURBUJAS/PUNTITOS */
.stApp {
    background-color: #87CEFA; /* Azul cielo súper Disney */
    background-image: radial-gradient(#FFF 15%, transparent 16%), radial-gradient(#FFF 15%, transparent 16%);
    background-size: 40px 40px;
    background-position: 0 0, 20px 20px;
}

/* BARRA LATERAL MAGENTA */
section[data-testid="stSidebar"] {
    background-color: #FF69B4;
    border-right: 8px dashed #FFF;
}
section[data-testid="stSidebar"] * {
    color: white !important;
    font-family: 'Comic Neue', cursive;
}

/* TÍTULO PRINCIPAL (LOGO) */
h1 {
    font-family: 'Chewy', cursive;
    color: #FFD700 !important; /* Amarillo brillante */
    text-align: center;
    font-size: 80px !important;
    text-shadow: 4px 4px 0px #FF1493, 8px 8px 0px #FFFFFF; /* Sombra doble 3D */
    margin-bottom: 20px;
    letter-spacing: 3px;
    -webkit-text-stroke: 2px #FF1493;
}

/* SUBTÍTULOS GLOBALES */
h2, h3 {
    font-family: 'Chewy', cursive;
    color: #FF1493 !important;
    text-shadow: 2px 2px 0px #FFF;
    letter-spacing: 1px;
}

/* CAJAS ESTILO DISNEY (REDONDEADAS Y COLORIDAS) */
.disney-box {
    background-color: #FFFFFF;
    border: 6px solid #32CD32; /* Verde Lima */
    border-radius: 40px; /* Súper redondas */
    padding: 30px;
    margin-bottom: 30px;
    box-shadow: 8px 8px 0px #FF69B4; /* Sombra rosa sólida */
}

.disney-box-blue {
    background-color: #E0FFFF;
    border: 6px dashed #FF69B4;
    border-radius: 30px;
    padding: 20px;
    margin-bottom: 20px;
}

/* TABS (PESTAÑAS ESTILO CARPETAS ESCOLARES) */
.stTabs [data-baseweb="tab"] {
    font-family: 'Chewy', cursive;
    background-color: #FFB6C1;
    border: 4px solid #FFF;
    border-radius: 25px 25px 0 0;
    margin-right: 5px;
    padding: 15px 25px;
    font-size: 22px;
    color: #FFF !important;
    text-shadow: 2px 2px #FF1493;
}
.stTabs [aria-selected="true"] {
    background-color: #32CD32 !important; /* Verde lima al seleccionar */
    border-bottom: 4px solid #32CD32;
}

/* BOTONES GORDITOS DE GOMITA */
.stButton>button {
    background-color: #FFD700;
    color: #FF1493 !important;
    font-family: 'Chewy', cursive;
    font-size: 24px !important;
    border: 4px solid #FFF;
    border-radius: 50px;
    padding: 10px 20px;
    box-shadow: 0px 6px 0px #FF69B4;
    transition: all 0.2s;
}
.stButton>button:hover {
    transform: translateY(3px);
    box-shadow: 0px 3px 0px #FF69B4;
}

/* ENTRADA DE BLOG (DIARIO) */
.blog-entry {
    background-color: #FFFACD; /* Amarillo pastel */
    border: 5px solid #9370DB; /* Morado */
    border-radius: 30px;
    padding: 25px;
    margin-bottom: 40px;
    position: relative;
    box-shadow: 10px 10px 0px rgba(147, 112, 219, 0.4);
}
.blog-date {
    background-color: #FF1493;
    color: white;
    font-family: 'Comic Neue', cursive;
    font-weight: bold;
    padding: 5px 15px;
    border-radius: 20px;
    position: absolute;
    top: -15px;
    left: 20px;
    border: 3px solid #FFF;
}
.blog-title {
    font-family: 'Chewy', cursive;
    color: #32CD32;
    font-size: 28px;
    margin-top: 10px;
    border-bottom: 3px dashed #FF69B4;
    padding-bottom: 10px;
}

/* TARJETA DEL QUIZ */
.quiz-card {
    background: linear-gradient(135deg, #FF69B4, #9370DB);
    border: 6px solid #FFF;
    border-radius: 40px;
    padding: 40px;
    color: #FFF;
    text-align: center;
    box-shadow: 0px 10px 20px rgba(0,0,0,0.2);
    margin-bottom: 20px;
}
.quiz-question {
    font-family: 'Chewy', cursive;
    font-size: 35px;
    text-shadow: 2px 2px 0px #FF1493;
}
</style>
""", unsafe_allow_html=True)

# =========================================================
# HEADER
# =========================================================

st.title("🌟 MATERIAL CHANNEL 🌟")

st.markdown("""
<div class="disney-box">
<h2 style="text-align:center;">¡Estás viendo Material Channel! 📺✨</h2>
<p style="text-align:center; font-size:20px; font-family:'Comic Neue', cursive;">
La red más cool para buscar aleaciones, descubrir los secretos de los metales y divertirte al máximo. ¡Agarra tus palomitas y explora! 🍿💖
</p>
</div>
""", unsafe_allow_html=True)

# BANNER - ESPACIO PARA FOTO DISNEY (1200x300)
st.image("https://via.placeholder.com/1200x300/FF69B4/FFFFFF?text=FOTO+DEL+REPARTO+AQUI+💖", use_container_width=True)

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "✨ MATCH MAKER",
    "🔍 BUSCADOR COOL",
    "📖 MY BLOG",
    "🎮 QUIZ TIME!"
])

# =========================================================
# TAB 1: RECOMENDADOR
# =========================================================

with tab1:
    st.markdown("""
    <div class="disney-box-blue">
    <h3>💖 ¡Crea tu Aleación Perfecta!</h3>
    <p>Mueve los deslizadores de la izquierda para decirle al sistema qué tipo de material estás buscando. ¡Nosotros hacemos el match!</p>
    </div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown("<h2>🎀 Ajustes🎀</h2>", unsafe_allow_html=True)

    uts = st.sidebar.slider("💪 Resistencia (Su)", int(df["Su"].min()), int(df["Su"].max()), int(df["Su"].mean()))
    ys = st.sidebar.slider("⚙️ Límite elástico (Sy)", int(df["Sy"].min()), int(df["Sy"].max()), int(df["Sy"].mean()))
    elong = st.sidebar.slider("🌸 Elongación (A5)", int(df["A5"].min()), int(df["A5"].max()), int(df["A5"].mean()))
    hb = st.sidebar.slider("🧁 Dureza (Bhn)", int(df["Bhn"].min()), int(df["Bhn"].max()), int(df["Bhn"].mean()))
    young = st.sidebar.slider("📏 Módulo Young (E)", int(df["E"].min()), int(df["E"].max()), int(df["E"].mean()))
    corte = st.sidebar.slider("🐰 Módulo cortante (G)", int(df["G"].min()), int(df["G"].max()), int(df["G"].mean()))

    if st.sidebar.button("✨ ¡Hacer Match! ✨"):
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
        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="rgba(255,255,255,0.5)", height=500)
        st.plotly_chart(fig, use_container_width=True)

# =========================================================
# TAB 2: BUSCADOR
# =========================================================

with tab2:
    st.markdown("""
    <div class="disney-box-blue">
    <h3>🔍 Buscador Súper Secreto</h3>
    <p>Escribe el nombre del material, un tratamiento o un número y encontraremos el archivo. ¡Súper fácil!</p>
    </div>
    """, unsafe_allow_html=True)
    
    busqueda = st.text_input("📝 Escribe aquí...")

    if busqueda:
        mask = np.column_stack([df[col].astype(str).str.contains(busqueda, case=False, na=False) for col in df.columns])
        resultados = df.loc[mask.any(axis=1)]

        if len(resultados) > 0:
            st.success(f"🌟 ¡Yay! Encontramos {len(resultados)} resultados para ti.")
            
            for i in range(min(10, len(resultados))):
                material = resultados.iloc[i]
                
                st.markdown(f"""
                <div class="disney-box" style="border-color: #FF69B4; box-shadow: 5px 5px 0px #32CD32; padding: 20px;">
                <h3 style="margin-top:0;">✨ {material['Material']} ✨</h3>
                <p><b>Tratamiento:</b> {material['Heat treatment']}</p>
                <p><b>Dureza (Bhn):</b> {material['Bhn']} HB | <b>Resistencia (Su):</b> {material['Su']} MPa</p>
                <p><b>Elongación:</b> {material['A5']}%</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.error("😭 ¡Oh no! No encontramos nada con esa palabra. ¡Intenta otra!")

# =========================================================
# TAB 3: MY BLOG (ESTILO DIARIO 2000s)
# =========================================================

with tab3:
    st.markdown("<h2>📖 El Diario de Materiales</h2>", unsafe_allow_html=True)
    
    # ENTRADA 1
    st.markdown("""
    <div class="blog-entry">
        <div class="blog-date">Viernes, 14 de Mayo 2004</div>
        <div class="blog-title">OMG! El drama del Acero Inoxidable 😱</div>
        <p><b>¡Hola chicos! Bienvenidos a otro post.</b> Tienen que saber lo que pasó hoy. Literalmente el Hierro y la Corrosión cortaron para siempre. 💔</p>
        <p>Resulta que el Hierro se hizo súper amigo del Cromo (obvio, necesitaban mínimo un 10.5% de él). Y el Cromo, siendo el amigo sobreprotector que es, formó una "capa pasiva" de óxido alrededor del Acero. Ahora el Acero es "Inoxidable" y no deja que la corrosión se le acerque para nada. Se toparon en el puerto marítimo y ni se miraron. ¡Qué fuerte!</p>
        <p><i>XOXO, tu bestie de laboratorio. 💋</i></p>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x300/32CD32/FFFFFF?text=FOTO+AQUI", use_container_width=True)
    st.write("---")

    # ENTRADA 2
    st.markdown("""
    <div class="blog-entry">
        <div class="blog-date">Lunes, 17 de Mayo 2004</div>
        <div class="blog-title">Robo de Identidad: Bronce vs Latón 🕵️‍♀️</div>
        <p><b>¡Hey! Espero que su inicio de semana esté súper.</b> Hoy en chismes históricos: El Bronce está furiosísimo con el Latón.</p>
        <p>El Bronce (cobre + estaño) dice que es súper exclusivo y resistente, ¡hasta le dieron su propia era en la historia! Pero el Latón (cobre + zinc) es como el gemelo que copia el look. Es más barato, brilla dorado padrísimo y ahora está en todas las llaves y cerraduras del mundo. ¡Qué escándalo! El Latón se defiende diciendo que es mucho más fácil de tornear. ¿De qué team son ustedes?</p>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x300/FFD700/FFFFFF?text=FOTO+AQUI", use_container_width=True)
    st.write("---")

    # ENTRADA 3
    st.markdown("""
    <div class="blog-entry">
        <div class="blog-date">Jueves, 20 de Mayo 2004</div>
        <div class="blog-title">El Glow Up del Aluminio ✨✈️</div>
        <p><b>¡Adivinen quién está de moda!</b> Obvio, el Aluminio. Hace muchísimo tiempo era un metal súper raro y más caro que el oro. Pero ahora que aprendieron a procesarlo, es el rey de la escuela.</p>
        <p>Pesa casi un tercio de lo que pesa el pobre acero. Literalmente los aviones lo aman porque es súper ligerito pero aguanta muchísimo cuando le ponen magnesio o zinc. El Acero está un poquito celoso porque ya no lo invitan a volar tanto, pero bueno, ¡así es la vida!</p>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x300/87CEFA/FFFFFF?text=FOTO+AQUI", use_container_width=True)
    st.write("---")

    # ENTRADA 4
    st.markdown("""
    <div class="blog-entry">
        <div class="blog-date">Sábado, 22 de Mayo 2004</div>
        <div class="blog-title">Titanio: ¿Súper diva? 💅</div>
        <p><b>¡Fin de semana!</b> Y tenemos que hablar del Titanio. O sea, sí, es guapísimo estructuralmente, no pesa nada, aguanta todo y el cuerpo humano no lo rechaza (súper útil para los médicos).</p>
        <p>¿Pero sabían que trabajar con él es una pesadilla? Rompe las herramientas en los talleres, exige condiciones súper limpias para soldarse (literalmente se contamina con el aire normal). Muchos ingenieros dicen que es demasiado "high maintenance". ¿Vale la pena tanto show?</p>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x300/9370DB/FFFFFF?text=FOTO+AQUI", use_container_width=True)
    st.write("---")

    # ENTRADA 5
    st.markdown("""
    <div class="blog-entry">
        <div class="blog-date">Lunes, 24 de Mayo 2004</div>
        <div class="blog-title">El Plomo está CANCELADO 🚫</div>
        <p><b>Bad news para los materiales antiguos.</b> El Plomo fue literalmente desterrado. Antes estaba en todas partes: en la pintura de los cuartos, en el gas del coche, en las tuberías...</p>
        <p>Pero se descubrió que es súper tóxico para el cerebro. Así que le quitaron todos sus contratos y ahora solo lo tienen escondido en los hospitales cuidando a la gente de los Rayos X por lo denso que es. ¡Moraleja: no confíen en metales pesados!</p>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x300/FF1493/FFFFFF?text=FOTO+AQUI", use_container_width=True)
    st.write("---")

    # ENTRADA 6
    st.markdown("""
    <div class="blog-entry">
        <div class="blog-date">Miércoles, 26 de Mayo 2004</div>
        <div class="blog-title">Tungsteno: El chico malo 🔥</div>
        <p><b>¡Hola!</b> Hoy les traigo un dato súper random. ¿Conocen al Tungsteno? Es ese tipo rudo que literalmente no se derrite con nada. Su punto de fusión está arriba de los 3,400 °C. O sea, ¡qué calor!</p>
        <p>Lo usaban muchísimo en los foquitos viejos porque se calentaba sin romperse. Y si lo mezclas con carbón, hace herramientas que pueden cortar el metal como si fuera mantequilla. Es el más rudo de todos, sin duda.</p>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x300/32CD32/FFFFFF?text=FOTO+AQUI", use_container_width=True)
    st.write("---")

    # ENTRADA 7
    st.markdown("""
    <div class="blog-entry">
        <div class="blog-date">Viernes, 28 de Mayo 2004</div>
        <div class="blog-title">Grafeno: Puro chisme y nada de acción 🙄</div>
        <p><b>TGIF chicos!</b> Últimamente todo el mundo habla del Grafeno. Que si es el material del futuro, que si es mil veces más fuerte que el acero, que si va a cambiar nuestras vidas...</p>
        <p>Pero la verdad es que producirlo en grandes cantidades es carísimo y súper difícil. Mientras el Grafeno sigue posando para las portadas de revistas de ciencia, el Silicio es el que realmente hace todo el trabajo pesado en nuestras compus y celulares. ¡Más reconocimiento al Silicio, por favor!</p>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x300/FFD700/FFFFFF?text=FOTO+AQUI", use_container_width=True)
    st.write("---")

    # ENTRADA 8
    st.markdown("""
    <div class="blog-entry">
        <div class="blog-date">Domingo, 30 de Mayo 2004</div>
        <div class="blog-title">Pobre Cobre, necesita vacaciones 😴</div>
        <p><b>Domingo de descanso... excepto para el Cobre.</b> Literalmente él nos da vida a todos. Cables, celulares, teles, todo funciona gracias a él porque es un excelente conductor eléctrico.</p>
        <p>La plata es mejor conductora, pero cobra carísimo, así que el cobre hace todo el trabajo. Últimamente se anda sobrecalentando y le sale esa capita verde cuando se oxida (como la Estatua de la Libertad). ¡Mándenle buenas vibras!</p>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x300/87CEFA/FFFFFF?text=FOTO+AQUI", use_container_width=True)
    st.write("---")

    # ENTRADA 9
    st.markdown("""
    <div class="blog-entry">
        <div class="blog-date">Martes, 1 de Junio 2004</div>
        <div class="blog-title">Polímeros: Drama Ecológico 🌍</div>
        <p><b>¡Hola! Empezamos mes con un temazo.</b> Los plásticos (polímeros). En los 50s todos decían que eran la octava maravilla: baratos, flexibles, de colores bonitos...</p>
        <p>Pero oh sorpresa, la naturaleza no tiene idea de cómo destruirlos porque sus enlaces son súper fuertes. Ahora andan con campañas de reciclaje porque el Océano ya se quejó formalmente. Ojalá lo solucionen pronto.</p>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x300/9370DB/FFFFFF?text=FOTO+AQUI", use_container_width=True)
    st.write("---")

    # ENTRADA 10
    st.markdown("""
    <div class="blog-entry">
        <div class="blog-date">Jueves, 3 de Junio 2004</div>
        <div class="blog-title">El Oro es un fresa 👑</div>
        <p><b>Cerrando la semana de chismes.</b> ¿Sabían que el Oro es súper presumido? Es un "metal noble", lo que significa que no se oxida, no se mancha y no reacciona con nada.</p>
        <p>Pero la verdad es que es súper débil. Si haces un anillo 100% de oro, se va a aplastar súper rápido. Tiene que invitar a la plata y al cobre para que lo hagan más fuerte (eso es lo que significan los quilates). ¡Atrapado!</p>
    </div>
    """, unsafe_allow_html=True)
    st.image("https://via.placeholder.com/800x300/FF1493/FFFFFF?text=FOTO+AQUI", use_container_width=True)

# =========================================================
# TAB 4: QUIZ ZONE 🎮
# =========================================================

with tab4:
    st.markdown("<h2>🎮 ¡Demuestra qué tan fan eres!</h2>", unsafe_allow_html=True)
    
    preguntas = [
        {"q": "¿Qué material es el favorito de los aviones por no pesar casi nada?", "o": ["Titanio", "Aluminio", "Cobre"], "c": "Aluminio", "r": "¡Yay! El aluminio es súper ligerito."},
        {"q": "¿Qué se le echa al hierro para que se vuelva Acero y sea súper fuerte?", "o": ["Cromo", "Carbono", "Zinc"], "c": "Carbono", "r": "¡Así es! El carbono es el secreto mágico."},
        {"q": "Material top para hacer cables por ser súper buen conductor:", "o": ["Cobre", "Níquel", "Estaño"], "c": "Cobre", "r": "¡Obvio! El cobre es el rey de la electricidad barata."},
        {"q": "¿Qué propiedad nos dice si un material es súper estirable sin romperse?", "o": ["Dureza", "Elongación", "Fatiga"], "c": "Elongación", "r": "¡Bingo! La elongación o ductilidad lo hace como chicle."},
        {"q": "¿Qué metal hace que el acero se vuelva 'Inoxidable'?", "o": ["Níquel", "Vanadio", "Cromo"], "c": "Cromo", "r": "¡Correcto! El Cromo forma el escudito protector."},
        {"q": "¿De qué están hechas las medallas de tercer lugar? (Cobre + Estaño)", "o": ["Latón", "Bronce", "Alpaca"], "c": "Bronce", "r": "¡Súper! El Bronce es el material histórico."},
        {"q": "¿Con qué prueba mides qué tan fácil se raya o se hunde un metal?", "o": ["Tracción", "Charpy", "Dureza"], "c": "Dureza", "r": "¡Exacto! Las pruebas Brinell o Rockwell lo miden."},
        {"q": "El metal más resistente al calor, ideal para focos y herramientas rudas:", "o": ["Magnesio", "Tungsteno", "Plomo"], "c": "Tungsteno", "r": "¡Súper smart! El Tungsteno no se derrite con nada."},
        {"q": "Un plástico está hecho de cadenas larguísimas llamadas polímeros. ¿Cuál es la pieza más chiquita que los forma?", "o": ["Cristales", "Monómeros", "Isótopos"], "c": "Monómeros", "r": "¡Wow! Monómero más monómero igual a polímero."},
        {"q": "¿Qué metal acepta tan bien el cuerpo humano que lo usan para implantes?", "o": ["Titanio", "Acero al carbono", "Aluminio"], "c": "Titanio", "r": "¡Correcto! El titanio es el bestie de los médicos."}
    ]

    if 'pregunta_actual' not in st.session_state:
        st.session_state.pregunta_actual = random.choice(preguntas)

    p = st.session_state.pregunta_actual

    # TARJETA DEL QUIZ DISEÑO DISNEY
    st.markdown(f"""
    <div class="quiz-card">
        <div style="font-family:'Comic Neue'; font-size:20px; color:#FFE4E1; margin-bottom:10px;">✨ PREGUNTA ✨</div>
        <div class="quiz-question">{p['q']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<div style='background:#E0FFFF; border:4px dashed #32CD32; border-radius:20px; padding:20px;'>", unsafe_allow_html=True)
    respuesta = st.radio("👇 Elige tu respuesta súper cool 👇", p["o"])
    st.markdown("</div><br>", unsafe_allow_html=True)

    colA, colB = st.columns(2)
    with colA:
        if st.button("💖 REVISAR RESPUESTA 💖"):
            if respuesta == p["c"]:
                st.balloons()
                st.markdown(f"<div class='disney-box' style='border-color:#FFD700;'><h3>🌟 ¡WOW! SÚPER CORRECTO</h3><p style='font-size:20px;'>{p['r']}</p></div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='disney-box' style='border-color:#FF1493;'><h3>😭 UPS! CASI...</h3><p style='font-size:20px;'>Era {p['c']}. {p['r']}</p></div>", unsafe_allow_html=True)
                
    with colB:
        if st.button("⏭️ SIGUIENTE PREGUNTA ⏭️"):
            st.session_state.pregunta_actual = random.choice(preguntas)
            st.rerun()
