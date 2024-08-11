from modelos.restaurante import Restaurante

Restaurante_praca = Restaurante('Praça', 'Gourmet')
Restaurante_mexicano = Restaurante('Mexican Food', 'Mexicana')
Restaurante_japones = Restaurante('Japa', 'Japonesa')

Restaurante_mexicano.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()