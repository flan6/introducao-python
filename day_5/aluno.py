import pessoa

class Aluno(Pessoa):
    _Nome = ""
    _Matricula = 0
    __Turma = 0

    def SetName(self, nome: str):
        self._Nome = nome

    def GetName(self) -> str:
        return self._Nome

    def SetTurma(self, turma: int):
        self.__Turma = turma

    def GetTurma(self) -> int:
        return self.__Turma
