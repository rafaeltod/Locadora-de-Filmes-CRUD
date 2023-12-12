import streamlit as st
import pandas as pd
from views import View

class VisualizarLocacoesUI:
    def main():
        st.header("Buscar Minhas Locações")
        VisualizarLocacoesUI.listar_locacoes()

    def listar_locacoes():
        datainicial = st.text_input("Informe a data inicial no formato *dd/mm/aaaa*")
        datafinal = st.text_input("Informe a data final no formato *dd/mm/aaaa*")
        
        if st.button("Visualizar"):
            locacoes = View.minhas_locacoes(datainicial, datafinal, st.session_state["cliente_id"])
            
            if len(locacoes) == 0:
                st.write("Nenhuma locação cadastrado")
            else:
                dic = [{"ID Locação": locacao.get_id(), "Entrega": locacao.get_entrega(), "Devolução" : locacao.get_devolucao(), "Cliente": View.cliente_listar_id(locacao.get_id_cliente()).get_nome(), "Filme": View.filme_listar_id(locacao.get_id_filme()).get_titulo()} for locacao in locacoes]
                df = pd.DataFrame(dic)
                st.dataframe(df)