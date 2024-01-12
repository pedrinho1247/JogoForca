import random 


posicoes_forca = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========
    """,
        """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========
    """
]


class Forca:

    def __init__(self,palavra):
        self.palavra = palavra
        self.letras_erradas = []
        self.letras_certas = []
    
    def advinha(self,letra):
        if letra in self.palavra and letra not in self.letras_certas:
            self.letras_certas.append(letra)
        elif letra not in self.palavra and letra not in self.letras_erradas:
            self.letras_erradas.append(letra)
        else:
            return False
        return True
    
    def forca_acabou(self):
        if self.forca_venceu() or (len(self.letras_erradas) >= 6):
            return True
        return False
    
    def forca_venceu(self):
        if '_' not in self.palavra_escondida():
            return True
        return False
    
    def palavra_escondida(self):
        status = ''
        for letra in self.palavra:
            if letra not in self.letras_certas:
                status += '_ '
            else:
                status += letra
        return status
    
    def mostra_jogo(self):
        print('\n========== Jogo da Forca ==========')
        print(posicoes_forca[len(self.letras_erradas)])
        print(f'Palavra: {self.palavra_escondida()}')
        print('\nLetras erradas: ')
        for letra in self.letras_erradas:
            print(f' {letra}')
        print('\nLetras Corretas: ')
        for letra in self.letras_certas:
            print(f' {letra}')
                             
def palavra_aleatoria():
    with open("Trilha 3\Jogo\palavras.txt", "rt") as f:
        banco = f.readlines()
    return banco[random.randint(0, len(banco))].strip()

def main():
    jogo = Forca(palavra_aleatoria())

    while not jogo.forca_acabou():
        jogo.mostra_jogo()
        letra_escolhida = input('\nDigite uma letra: ')
        #Criar validação para somente uma letra
        #Opção de tentaar advinha a palavra
        jogo.advinha(letra_escolhida)

    jogo.mostra_jogo()

    if jogo.forca_venceu():
        print('\nParabéns! Você ganhou!!')
    else:
        print('\nFinal do Jogo! Você perdeu.')
        print('A palavra era ' + jogo.palavra)

    print('\nFoi bom jogar com você! \n')


if __name__ == "__main__":
    main()