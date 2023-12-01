import streamlit as st
import pandas as pd
from views import View
import time

class ManterFilmeUI:
  def main():
    st.header("Cadastro de Filmes")
    tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
    with tab1: ManterFilmeUI.listar()
    with tab2: ManterFilmeUI.inserir()
    with tab3: ManterFilmeUI.atualizar()
    with tab4: ManterFilmeUI.excluir()

  def listar():
    filmes = View.filme_listar()
    if len(filmes) == 0:
      st.write("Nenhum serviço cadastrado")
    else:  
      dic = []
      for obj in filmes: dic.append(obj.__dict__)
      df = pd.DataFrame(dic)
      st.dataframe(df)

  def inserir():
    titulo = st.text_input("Informe o título do filme")
    genero = st.text_input("Informe o gênero do filme")
    duracao = st.text_input("Informe a duração do filme (min)")
    if st.button("Inserir"):
      try:
        View.filme_inserir(titulo, genero, int(duracao), False)
        st.success("Filme inserido com sucesso")
        time.sleep(2)
        st.rerun()
      except ValueError as error:
        st.error(f"Erro: {error}")  

  def atualizar():
    filmes = View.filme_listar()
    if len(filmes) == 0:
      st.write("Nenhum serviço cadastrado")
    else:  
      op = st.selectbox("Atualização de Filmes", filmes)
      titulo = st.text_input("Informe o novo titulo do filme", op.get_titulo())
      genero = st.text_input("Informe o novo genero do filme", op.get_genero())
      duracao = st.text_input("Informe a nova duração do filme", op.get_duracao())
      if st.button("Atualizar"):
        try:
          id = op.get_id()
          View.filme_atualizar(id, titulo, genero, int(duracao), False)
          st.success("Filme atualizado com sucesso")
          time.sleep(2)
          st.rerun()
        except ValueError as error:
          st.error(f"Erro: {error}")

  def excluir():
    filmes = View.filme_listar()
    if len(filmes) == 0:
      st.write("Nenhum serviço cadastrado")
    else:  
      op = st.selectbox("Exclusão de Filmes", filmes)
      if st.button("Excluir"):
        id = op.get_id()
        View.filme_excluir(id)
        st.success("Filme excluído com sucesso")
        time.sleep(2)
        st.rerun()