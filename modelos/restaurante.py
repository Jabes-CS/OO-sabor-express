class Restaurante: # class do nosso programa 
    restaurantes = []

    def __init__ (self, nome, categoria): # Metodos especiais
        self._nome = nome.title() # .title() faz com que a primeira letra da primeira palvra fique com a letra maiúscula.
        self._categoria = categoria.upper() # .upper() faz com que todos os caractéres/todas as letras, fique com a letra maiúscula.
        self._ativo = False # O undeline serve para proteger e não privar o acesso das pessoas de modificar a ativação do restaurante.
        Restaurante.restaurantes.append(self) # .append() adiciona mais informações na lista que vc desejar.
    
    def __str__ (self): # O método __str__ fornece uma representação em string da instância.
        return f'{self._nome} | {self._categoria}'
    
    @classmethod # Método da classe que não está referenciando a instância
    def listar_restaurantes(cls): # Metodos próprios
        print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.ativo.ljust(25)}")

    @property #Modificar a forma como aquele atributo vai ser lido
    def ativo(self):
        return '👍' if self._ativo else '👎'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

'''
restaurante_praca = Restaurante('praça', 'gourmet')
#restaurante_praca.nome = 'Praça 2.0' # Se eu tentar modificar o valor dessa linha de código não vai acontecer nada, pois os objetos está configurados "privados", para não sofrer alterações.
restaurante_praca.alternar_estado()

restaurante_pizza = Restaurante('pizza express', 'italiana')

Restaurante.listar_restaurantes()
'''