from django.shortcuts import render, redirect, get_object_or_404
from .models import Alimento
from .calcularGET import calcularGET
from .solver import calculoSolver

# Create your views here.
def principal(request):
    if request.method == "POST":
        peso = float(request.POST.get('peso', 0))
        altura = float(request.POST.get('altura', 0))
        idade = int(request.POST.get('idade', 0))
        sexo = request.POST.get('sexo')
        atividade = request.POST.get('atividade')
        objetivo = request.POST.get('objetivo')

        calculo = calcularGET()
        get = calculo.calcular_gasto_energetico(peso=peso, altura=altura, idade=idade, sexo=sexo, nivel_atividade=atividade, objetivo=objetivo)
        nutrientes = calculo.calcular_nutrientes(get=get)
        
        resultado_formatado = {}
        for chave, valor in nutrientes.items():
            unidade = "g" if chave in ["proteinas", "carboidratos", "gorduras"] else "kcal" if chave == "calorias" else "mg"
            resultado_formatado[chave.capitalize()] = f"{valor} {unidade}"

        parametros_solver = {
            "calorias": nutrientes.get("calorias", 0),
            "proteinas": nutrientes.get("proteinas", 0),
            "carboidratos": nutrientes.get("carboidratos", 0),
            "gorduras": nutrientes.get("gorduras", 0),
            "calcio": nutrientes.get("calcio", 0),
            "ferro": nutrientes.get("ferro", 0),
            "vitamina_c": nutrientes.get("vitamina_c", 0),
            "sodio": nutrientes.get("sodio", 0),
            "magnesio": nutrientes.get("magnesio", 0),
        }
        cs = calculoSolver(**parametros_solver)

        return render(request, './DietaMais/resultado.html', {'resultado': resultado_formatado})

    return render(request, './DietaMais/principal.html')

def resultado(request):
    return render(request, './DietaMais/resultado.html')

def listarAlimentos(request):
    if request.method == "POST":
        numId = request.POST.get('deletar')
        alimento = get_object_or_404(Alimento, id=numId)
        alimento.delete()
    alimentos = Alimento.objects.all()
    return render(request, './DietaMais/listarAlimentos.html', {'alimentos': alimentos})

def cadastrarAlimentos(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        proteina = request.POST.get('proteina')
        caloria = request.POST.get('caloria')
        carboidrato = request.POST.get('carboidrato')
        gordura = request.POST.get('gordura')
        sodio = request.POST.get('sodio')
        vitaminaC = request.POST.get('vitaminaC')
        ferro = request.POST.get('ferro')
        magnesio = request.POST.get('magnesio')
        calcio = request.POST.get('calcio')
        preco = request.POST.get('preco')

        alimento = Alimento(nome=nome, proteina=proteina, caloria=caloria, carboidrato=carboidrato, gordura=gordura, sodio=sodio, vitaminaC=vitaminaC, ferro=ferro, magnesio=magnesio, calcio=calcio, preco=preco)
        alimento.save()
        return redirect('listarAlimentos')
    return render(request, './DietaMais/cadastrarAlimento.html')