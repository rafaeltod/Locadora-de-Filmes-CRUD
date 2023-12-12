import streamlit as st
from views import View
import pandas as pd

class BuscarLocacaoUsuarioUI:

    def main():
        st.header("Buscar Locação de Usuário")
        BuscarLocacaoUsuarioUI.buscar_locacao_usuario()

    def buscar_locacao_usuario():
        clientes = View.cliente_listar()
        cliente = st.selectbox("Selecione o cliente", clientes)

        if st.button("Buscar Locações"):
            locacoes_encontradas = View.buscar_locacao_usuario(cliente)

            if not locacoes_encontradas:
                st.write("Nenhuma locação encontrada para o cliente informado.")
            else:
                dic = [{"ID Locação": locacao.get_id(), "Entrega": locacao.get_entrega(), "Devolução" : locacao.get_devolucao(), "Cliente": View.cliente_listar_id(locacao.get_id_cliente()).get_nome(), "Filme": View.filme_listar_id(locacao.get_id_filme()).get_titulo()} for locacao in locacoes_encontradas]
                df = pd.DataFrame(dic)
                st.dataframe(df)