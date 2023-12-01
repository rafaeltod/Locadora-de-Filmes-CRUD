import streamlit as st
from views import View
import pandas as pd

class BuscarFilmeUI:

    def main():
        st.header("Buscar Filme")
        BuscarFilmeUI.buscar_filme()

    def buscar_filme():
        filmebuscado = st.text_input("Insira aqui o nome do filme a ser buscado")

        if st.button("Visualizar"):
            resultado = View.buscar_filme(filmebuscado)

            if len(resultado) == 0:
                st.write("Nenhum filme encontrado com o título informado.")
            else:
                dic = []
                for filme in resultado:
                    dic.append(filme.__dict__)

                df = pd.DataFrame(dic)
                st.dataframe(df)