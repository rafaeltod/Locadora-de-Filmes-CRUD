import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime
from models.filme import NFilme

class DevolverFilmeUI:
  def main():
    st.header("Filmes para Alugar")
    DevolverFilmeUI.listar_filmes()
    DevolverFilmeUI.devolver_filme()

  def listar_filmes():
    locacoes = View.minhas_locacoes_de_agora(st.session_state["cliente_id"])
            
    if len(locacoes) == 0:
        st.write("Nenhuma locação cadastrada")
    else:
        dic = []
        for obj in locacoes: dic.append(obj.to_json())
                
        df = pd.DataFrame(dic)
        st.dataframe(df)

  def devolver_filme():
        id = st.session_state['cliente_id']
        filmes = View.minhas_locacoes_de_agora()
        filme = st.selectbox("Selecione o filme", filmes)
        if st.button("Devolver Filme"):
            try:
                View.locacao_inserir(datetime.today(), st.session_state['cliente_id'], filme.get_id())
                st.success("Locação realizada com sucesso")
                time.sleep(2)
                st.rerun()
            except ValueError as error:
                st.error(f"Erro: {error}")