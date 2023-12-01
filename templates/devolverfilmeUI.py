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
        id_cliente = st.session_state['cliente_id']
        locacoes = View.minhas_locacoes_de_agora(id_cliente)

        if not locacoes:
            st.write("Nenhuma locação encontrada para devolução.")
        else:
            filmes_locados = {locacao.get_id_filme(): NFilme.listar_id(locacao.get_id_filme()) for locacao in locacoes}

            filme_devolver = st.selectbox("Selecione o filme para devolução", list(filmes_locados.values()))

            if st.button("Realizar Devolução"):
                try:
                    id_filme_devolver = next((id_filme for id_filme, filme in filmes_locados.items() if filme == filme_devolver), None)
                    if id_filme_devolver is not None:
                        View.devolver_filme(id_filme_devolver, id_cliente)
                        st.success("Devolução realizada com sucesso")
                        time.sleep(2)
                        st.rerun()
                    else:
                        st.error("Erro ao encontrar o filme correspondente.")
                except ValueError as error:
                    st.error(f"Erro: {error}")