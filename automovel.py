from datetime import date

class Automovel:
    def __init__(self, marca, modelo, matricula, cilindrada, data_fabricacao):
        self.marca = marca if marca is not None else ""
        self.modelo = modelo if modelo is not None else ""
        self.matricula = matricula if self.verifica_matricula(matricula) else "AA-00-00"
        self.cilindrada = cilindrada if cilindrada > 0 else "NA"
        self.data_fabricacao = data_fabricacao

    def verifica_matricula(self, matricula):
        array_matricula = matricula.split('-')
        if len(array_matricula) == 3:
            for i in range(len(array_matricula)):
                if (len(array_matricula[i]) == 2):
                    if not (array_matricula[i].isnumeric() or array_matricula[i].isalpha()):
                        return False
                else:
                    return False
            return True

    def compara_automovel(self, automovelComparador):
        if self.marca != automovelComparador.marca or self.modelo != automovelComparador.modelo:
            return False
        return True

    def info_automovel(self):
        return (f'{self.marca} {self.modelo}, {self.matricula} e {self.cilindrada} de cilindrada')

# Criando uma instância da classe Automovel
automovel = Automovel(marca="Ford", modelo="Focus", matricula="13-FK-14", cilindrada=-12, data_fabricacao=date(2022, 1, 1))
automovelComparador = Automovel(marca="Ford", modelo="Supra", matricula="13-FK-14", cilindrada=-12, data_fabricacao=date(2022, 1, 1))

# Testando o método verifica_matricula
resultado = automovel.verifica_matricula(automovel.matricula)
info = automovel.compara_automovel(automovelComparador)
print(info)
