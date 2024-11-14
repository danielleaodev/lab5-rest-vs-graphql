# Lab5_GraphQLxREST
 
Hipótese Nula (H0): Não há diferença significativa entre o tempo de resposta e o tamanho das respostas das APIs GraphQL e REST.

Hipótese Alternativa (H1): Há uma diferença significativa nos tempos de resposta e tamanhos das respostas entre as APIs GraphQL e REST.


Variáveis:
    Dependentes:
        - Tamanho das respostas das APIs
        - Tempo de resposta das APIs
    Independentes:
        - Tipo de API (GraphQL x REST)


Tratamentos: Aplicar diferentes consultas para cada tipo de API, registrando o tempo de resposta e o tamanho das respostas.

Objetos Experimentais:
    - Servidores configurados para rodar endpoints das APIs GraphQL e REST;
    - Scripts para simular as consultas e medir o tempo e o tamanho das respostas;

Tipo de Projeto Experimental: Projeto de comparação controlada

Quantidade de Medições: Realizar múltiplas consultas (ao menos 50 de cada API) para poder analisar variações nos tempos e tamanhos das respostas.

Ameaças à Validade:
    Internas:
        - Variabilidade no desempenho do servidor ou da rede que possa impactar os tempos de resposta;
    Externas:
        - Generalização dos resultados para outros ambientes ou APIs distintas.

## Resultados

No arquivo resultados.csv temos todos os retornos das requisições

E no arquivo médias.md temos a média de tempo e tamanho da resposta, dividos pela API. Informações que são printadas ao fim da execução.