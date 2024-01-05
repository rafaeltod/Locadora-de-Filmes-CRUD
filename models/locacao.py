import json
from datetime import datetime
from models.modelo import Modelo

class Locacao:
  def __init__(self, id, entrega, devolucao, id_cliente, id_filme):
    self.set_id(id)
    self.set_entrega(entrega)
    self.set_devolucao(devolucao)
    self.set_id_cliente(id_cliente)
    self.set_id_filme(id_filme)

  def get_id(self): return self.__id
  def get_entrega(self): return self.__entrega
  def get_devolucao(self): return self.__devolucao
  def get_id_cliente(self): return self.__id_cliente
  def get_id_filme(self): return self.__id_filme

  def set_id(self, id): self.__id = id
  def set_entrega(self, entrega): self.__entrega = entrega
  def set_devolucao(self, devolucao): self.__devolucao = devolucao
  def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
  def set_id_filme(self, id_filme): self.__id_filme = id_filme

  def __eq__(self, x):
    if self.__id == x.__id and self.__entrega == x.__entrega and self.__devolucao == x.__devolucao and self.__id_cliente == x.__id_cliente and self.__id_filme == x.__id_filme:
      return True
    return False

  def __str__(self):
    if self.__devolucao == "":
      return f"{self.__id} - {self.__entrega.strftime('%d/%m/%Y %H:%M')} - {self.__devolucao} - {self.__id_cliente} - {self.__id_filme}"
    else:
      return f"{self.__id} - {self.__entrega.strftime('%d/%m/%Y %H:%M')} - {self.__devolucao.strftime('%d/%m/%Y %H:%M')} - {self.__id_cliente} - {self.__id_filme}"

  def to_str(self):
    if self.__devolucao == "":
      return f"{self.__id} - {self.__entrega.strftime('%d/%m/%Y %H:%M')} - {self.__devolucao}"
    else:
      return f"{self.__id} - {self.__entrega.strftime('%d/%m/%Y %H:%M')} - {self.__devolucao.strftime('%d/%m/%Y %H:%M')}"

  def to_json(self):
    if self.__devolucao == "":
      return {
        'id': self.__id,
        'entrega': self.__entrega.strftime('%d/%m/%Y %H:%M'),
        'devolucao': self.__devolucao,
        'id_cliente': self.__id_cliente,
        'id_filme': self.__id_filme}
    else:
      return {
        'id': self.__id,
        'entrega': self.__entrega.strftime('%d/%m/%Y %H:%M'),
        'devolucao': self.__devolucao.strftime('%d/%m/%Y %H:%M'),
        'id_cliente': self.__id_cliente,
        'id_filme': self.__id_filme}


class NLocacao(Modelo):
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("locacoes.json", mode="r") as arquivo:
        locacoes_json = json.load(arquivo)
        for obj in locacoes_json:
          if obj["devolucao"] == "":
            aux = Locacao(
              obj["id"],
              datetime.strptime(obj["entrega"], "%d/%m/%Y %H:%M"), obj["devolucao"], obj["id_cliente"], obj["id_filme"])
          else:
            aux = Locacao(
              obj["id"],
              datetime.strptime(obj["entrega"], "%d/%m/%Y %H:%M"), datetime.strptime(obj["devolucao"], "%d/%m/%Y %H:%M"), obj["id_cliente"], obj["id_filme"])
          cls.objetos.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("locacoes.json", mode="w") as arquivo:
      json.dump(cls.objetos, arquivo, default=Locacao.to_json)
