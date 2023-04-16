class aluno():
    def __init__(self, codigo, nome, matricula):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula
        
    def imprimir(self):
        print(f" Codigo:{self.codigo} ")
        print(f" Nome:{self.nome} ")
        print(f" Matricula :{self.matricula} ")

class AlunoEnsinoMedio(aluno):
    def __init__(self, codigo, nome, matricula, ano_letivo):
        super().__init__(codigo, nome, matricula)
        self.__ano_letivo = ano_letivo

    def imprimir(self):
        super().imprimir()
        print(f"Ano letivo:{self.__ano_letivo}")

class AlunoGraduacao(aluno):
    def __init__(self, codigo, nome, matricula, semestre):
        super().__init__(codigo, nome, matricula)
        self.semestre = semestre

    def imprimir(self):
        super().imprimir()
        print (f"Semestre: {self.semestre}")


a = aluno(1, "GABRIEL SABADIN"," 978412")
a.imprimir()

b = AlunoEnsinoMedio(2, "JANDIR SABADIN"," 1231", 19992)
b.imprimir()

c = AlunoGraduacao(4, "NELCI BELLEBONI", "72391", 2)
c.imprimir()