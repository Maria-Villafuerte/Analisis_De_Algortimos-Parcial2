def count_combinations(n):
    """
    Cuenta las combinaciones posibles de longitud n en un teclado Nokia 3230.
    Cada dígito puede moverse a sí mismo y a sus adyacentes (máximo 4 opciones).
    """
    # Definir el mapa de adyacencia correcto basado en el teclado físico del Nokia 3230
    # Solo incluimos adyacencia horizontal, vertical y reflexiva (sí mismo)
    adjacency = {
        '0': ['0', '8'],            
        '1': ['1', '2', '4'],        
        '2': ['2', '1', '3', '5'],   
        '3': ['3', '2', '6'],         
        '4': ['4', '1', '5', '7'],  
        '5': ['5', '2', '4', '6', '8'],  
        '6': ['6', '3', '5', '9'], 
        '7': ['7', '4', '8'],        
        '8': ['8', '5', '7', '0','9'],  
        '9': ['9', '6', '8']         
    }
    
    # Diccionario para memoización
    memorzacion_de_subproblemas = {}
    
    def dp(digit, length):
        """
        Función recursiva con memoización para contar combinaciones.
        digit: Dígito actual
        length: Longitud restante de la secuencia
        """
        # Caso base
        if length == 1:
            return 1
        
        # Verificar si el subproblema ya se ha resuelto
        if (digit, length) in memorzacion_de_subproblemas:
            return memorzacion_de_subproblemas[(digit, length)]
        
        # Calcular recursivamente sumando las combinaciones
        # para cada dígito adyacente
        count = 0
        for next_digit in adjacency[digit]:
            count += dp(next_digit, length - 1)
        
        # Almacenar el resultado en la memoria
        memorzacion_de_subproblemas[(digit, length)] = count
        return count
    
    # Sumar las combinaciones empezando desde cada dígito del 0 al 9
    total = 0
    for digit in '0123456789':
        total += dp(digit, n)
    
    return total

# Verificación con el ejemplo dado
print(f"Para n = 2: {count_combinations(2)} combinaciones")  # Debería ser 36

# Cálculo para n = 10
print(f"Para n = 10: {count_combinations(10)} combinaciones")