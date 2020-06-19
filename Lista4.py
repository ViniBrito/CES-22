# Vinícius Brito Bastos Antunes: COMP-22

# Exercício 1

from abc import ABCMeta, abstractmethod
import tkinter as tk
import tkinter.messagebox as msg

class Motor:
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def getNome(self):
        return self.__nome__
    @abstractmethod
    def getPotencia(self):
        return self.__potencia__


class MotorEletrico(Motor):
    __nome__ = "Elétrico"
    __potencia__ = 3.2

class MotorCombustao(Motor):
    __nome__ = "de combustão"
    __potencia__ = 3
    
class MotorHibrido(Motor):
    __nome__ = "Híbrido"
    __potencia__ = 4


class Veiculo:
    __metaclass__ = ABCMeta
    __nome__ = None
    __rodas__ = 2
    __capacidade__ = 2
    __motor__ = None
    
    @abstractmethod
    def getNome(self):
        return self.__nome__
    @abstractmethod
    def getRodas(self):
        return self.__rodas__
    @abstractmethod
    def getCapacidade(self):
        return self.__capacidade__
    
class Carro(Veiculo):
    __nome__ = "Carro"
    __rodas__ = 4
    __capacidade__ = 5
    
    def setMotor(self, nome):
        self.__motor__ = nome

class Bicicleta(Veiculo):
    __nome__ = "Bicicleta"
    __rodas__ = 2
    __capacidade__ = 1
    
class Moto(Veiculo):
    __nome__ = "Moto"
    __rodas__ = 2
    __capacidade__ = 2
    
    def setMotor(self, nome):
        self.__motor__ = nome

class Caminhao(Veiculo):
    __nome__ = "Caminhão"
    __rodas__ = 8
    __capacidade__ = 2
    
    def setMotor(self, nome):
        self.__motor__ = nome

class Onibus(Veiculo):
    __nome__ = "Ônibus"
    __rodas__ = 4
    __capacidade__ = 30
    
    def setMotor(self, nome):
        self.__motor__ = nome

# Exercício 2

"""Creating basic pizza ingredients"""

class Ingredient:
    def getDescription(self):
        return self.__class__.__name__
    
    def getTotalCost(self):
        return self.__class__.cost*self.__class__.amount

class Cheese(Ingredient):
    cost = 0.2
    amount = 2

class Decorator(Ingredient):
    def __init__ (self, Ingredient):
        self.component = Ingredient
    def getTotalCost(self):
        return self.component.getTotalCost() + Ingredient.getTotalCost(self)
    def getDescription(self):
        return self.component.getDescription() + ' '+ Ingredient.getDescription(self)

class Meat(Decorator):
    cost = 0.75
    amount = 1
    def __init__(self, Ingredient):
        Decorator.__init__(self, Ingredient)
    
class Chicken(Decorator):
    cost = 0.6
    amount = 1.4
    def __init__(self, Ingredient):
        Decorator.__init__(self, Ingredient)

class Tomato(Decorator):
    cost = 0.25
    amount = 0.7
    def __init__(self, Ingredient):
        Decorator.__init__(self, Ingredient)

class Bacon(Decorator):
    cost = 0.25
    amount = 0.3
    def __init__(self, Ingredient):
        Decorator.__init__(self, Ingredient)

class Pasta(Decorator):
    cost = 0.25
    amount = 3
    def __init__(self, Ingredient):
        Decorator.__init__(self, Ingredient)

class Corn(Decorator):
    cost = 0.25
    amount = 1
    def __init__(self, Ingredient):
        Decorator.__init__(self, Ingredient)
        
"""Now, let's order a yummy pizza"""

order = Bacon(Tomato(Meat(Cheese(Pasta()))))

# Exercício 3

"""Setting up two factories: motors and vehicles"""

class Fabricamotor:
    __metaclass__ = ABCMeta
    
    def cria(self, tipo):
        if tipo=="elétrico" or tipo=="Elétrico":
            return motoreletrico( )
        elif tipo=="híbrido" or tipo=="Híbrido":
            return motorhibrido( )
        else:
            return motorcombustao( )
    
    @abstractmethod
    def getNome(self):
        return self.__nome__
    @abstractmethod
    def getPotencia(self):
        return self.__potencia__


