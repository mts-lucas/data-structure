# README

Nesta sessão do  repositório esta os algoritmo tabela de Dikstra referente a atividade avaliativa da terceira unidade da disciplina de estrutura de dados . Neste arquivo README, você encontrará instruções sobre como configurar o ambiente virtual e executar os programas.

## Configurando o Ambiente Virtual

1. Certifique-se de ter o Python instalado em sua máquina, com a versão mais recente, pois os algoritmos nessa sessão usam type hint, que só está disponível em versões mais atualizadas. Você pode fazer o download em https://www.python.org/downloads/.

2. Abra o terminal ou prompt de comando e navegue até o diretório /atividade_u03/fontes.

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

2. Execute o seguinte comando no terminal:

```bash
python dikstra.py 1 25
```