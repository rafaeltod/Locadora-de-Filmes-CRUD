from templates.manterclienteUI import ManterClienteUI
from templates.manterfilmeUI import ManterFilmeUI
from templates.manterlocacaoUI import ManterLocacaoUI
from templates.buscarfilmeUI import BuscarFilmeUI
from templates.loginUI import LoginUI
from templates.abrircontaUI import AbrirContaUI
from templates.editarperfilUI import EditarPerfilUI
from templates.realizarlocacaoUI import RealizarLocacaoUI
from templates.minhaslocacoesUI import VisualizarLocacoesUI
from templates.buscarusuarioUI import BuscarLocacaoUsuarioUI
from templates.devolverfilmeUI import DevolverFilmeUI
from views import View

import streamlit as st

class IndexUI:

  def menu_visitante():
    op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta"])
    if op == "Login": LoginUI.main()
    if op == "Abrir Conta": AbrirContaUI.main()

  def menu_admin():
    op = st.sidebar.selectbox("Menu", ["Manter Locacao", "Manter Clientes", "Manter Filmes", "Editar Perfil", "Buscar Locação de Usuário"])
    if op == "Manter Locacao": ManterLocacaoUI.main()
    if op == "Manter Clientes": ManterClienteUI.main()
    if op == "Manter Filmes": ManterFilmeUI.main()
    if op == "Editar Perfil": EditarPerfilUI.main()
    if op == "Buscar Locação de Usuário": BuscarLocacaoUsuarioUI.main()

  def menu_cliente():
    op = st.sidebar.selectbox("Menu", ["Buscar um Filme", "Editar Perfil", "Realizar uma Locação", "Minhas Locações", "Devolver Filme"])
    if op == "Buscar um Filme": BuscarFilmeUI.main()
    if op == "Editar Perfil": EditarPerfilUI.main()
    if op == "Realizar uma Locação": RealizarLocacaoUI.main()
    if op == "Minhas Locações": VisualizarLocacoesUI.main()
    if op == "Devolver Filme": DevolverFilmeUI.main()

  def btn_logout():
    if st.sidebar.button("Logout"):
      del st.session_state["cliente_id"]
      del st.session_state["cliente_nome"]
      st.rerun()

  def sidebar():
    if "cliente_id" not in st.session_state:
      IndexUI.menu_visitante()   
    else:
      st.sidebar.write("Bem-vindo(a), " + st.session_state["cliente_nome"])
      clientes = View.cliente_listar()
      if st.session_state["cliente_nome"] == clientes[0].get_nome(): IndexUI.menu_admin()
      else: IndexUI.menu_cliente()
      IndexUI.btn_logout()  

  def main():
    View.cliente_admin()
    IndexUI.sidebar()

IndexUI.main()