class motoreletrico(Fabricamotor):
    
    def __init__(self):
        self.__nome__ = "Elétrico"
        self.__potencia__ = 3.2

class motorcombustao:
    
    def __init__(self):
        self.__nome__ = "de combustão"
        self.__potencia__ = 3
    
class motorhibrido:
    
    def __init__(self):
        self.__nome__ = "Híbrido"
        self.__potencia__ = 4

class Fabricaveiculo:
    __metaclass__ = ABCMeta
    __nome__ = None
    __rodas__ = 2
    __capacidade__ = 2
    __motor__ = None
    
    def cria(self, tipo):
        if tipo=="carro":
            return carro()
        elif tipo=="bicicleta":
            return bicicleta()
        elif tipo=="caminhao":
            return caminhao()
        elif tipo=="moto":
            return moto()
        else:
            return onibus()
    
    @abstractmethod
    def getNome(self):
        return self.__nome__
    @abstractmethod
    def getRodas(self):
        return self.__rodas__
    @abstractmethod
    def getCapacidade(self):
        return self.__capacidade__
    
class carro(Fabricaveiculo):
    __nome__ = "Carro"
    __rodas__ = 4
    __capacidade__ = 5
    
    def setMotor(self, nome):
        self.__motor__ = nome

class bicicleta(Fabricaveiculo):
    __nome__ = "Bicicleta"
    __rodas__ = 2
    __capacidade__ = 1
    
class moto(Fabricaveiculo):
    __nome__ = "Moto"
    __rodas__ = 2
    __capacidade__ = 2
    
    def setMotor(self, nome):
        self.__motor__ = Fabricamotor().cria(nome)

class caminhao(Fabricaveiculo):
    __nome__ = "Caminhão"
    __rodas__ = 8
    __capacidade__ = 2
    
    def setMotor(self, nome):
        self.__motor__ = nome

class onibus(Fabricaveiculo):
    __nome__ = "Ônibus"
    __rodas__ = 4
    __capacidade__ = 30
    
    def setMotor(self, nome):
        self.__motor__ = nome

"""The following shows how this can be used:
    v = Fabricaveiculo().cria("moto")
    v.setMotor("Elétrico")
    v.__nome__
    v.__motor__.__nome__
"""

# Exercício 4

"""
Disclaimer: I've tried hard to set up
            a class per command (Exibir extrato, pagar...),
            but the code simply wouldn't run.
            So I've put it all inside the Interface,
            but I know it should call each
            specific class at each button
"""

