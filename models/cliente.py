import json
from models.modelo import Modelo

class Cliente:
  def __init__(self, id, nome, email, fone, senha):
    self.set_id(id)
    self.set_nome(nome)
    self.set_email(email)
    self.set_fone(fone)
    self.set_senha(senha)

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_email(self): return self.__email
  def get_fone(self): return self.__fone
  def get_senha(self): return self.__senha

  def set_id(self, id): self.__id = id
  def set_nome(self, nome):
    self.__nome = nome
  def set_email(self, email):
    self.__email = email
  def set_fone(self, fone):
    self.__fone = fone
  def set_senha(self, senha):
    self.__senha = senha

  def __eq__(self, x):
    if self.__id == x.__id and self.__nome == x.__nome and self.__email == x.__email and self.__fone == x.__fone and self.__senha == x.__senha:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"


class NCliente(Modelo):
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("clientes.json", mode="r") as arquivo:
        clientes_json = json.load(arquivo)
        for obj in clientes_json:
          aux = Cliente(obj["_Cliente__id"], 
                        obj["_Cliente__nome"], 
                        obj["_Cliente__email"],
                        obj["_Cliente__fone"],
                        obj["_Cliente__senha"])
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=vars)