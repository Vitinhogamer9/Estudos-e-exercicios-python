#### Calculadora simples
## Como funciona?

#O usuário insere números. Após isso, o usuário também insere a operação que deseja realizar. Não importando a ordem, a calculadora irá realizar as operações na seguinte ordem: multiplicação, divisão, adição e subtração. O resultado é mostrado ao usuário.
## Adiciona uma casa a cada operação, ou seja, se o usuário inserir 2 + 3 * 4, a calculadora irá realizar a multiplicação primeiro, depois a adição, e o resultado final será 14. Se o usuário inserir 10 - 5 / 2, a calculadora irá realizar a divisão primeiro, depois a subtração, e o resultado final será 7.5.
##Config das operações



##Primeiro o Número e depois a operação, ou seja, o usuário pode digitar 2 + 3 ou sei lá, o importante é que ele digite o número e a operação e depois o próximo número [[Primeira casa]]
## casa 1: primeiro número e operação e assim por diante.
Casa = 1
Contador = 0

#### Antes disso, é preciso saber qual vai ser a próxima operação e o próximo número, para que a calculadora possa realizar as operações na ordem correta.
Casas = []

def CriarCasa(numero, operacao, contador):
        return {
                "numero": numero,
                "operacao": operacao,
                "contador": contador
        }


def CalculacaoComeco():
        global Contador
        global Casa
        Contador += 1
        ProximoNumeroDigitado = input("Digite o próximo número: ")
        ProximaOperacaoDigitada = input("Digite a próxima operação (+, -, *, /): ")
                
        return ProximoNumeroDigitado, ProximaOperacaoDigitada
        

def OperacaoSelecionada(Numero1, Numero2, Operacao):
        if Operacao == "+":
                return int(Numero1) + int(Numero2)
        elif Operacao == "-":
                return int(Numero1) - int(Numero2)
        elif Operacao == "*":
                return int(Numero1) * int(Numero2)
        elif Operacao == "/":
                return int(Numero1) / int(Numero2)


# Primeiro número — fora do loop, pergunta só uma vez
NumeroDigitado = input("Digite o primeiro número: ")
TotalAtual = int(NumeroDigitado)  # guarda o total acumulado

##chama a função e desenpacota os valores — agora dentro do loop
while True:
       Contador += 1

       # Agora chama e guarda o retorno corretamente
       ProximoNumero, Operacao = CalculacaoComeco()

       novaCasa = CriarCasa(ProximoNumero, Operacao, Contador)
       Casas.append(novaCasa)
       print(f"Casa {Contador} adicionada ✅")

       Entrada = input("Adicionar Outro operador(Sim) ou Resultar (=): ")
       if Entrada == "Sim":
               pass  # volta pro topo do loop e pede nova casa
       elif Entrada == "=":
               # Calcula tudo em ordem
               for casa in Casas:
                       TotalAtual = OperacaoSelecionada(TotalAtual, casa["numero"], casa["operacao"])
               
               print(f"\nResultado final: {TotalAtual}")