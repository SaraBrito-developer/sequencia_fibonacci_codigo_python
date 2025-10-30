Projeto: Gerador de Sequência Fibonacci (Python)

Este é um projeto em Python que gera os primeiros números da sequência de Fibonacci, com base na entrada do utilizador.

O objetivo principal do projeto é demonstrar as boas práticas de desenvolvimento:
1.  Refatoração: O código original foi refatorado, separando a lógica de negócio (o cálculo da sequência) da interface do utilizador.
2.  Robustez:O programa agora valida a entrada do utilizador, tratando erros de valores não numéricos e garantindo que o número inserido seja positivo.
3.  Testes Unitários: A lógica de cálculo pura encontrar_sequencia_fibonacci é validada por uma suíte de testes unitários.

---

Estrutura do Projeto

O projeto é dividido em dois ficheiros principais:

1.  fibonacci.py
    Contém a lógica de negócio isolada na função encontrar_sequencia_fibonacci(), que retorna uma lista com os números.
    Contém a função rodar_programa_principal() que lida com a interação do utilizador e o tratamento de erros.

2.  test_fibonacci.py
    Contém a suíte de testes unitários que valida a função encontrar_sequencia_fibonacci() em múltiplos cenários.

---

Como Usar

1. Executar o Programa Principal

Para executar o programa e interagir com ele no terminal:

python fibonacci.py
