class Asiento:
     pass
     def __init__(self,color,registro):
        self.color = color
        self.precio = precio 
        self.registro = registro

     def Ccolor(self,color):
         if color == "rojo" or color == "verde" or color == "amarillo"or color == "negro"or color == "blanco":
              self.color = color 

class Auto:
     pass
     def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio 
        self.asientos = list(asientos)
        self.marca = marca
        self.motor = motor
        self.registro = registro

     def cantAsientos(self):
         contador = 0
         if sel.asientos != None:
           for asientos in self.asientos:
             if asientos = != None:
               contador += 1
         return contador

     def verintegridad(self):
       m_1 = "Auto original"
       m_2 = "Las piezas no son originales"
       if self.registro == self.asientos[0].registro:
         if self.motor.registro == self.registro:
           return m_1
         else:
           return m_2 
       return m_2

class motor:
    pass
     def __init__ (self, ncilindros, tipo, registro):
         self.tipo = tipo
         self.ncilindros = ncilindros
         self.registro = registro

     def Cregistro(self, registro):
         self.registro = registro

     def Asigtipo(self, tipo):
         if tipo == "gasolina" or tipo == "electrico":
             self.tipo = tipo 