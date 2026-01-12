def verify():
    entry = int(input("Escreva sua idade:"))
    if entry >= 18:
        print("Você possui idade para beber e votar!")
    elif entry <= 15:
        print("Você não possui idade para beber e nem votar :(")
    elif entry == 16 or 17:
        print("Você pode votar, porém não pode beber :(")

verify()

def mencao():
    entry2 = input("Insira a nota de sua provas, projetos e questionarios separados por espaco:").split()
    p1,p2,proj1,proj2,quest = map(int,entry2)
    mpp = (p1+2*p2)/3
    mpproj = (proj1+2*proj2)/3
    nf = 0.5*mpp+0.4*mpproj + 0.1* quest

    if 90 <= nf <= 100:
        mencao = "SS"
    elif 70 <= nf < 90:
        mencao = "MS"
    elif 50 <= nf < 70:
        mencao = "MM"
    elif 30 <= nf < 50:
        mencao = "MI"
    elif 0 <= nf < 30:
        mencao = "II"
    else:
        mencao = "Nota inválida"

    print(f"Sua mencao em apc é:",mencao)
mencao()

    
    


 
     
