import streamlit as st

# Configuração da página
st.set_page_config(layout="centered")

# Função de autenticação
def autenticar(usuario, senha):
    return usuario == "marcelo" and senha == "369"

# Inicializa variáveis de sessão
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False
if "canal" not in st.session_state:
    st.session_state.canal = None
if "link" not in st.session_state:
    st.session_state.link = None
if "guia" not in st.session_state:
    st.session_state.guia = None

# Tela de login
if not st.session_state.autenticado:


    st.markdown("""
        <style>
        .login-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding-top: 100px;
        }
        .login-title {
            font-size: 32px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="login-container">', unsafe_allow_html=True)
    st.markdown('<div class="login-title">🔐 Login</div>', unsafe_allow_html=True)

    with st.form("login_form", clear_on_submit=False):
        usuario = st.text_input("Usuário", label_visibility="collapsed", placeholder="Usuário")
        senha = st.text_input("Senha", type="password", label_visibility="collapsed", placeholder="Senha")
        entrar = st.form_submit_button("🚪 Entrar")
        if entrar:
            if autenticar(usuario, senha):
                st.session_state.autenticado = True
                st.success("Login realizado com sucesso!")
                st.rerun()
            else:
                st.error("Usuário ou senha incorretos.")
    st.markdown('</div>', unsafe_allow_html=True)
    st.stop()

# Dicionário de canais por categoria
categorias = {
    "🎬 HBO": {
        "HBO": ["https://redecanaistv.sh/assistir-hbo-online-24-horas-ao-vivo_d1160d077.html", "https://mi.tv/br/canais/hbo"],
        "HBO 2": ["https://redecanaistv.sh/assistir-hbo-2-online-24-horas-ao-vivo_8c78a7e25.html", "https://mi.tv/br/canais/hbo-2"],
        "HBO Family": ["https://redecanaistv.sh/assistir-hbo-family-online-24-horas-ao-vivo_b5ced4611.html", "https://mi.tv/br/canais/hbo-family-hd"],
        "HBO Mundi": ["https://redecanaistv.sh/assistir-hbo-mundi-online-24-horas-ao-vivo_b5817d64b.html", "https://mi.tv/br/canais/hbo-mundi"],
        "HBO Pop": ["https://redecanaistv.sh/assistir-hbo-pop-online-24-horas-ao-vivo_e449af1b8.html", "https://mi.tv/br/canais/hbo-pop"],
        "HBO Signature": ["https://redecanaistv.sh/assistir-hbo-signature-online-24-horas-ao-vivo_421493b85.html", "https://mi.tv/br/canais/hbo-signature"],
        "HBO Xtreme": ["https://redecanaistv.sh/assistir-hbo-xtreme-online-24-horas-ao-vivo_8586fbbe2.html", "https://mi.tv/br/canais/hbo-xtreme"]
    },
    "🎞️ Telecine": {
        "Telecine Cult": ["https://redecanaistv.sh/assistir-telecine-cult-online-24-horas-ao-vivo_efbdd89bb.html", "https://mi.tv/br/canais/telecine-cult"],
        "Telecine Fun": ["https://redecanaistv.sh/assistir-telecine-fun-online-24-horas-ao-vivo_a536c2b27.html", "https://mi.tv/br/canais/telecine-fun"],
        "Telecine Pipoca": ["https://redecanaistv.sh/assistir-telecine-pipoca-online-24-horas-ao-vivo_563a37d1a.html", "https://mi.tv/br/canais/telecine-pipoca"],
        "Telecine Premium": ["https://redecanaistv.sh/assistir-telecine-premium-online-24-horas-ao-vivo_d5f664391.html", "https://mi.tv/br/canais/telecine-premium"],
        "Telecine Touch": ["https://redecanaistv.sh/assistir-telecine-touch-online-24-horas-ao-vivo_e06631de7.html", "https://mi.tv/br/canais/telecine-touch"]
    },
    "🎥 Filmes Variados": {
        "TNT": ["https://redecanaistv.sh/assistir-tnt-online-24-horas-ao-vivo_93b3cd376.html", "https://mi.tv/br/canais/tnt"],
        "Megapix": ["https://redecanaistv.sh/assistir-megapix-online-24-horas-ao-vivo_267d04e36.html", "https://mi.tv/br/canais/megapix"],
        "Space": ["https://redecanaistv.sh/assistir-space-online-24-horas-ao-vivo_568e0b475.html", "https://mi.tv/br/canais/space"],
        "Studio Universal": ["https://redecanaistv.sh/assistir-studio-universal-online-24-horas-ao-vivo_2272b2959.html", "https://mi.tv/br/canais/studio-universal"],
        "Cinemax": ["https://redecanaistv.sh/assistir-cinemax-online-24-horas-ao-vivo_7a8a40375.html", "https://mi.tv/br/canais/cinemax"]
    },
    "🏅 Esporte": {
        "Combate": ["https://redecanaistv.sh/assistir-combate-lutas-ufc-online-24-horas-ao-vivo_5192928f1.html", "https://mi.tv/br/canais/combate"],
        "UFC Fight Pass": ["https://redecanaistv.sh/assistir-ufc-fight-pass-online-24-horas-ao-vivo_e15a0cfd6.html", "https://www.ufc.com.br/events"],
        "SporTV": ["https://redecanaistv.sh/assistir-sportv-online-24-horas-ao-vivo_30439d2e3.html", "https://mi.tv/br/canais/sportv"],
        "SporTV 2": ["https://redecanaistv.sh/assistir-sportv-2-online-24-horas-ao-vivo_6012803d7.html", "https://mi.tv/br/canais/sportv-2"],
        "SporTV 3": ["https://redecanaistv.sh/assistir-sportv-3-online-24-horas-ao-vivo_b5ba01607.html", "https://mi.tv/br/canais/sportv-3"],
        "ESPN": ["https://redecanaistv.sh/assistir-espn-online-24-horas-ao-vivo_d1dcae581.html", "https://mi.tv/br/canais/espn"],
        "BandSports": ["https://redecanaistv.sh/assistir-band-sports-online-24-horas-ao-vivo_e192145ad.html", "https://mi.tv/br/canais/band-sports"]
    },
    "📺 Variedades": {
        "A Fazenda": ["https://redecanaistv.sh/assistir-a-fazenda-17-camera-principal-online-24-horas-ao-vivo_f726101e5.html", "https://mi.tv/br/canais/record"],
        "Animal Planet": ["https://redecanaistv.sh/assistir-animal-planet-online-24-horas-ao-vivo_b008d98bf.html", "https://mi.tv/br/canais/animal-planet"],
        "Comedy Central": ["https://redecanaistv.sh/assistir-comedy-central-online-24-horas-ao-vivo_457ae2ac8.html", "https://mi.tv/br/canais/comedy-central"],
        "Discovery Home & Health": ["https://redecanaistv.sh/assistir-discovery-home-health-online-24-horas-ao-vivo_fd7e8223b.html", "https://mi.tv/br/canais/discovery-home-health"],
        "Discovery Science": ["https://redecanaistv.sh/assistir-discovery-science-online-24-horas-ao-vivo_2f369e9c3.html", "https://mi.tv/br/canais/discovery-science"],
        

    },
    "📺 Abertos": {
    "Globo SP": [
        "https://redecanaistv.sh/assistir-rede-globo-sp-online-24-horas-ao-vivo_5c0180d66.html",
        "https://mi.tv/br/canais/globo"
    ],
    "Globo RJ": [
        "https://redecanaistv.sh/assistir-rede-globo-rj-online-24-horas-ao-vivo_89f2ea726.html",
        "https://mi.tv/br/canais/globo"
    ],
    "Band": [
        "https://redecanaistv.sh/assistir-rede-bandeirantes-band-online-24-horas-ao-vivo_db41bec29.html",
        "https://mi.tv/br/canais/band"
    ],
    "SBT": [
        "https://redecanaistv.sh/assistir-sbt-online-24-horas-ao-vivo_8a0548907.html",
        "https://mi.tv/br/canais/sbt"
    ]
    }
}

# Botões na barra lateral
for categoria, canais in categorias.items():
    st.sidebar.title(categoria)
    for nome, dados in canais.items():
        if st.sidebar.button(nome):
            st.session_state.canal = nome
            st.session_state.link = dados[0]
            st.session_state.guia = dados[1]

# Exibe player e programação
if st.session_state.canal and st.session_state.link:
    st.title(st.session_state.canal)
    st.markdown(f"""
    <iframe name="Player" src="{st.session_state.link}" 
    frameborder="0" height="440" scrolling="no" width="680" allow="encrypted-media" allowfullscreen></iframe>
    """, unsafe_allow_html=True)
    st.markdown(f"📅 [Ver programação de {st.session_state.canal}]({st.session_state.guia})")
else:
    st.title("Player de Canal")
    st.info("Selecione um canal na barra lateral para iniciar o player.")

# Botão de logout
st.divider()
if st.button("🔒 Logout"):
    st.session_state.autenticado = False
    st.session_state.canal = None
    st.session_state.link = None
    st.session_state.guia = None
    st.rerun()