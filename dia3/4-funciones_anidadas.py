# FUNCIONES ANIDADAS
# Las funciones anidadas son funciones definidas dentro de otras funciones.


def operacion(a,b):
    def suma(a,b):
        return a + b
    def resta(a,b):
        return a - b
    
    print("Suma:", suma(a,b))
    print("Resta:", resta(a,b))
    
operacion(10,5)