# README

Nesta sessão do  repositório estão os algoritmos de ordenaçaõ referentes a atividade avaliativa da primeira unidade da disciplina de estrutura de dados . Neste arquivo README, você encontrará instruções sobre como configurar o ambiente virtual e executar os programas.

## Configurando o Ambiente Virtual

1. Certifique-se de ter o Python instalado em sua máquina, com a versão mais recente, pois os algoritmos nessa sessão usam type hint, que só está disponível em versões mais atualizadas. Você pode fazer o download em https://www.python.org/downloads/.

2. Abra o terminal ou prompt de comando e navegue até o diretório /atividade_u01/fontes.

3. Crie um ambiente virtual executando o seguinte comando:

```bash
python -m venv nome_do_ambiente
```

4. Ative o ambiente virtual:

- No Windows:
```bash
nome_do_ambiente\Scripts\activate
```

- No macOS e Linux:
```bash
source nome_do_ambiente/bin/activate
```

## Executando os códigos

Após configurar o ambiente virtual, siga os passos abaixo para executar os programas:

1. No terminal ou prompt de comando, certifique-se de estar neste diretório.

2. Escolha um dos programas , seguido pelo tamanho do vetor desejado. Por exemplo, para um vetor de tamanho 10:

```bash
python programa.py 10
```

3. O programa será executado e exibirá o tempo em nano segundos em eu foi executado.


## Executando com o iterate

O script iterate.sh só pode ser executado no terminal no linux ou usando WSL para windows. O iterate irá interagir com os scripts python gerando vetores cada vez maiores e os salvando em arquivos txt para posteriormente poderem ser usados para gráficos.

1. Ainda do diretório /atividade_u01/fontes execute o seguinte comando no terminal.

```bash
./iterate.sh execuções tamanho_inicial_n aumento_n tamanho_final "python3 nome_do_arquivo.py" nome_do_txt
```

2. Exemplo:

```bash
./iterate.sh 50 100 100 900 "python3 quick_sort.py" quick
```