class Interface(tk.Frame):
    tflag = False;
    
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack(expand=True)
        self.create_widgets()
        self.saldo = 0
        self.hist = []

    def create_widgets(self):
        self.extrato = tk.Button(self, bg="cyan", width=15)
        self.extrato["text"] = "Exibir Extrato"
        self.extrato["command"] = self.extra
        self.extrato.pack( )
        self.pagamento = tk.Button(self, bg="cyan", text="Pagar", width=15, command=self.paylabel)
        self.pagamento.pack( )
        self.transf = tk.Button(self, bg="cyan", text="Transferir", command=self.transflabel)
        self.transf["width"] = 15
        self.transf.pack( )
        self.sair = tk.Button(self, text="Sair", fg="red", command=self.master.destroy)
        self.sair["width"] = 15
        self.sair.pack(side="bottom")

    def paylabel(self):
        if not self.tflag:
            self.tflag = True
            self.text3 = tk.StringVar(self)
            self.text3.set("Digite aqui o valor do pagamento")
            self.entry3 = tk.Entry(textvariable = self.text3)
            self.entry3.config(width=40)
            self.entry3.pack(side="top")
            self.text4 = tk.StringVar(self)
            self.text4.set("Digite aqui o código do boleto")
            self.entry4 = tk.Entry(textvariable = self.text4)
            self.entry4.config(width=40)
            self.entry4.pack(side="top")
            self.concl2 = tk.Button(self, bg="cyan", text="Concluir pagamento", command=self.success)
            self.concl2["width"] = 20
            self.concl2.pack(side="bottom")
            
    def transflabel(self):
        if not self.tflag:
            self.tflag = True
            self.text1 = tk.StringVar(self)
            self.text1.set("Digite aqui o valor a ser transferido")
            self.entry1 = tk.Entry(textvariable = self.text1)
            self.entry1.config(width=40)
            self.entry1.pack(side="top")
            self.text2 = tk.StringVar(self)
            self.text2.set("Digite aqui o CPF ou CNPJ do destino")
            self.entry2 = tk.Entry(textvariable = self.text2)
            self.entry2.config(width=40)
            self.entry2.pack(side="top")
            self.concl = tk.Button(self, bg="cyan", text="Concluir transferência", command=self.print_success)
            self.concl["width"] = 20
            self.concl.pack(side="bottom")

    def success(self):
        try:
            float(self.entry3.get())    
        except ValueError:
            self.msg = msg.showerror(title="Conclusão", message="Insira um valor válido de pagamentp", options=None)
        else:
            if float(self.entry3.get())<0.0:
                self.msg = msg.showerror(title="Conclusão", message="Insira um valor válido de transferência", options=None)
            else:
                self.msg = msg.showinfo(title="Conclusão", message="Transferência concluída com sucesso!", options=None)
                self.hist.append("Pagamento de boleto no valor de R$ "+self.text3.get())
                self.saldo-=float(self.text3.get())
                self.tflag = False
                self.entry3.destroy()
                self.entry4.destroy()
                self.concl2.destroy()
    
    def print_success(self):
        try:
            float(self.entry1.get())    
        except ValueError:
            self.msg = msg.showerror(title="Conclusão", message="Insira um valor válido de transferência", options=None)
        else:
            if float(self.entry1.get())<0.0:
                self.msg = msg.showerror(title="Conclusão", message="Insira um valor válido de transferência", options=None)
            else:
                self.msg = msg.showinfo(title="Conclusão", message="Transferência concluída com sucesso!", options=None)
                self.hist.append("Transferência de R$ "+self.text1.get())
                self.saldo-=float(self.text1.get())
                self.tflag = False
                self.entry1.destroy()
                self.entry2.destroy()
                self.concl.destroy()

    def extra(self):
        print("-------------------------\nExtrato atual do cliente\n-------------------------")
        if self.hist == []:
            print("Nada a exibir")
        else:
            for x in self.hist:
                print(x)
        print("Saldo final =",self.saldo)
        

root = tk.Tk()
root.geometry("400x200+500+250")
app = Interface(master=root)
app.mainloop()

# Exercício 5

class State:
    __author__ = None
    __revapproved__ = False
    __pubuser__ = False
    __pubadmin__ = False
    __expired__ = False
    
    def __init__(self, nome, nome2):
        self.__name__ = nome
        self.__author__ = nome2
    
    def write(self):
        """redige"""
    
    def publish(self):
        """publica"""
    
    def analyse(self):
        """avalia documento"""
    
class Draft(State):
    
    def write(self):
        if (not self.__pubuser__) or (not self.__revapproved__) or self.__expired__:
            """escreve ou corrige rascunho"""
    
    def publish(self):
        if not self.__pubuser__:
            """publica como usuário"""
            self.__pubuser__ = True
        else:
            """publica como admin"""
            self.__pubadmin__ = True

class Moderation(State):
    
    def analyse(self):
        """usa critérios técnicos;
           modifica self.__revapproved__"""
        
    
class Published(State):
    
    def analyse(self):
        """avalia se o documento expirou
           pode modificar self.__expired__"""

class Context:
    def __init__(self, nome, nome2):
        self.__state__ = Draft(nome, nome2)
    
    def manage(self):
        """verifica se é necessário mudar
           de estado, e o faz, em caso afirmativo"""