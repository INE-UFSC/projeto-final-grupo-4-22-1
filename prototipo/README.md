# GRUPO 04 - Jogo do Sapo

## Protótipo

Nesse diretório, está o primeiro protótipo do jogo. A ideia do protótipo não é que ele seja uma versão demo do jogo completo, mas sim que o principal mecanismo do jogo esteja implementado com certo grau de sucesso.

## Instalação

Para a instalação você precisa utilizar o gerenciador de pacotes [pip](https://pip.pypa.io/en/stable/).

bash
pip install -r requirements.txt


## Execução

Para executar o protótipo do jogo você deve abrir o terminal de comando no seu computador e digitar o seguindo comando:

python
python3 app.py


## Dinâmica do jogo

O jogador (sapo) é representado por um quadrado preto. Seus inimigos (cobra e jacaré) são representados por 2 sprites temporários que ficam andando aleatoriamente pelo mapa. O objetivo é coletar as flores, que estão representadas por retângulos brancos e amarelos, e levar até a sua amada que está representada como um quadrado roxo no canto inferior esquerdo da tela. Ao coletar as flores a velocidade do jogador é diminuída, conforme o peso da flor coletada, até chegar ao mínimo que é 1, para aumentar a velocidade pode-se coletar maçãs, que estão representadas em vermelho e aumentam em 5 a velocidade do jogador.
Quando o jogador colide com a cobra ou o jacaré, o jogo termina e aparece no terminal `Perdeu! O jacaré te pegou!` ou `Perdeu! A cobra te pegou!`. Caso o jogador colida com as flores elas são coletadas por ele e somem do mapa. Da mesma forma, caso o jogador colida com as maçãs, sua velocidade aumenta e a maçã some do mapa. Para entregar as flores e o peso delas serem descontados da velocidade basta o jogador colidir com a sua amada. Ainda não existe mensagem para quando ele entrega todas as flores.


## Comandos

> *Para cima:* Tecla direcional para cima. <br>
> *Para baixo:* Tecla direcional para baixo. <br>
> *Para esquerda:* Tecla direcional para esquerda. <br>
> *Para direita:* Tecla direcional para direita. <br>
