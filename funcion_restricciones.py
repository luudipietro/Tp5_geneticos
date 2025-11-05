import math
import matplotlib.pyplot as plt
import random
import numpy as np
import itertools
import sympy as sp
from shapely.geometry import LineString, Point

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

def distancia(coord_i, coord_j):
  #distancia Euclidea
  return math.sqrt((coord_i[0]-coord_j[0])**2 + (coord_i[1]-coord_j[1])**2)


def funcion_evaluacion(individuo, coordenadas):
    dist_total = sum(distancia(coordenadas[individuo[i]], coordenadas[individuo[i+1]]) for i in range(len(individuo) - 1))
    dist_total += distancia(coordenadas[0], coordenadas[individuo[0]])
    dist_total += distancia(coordenadas[individuo[-1]], coordenadas[0])
   
  
    #dist_total = dist_total ** 2
    return dist_total


def penalizacion_por_interseccion(individuo, measure_intersections):
    if measure_intersections:
         intersections = count_intersections(get_routes_info(individuo, coordenadas))
         print(len(intersections))

    return len(intersections) if len(intersections) > 0 else 0

def g_solucion(individuo, coordenadas, fitness_weight = 1, intersections_weight= 30, measure_intersections=False):
  penalizacion = intersections_weight * penalizacion_por_interseccion(individuo, measure_intersections)
  evaluacion = fitness_weight * funcion_evaluacion(individuo, coordenadas)

  return 1/((evaluacion + penalizacion) ** 2)

def get_routes_info(individuo, coordenadas):
    r = []
    for i in range(len(individuo) - 1):
        try:
            slope = (coordenadas[individuo[i+1]][1] - coordenadas[individuo[i]][1]) / (coordenadas[individuo[i+1]][0] - coordenadas[individuo[i]][0])
        except ZeroDivisionError:
            slope = 0
        r.append([[coordenadas[individuo[i]][0], coordenadas[individuo[i]][1]],
         [coordenadas[individuo[i+1]][0], coordenadas[individuo[i+1]][1]], slope, i, i+1])
    return r

def count_intersections(segments):
    intersection_points = []

    for seg1, seg2 in itertools.combinations(segments, 2):
        point = find_segment_intersection_v2(seg1, seg2)

        if point is not None:
            # print(f'Hay una interseccion entre el segmento {seg1[3]}-{seg1[4]} y el segmento {seg2[3]}-{seg2[4]}')
            # print(f'En el punto: X-{point[0]} - Y-{point[1]}')
            intersection_points.append([point[0], point[1]])

    return intersection_points

def find_segment_intersection(rec1, rec2):
    (x1, y1), (x2, y2), slope1, _, _ = rec1
    (x3, y3), (x4, y4), slope2, _, _ = rec2

    x, y = sp.symbols('x y')

    rs1 = slope1 * x1 - y1
    rs2 = slope2 * x3 - y3

    eq1 = sp.Eq(slope1*x - 1*y, rs1)

    eq2 = sp.Eq(slope2*x - 1*y, rs2)

    solucion = sp.solve((eq1, eq2), (x, y))

    if min(x1, x2) < round(solucion[x], 4) < max(x1, x2) and min(x3, x4) < round(solucion[x], 4) < max(x3, x4):
        if min(y1, y2) < round(solucion[y], 4) < max(y1, y2) and min(y3, y4) < round(solucion[y], 4) < max(y3, y4):
            if min(x1, x2) != int(solucion[x] * 10000) / 10000 and max(x1, x2) != int(solucion[x] * 10000) / 10000:
                if min(y1, y2) != int(solucion[y] * 10000) / 10000 and max(y1, y2) != int(solucion[y] * 10000) / 10000:
                    # print(f'Interseccion: {solucion}')

                    # print(f'Limites en y: {min(y1, y2)} - {max(y1, y2) }')
                    # print(f'Limites en x: {min(x1, x2)} - {max(x1, x2)}')

                    return [solucion[x], solucion[y]]
                else:
                    return None

def find_segment_intersection_v2(rec1, rec2):
    (x1, y1), (x2, y2), slope1, _, _ = rec1
    (x3, y3), (x4, y4), slope2, _, _ = rec2

    l1 = LineString([(x1, y1), (x2, y2)])
    l2 = LineString([(x3, y3), (x4, y4)])

    intersection = l1.intersection(l2)

    if isinstance(intersection, Point):
        if min(x1, x2) != int(intersection.x * 10000) / 10000 and max(x1, x2) != int(intersection.x * 10000) / 10000:
                if min(y1, y2) != int(intersection.y * 10000) / 10000 and max(y1, y2) != int(intersection.y * 10000) / 10000:
                    # print(f'X: {intersection.x}')
                    # print(f'Y: {intersection.y}')
                    return [intersection.x, intersection.y]
                else:
                    return None

#mejor_ruta =[1, 4, 5, 2, 3, 6, 8, 7, 9, 10, 11, 12, 13]
#mejor_ruta =[1, 3, 5, 2, 4, 6, 8, 7, 9, 10, 11, 12, 13]
mejor_ruta = [0, 6, 2, 7, 9, 10, 12, 11, 13, 5, 4, 8, 3, 1, 0]

print(f'La menor distancia posible es {math.sqrt(1 / g_solucion(mejor_ruta, coordenadas, measure_intersections=True))}')