#questao 1
def media():
    notas = input(f"Digite as notas separadas por espaço: ").split()
    n1,n2,n3,n4 = map(float,notas)
    med_base = (n1 + n2 + n3 + n4) / 4
    pesos = [2, 3, 5, 7]
    plus_pesos = sum(pesos)
    med_base = (n1 + n2 + n3 + n4) / 4
    med_pond = (n1 * pesos[0] + n2 * pesos[1] + n3 * pesos[2] + n4 * pesos[3]) / 4
    plus_pesos
    print(f"MA: {med_base:.2f}")
    print(f"MB: {med_pond:.2f}")
media()
#questao 2
def change(entry):
    coins = [50, 25, 10, 5, 1]
    quants = []
    for coin in coins:
        quant = entry // coin
        quants.append(quant)
        entry %= coin
    print(f"{quants[0]} moedas de 50 centavos")
    print(f"{quants[1]} moedas de 25 centavos")
    print(f"{quants[2]} moedas de 10 centavos")
    print(f"{quants[3]} moedas de 5 centavos")
    print(f"{quants[4]} moedas de 1 centavo")
change(27)