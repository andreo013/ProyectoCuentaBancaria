from cuentabancaria import CuentaCorriente, CuentaAhorro

def main():
    # Cuenta corriente con límite de extracción de 7000
    cuenta1 = CuentaCorriente("Andrea", 1313131313, '1965/06/19', 15000, limite_extraccion=7000)
    print(f"Edad del titular: {cuenta1.obtener_edad()} años")
    cuenta1.depositar(5000)
    cuenta1.extraer(6000)  # Dentro del límite (6000 < 7000)
    cuenta1.extraer(8000)  # Excede el límite (8000 > 7000)

    print("---")

    # Cuenta de ahorro
    cuenta2 = CuentaAhorro("Sofia", 2121212121, '1989/03/21', 10000)
    print(f"Edad del titular: {cuenta2.obtener_edad()} años")
    print(f"Tasa de interés: {cuenta2._tasa_interes}")  # muestra 0.001
    print(f"Interés calculado sobre el saldo actual: ${cuenta2.calcular_interes():.2f}")# mostrara 10.0
    cuenta2.depositar(3000)
    cuenta2.extraer(2000)

    print("---")

    # Prueba de saldo insuficiente pero dentro del límite
    cuenta3 = CuentaCorriente("Laura", 11112222, '1970/01/01', saldo=1000, limite_extraccion=2000)
    print(f"Edad del titular: {cuenta3.obtener_edad()} años")
    cuenta3.extraer(1500)  # Saldo insuficiente → "Usted no posee saldo suficiente para realizar la operación"


    

if __name__ == "__main__":
    main()
