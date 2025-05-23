from abc import ABC, abstractmethod
from datetime import date, datetime

class CuentaBancaria(ABC):
    def __init__(self,nombre_titular,dni_titular, fecha_nacimiento, saldo=0):
        self._nombre_titular = nombre_titular       #atributo privado
        self._dni_titular = dni_titular             #atributo privado
        self._fecha_nacimiento = datetime.strptime(fecha_nacimiento, '%Y/%m/%d').date()
        self._saldo = saldo                         #atributo privado

    def obtener_saldo(self):
        return self._saldo

    @abstractmethod
    def depositar(self,monto):
        pass
    
    @abstractmethod
    def extraer(self,monto):
        pass

    def _calcular_edad(self):
        fecha_actual = date.today()
        edad = fecha_actual - self._fecha_nacimiento
        return edad.days // 365
    
    def obtener_edad(self):
        return self._calcular_edad()

# Clase CuentaCorriente heredando CuentaBancaria
class CuentaCorriente(CuentaBancaria):
    def __init__(self, nombre_titular, dni_titular, fecha_nacimiento, saldo=0,limite_extraccion = 500):
        super().__init__(nombre_titular, dni_titular, fecha_nacimiento, saldo)
        self._limite_extraccion = limite_extraccion
    
    def depositar(self,monto):
        if monto > 0:
            self._saldo += monto
            print(f"Se ha depositado {monto} a la cuenta de {self._nombre_titular}, su saldo es de: {self.obtener_saldo()}")
        else:
            print("El monto a depositar debe ser mayor a 0")

    def extraer(self,monto):
        if monto <= self.obtener_saldo() and monto <= self._limite_extraccion:
            self._saldo -= monto
            print(f"Se ha extraído {monto} de la cuenta de {self._nombre_titular}, su saldo actual es de: {self.obtener_saldo()}")
        else:
            if monto > self._limite_extraccion:
                print("Usted no puede extraer ese monto")
            else:
                print("Usted no posee saldo suficiente para realizar la operación")

# Nueva clase CuentaAhorro que hereda CuentaBancaria
                
class CuentaAhorro(CuentaBancaria):
    def __init__(self,nombre_titular,dni_titular,fecha_nacimiento,saldo=0):
        super().__init__(nombre_titular,dni_titular,fecha_nacimiento,saldo)
        self._tasa_interes = 0.001

    def __aplicar_interes(self):
        self._saldo += self._saldo * self._tasa_interes

    def calcular_interes(self):
        return self._saldo * self._tasa_interes

    def depositar(self,monto):
        if monto > 0:
            self.__aplicar_interes()    # Aplico interés antes de depositar
            self._saldo += monto
            print(f"Se depositaron {monto} en la cuenta de {self._nombre_titular}. Saldo actual: {self._saldo}")
        else:
            print("El monto a depositar debe ser mayor a 0.")

    def extraer(self,monto):
        self.__aplicar_interes()        # Aplico interés antes de extraer
        if monto <= self._saldo:
            self._saldo -= monto
            print(f"Se extrajeron {monto} de la cuenta de {self._nombre_titular}. Saldo actual: {self._saldo}")
        else:
            print("Saldo insuficiente para realizar la operación.")

    def obtener_saldo(self):
        self.__aplicar_interes()        # Aplico interés antes de consultar saldo
        return self._saldo
