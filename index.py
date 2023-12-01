from templates.manterclienteUI import ManterClienteUI
from templates.manterservicoUI import ManterFilmeUI
from templates.manteragendaUI import ManterLocacaoUI
from templates.abriragendaUI import AbrirLocacaoUI
from templates.loginUI import LoginUI
from templates.agendahojeUI import LocacaoHojeUI
from templates.servicoreajusteUI import FilmeReajusteUI
from templates.abrircontaUI import AbrirContaUI
from templates.editarperfilUI import EditarPerfilUI
from templates.agendarhorarioUI import LocacaorHorarioUI
from templates.agendamentosUI import VisualizarLocacaomentoUI
from templates.admconfirmarUI import ConfirmarLocacaomentoUI
from views import View

import streamlit as st

class IndexUI:

  def menu_visitante():
    op = st.sidebar.selectbox("Menu", ["Login", "Abrir Conta"])
    if op == "Login": LoginUI.main()
    if op == "Abrir Conta": AbrirContaUI.main()

  def menu_admin():
    op = st.sidebar.selectbox("Menu", ["Manter Locacao", "Manter Clientes", "Manter Filmes", "Abrir Locacao do Dia", "Reajustar Preço", "Confirmar Locacaomento", "Editar Perfil"])
    if op == "Manter Locacao": ManterLocacaoUI.main()
    if op == "Manter Clientes": ManterClienteUI.main()
    if op == "Manter Filmes": ManterFilmeUI.main()
    if op == "Abrir Locacao do Dia": AbrirLocacaoUI.main()
    if op == "Confirmar Locacaomento": ConfirmarLocacaomentoUI.main()
    if op == "Editar Perfil": EditarPerfilUI.main()

  def menu_cliente():
    op = st.sidebar.selectbox("Menu", ["Locacao de Hoje", "Editar Perfil", "Locacaor um horário", "Meus Locacaomentos"])
    if op == "Locacao de Hoje": LocacaoHojeUI.main()
    if op == "Editar Perfil": EditarPerfilUI.main()
    if op == "Locacaor um horário": LocacaorHorarioUI.main()
    if op == "Meus Locacaomentos": VisualizarLocacaomentoUI.main()

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



