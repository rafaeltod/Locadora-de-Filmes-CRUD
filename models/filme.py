import json

class Filme:
  def __init__(self, id, titulo, genero, duracao, alugado):
    self.__id = id
    self.__titulo = titulo
    self.__genero = genero
    self.__duracao = duracao
    self.__alugado = alugado
    if titulo == "": raise ValueError("Título inválido")
    if genero == "": raise ValueError("Gênero inválido")
    if duracao <= 0: raise ValueError("Duração inválida")
    self.set_id(id)
    self.set_titulo(titulo)
    self.set_genero(genero)
    self.set_duracao(duracao)
    self.set_alugado(alugado)

  def get_id(self): return self.__id
  def get_titulo(self): return self.__titulo
  def get_genero(self): return self.__genero
  def get_duracao(self): return self.__duracao
  def get_alugado(self): return self.__alugado

  def set_id(self, id): self.__id = id
  def set_titulo(self, titulo):
    if titulo == "": raise ValueError("Título inválido")
    self.__titulo = titulo
  def set_genero(self, genero): 
    if genero == "": raise ValueError("Gênero inválido")
    self.__genero = genero
  def set_duracao(self, duracao):
    if duracao <= 0: raise ValueError("Duração inválida")
    self.__duracao = duracao
  def set_alugado(self, alugado): self.__alugado = alugado

  def __eq__(self, x):
    if self.__id == x.__id and self.__titulo == x.__titulo and self.__genero == x.__genero and self.__duracao == x.__duracao and self.__alugado == x.__alugado:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__titulo} - {self.__genero} - {self.__duracao} min - {self.__alugado}"


class NFilme:
  __filmes = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.__filmes:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.__filmes.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__filmes

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__filmes:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_titulo(obj.get_titulo())
      aux.set_genero(obj.get_genero())
      aux.set_duracao(obj.get_duracao())
      aux.set_alugado(obj.get_alugado())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__filmes.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.__filmes = []
    try:
      with open("filmes.json", mode="r") as arquivo:
        filmes_json = json.load(arquivo)
        for obj in filmes_json:
          aux = Filme(obj["_Filme__id"], obj["_Filme__titulo"], obj["_Filme__genero"], obj["_Filme__duracao"], obj["_Filme__alugado"])
          cls.__filmes.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("filmes.json", mode="w") as arquivo:
      json.dump(cls.__filmes, arquivo, default=vars)