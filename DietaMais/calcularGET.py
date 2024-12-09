class calcularGET:
    def calcular_gasto_energetico(self, peso, altura, idade, sexo, nivel_atividade, objetivo):

        if sexo == "masculino":
            tmb = 10 * peso + 6.25 * altura - 5 * idade + 5
        else:
            tmb = 10 * peso + 6.25 * altura - 5 * idade - 161

        # Multiplicador de nível de atividade
        multiplicadores = {
            "sedentario": 1.2,
            "leve": 1.375,
            "moderado": 1.55,
            "intenso": 1.725
        }
        fator_atividade = multiplicadores.get(nivel_atividade.lower(), 1.2)
        get = tmb * fator_atividade

        # Ajuste para objetivo
        if objetivo == "aumentar":
            get += 500
        elif objetivo == "diminuir":
            get -= 500

        return get

    def calcular_nutrientes(self, get):
        """
        Calcula a distribuição de macronutrientes e micronutrientes baseada no GET.
        """
        # Macronutrientes (em gramas)
        proteinas = get * 0.20 / 4
        carboidratos = get * 0.55 / 4
        gorduras = get * 0.25 / 9

        # Micronutrientes (valores diários de referência aproximados para adultos)
        calcio = 1000  # mg
        ferro = 18  # mg
        vitamina_c = 90  # mg
        sodio = 2300  # mg
        magnesio = 400  # mg

        return {
            "calorias": round(get, 2),
            "proteinas": round(proteinas, 2),
            "carboidratos": round(carboidratos, 2),
            "gorduras": round(gorduras, 2),
            "calcio": calcio,
            "ferro": ferro,
            "vitamina_c": vitamina_c,
            "sodio": sodio,
            "magnesio": magnesio
        }

