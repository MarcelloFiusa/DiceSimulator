# simular o uso de um dado, gerando um valor de 1 até 6

import random
import PySimpleGUI as sg

class SimuladorDeDados:

    def __init__(self):
        self.valor_minimo = 1
        self.valor_maximo = 6
        self.mensagem = 'Você gostaria de gerar um novo valor para o dado?'

    def Iniciar(self):
        resposta = input(self.mensagem)

        try:
            while resposta != 's' or resposta != 'n' or resposta == 'sim' or resposta == 'não':
                if resposta == 'sim' or resposta == 's':
                    self.GerarValorDoDado()
                    break
                elif resposta == 'não' or resposta == 'n':
                    print('Agradecemos sua participação!')
                    break
                else:
                    print('Por favor, digitar sim ou não')
                    resposta = input(self.mensagem)
        except:
            print('Ocorreu um erro ao receber sua resposta')

    def GerarValorDoDado(self):
        print(random.randint(self.valor_minimo, self.valor_maximo))


simulador = SimuladorDeDados()
simulador.Iniciar()
