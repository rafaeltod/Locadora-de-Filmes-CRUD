import streamlit as st
import pandas as pd
from views import View
import time
import datetime

class ManterLocacaoUI:
  def main():
    st.header("Cadastro de Locações")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterLocacaoUI.listar()
    with tab2: ManterLocacaoUI.inserir()
    with tab3: ManterLocacaoUI.atualizar()
    with tab4: ManterLocacaoUI.excluir()    

  def listar():
    locacoes = View.locacao_listar()
    if len(locacoes) == 0:
      st.write("Nenhuma locação cadastrado")
    else:
      df = pd.DataFrame(locacoes)
      st.dataframe(df)

  def inserir():
    datastr = st.text_input("Informe a data no formato *dd/mm/aaaa HH\:MM*")
    clientes = View.cliente_listar()
    cliente = st.selectbox("Selecione o cliente", clientes)
    filmes = View.filme_listar()
    filme = st.selectbox("Selecione o filme", filmes)
    if st.button("Inserir"):
      try:
        entrega = datetime.datetime.strptime(datastr, "%d/%m/%Y %H:%M")
        View.locacao_inserir(entrega, "", cliente.get_id(), filme.get_id())
        st.success("Locação inserida com sucesso")
        time.sleep(2)
        st.rerun()
      except ValueError as error:
        st.error(f"Erro: {error}")

  def atualizar():
    locacoes = View.locacao_listar_normal()
    if len(locacoes) == 0:
      st.write("Nenhuma locação disponível")
    else:  
      op = st.selectbox("Atualização de locações", locacoes)
      datastr = st.text_input("Informe a nova data no formato *dd/mm/aaaa HH\:MM*", op.get_entrega().strftime('%d/%m/%Y %H:%M'))
      clientes = View.cliente_listar()
      cliente_atual = View.cliente_listar_id(op.get_id_cliente())
      if cliente_atual is not None:
        cliente = st.selectbox("Selecione o novo cliente", clientes, clientes.index(cliente_atual))
      else:  
        cliente = st.selectbox("Selecione o novo cliente", clientes)
      filmes = View.filme_listar()
      filme_atual = View.filme_listar_id(op.get_id_filme())
      if filme_atual is not None:
        filme = st.selectbox("Selecione o novo filme", filmes, filmes.index(filme_atual))
      else:
        filme = st.selectbox("Selecione o novo filme", filmes)
      if st.button("Atualizar"):
        try:
          entrega = datetime.datetime.strptime(datastr, "%d/%m/%Y %H:%M")
          View.locacao_atualizar(op.get_id(), entrega, "", cliente.get_id(), filme.get_id())
          st.success("Locação atualizada com sucesso")
          time.sleep(2)
          st.rerun()
        except ValueError as error:
          st.error(f"Erro: {error}")

  def excluir():
    locacoes = View.locacao_listar_str()
    if len(locacoes) == 0:
      st.write("Nenhuma locação disponível")
    else:  
      op = st.selectbox("Exclusão de locações", locacoes)
      if st.button("Excluir"):
        id = int(op.split(" - ")[0])
        View.locacao_excluir(id)
        st.success("Locação excluída com sucesso")
        time.sleep(2)
        st.rerun()