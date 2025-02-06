#      Codigo que implementa el cálculo    
#         de operaciones numericas 
#
#     Autor: Mendez Cervra Gilbert Alexander
#            mendezgilbert222304@outlok.com
#           versión: 1.01 05/02/2025


def calcular_errores(x, y, valor_real): #Método para calcular errores con parámetros
    diferencia = x - y #Cálculo de la resta de dos números cercanos entre sí 
    error_abs = abs(valor_real - diferencia) #Cálculo del error abosluto
    error_rel = error_abs / abs(valor_real) #Cálculo del error relativo
    error_pct = error_rel * 100 #Cálculo del error porcentual
    error_cua = error_abs**2 #Cálculo del error cuadrático 
    print(f"Diferencia: {diferencia}") #Impresión del resultado de la diferencia de la resta de dos números cercanos entre sí
    print(f"Error absoluto: {error_abs}") #Impresión del resultado del error absoluto
    print(f"Error relativo: {error_rel}") #Impresión del resultado del error relativo
    print(f"Error porcentual: {error_pct}%") #Impresión del resultado del error porcentual
    print(f"Error cuadrático: {error_cua}") #Impresión del resultado del error cuadrático
    return error_abs, error_rel #Retorna los resultados del error absoluto y el error relativo

valores = [(1.0000001, 1.0000000, 0.0000001), (1.000000000000001, 1.000000000000000, 0.000000000000001)] #Se especifican los valores que usaremos para esta prueba

for x, y, real in valores: #Bluce for para calcular los errores
    print(f"\nPara x={x}, y={y}:") #Impresion de que valores de x - se usaron para esta prueba
    calcular_errores(x, y, real) #Se llama al método para cakcular errores enviandole los datos de x, y y valor real