from modelos.avaliacao import Avaliacao

class Restaurante: # class do nosso programa 
    restaurantes = []

    def __init__ (self, nome, categoria): # Metodos especiais
        self._nome = nome.title() # .title() faz com que a primeira letra da primeira palvra fique com a letra maiúscula.
        self._categoria = categoria.upper() # .upper() faz com que todos os caractéres/todas as letras, fique com a letra maiúscula.
        self._ativo = False # O undeline serve para proteger e não privar o acesso das pessoas de modificar a ativação do restaurante.
        self._avaliacao = []
        Restaurante.restaurantes.append(self) # .append() adiciona mais informações na lista que vc desejar.
    
    def __str__ (self): # O método __str__ fornece uma representação em string da instância.
        return f'{self._nome} | {self._categoria}'
    
    @classmethod # Método da classe que não está referenciando a instância
    def listar_restaurantes(cls): # Metodos próprios
        print(f"{'Nome do Restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avalições'.ljust(25)} | {'Status'}")

        for restaurante in cls.restaurantes:
            print(f"{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}")

    @property #Modificar a forma como aquele atributo vai ser lido
    def ativo(self):
        return '👍' if self._ativo else '👎'
    
    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):

        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)

    @property
    def media_avaliacoes(self):

        if not self._avaliacao:
            return '-'
        
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

