from alimento import alimento

class Main:
    @staticmethod
    def executar():
        # Criando alguns alimentos
        banana = alimento(
            proteina=1.3,
            caloria=89,
            carboidrato=22.8,
            gordura=0.3,
            sodio=1,
            vitaminaC=8.7,
            ferro=0.3,
            magnesio=27,
            calcio=5,
            preco=1.50
        )

        maca = alimento(
            proteina=0.3,
            caloria=52,
            carboidrato=13.8,
            gordura=0.2,
            sodio=1,
            vitaminaC=4.6,
            ferro=0.1,
            magnesio=5,
            calcio=6,
            preco=2.00
        )

        # Exibindo informações
        print("Informações da Banana:")
        banana.exibir_informacoes()
        print("\nInformações da Maçã:")
        maca.exibir_informacoes()


# Ponto de entrada do programa
if __name__ == "__main__":
    Main.executar()
