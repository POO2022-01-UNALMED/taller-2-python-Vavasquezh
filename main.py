class Asiento:
     pass
     def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio 
        self.registro = registro
     def cambiarColor(self,color):
         if color == "rojo" or color == "verde" or color == "amarillo"or color == "negro"or color == "blanco":
              self.color = color 

class Auto:
     cantidadCreados = int
     def __init__(self,modelo,precio,asientos,marca,motor,registro):
        self.modelo = modelo
        self.precio = precio 
        self.asientos = list(asientos)
        self.marca = marca
        self.motor = motor
        self.registro = registro

     def cantidadAsientos(self):
         contador = 0
         if self.asientos != None:
           for asientos in self.asientos:
             if asientos != None:
               contador += 1
         return contador

     def verificarIntegridad(self):
       m_1 = 'Auto original'
       m_2 = 'Las piezas no son originales'
       if self.registro == self.asientos[0].registro:
         if self.motor.registro == self.registro:
           return m_1
         else:
           return m_2 
       return m_2

class Motor:
     pass
     def __init__ (self, numeroCilindros, tipo, registro):
         self.tipo = tipo
         self.numeroCilindros = numeroCilindros
         self.registro = registro

     def cambiarRegistro(self, registro):
         self.registro = registro

     def asignarTipo(self, tipo):
         if tipo == "gasolina" or tipo == "electrico":
             self.tipo = tipo