#metodo para criar classe e objetos, para programações oreintadas a objetos

class Aluno:  #definição de classe
    def __init__(self, nome, matricula):  #criação do objeto
        self.nome = nome
        self.matricula = matricula

    def apresentar_aluno(self):
        print(f"Nome do aluno: {self.nome}")
        print(f"Matricula do aluno: {self.matricula}")

a1 = Aluno("João", "123456")
print(a1.nome)
a1.apresentar_aluno()

a2 = a1
a1.nome = "Maria"
a2.apresentar_aluno()
