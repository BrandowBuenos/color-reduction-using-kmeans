Carregamento da imagem PPM P3:
Lê-se as primeiras linhas que contêm informações sobre o tipo de imagem, a largura, a altura e o número máximo de cores.
Armazene os pixels da imagem em uma matriz, onde cada pixel é um vetor [R, G, B].
Inicialização dos centróides:
Escolha K cores aleatórias da matriz de pixels como centróides iniciais.
Armazene estes centróides em uma lista.
Cálculo dos clusters:
Para cada pixel da matriz de pixels, calcule a distância euclidiana dele até cada um dos K centróides.
Atribua o pixel ao cluster cujo centróide tenha a menor distância.
Repita este processo para todos os pixels da imagem.
Atualização dos centróides:
Para cada um dos K clusters, calcule a média de todos os pixels que pertencem a ele.
Substitua o antigo centróide pelo novo.
Repita este processo até que os centróides não mudem mais.
Redução de cores:
Substitua a cor de cada pixel pela cor do centróide ao qual ele pertence.
Salve a nova imagem como uma nova imagem PPM P3.
Finalização:
Exiba a nova imagem na tela ou salve-a em arquivo.
