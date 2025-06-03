# Duan Antonio Espinoza Olivares
# 2019079490
# Diseño de software
# Ejemplo código adaptador objeto
###############
# La clase MotorNuevo define la interfaz esperada por el cliente (Target).
class MotorNuevo:
    def request(self):
        # Retorna una cadena que representa el funcionamiento estándar del motor nuevo.
        return "Motor Nuevo: Funcionamiento estándar"

# La clase MotorViejo representa la clase existente con una interfaz no compatible (Adaptee).
class MotorViejo:
    def specific_request(self):
        # Retorna una cadena invertida que necesita ser adaptada para el cliente.
        return "etnega roloV"

# La clase AdaptadorObjeto implementa el patrón Adapter mediante composición.
# Recibe una instancia del Adaptee (MotorViejo) y traduce su interfaz a la esperada por el cliente.
class AdaptadorObjeto:
    def __init__(self, adaptee):
        # Recibe y almacena una instancia del Adaptee.
        # Se espera que el objeto pasado tenga el método specific_request.
        self._adaptee = adaptee

    def request(self):
        # Llama al método specific_request del Adaptee.
        # Invierte la cadena resultante para adaptarla al formato esperado.
        # Retorna una cadena legible por el cliente.
        resultado = self._adaptee.specific_request()  # Obtiene la cadena del adaptee.
        resultado = resultado[::-1]                   # La invierte para hacerla comprensible.
        return f"Adaptador: (Traducido) {resultado}"

# Se instancia el MotorViejo y luego se pasa al AdaptadorObjeto.
# El cliente llama a request, que ahora es compatible gracias al adaptador.
motor_viejo = MotorViejo()
adaptador = AdaptadorObjeto(motor_viejo)
print(adaptador.request())  # Salida esperada: Adaptador: (Traducido) Volor agente
