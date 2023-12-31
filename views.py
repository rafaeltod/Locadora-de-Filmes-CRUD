from models.cliente import Cliente, NCliente
from models.filme import Filme, NFilme
from models.locacao import Locacao, NLocacao
from models.modelo import Modelo
import datetime
from datetime import timedelta
from datetime import datetime

class View:
  def cliente_inserir(nome, email, fone, senha):
    cliente = Cliente(0, nome, email, fone, senha)
    if nome == "" or email == "" or fone == "" or senha == "": raise ValueError("Nome, e-mail, fone ou senha vazios")
    for obj in View.cliente_listar():
      if obj.get_email() == email: raise ValueError("E-mail repetido")
    NCliente.inserir(cliente)

  def cliente_listar():
    return NCliente.listar()
  
  def cliente_listar_id(id):
    return NCliente.listar_id(id)

  def cliente_atualizar(id, nome, email, fone, senha):
    cliente = Cliente(id, nome, email, fone, senha)
    if nome == "" or email == "" or fone == "" or senha == "": raise ValueError("Nome, e-mail, fone ou senha vazios")
    for obj in View.cliente_listar():
      if obj.get_email() == email: raise ValueError("E-mail repetido")
    NCliente.atualizar(cliente)
    
  def cliente_excluir(id):
    cliente = Cliente(id, "", "", "", "")
    NCliente.excluir(cliente)    

  def cliente_admin():
    for cliente in View.cliente_listar():
      if cliente.get_nome() == "admin": return
    View.cliente_inserir("admin", "admin", "0000", "admin")  

  def cliente_login(email, senha):
    for cliente in View.cliente_listar():
      if cliente.get_email() == email and cliente.get_senha() == senha:
        return cliente
    return None

  def filme_listar():
    return NFilme.listar()

  def filme_listar_id(id):
    return NFilme.listar_id(id)

  def filme_inserir(titulo, genero, duracao, alugado):
    if titulo == "": raise ValueError("Descrição vazia")
    if genero == "": raise ValueError("Gênero vazio")
    if duracao <= 0: raise ValueError("Duração negativa ou nula")
    NFilme.inserir(Filme(0, titulo, genero, duracao, alugado))

  def filme_atualizar(id, titulo, genero, duracao, alugado):
    if titulo == "": raise ValueError("Descrição vazia")
    if genero == "": raise ValueError("Gênero vazio")
    if duracao <= 0: raise ValueError("Duração negativa ou nula")
    NFilme.atualizar(Filme(id, titulo, genero, duracao, alugado))

  def filme_excluir(id):
    NFilme.excluir(Filme(id, "", "", 10, ""))

  def locacao_listar_normal():
    return NLocacao.listar()

  def locacao_listar():
    locacoes = View.locacao_listar_normal()
    lista = []
    for locacao in locacoes:
      cliente = View.cliente_listar_id(locacao.get_id_cliente())
      filme = View.filme_listar_id(locacao.get_id_filme())
      dic = {"ID Locação": locacao.get_id(), "Entrega": locacao.get_entrega(), "Devolução" : locacao.get_devolucao(), "Cliente": cliente.get_nome(), "Filme": filme.get_titulo()}
      lista.append(dic)

    return lista

  def locacao_listar_str():
    locacoes = View.locacao_listar_normal()
    lista = []
    for locacao in locacoes:
      cliente = View.cliente_listar_id(locacao.get_id_cliente())
      filme = View.filme_listar_id(locacao.get_id_filme())
      dicstr = locacao.to_str() + " - " + cliente.get_nome() + " - " + filme.get_titulo()
      lista.append(dicstr)

    return lista

  def locacao_listar_id(id):
    return NLocacao.listar_id(id)

  def locacao_inserir(entrega, devolucao, id_cliente, id_filme):
    filmes = View.filme_listar()
    for filme in filmes:
      if id_filme == filme.get_id():
        if filme.get_alugado() == False:
          filme.set_alugado(True)
          NFilme.atualizar(filme) 
          NLocacao.inserir(Locacao(0, entrega, devolucao, id_cliente, id_filme))
          return
        else:
          raise ValueError("Filme já alugado")

  def locacao_atualizar(id, entrega, devolucao, id_cliente, id_filme):
    filmes = View.filme_listar()
    for filme in filmes:
      if id_filme == filme.get_id():
        if filme.get_alugado() == False:
          filme.set_alugado(True)
          NFilme.atualizar(filme)
          NLocacao.atualizar(Locacao(id, entrega, devolucao, id_cliente, id_filme))
          return
        else:
          raise ValueError("Filme já alugado")
        
  def locacao_excluir(id):
    NLocacao.excluir(Locacao(id, "", "", 0, 0))

  def editar_perfil(id, nome, email, fone, senha):
    NCliente.atualizar(Cliente(id, nome, email, fone, senha))

  def minhas_locacoes(datainicial, datafinal, idcliente):
    datainicial = datetime.strptime(f"{datainicial}", "%d/%m/%Y")
    datafinal = datetime.strptime(f"{datafinal}", "%d/%m/%Y")
    
    locacoes = []
    
    for locacao in View.locacao_listar_normal():
        if locacao.get_id_cliente() == idcliente:
            if datainicial <= locacao.get_entrega() <= datafinal:
                locacoes.append(locacao)
    
    return locacoes
  
  def listar_filmes_nao_alugados():
    nao_alugados = []
    for filme in View.filme_listar():
      if filme.get_alugado() == False:
        nao_alugados.append(filme)
    
    return nao_alugados
  
  def buscar_filme(titulo):
        filmes_encontrados = []

        for filme in View.filme_listar():
            if filme.get_titulo().lower() == titulo.lower():
                filmes_encontrados.append(filme)

        return filmes_encontrados
  
  def buscar_locacao_usuario(locacao_cliente):
      locacoes = View.locacao_listar_normal()
      resultado = []
      for locacao in locacoes:
        if locacao.get_id_cliente() == locacao_cliente.get_id():
          resultado.append(locacao)
        
      return resultado

        
  def meus_filmes_de_agora(id_cliente):
     filmes = []
     for locacao in View.locacao_listar_normal():
       if locacao.get_id_cliente() == id_cliente and locacao.get_devolucao() == "":
         for filme in View.filme_listar():
           if filme.get_id() == locacao.get_id_filme() and filme.get_alugado() == True:
             filmes.append(filme)

     return filmes
  
  def devolver_filme(id_filme, id_cliente):
    locacoes = View.locacao_listar_normal()
    filmes = View.filme_listar()

    for locacao in locacoes:
        if locacao.get_id_cliente() == id_cliente and locacao.get_id_filme() == id_filme and locacao.get_devolucao() == "":
            for filme in filmes:
                if filme.get_id() == id_filme and filme.get_alugado() == True:
                    locacao.set_devolucao(datetime.today())
                    NLocacao.atualizar(locacao)
                    filme.set_alugado(False)
                    NFilme.atualizar(filme)
                    return

    raise ValueError("Filme não encontrado ou já devolvido")
