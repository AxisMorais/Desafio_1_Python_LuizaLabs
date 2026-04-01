from abc import ABC, abstractclassmethod, abstractproperty
from datetime import  datetime


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas =[]

    #Erro voltar no minuto 1:58
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self,conta):
        self.contas.append(conta)

#Pessoa física foi extendida a Cliente. Pessoa Física classe filha, Cliente, classe pai
class PessoaFisica(Cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        #Aciona a super classe "classe pai - cliente" para armezaenar endereco
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento= data_nascimento
        self.cpf=cpf



class Conta:
    def __init__(self, numero, cliente):
        self._saldo =0
        self._numero = numero
        self._agenfica ="0001"
        self._cliente = cliente
        #self._historico = Historico();

    #Isso é um métdo de classe, ele recebe um parametro do tipo cliente e retorna atributos do cliente
    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agenfica

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo

        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação Falhou ! Saldo Insuficiente!")

        elif  valor >  0:
            self.saldo -= valor
            print("Saque realizado com sucesso !")
            return True
        else:
            print("Operacao falhou! O valor informado é inválido!")


    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Deposito realizado com sucesso!")
        else:
            print("Operação falhou! Valor inválido!")
            return False
        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saque = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saque

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite. ")

        elif excedeu_saques:
            print(" Operação falhou! Número máximo de saques excedido. ")

        else:
            #Chama o método sacar da classe pai, nesse caso a classe conta
            return super().sacar(valor)

        return False

    def  __str__(self):
        return f"""\
                     Agência:\t{self.agencia}
                     Conta Corrente:\t\t {self.numero}
                     Titular:\t{self.cliente.nome}
                 """

class Historico:
    def __init__(self):
        self.transacoes =[]

    @property
    def transacoes(self):
        return self.transacoes


    def adicionar_transacao(self, transacao):
        self._tarnsacoes.append(
        {
                "tipo": transacao.__class__.name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime
                ("%d-%m-%Y %H:%M:%s"),
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    @property
    def  valor(self):
        return self.valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)











