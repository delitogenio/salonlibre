from abc import ABC, abstractmethod

class Espacio(ABC):

  edificio=None
  nombre=None

  @abstractmethod
  def __init__(self, edicio, nombre):
   self.edificio = edicio
   self.nombre = nombre
  
  def get_edificio(self):
    return self.edificio

  def get_nombre(self):
    return self.nombre

  def set_edificio(self,x):
    self.edificio=x

  def set_nombre(self,x):
    self.nombre=x


    