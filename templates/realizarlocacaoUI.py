import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime

class RealizarLocacaoUI:
  def main():
    st.header("Filmes para Alugar")
    RealizarLocacaoUI.listar_filmes()
    RealizarLocacaoUI.realizar_locacao()

  def listar_filmes():
    agendas = View.listar_filmes_nao_alugados()
    if len(agendas) == 0:
      st.write("Nenhum horário cadastrado")
    else:
      dic = []
      for obj in agendas: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def realizar_locacao():
    id = st.session_state['cliente_id']
    filmes = View.listar_filmes_nao_alugados()
    filme = st.selectbox("Selecione o filme", filmes)
    if st.button("Realizar Locação"):
      try:
        View.locacao_inserir(datetime.today(), "", id, filme.get_id())
        st.success("Locação realizada com sucesso")
        time.sleep(2)
        st.rerun()
      except ValueError as error:
        st.error(f"Erro: {error}")