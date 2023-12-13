import streamlit as st
import pandas as pd
from views import View
import time

class DevolverFilmeUI:
  def main():
    st.header("Devolver Filmes")
    DevolverFilmeUI.listar_filmes()
    DevolverFilmeUI.devolver_filme()

  def listar_filmes():
    locacoes = View.meus_filmes_de_agora(st.session_state["cliente_id"])
            
    if len(locacoes) == 0:
        st.write("Nenhuma locação cadastrada")
    else:
        dic = []
        for obj in locacoes: dic.append(obj.__dict__)
                
        df = pd.DataFrame(dic)
        st.dataframe(df)

  def devolver_filme():
    id_cliente = st.session_state['cliente_id']
    filmes = View.meus_filmes_de_agora(id_cliente)
    filme = st.selectbox("Selecione o filme", filmes)
    if st.button("Devolver Filme"):
        try:
            View.devolver_filme(filme.get_id(), id_cliente)
            st.success("Devolução realizada com sucesso")
            time.sleep(2)
            st.rerun()
        except ValueError as error:
            st.error(f"Erro: {error}")