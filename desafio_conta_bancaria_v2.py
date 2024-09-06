from datetime import datetime, timedelta
import textwrap
menu = '''[D]\tDepositar
[S]\tSacar
[E]\tExtrato
[Q]\tSair 
[nc]\tNova conta
[lc]\tListar contas
[nu]\tNovo usuário

O que deseja fazer: '''


saldo = 0
extrato=""
ultima_transacao_data_hora=datetime.now()
#
hora_atual_simulada = datetime.strptime('06/09/2024 14:30:00', "%d/%m/%Y %H:%M:%S")
numero_saque=0
saque_restante=3
VALOR_MAXIMO_SAQUE = 500
LIMITE_SAQUES = 3
LIMITE_TRANSACAO_DIARIA= 10 
LIMITE_TRANSACAO =10
transacoes =0
ate_10_transac_nesse_periodo=  ultima_transacao_data_hora+ timedelta(minutes=1440) 
conta= 0
AGENCIA= "0001"
usuarios= []
contas = []
#função de deposito bancario
def depositar(saldo, valor,extrato,/):
           
     if valor > 0:
          saldo += valor                                           
          extrato +=f"Depositado: R$ {valor:.2f} \n"
          print("\nDepositado!")        
     else:
          print("Operação não realizada: Valor inválido")                    
     return saldo,extrato
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = existente_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def criar_usuario(usuarios):
      cpf = input("Insira o CPF")
      usuario = existente_usuario(cpf,usuarios)
      if usuario:
            print("Usuario ja existe")
            return
      
      nome_usuario = input("insira seu nome:\t")
      data_nascimento = input("Data de nescimento (formato dd/mm/yyyy ):\t")
      endereco = input("Enderco completo:\t")
      usuarios.append({"cpf":cpf,"nome":nome_usuario,"data_nascimento":data_nascimento})

      print("Criado com sucesso")
     
def existente_usuario(cpf, usuarios):
      for usuario in usuarios:
            if usuario['cpf'] == cpf:
                  return usuario
      

def gravador( hora_transacao, limite_trasacoes_restantes):
          message_hora = datetime.strftime( hora_transacao,"%d/%m/%Y %H:%M:%S")
          message_limite = limite_trasacoes_restantes
          return message_hora, message_limite
       
#funcão de saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
     sem_saldo =valor > saldo
     sem_limite = valor > limite
     sem_saques_disponiveis =  numero_saques >= limite_saques
    
     if sem_saldo:
          print("Operação não realizada:e Saldo insuficiente")
          
     elif sem_limite:
          print("Operação não realizada: Valor excedido por saque")
          
     elif sem_saques_disponiveis:
          print("Operação não realizada: Limite de saques excedido")
          
     elif valor > 0:
          saldo -=valor         
          numero_saques +=1
          
          #saque_restante -= 1         
          extrato +=f" Realizado saque de: R$ {valor:.2f} \n"
               
     else:
          print("Operação não realizada: Valor inválido")
          
    
     return saldo, extrato

#funcão de extrato bancario
def exibir_extrato( saldo,/,*,extrato):

 
    print("***************EXTRATO*****************")

    if extrato=="":            
        print("Não foram realizados transações.")
        print(f"\nSaldo em conta: R$ {saldo:.2f}")
        
        print("***************************************")
    else:
        print(extrato)
        print(f"\nSaldo em conta: R$ {saldo:.2f}")
      
        print("***************************************")

#loop do menu 
while True:
        op = input(menu)
          # COLOQUE AQUI PARA SIMULARA HORA ATUAL SE PARA TESTES
        #hora_atual_simulada = datetime.strptime(input("Insira a data e hora para simular"), "%d/%m/%Y %H:%M:%S")
        
        
        if op.upper() == "D":
                try:
                    valor = float(input("Digite o valor a ser depositado: R$ "))
                    saldo, extrato = depositar(saldo, valor,extrato)
                   
                except ValueError:
                     print("Erro invalido valor")
                
        
        elif op.upper()  == "S":
             valor = float(input("Digite o valor a ser sacado: R$ "))
             
             saldo,extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=VALOR_MAXIMO_SAQUE,
                numero_saques=numero_saque,
                limite_saques=LIMITE_SAQUES,
            )

        elif op.upper()  == "E":
              exibir_extrato(saldo, extrato=extrato)

        elif op.upper()  == "Q":
              print("Obrigado por usar nosso sistema, até mais.\n")
              break
        elif op.upper() == "NC":
               num_conta =len(contas)+1
               criar_conta(AGENCIA,num_conta,usuarios)
        elif op.upper() =="LC":
               listar_contas(contas)

        elif op.upper() =="NU":              
              criar_usuario(usuarios)
        else:
             print("Opção incorreta tente novamente.\n\n")
              





        