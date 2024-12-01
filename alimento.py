class alimento:
    def __init__(self, proteina, caloria, carboidrato, gordura, sodio, vitaminaC, ferro, magnesio, calcio, preco):
        self.proteina = proteina
        self.caloria = caloria
        self.carboidrato = carboidrato
        self.gordura = gordura
        self.sodio = sodio
        self.vitaminaC = vitaminaC
        self.ferro = ferro
        self.magnesio = magnesio
        self.calcio = calcio
        self.preco = preco

    def exibir_informacoes(self):
        print(f"Proteína: {self.proteina}g")
        print(f"Caloria: {self.caloria} kcal")
        print(f"Carboidrato: {self.carboidrato}g")
        print(f"Gordura: {self.gordura}g")
        print(f"Sódio: {self.sodio}mg")
        print(f"Vitamina C: {self.vitaminaC}mg")
        print(f"Ferro: {self.ferro}mg")
        print(f"Magnésio: {self.magnesio}mg")
        print(f"Cálcio: {self.calcio}mg")
        print(f"Preço: R$ {self.preco:.2f}")


