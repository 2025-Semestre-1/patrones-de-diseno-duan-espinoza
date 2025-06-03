# Duan Antonio Espinoza Olivares
# 2019079490
# Diseño de software
# Ejemplo código adaptador clase
###############
# La clase MotorNuevo actúa como la interfaz objetivo (Target).
# Define la interfaz que el cliente espera utilizar.
class MotorNuevo:
    def request(self):
        # Retorna una cadena que representa el funcionamiento estándar del motor nuevo.
        # No recibe parámetros.
        # No tiene restricciones.
        return "Motor Nuevo: Funcionamiento estándar"

# La clase MotorViejo representa una clase existente con una interfaz incompatible (Adaptee).
class MotorViejo:
    def specific_request(self):
        # Retorna una cadena invertida que representa un mensaje no legible directamente por el cliente.
        # No recibe parámetros.
        # No es compatible con la interfaz esperada por el cliente.
        return "etnega roloV"

# La clase AdaptadorClase implementa el patrón Adapter usando herencia múltiple.
# Hereda de MotorNuevo (Target) y MotorViejo (Adaptee) para traducir la interfaz incompatible.
class AdaptadorClase(MotorNuevo, MotorViejo):
    def request(self):
        # Adapta la respuesta del método specific_request del MotorViejo.
        # Llama al método original y transforma su salida invirtiendo la cadena.
        # Retorna una cadena legible para el cliente.
        resultado = self.specific_request()       # Obtiene la cadena invertida del Adaptee.
        resultado = resultado[::-1]               # Invierte la cadena para que tenga sentido.
        return f"Adaptador: (Traducido) {resultado}"

# Se instancia el adaptador de clase y se llama al método 'request' que el cliente espera.
cliente = AdaptadorClase()
print(cliente.request())  # Salida esperada: Adaptador: (Traducido) Volor agente
