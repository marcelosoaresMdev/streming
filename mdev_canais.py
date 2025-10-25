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

# Tela de login
if not st.session_state.autenticado:
    st.markdown(
        """
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
        """,
        unsafe_allow_html=True
    )

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

# Interface principal após login
st.sidebar.title("Canais")
if st.sidebar.button("HBO"):
    st.session_state.canal = "HBO"
if st.sidebar.button("Telecine"):
    st.session_state.canal = "Telecine"

canal = st.session_state.canal

# Exibe título e player conforme canal selecionado
if canal == "HBO":
    st.title("HBO")
    iframe_code = """
    <iframe name="Player" src="https://redecanaistv.sh/assistir-hbo-online-24-horas-ao-vivo_d1160d077.html" 
    frameborder="0" height="400" scrolling="no" width="640" allow="encrypted-media" allowfullscreen></iframe>
    """
    st.markdown(iframe_code, unsafe_allow_html=True)

elif canal == "Telecine":
    st.title("Telecine Action")
    iframe_code = """
    <iframe name="Player" src="https://redecanaistv.sh/assistir-telecine-action-online-24-horas-ao-vivo_74513ff1c.html" 
    frameborder="0" height="400" scrolling="no" width="640" allow="encrypted-media" allowfullscreen></iframe>
    """
    st.markdown(iframe_code, unsafe_allow_html=True)

else:
    st.title("Player de Canal")
    st.info("Selecione um canal no menu lateral para iniciar o player.")

# Botão de logout abaixo do conteúdo
st.divider()
if st.button("🔒 Logout"):
    st.session_state.autenticado = False
    st.session_state.canal = None
    st.rerun()
