from salon import Salon
from laboratorio import Laboratorio


def create_ed(edi, nombre):

  edi='a'
  nombre='201'
  salon= Salon
  salon.edificio=nombre
  salon.nombre=edi
  return salon



def create_lab(edi, nombre):
  edi='a'
  nombre='201'
  lab= Laboratorio
  Laboratorio.edificio=nombre
  Laboratorio.nombre=edi
  return lab



