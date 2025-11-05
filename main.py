from tp5_aplicaciones import funcion_evaluacion, geneticoSimple, init_pop_tsp, graficarEvolucionFitness, sel_ruleta, xov_uniform, mut_binary

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

Bounds = [[1, 14] for i in range(13)]  #ciudades del 2 al 14 

Enteras = [True]*13
f = funcion_evaluacion
cant_individuos = 18
cant_generac = 50
cant_elite = 1
sel = sel_ruleta
eps = 0.1
xover = xov_uniform
cant_cruzados = round(0.8 * cant_individuos)
mut = mut_binary
cant_mutados = round(0.1 * cant_individuos)
callback = None #usar None para que no grafique y vaya mas rapido

Pop = init_pop_tsp(len(coordenadas), 0, cant_individuos, Bounds)

sol, solF, Pop, Fit, traceBest, traceAvg, bestSols = \
    geneticoSimple(Pop, cant_generac, Bounds, Enteras, sel, xover, mut, \
        cant_cruzados, cant_mutados, cant_elite, eps, f,coordenadas, callback)

graficarEvolucionFitness(traceBest, traceAvg)

print(bestSols)
print("Mejor solución: {0} (Fitness: {1})".format(sol, solF))