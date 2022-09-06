from abc import ABC, abstractmethod

class Espacio(ABC):

  edificio=None
  nombre=None

  def get_edificio(self):
    return self.edificio

  def get_nombre(self):
    return self.nombre

  def set_edificio(self,x):
    self.edificio=x

  def set_nombre(self,x):
    self.nombre=x




    