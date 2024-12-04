from ortools.linear_solver import pywraplp
from .models import Alimento

def calculoSolver(calorias, proteinas, carboidratos, gorduras, calcio, ferro, vitamina_c, sodio, magnesio):
    # Instanciamento do Solver
    solver = pywraplp.Solver.CreateSolver("CBC_MIXED_INTEGER_PROGRAMMING")
    infinito = solver.infinity()

    # Coleta dos objetos no banco de dados em um Vetor
    alimentos = Alimento.objects.all()

    # Definição dos vetores
    n = len(alimentos)
    c = []
    for alimento in alimentos:
        c.append(alimento.preco)

    # Definição das variáveis
    x = {}
    for i in range(n):
        x[i] = solver.NumVar(0, infinito, f'x_{i}')

    print("Número de variáveis =", solver.NumVariables())

    # Definição da função objetivo
    objective = solver.Objective()
    for i in range(n):
        objective.SetCoefficient(x[i], c[i])
    objective.SetMinimization()

    # Definição das restrições
    solver.Add(sum(x[i] * alimento.caloria for i, alimento in enumerate(alimentos)) <= calorias * 1.05)
    solver.Add(sum(x[i] * alimento.caloria for i, alimento in enumerate(alimentos)) >= calorias * 0.95)
    solver.Add(sum(x[i] * alimento.proteina for i, alimento in enumerate(alimentos)) <= proteinas * 1.1)
    solver.Add(sum(x[i] * alimento.proteina for i, alimento in enumerate(alimentos)) >= proteinas * 0.9)
    solver.Add(sum(x[i] * alimento.carboidrato for i, alimento in enumerate(alimentos)) <= carboidratos * 1.1)
    solver.Add(sum(x[i] * alimento.carboidrato for i, alimento in enumerate(alimentos)) >= carboidratos * 0.9)
    solver.Add(sum(x[i] * alimento.gordura for i, alimento in enumerate(alimentos)) <= gorduras * 1.1)
    solver.Add(sum(x[i] * alimento.gordura for i, alimento in enumerate(alimentos)) >= gorduras * 0.9)
    solver.Add(sum(x[i] * alimento.calcio for i, alimento in enumerate(alimentos)) <= calcio * 1.1)
    solver.Add(sum(x[i] * alimento.calcio for i, alimento in enumerate(alimentos)) >= calcio * 0.9)
    solver.Add(sum(x[i] * alimento.ferro for i, alimento in enumerate(alimentos)) <= ferro * 1.1)
    solver.Add(sum(x[i] * alimento.ferro for i, alimento in enumerate(alimentos)) >= ferro * 0.9)
    solver.Add(sum(x[i] * alimento.vitaminaC for i, alimento in enumerate(alimentos)) <= vitamina_c * 1.1)
    solver.Add(sum(x[i] * alimento.vitaminaC for i, alimento in enumerate(alimentos)) >= vitamina_c * 0.9)
    solver.Add(sum(x[i] * alimento.sodio for i, alimento in enumerate(alimentos)) <= sodio * 1.1)
    solver.Add(sum(x[i] * alimento.sodio for i, alimento in enumerate(alimentos)) >= sodio * 0.9)
    solver.Add(sum(x[i] * alimento.magnesio for i, alimento in enumerate(alimentos)) <= magnesio * 1.1)
    solver.Add(sum(x[i] * alimento.magnesio for i, alimento in enumerate(alimentos)) >= magnesio * 0.9)

    # Criar o solver
    status = solver.Solve()
    b = []

    # Verifica se encontrou a solução ótima
    if status == pywraplp.Solver.OPTIMAL:
        resultado = solver.Objective().Value()
        for i in range(n):
            b.append(x[i].solution_value())
        return x, b, resultado
    else:
        return False
    