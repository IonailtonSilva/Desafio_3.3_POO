class UsuarioTelefone:
    def __init__(self, nome_usuario, numero_usuario, saldo):
        self.nomeusuario = nome_usuario
        self.numerousuario = numero_usuario
        self.saldo = saldo
        

    @classmethod
    def verificar_saldo(cls, saldo_inicial, saldo):

        saldo_inicial.append(saldo)

        return cls(saldo)
    
    @classmethod
    def calcular_custos(cls, custo_minuto, duracao_chamada, custo_chamada):
         
        custo_minuto = 0.10

        custo_chamada = custo_minuto * duracao_chamada

        return cls(custo_chamada, custo_minuto, duracao_chamada)
    
    @staticmethod
    def fazer_chamada(cls, saldo, custo_chamada):
        
        
        if saldo >= custo_chamada:

            print(f"Chamada para {numero_destinatario} realizada com sucesso. Saldo: {diferenca_saldo}")

        else:

            print("Saldo insuficiente para fazer a chamada.")

        return cls (saldo, custo_chamada)
           
class Plano:
    def __init__(self, saldo, custo_chamada):
        self.saldo = saldo
        self.custo = custo_chamada

    @classmethod
    def deduzir_saldo(cls, saldo, custo_chamada):

        diferenca_saldo = (saldo - custo_chamada)

        return cls (diferenca_saldo)

class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome_usuario, numero_usuario, saldo):
        super().__init__(nome_usuario, numero_usuario, Plano(saldo))


nome_usuario = input("digite seu nome: ")
numero_usuario = str(input("digite seu nro: "))
saldo_inicial = float(input("digite o seu saldo: "))
numero_destinatario = str(input("digite o numero do destinatario: "))
duracao_chamada = float(input("digite a duracão da chamada(mins): "))    


#plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
#usuario = UsuarioTelefone(nome_usuario, nome_plano) 
UsuarioPrePago.fazer_chamada(numero_destinatario, duracao_chamada)
#UsuarioTelefone.fazer_chamada(saldo_inicial, numero_destinatario)
#Plano.deduzir_saldo(diferenca_saldo)
#UsuarioPrePago.fazer_chamada(nome_usuario, numero_usuario, numero_destinatario, duracao_chamada, saldo_inicial)
