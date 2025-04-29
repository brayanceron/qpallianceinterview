# 1
¿Cómo diseñarías un sistema tipo MRP modular y escalable que permita añadir funcionalidades como predicción de demanda o reportes BI en el futuro? ¿Qué patrón(s) o arquitectura usarías y por qué?

Yo utilizaria una arquitectura en capas como Clean Architecture o arquitectura hexagonal que me permitiera separar la lógica de negocio, la base de datos, y la interfaz (sea  una API o GUI) para de esta forma tener el código ordenado y que cada parte tenga una responsabilidad unica. Ya si el sistema comienza a crecer demasiado, para hacerlo mas escalable concideraria utilizar un patron de microservicios


# 2
Supón que el sistema MRP debe manejar miles de productos y transacciones por día. ¿Qué estrategias de diseño y herramientas aplicarías para asegurar un rendimiento óptimo en consultas, validaciones y alertas relacionadas con el inventario?

Para esto yo tendria muy encuenta que las base de datos  esten bien indexadas y normalizadas, cuidando especialmente los índices en columnas clave. Tambien creo que seria conveniente aplicar caching para datos que no cambien muy seguido. Para validaciones y alertas en tiempo real, usaría eventos asíncronos para no bloquear el flujo principal del sistema.

# 3
Escribe una función en el lenguaje que prefieras que reciba una lista de números
enteros y retorne el primer número que no se repite.
```
def no_repeat(param : list) :
    if not param : return "invalid list"
    for i in param :
        if param.count(i) == 1 : return i;

result = no_repeat([4, 5, 1, 2, 0, 4, 1, 0])
print(result)
```
pd: se puede hacer con collections tambien