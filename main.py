class Node:
    def __init__(self, caractere=None):
        self.caractere = caractere
        self.filho_esquerdo = None
        self.filho_direito = None

class ArvoreBinariaMorse:
    def __init__(self):
        self.raiz = Node()

    def inserir(self, codigo_morse, caractere):
        no_atual = self.raiz
        for simbolo in codigo_morse:
            if simbolo == '.':
                if no_atual.filho_esquerdo is None:
                    no_atual.filho_esquerdo = Node()
                no_atual = no_atual.filho_esquerdo
            elif simbolo == '-':
                if no_atual.filho_direito is None:
                    no_atual.filho_direito = Node()
                no_atual = no_atual.filho_direito
        no_atual.caractere = caractere

    def remocao(self, busca):
        return self.remover(busca, self.raiz)


    def remover(self, busca, no):
        if no.caractere == busca:
            no.caractere = None
            return True
        if no.filho_direito:
            if self.remover(busca, no.filho_direito):
                return True
        if no.filho_esquerdo:
            if self.remover(busca, no.filho_esquerdo):
                return True
        else:
            return False

    def busca(self, texto):
        codigo = ""
        for caractere in texto:
            if caractere == " ":
                codigo += " "
            else:
                caminho = self.buscar(caractere, self.raiz)
                if caminho is None:
                    return None
                codigo+=caminho+" "
        return codigo

    def buscar(self, caractere, no, caminho=''):
        if no is None:
            return None
        if no.caractere == caractere:
            return caminho
        esquerda = self.buscar(caractere, no.filho_esquerdo, caminho + '.')
        if esquerda:
            return esquerda
        direita = self.buscar(caractere, no.filho_direito, caminho + '-')
        if direita:
            return direita
        return None

    def exibir(self):
        linhas = []
        for i in range(self.altura()):
            linhas.append("")
            for j in range(2**i):
                no_atual = self.raiz
                resposta = " "
                numero = (j + 2 ** i)
                ordem = ""
                for k in range(self.altura()):
                    if numero%2==0 and numero >= 2:
                        ordem+="e"
                    elif numero%2==1 and numero >= 2:
                        ordem+="d"
                    numero = numero//2
                ordem = ordem[::-1]
                for l in ordem:
                    if l == "d":
                        no_atual = no_atual.filho_direito
                    elif l == "e":
                        no_atual = no_atual.filho_esquerdo
                if no_atual is not None:
                    if resposta != "?" and j+i != 0 and no_atual.caractere is not None:
                        resposta = no_atual.caractere
                    else:
                        resposta = "?"
                else:
                    resposta = "?"
                linhas[i]+=((" " * int((2 ** (self.altura() - (i+1))-1))) + str(resposta)+" " * int(2 ** (self.altura() - (i+1))))
        for linha in linhas:
            print(linha)



    def altura(self, no=None):
        if no is None:
            no = self.raiz
        if no is None:
            return 0
        altura_esquerda = self.altura(no.filho_esquerdo) if no.filho_esquerdo else 0
        altura_direita = self.altura(no.filho_direito) if no.filho_direito else 0
        if altura_direita>altura_esquerda:
            return altura_direita+1
        else:
            return altura_esquerda+1


    def incercao_automatica(self):
        codigo_morse = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..',
            '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
            '8': '---..', '9': '----.', '0': '-----', '+': '.-.-.', '=': '-...-', '/': '-..-.',
        }
        for caractere, codigo in codigo_morse.items():
            self.inserir(codigo, caractere)


arvore = ArvoreBinariaMorse()
arvore.incercao_automatica()

acao = 0
while True:
    acao = input(f"""
--------------------
    Selecione ação:
1 - adicionar caractere
2 - remover caractere
3 - traduzir para morse
4 - exibir a arvore
5 = fechar
--------------------
""")
    if acao == "1":
        caractere = input("caractere a ser adicionado")
        codigo = input("caractere em morse")
        arvore.inserir(codigo, caractere)
        print("adicionado")
    elif acao == "2":
        caractere = input("caractere a ser removido")
        if arvore.remocao(caractere):
            print("caractere removido com sucesso")
        else:
            print("caractere não existe")
    elif acao == "3":
        mensagem = input("inserir mensagem ou caractere para tradução")
        resposta = arvore.busca(mensagem.upper())
        if resposta:
            print(resposta)
        else:
            print("Algum caractere não está inserido")
    elif acao == "4":
        arvore.exibir()
    elif acao == "5":
        break
    else:
        print("ação invalida")
