import json
import os

def salvar_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_aberto:
        json.dump(lista, arquivo_aberto, ensure_ascii=False, indent=4)

def ler_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_aberto:
            lista = json.load(arquivo_aberto)
        return lista
    except:
        return []

def exibir_menu_principal():
    print("__________MENU PRINCIPAL__________")
    print("")
    print("          (1) Estudantes")
    print("          (2) Professor")
    print("          (3) Disciplina")
    print("          (4) Turmas")
    print("          (5) Matrículas")
    print("          (9) Sair")
    print("")
    return int(input("Informe a opção desejada: "))

def exibir_menu_operaçoes():
    print("(1) Incluir")
    print("(2) Listar")
    print("(3) Atualizar")
    print("(4) Excluir")
    print("(9) Voltar ao menu principal")
    print("")

def linha_e_espaco():
    print("__________________________________")
    print("")
    
principal = 0

while True:
    try:
        if principal == 9:
            break
        
        principal = exibir_menu_principal()

        while True:
            try:
                if principal == 1:
                    linha_e_espaco()
                    print("[ESTUDANTES] MENU DE OPERAÇÕES")
                    exibir_menu_operaçoes()
                    opera = int(input("Informe a ação desejada: "))
                    
                    if opera == 1:
                        linha_e_espaco()
                        print("==============INCLUIR=============\n")
                        codigo = int(input("Informe o código do estudante: "))
                        nomes = input("Informe o nome do estudante: ")
                        cpf = input("Informe o CPF do estudante: ")
                        dados_estud = {}
                        dados_estud["código_estudante"]= codigo
                        dados_estud["nome_estudante"]= nomes
                        dados_estud["cpf"]= cpf
                        nome_est = ler_arquivo("estudantes.json")
                        nome_est.append(dados_estud)
                        salvar_arquivo(nome_est,"estudantes.json")
                        input("\nPressione ENTER para continuar")
                            
                    elif opera == 2:
                        linha_e_espaco()
                        print("==============LISTAR=============\n")
                        nome_est = ler_arquivo("estudantes.json")
                        if len(nome_est) == 0:
                            print("Não há estudantes cadastrados")
                        else:
                             for est in nome_est:
                                print("-", est)
                        input("\nPressione ENTER para continuar")
     
                    elif opera == 3:
                        linha_e_espaco()
                        print("==============ATUALIZAR===========\n")
                        nome_est = ler_arquivo("estudantes.json")
                        if len(nome_est) == 0:
                            print("\nNenhum estudante foi incluído ainda")
                        else: 
                            codigo_atualizar = int(input("Qual é o código que deseja atualizar? : "))
                            encontrado = False
                            for dados_estud in nome_est:
                                if dados_estud["código_estudante"] == codigo_atualizar:
                                    dados_estud["código_estudante"] = int(input("\nInforme o novo código: "))
                                    dados_estud["nome_estudante"] = input("Informe o novo nome: ")
                                    dados_estud["cpf"]= input("Informe o novo CPF: ")
                                    print("\nESTUDANTE ATUALIZADO")
                                    encontrado = True
                                    break
                            
                            if not encontrado:
                                print("\nNenhum estudante encontrado com esse código.")
                            
                            salvar_arquivo(nome_est, "estudantes.json")
                                
                    elif opera == 4:
                        linha_e_espaco()
                        print("==============EXCLUIR=============\n")
                        nome_est = ler_arquivo("estudantes.json")
                        if len(nome_est) == 0:
                            print("\nNenhum estudante foi incluído ainda")
                        else: 
                            codigo_excluir = int(input("Qual é o código que deseja excluir? : "))
                            encontrado = False
                            for dados_estud in nome_est:
                                if dados_estud["código_estudante"] == codigo_excluir:
                                    nome_est.remove(dados_estud)
                                    print("\nESTUDANTE EXCLUÍDO")
                                    encontrado = True
                                    break
                            
                            if not encontrado:
                                print("\nNenhum estudante encontrado com esse código.")
                                
                            salvar_arquivo(nome_est, "estudantes.json")
                        
                    elif opera == 9:
                        print("__________________________________")
                        break 

                    else: 
                        linha_e_espaco()
                        print("Essa opção não existe, tente novamente.")
                        print("")
                    
                elif principal == 2:
                    linha_e_espaco()
                    print("[PROFESSOR] MENU DE OPERAÇÕES")
                    exibir_menu_operaçoes()
                                                    
                    opera = int(input("Informe a ação desejada: "))
                    
                    if opera == 1:
                        linha_e_espaco()
                        print("==============INCLUIR=============\n")
                        codigop = int(input("Informe o código do professor: "))
                        nomesp = input("Informe o nome do professor: ")
                        cpfp = input("Informe o CPF do professor: ")
                        dados_prof = {}
                        dados_prof["código_professor"]= codigop
                        dados_prof["nome_professor"]= nomesp
                        dados_prof["cpf"]= cpfp
                        nome_prof = ler_arquivo("professor.json")
                        nome_prof.append(dados_prof)
                        salvar_arquivo(nome_prof,"professor.json")
                        input("\nPressione ENTER para continuar")
                        
                    elif opera == 2:
                        linha_e_espaco()
                        print("==============LISTAR=============\n")
                        nome_prof = ler_arquivo("professor.json")
                        if len(nome_prof) == 0:
                            print("Não há professores cadastrados")
                        else:
                             for prof in nome_prof:
                                print("-", prof)
                        input("\nPressione ENTER para continuar")
     
                    elif opera == 3:
                        linha_e_espaco()
                        print("==============ATUALIZAR===========\n")
                        nome_prof = ler_arquivo("professor.json")
                        if len(nome_prof) == 0:
                            print("\nNenhum professor foi incluído ainda")
                        else: 
                            codigo_atualizarp = int(input("Qual é o código que deseja atualizar? : "))
                            encontrado = False
                            for dados_prof in nome_prof:
                                if dados_prof["código_professor"] == codigo_atualizarp:
                                    dados_prof["código_professor"] = int(input("\nInforme o novo código: "))
                                    dados_prof["nome_professor"] = input("Informe o novo nome: ")
                                    dados_prof["cpf"]= input("Informe o novo CPF: ")
                                    print("\nPROFESSOR ATUALIZADO")
                                    encontrado = True
                                    break
                            
                            if not encontrado:
                                print("\nNenhum professor encontrado com esse código.")
                                
                            salvar_arquivo(nome_prof, "professor.json")
                                
                    elif opera == 4:
                        linha_e_espaco()
                        print("==============EXCLUIR=============\n")
                        nome_prof = ler_arquivo("professor.json")
                        if len(nome_prof) == 0:
                            print("\nNenhum professor foi incluído ainda")
                        else: 
                            codigo_excluir = int(input("Qual é o código que deseja excluir? : "))
                            encontrado = False
                            for dados_prof in nome_prof:
                                if dados_prof["código_professor"] == codigo_excluir:
                                    nome_prof.remove(dados_prof)
                                    print("\nPROFESSOR EXCLUÍDO")
                                    encontrado = True
                                    break
                            
                            if not encontrado:
                                print("\nNenhum professor encontrado com esse código.")
                                
                            salvar_arquivo(nome_prof, "professor.json")
                    
                    elif opera == 9:
                        print("__________________________________")
                        break
                    
                    else: 
                        linha_e_espaco()
                        print("Essa opção não existe, tente novamente.")
                        print("")
            
                elif principal == 3:
                    linha_e_espaco()
                    print("[DISCIPLINA] MENU DE OPERAÇÕES")
                    exibir_menu_operaçoes()
                    opera = int(input("Informe a ação desejada: "))
                    
                    if opera == 1:
                        linha_e_espaco()
                        print("==============INCLUIR=============\n")
                        codigod = int(input("Informe o código da disciplina: "))
                        nomesd = input("Informe o nome da disciplina: ")
                    
                        dados_dis = {}
                        dados_dis["código_disciplina"]= codigod
                        dados_dis["nome_disciplina"]= nomesd
                        
                        nome_dis = ler_arquivo("disciplina.json")
                        nome_dis.append(dados_dis)
                        salvar_arquivo(nome_dis,"disciplina.json")
                        input("\nPressione ENTER para continuar")
                          
                    elif opera == 2:
                        linha_e_espaco()
                        print("==============LISTAR=============\n")
                        nome_dis = ler_arquivo("disciplina.json")
                        if len(nome_dis) == 0:
                            print("Não há disciplinas cadastradas")
                        else:
                             for disc in nome_dis:
                                print("-", disc)
                        input("\nPressione ENTER para continuar")
     
                    elif opera == 3:
                        linha_e_espaco()
                        print("==============ATUALIZAR===========\n")
                        nome_dis = ler_arquivo("disciplina.json")
                        if len(nome_dis) == 0:
                            print("\nNenhuma disciplina foi incluída ainda")
                        else: 
                            codigo_atualizard = int(input("Qual é o código que deseja atualizar? : "))
                            encontrado = False
                            for dados_dis in nome_dis:
                                if dados_dis["código_disciplina"] == codigo_atualizard:
                                    dados_dis["código_disciplina"] = int(input("\nInforme o novo código: "))
                                    dados_dis["nome_disciplina"] = input("Informe o novo nome: ")
                                    print("\nDISCIPLINA ATUALIZADA")
                                    encontrado = True
                                    break
                            
                            if not encontrado:
                                print("\nNenhuma disciplina encontrada com esse código.")
                                
                            salvar_arquivo(nome_dis, "disciplina.json")
                                
                    elif opera == 4:
                        linha_e_espaco()
                        print("==============EXCLUIR=============\n")
                        nome_dis = ler_arquivo("disciplina.json")
                        if len(nome_dis) == 0:
                            print("\nNenhuma disciplina foi incluída ainda")
                        else: 
                            codigo_excluir = int(input("Qual é o código que deseja excluir? : "))
                            encontrado = False
                            for dados_dis in nome_dis:
                                if dados_dis["código_disciplina"] == codigo_excluir:
                                    nome_dis.remove(dados_dis)
                                    print("\nDISCIPLINA EXCLUÍDA")
                                    encontrado = True
                                    break
                            
                            if not encontrado:
                                print("\nNenhuma disciplina encontrada com esse código.")
                                
                            salvar_arquivo(nome_dis, "disciplina.json")
                    
                    elif opera == 9:
                        print("__________________________________")
                        break 

                    else: 
                        linha_e_espaco()
                        print("Essa opção não existe, tente novamente.")
                        print("")

                elif principal == 4:
                    linha_e_espaco()
                    print("[TURMAS] MENU DE OPERAÇÕES")
                    print("Em desenvolvimento...")
                    break
                        
                elif principal == 5:
                    linha_e_espaco()
                    print("[MATRÍCULAS] MENU DE OPERAÇÕES")
                    print("Em desenvolvimento...")
                    break
                        
                elif principal == 9:
                    linha_e_espaco()
                    print("Saindo")
                    print("")
                    break
                  
                else:
                    linha_e_espaco()
                    print("Essa opção não existe, tente novamente.")
                    print("")
                    break
            
            except ValueError:
                linha_e_espaco()
                print("São aceitos apenas números inteiros, tente novamente.")
                print("")
            
    except ValueError:
        linha_e_espaco()
        print("São aceitos apenas números inteiros, tente novamente.")
        print("")
