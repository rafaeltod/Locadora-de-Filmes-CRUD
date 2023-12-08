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
                dic = [{"ID Locação": locacao.get_id(), "Data": locacao.get_entrega(),"ID Cliente": locacao.get_id_cliente(), "ID Filme": locacao.get_id_filme()} for locacao in locacoes_encontradas]
                df = pd.DataFrame(dic)
                st.dataframe(df)