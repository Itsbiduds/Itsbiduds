nota1 = int(input("Digite a primeira nota:"))
nota2 = int(input("Digite a segunda nota:"))
nota3 = int(input("Digite a terceira nota:"))


media = (nota1 + nota2 + nota3) / 3 
print("A média do aluno é: {:.2f}".format(media))

if media < 5:
    print("Aluno reprovado!")
elif media >= 5 and media < 6.9:
    print("Aluno de recuperação!")
elif media >= 7:
    print("Aluno aprovado!")
    
    