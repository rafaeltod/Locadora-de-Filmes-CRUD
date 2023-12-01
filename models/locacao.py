import json
import datetime

class Locacao:
  def __init__(self, id, entrega, id_cliente, id_filme):
    self.__id = id
    self.__entrega = entrega
    self.__id_cliente = id_cliente
    self.__id_filme = id_filme

  def get_id(self): return self.__id
  def get_entrega(self): return self.__entrega
  def get_id_cliente(self): return self.__id_cliente
  def get_id_filme(self): return self.__id_filme

  def set_id(self, id): self.__id = id
  def set_entrega(self, entrega): self.__entrega = entrega
  def set_id_cliente(self, id_cliente): self.__id_cliente = id_cliente
  def set_id_filme(self, id_filme): self.__id_filme = id_filme

  def __eq__(self, x):
    if self.__id == x.__id and self.__entrega == x.__entrega and self.__id_cliente == x.__id_cliente and self.__id_filme == x.__id_filme:
      return True
    return False

  def __str__(self):
    return f"{self.__id} - {self.__entrega.strftime('%d/%m/%Y %H:%M')} - {self.__id_cliente} - {self.__id_filme}"

  def to_json(self):
    return {
      'id': self.__id,
      'entrega': self.__entrega.strftime('%d/%m/%Y %H:%M'),
      'id_cliente': self.__id_cliente,
      'id_filme': self.__id_filme}


class NLocacao:
  __locacoes = []

  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    id = 0
    for aux in cls.__locacoes:
      if aux.get_id() > id: id = aux.get_id()
    obj.set_id(id + 1)
    cls.__locacoes.append(obj)
    cls.salvar()

  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.__locacoes

  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for obj in cls.__locacoes:
      if obj.get_id() == id: return obj
    return None

  @classmethod
  def atualizar(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      aux.set_entrega(obj.get_entrega())
      aux.set_id_cliente(obj.get_id_cliente())
      aux.set_id_filme(obj.get_id_filme())
      cls.salvar()

  @classmethod
  def excluir(cls, obj):
    cls.abrir()
    aux = cls.listar_id(obj.get_id())
    if aux is not None:
      cls.__locacoes.remove(aux)
      cls.salvar()

  @classmethod
  def abrir(cls):
    cls.__locacoes = []
    try:
      with open("locacoes.json", mode="r") as arquivo:
        locacoes_json = json.load(arquivo)
        for obj in locacoes_json:
          aux = Locacao(
            obj["id"],
            datetime.datetime.strptime(obj["entrega"], "%d/%m/%Y %H:%M"), obj["id_cliente"], obj["id_filme"])
          cls.__locacoes.append(aux)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("locacoes.json", mode="w") as arquivo:
      json.dump(cls.__locacoes, arquivo, default=Locacao.to_json)
