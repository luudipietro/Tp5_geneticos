import math
def distancia(coord_i, coord_j):
  #distancia Euclidea
  return math.sqrt((coord_i[0]-coord_j[0])**2 + (coord_i[1]-coord_j[1])**2)


coordenadas = [
  [-7.5984,-1.9725],
  [-6.7323, 1.8807],
  [-2.7165, 4.2661],
  [-1.2992, 5.5505],
  [-6.1024, 8.9450],
  [-2.4803, 8.9450],
  [ 4.2913, 7.0183],
  [ 7.0472, 6.1009],
  [ 8.1496, 8.4862],
  [ 8.9370, 0.5963],
  [ 2.6378, 0.6881],
  [ 6.1811,-4.6330],
  [ 1.7717,-7.0183],
  [-5.1575,-8.4862]
]

coordenadas_prueba = [
   [0, 0],
   [2, 0],
    [4, 0],
    [6, 0],
    [8, 0],
    [10, 0],
    [12, 0],
    [14, 0],
    [16, 0],
    [18, 0],
    [20, 0],
    [22, 0],
    [24, 0],
    [26, 0]
]

def funcion_evaluacion(individuo, coordenadas):
    for i in range(len(individuo)-1):
       dist = distancia(coordenadas[individuo[i]-1], coordenadas[individuo[i+1]-1]) 
       
    
    dist_total = sum(distancia(coordenadas[individuo[i]-1], coordenadas[individuo[i+1]-1]) for i in range(len(individuo) - 1))
    dist_total += distancia(coordenadas[0], coordenadas[individuo[0]-1])
    dist_total += distancia(coordenadas[individuo[-1]-1], coordenadas[0])
    return dist_total
#individuo_prueba = [2,4,3,6,8,11,13,5,8,9,10,12,7,14]
individuo_prueba = [2,3,4,5,6,7,8,9,10,11,12,13,14]

print(funcion_evaluacion(individuo_prueba, coordenadas_prueba))
