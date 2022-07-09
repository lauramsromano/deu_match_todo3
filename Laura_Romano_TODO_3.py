#--------------------------------------------#
#                 DEU MATCH!                 #

def validacao_das_notas():
    cand = []
    for i, lista in enumerate(cadidatos_numerica):
        count_1 = 0
        for j, valor in enumerate(lista):
            if notas_validacao[j] <= valor:
                count_1 += 1
        if count_1 == 4:
            cand.append(cadidatos_numerica[i])

    for i, valor in enumerate(cand):
        print(
            f"Candidato {i}: e{valor[0]}_t{valor[1]}_p{valor[2]}_s{valor[3]}")


cadidatos = ['e5_t10_p8_s8', 'e10_t7_p7_s8',
             'e8_t5_p4_s9', 'e2_t2_p2_s1', 'e10_t10_p8_s9']

cadidatos_numerica = [[5, 10, 8, 8], [10, 7, 7, 8],
                      [8, 5, 4, 9], [2, 2, 2, 1], [10, 10, 8, 8]]

while True:
    voltar = True
    verificacao = input(
        "Se você deseja inserir um novo conjunto de notas, digite 1.\nMas, se deseja verificar os cadidados na base, digite 2: ")
    if verificacao == '1' or verificacao == '2':
        verificacao = int(verificacao)
    if not(verificacao == 1 or verificacao == 2):
        voltar == True
    else:
        break

while True:
    voltar = True
    if verificacao == 1:
        print('----------')
        nova_nota_e = input('Digite a nota de e (entrevista): ')
        nova_nota_t = input('Digite a nota de t (teste teórico): ')
        nova_nota_p = input('Digite a nota de p (teste prático): ')
        nova_nota_s = input('Digite a nota de s (avaliação soft skills): ')
        print('----------')
        notas_cand_formatado = (
            f'e{nova_nota_e}_t{nova_nota_t}_p{nova_nota_p}_s{nova_nota_s}')
        notas_numericas = [int(nova_nota_e), int(
            nova_nota_t), int(nova_nota_p), int(nova_nota_s)]
        cadidatos.append(notas_cand_formatado)
        cadidatos_numerica.append(notas_numericas)
        verificacao = int(input(
            "Se você deseja inserir um novo conjunto de notas, digite 1.\nMas, se deseja verificar os cadidados na base, digite 2: "))
        if verificacao == 1:
            voltar == True
        elif verificacao == 2:
            voltar == False
        print('----------')
    elif verificacao == 2:
        break

notas_validacao = []

nota_de_corte_e = int(input('Digite a nota de corte e (entrevista): '))
nota_de_corte_t = int(input('Digite a nota de corte t (teste teórico): '))
nota_de_corte_p = int(input('Digite a nota de corte p (teste prático): '))
nota_de_corte_s = int(
    input('Digite a nota de corte e (avaliação soft skills): '))
notas_validacao = [nota_de_corte_e, nota_de_corte_t,
                   nota_de_corte_p, nota_de_corte_s]
print('----------')
print('Os candidatos aprovados segundo as notas de corte estabalecidas são: ')
