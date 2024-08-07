class Restaurante:
    restaurantes = []

    def __init__ (self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False # O undeline serve para proteger e não privar o acesso das pessoas de modificar a ativação do restaurante
        Restaurante.restaurantes.append(self)
    
    def __str__ (self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'
    
    def listar_restaurantes():
        print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}")
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo.ljust(25)}")

    @property #Modificar a forma como aquele atributo vai ser lido
    def ativo(self):
        return '👍' if self._ativo else '👎'


restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pazzaria express', 'Italiana')

Restaurante.listar_restaurantes()