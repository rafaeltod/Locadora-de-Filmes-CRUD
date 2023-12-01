from models.cliente import Cliente, NCliente
from models.filme import Filme, NFilme
from models.locacao import Locacao, NLocacao
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
    if genero =="": raise ValueError("Gênero vazio")
    if duracao <= 0: raise ValueError("Duração negativa ou nula")
    NFilme.inserir(Filme(0, titulo, genero, duracao, alugado))

  def filme_atualizar(id, titulo, genero, duracao, alugado):
    if titulo == "": raise ValueError("Descrição vazia")
    if genero =="": raise ValueError("Gênero vazio")
    if duracao <= 0: raise ValueError("Duração negativa ou nula")
    NFilme.atualizar(Filme(id, titulo, genero, alugado))

  def filme_excluir(id):
    NFilme.excluir(Filme(id, "", 0, 10))

  def locacao_listar():
    return NLocacao.listar()   

  def locacao_inserir(data, confirmado, id_cliente, id_filme):
    NLocacao.inserir(Locacao(0, data, confirmado, id_cliente, id_filme))

  def locacao_atualizar(id, data, confirmado, id_cliente, id_filme):
    NLocacao.atualizar(Locacao(id, data, confirmado, id_cliente, id_filme))

  def locacao_excluir(id):
    NLocacao.excluir(Locacao(id, "", "", 0, 0))

  def editar_perfil(id, nome, email, fone, senha):
    NCliente.atualizar(Cliente(id, nome, email, fone, senha))

  def minhas_locacoes(datainicial, datafinal, idcliente):
    datainicial = datetime.strptime(f"{datainicial}", "%d/%m/%Y")
    datafinal = datetime.strptime(f"{datafinal}", "%d/%m/%Y")
    
    periodo = []
    
    for horario in View.locacao_listar():
        if horario.get_id_cliente() == idcliente:
            if datainicial <= horario.get_data() <= datafinal:
                periodo.append(horario)
    
    return periodo
  
  def listar_naoalocados():
    nao_alocados = []
    for filme in View.filme_listar():
      for locacao in View.locacao_listar():
        if locacao.get_id_filme() != filme.get_id():
          nao_alocados.append(filme)
    
    return nao_alocados