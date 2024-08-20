from modelos.restaurante import Restaurante

Restaurante_praca = Restaurante('Praça', 'Gourmet')
'''
Restaurante_praca.receber_avaliacao('Jabes', 8)
Restaurante_praca.receber_avaliacao('Jhonata', 10)
Restaurante_praca.receber_avaliacao('Rilary', 7.5)
'''

Restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
Restaurante_mexicano.receber_avaliacao('Jabes', 5)
Restaurante_mexicano.receber_avaliacao('Jhonata', 7)
Restaurante_mexicano.receber_avaliacao('Rilary', 3.5)
Restaurante_mexicano.alternar_estado()


Restaurante_japones = Restaurante('Japa', 'Japonesa')
'''
Restaurante_japones.receber_avaliacao('Jabes', 10)
Restaurante_japones.receber_avaliacao('Jhonata', 7)
Restaurante_japones.receber_avaliacao('Rilary', 10)
'''


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()