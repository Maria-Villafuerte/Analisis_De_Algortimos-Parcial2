def largest_plus_sign(grid):
    if not grid or not grid[0]:
        return 0
        
    n = len(grid)
    m = len(grid[0])
    
    # Inicializar las cuatro matrices auxiliares
    left = [[0 for _ in range(m)] for _ in range(n)]
    right = [[0 for _ in range(m)] for _ in range(n)]
    top = [[0 for _ in range(m)] for _ in range(n)]
    bottom = [[0 for _ in range(m)] for _ in range(n)]
    
    # Llenar la matriz left (izquierda a derecha)
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                left[i][j] = 1 + (left[i][j-1] if j > 0 else 0)
    
    # Llenar la matriz right (derecha a izquierda)
    for i in range(n):
        for j in range(m-1, -1, -1):
            if grid[i][j] == 1:
                right[i][j] = 1 + (right[i][j+1] if j < m-1 else 0)
    
    # Llenar la matriz top (arriba a abajo)
    for j in range(m):
        for i in range(n):
            if grid[i][j] == 1:
                top[i][j] = 1 + (top[i-1][j] if i > 0 else 0)
    
    # Llenar la matriz bottom (abajo a arriba)
    for j in range(m):
        for i in range(n-1, -1, -1):
            if grid[i][j] == 1:
                bottom[i][j] = 1 + (bottom[i+1][j] if i < n-1 else 0)
    
    # Calcular el tamaño máximo de la cruz
    max_size = 0
    max_i, max_j = -1, -1  # Coordenadas de la cruz más grande
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                # Encontrar el brazo más corto
                arm_length = min(left[i][j], right[i][j], top[i][j], bottom[i][j])
                
                # Calcular el tamaño de la cruz:
                # Cada brazo tiene longitud arm_length-1 (sin contar el centro)
                # La cruz tiene 4 brazos + el centro
                cruz_size = 4 * (arm_length - 1) + 1
                
                if cruz_size > max_size:
                    max_size = cruz_size
                    max_i, max_j = i, j
    
    return max_size

# Prueba con el primer ejemplo
grid1 = [
    [1, 0, 1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 0, 1, 1],
    [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0]
]

# Prueba con el segundo ejemplo
grid2 = [
    [1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 0]
]

print(f"Resultado para el primer grid: {largest_plus_sign(grid1)}")
print(f"Resultado para el segundo grid: {largest_plus_sign(grid2)}")