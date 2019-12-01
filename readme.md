Para rodar o projeto é necessário ter a versão 3.7 do python
instalada na sua máquina

no prompt/terminal vá até a pasta raiz do projeto e rode o 
comando: python ./Main.py nome_do_arquivo.java, o nome do 
arquivo pode ser qualquer um dos abaixos:

BinarySearch.java
BinaryTree.java
BubbleSort.java
Factorial.java
LinearSearch.java
LinkedList.java
QuickSort.java
TreeVisitor.java
gb.java
gb++.java

Para adicionar mais arquivos basta incluí-los dentro da pasta
archives.

Ao rodar o comando o projeto realizara o parse do arquivo
e exibirá uma lista de tokens.

Arquivo SymbolTable.py:
    Usado para organizar todos os símbolos, escopos e tipos dinâmicos da linguagem.

Arquivo Lex.py:
    Contém a classe que da origem ao objeto afd, este objeto valida, 
    ou não, se um caracter ou um agrupamento deles pertencem ao afd.

Arquivo LexRules.py:
    Contém as regras dos lexemas da gramática.

Arquivo SyntaticRules.py:
    Contém as regras sintáticas da gramática.

Arquivo SyntaticParser.py:
    Guarga a lógica necessária para realizar a análise sintática e semântica da gramática.
    Regras semânticas tipo de dado da variavel e scopo da variável.

Arquivo MegaAutomato.py:
    Estrutura que gerência a lista de afnds sintáticos da gramática.

Arquivo AFND.py:
    Monta o automato não determinístico.

Arquivo Reader.py:
    Contém a classe que dado uma string busca abrir o respectivo arquivo
    dentro da pasta archives. Além de abrir o arquivo possui controles de
    leitura de buffer, develução de caracter ao buffer e verificação do
    fim do arquivo.

Arquivo Token.py:
    Contém a classe token que guarda as pripriedades de um token e também
    sua função to_string().

Arquivo Main.py:
    Contém a classe compiler responsável por gerenciar tokens e afds, ler os
    caracteres do arquivo e identificar e alocar em uma lista os tokens. 
    O método "init_afds" é o responsável por instaciar os objetos tokens e seu
    respectivo afd. 

    O método "find_token" ao receber uma palavra dispacha para os afds que por sua
    vez responde se esta é valida ou não, aquele que responde como válida será o
    token determinado.

    O método "parse" é responsavél por percorrer o arquivo, contralar a atualização
    das colunas e linhas, remover os espaços em brancos/tabs, montar as palavras 
    para que sejam validadas e adicionar os tokens a lista.
