import json
from models.modelo import Modelo

class Filme:
  def __init__(self, id, titulo, genero, duracao, alugado):
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
    self.__titulo = titulo
  def set_genero(self, genero): 
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


class NFilme(Modelo):
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("filmes.json", mode="r") as arquivo:
        filmes_json = json.load(arquivo)
        for obj in filmes_json:
          aux = Filme(obj["_Filme__id"], obj["_Filme__titulo"], obj["_Filme__genero"], obj["_Filme__duracao"], obj["_Filme__alugado"])
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("filmes.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=vars)