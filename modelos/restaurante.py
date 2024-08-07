class Restaurante:
    restaurantes = []

    def __init__ (self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False # O undeline serve para proteger e não privar o acesso das pessoas de modificar a ativação do restaurante
        Restaurante.restaurantes.append(self)
    
    def __str__ (self):
        return f'{self._nome} | {self._categoria}'
    
    def listar_restaurantes():
        print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}")
        for restaurante in Restaurante.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)}")

    @property #Modificar a forma como aquele atributo vai ser lido
    def ativo(self):
        return '👍' if self._ativo else '👎'

restaurante_praca = Restaurante('praça', 'gourmet')
restaurante_praca.nome = 'Praça 2.0'
restaurante_pizza = Restaurante('pizza express', 'italiana')

Restaurante.listar_restaurantes()
