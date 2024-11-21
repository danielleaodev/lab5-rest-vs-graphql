# Comparação de Desempenho entre APIs GraphQL e REST

Daniel Leão, Juliana Serra e Letícia Fraga

## Introdução

Este trabalho tem como objetivo comparar o desempenho de APIs GraphQL e REST em termos de tempo de resposta e tamanho das respostas. Com o crescimento do uso de APIs em aplicações modernas, entender as diferenças entre esses dois modelos é essencial para decisões arquiteturais. Para isso, serão realizadas medições do desempenho de ambos os modelos para responder às seguintes perguntas de pesquisa:

-   RQ1: As respostas das consultas GraphQL são mais rápidas que as respostas das consultas REST?
-   RQ2: As respostas das consultas GraphQL têm tamanho menor que as respostas das consultas REST?

### Hipóteses Iniciais

-   Hipótese Nula (H₀): Não há diferença significativa entre o tempo de resposta e o tamanho das respostas das APIs GraphQL e REST.
-   Hipótese Alternativa (H₁): Há uma diferença significativa no tempo de resposta e no tamanho das respostas entre APIs GraphQL e REST.

### Ameaças à Validade

Algumas ameaças à validade foram identificadas.
- Internas:
    - Variabilidade no desempenho do servidor ou da rede que possa impactar os tempos de resposta, o que foi mitigado com um grande número de consultas para cada API (1000) e iteração entre os tipos de consulta
- Externas:
    - Generalização dos resultados para outros ambientes ou APIs distintas. Por isso, os resultados são apresentados dentro do contexto específico do experimento.

## Metodologia

Para este experimento, foram desenvolvidos scripts automatizados para executar endpoints das APIs GraphQL e REST, com o objetivo de realizar consultas e medir o tempo de resposta e o tamanho das respostas das APIs. A variável independente considerada foi o tipo de API (GraphQL ou REST), enquanto as variáveis dependentes foram o tempo de resposta, medido em milissegundos, e o tamanho das respostas, medido em bytes.

O experimento foi realizado por meio de múltiplas medições, totalizando 1000 consultas para cada tipo de API, com o objetivo de obter uma amostra significativa para análise estatística.

### Consultas realizadas

Na API GraphQL, foram realizadas duas versões de cada consulta, para avaliar o impacto da quantidade de dados retornada.

-   Uma consulta básica (GraphQL 1).
-   Uma consulta detalhada (GraphQL 2), que incluía informações adicionais.

Na API REST, a consulta equivalente foi feita usando endpoints de listagem, retornando os campos padrão fornecidos pela API.

Foram definidas consultas que pudessem ser realizadas tanto em GraphQL, quanto em REST, visto que a API REST possui algumas limitações em relação a filtros e ordenação. Foram selecionados os seguintes dados para a coleta:

#### Consulta de Repositórios

-   Repositórios do GitHub de um usuário específico, "torvalds" (Linus Torvalds)
-   Ordenação pelo campo `updated_at`
-   Limite de 30 repositórios por página

#### Consulta de Pull Requests

-   Repositório "linux" do usuário "torvalds"
-   Ordenação pelo campo `updated_at`
-   Limite de 30 pull requests por página

Os dados coletados foram registrados em um arquivo CSV, enquanto as médias de tempo de resposta e tamanho das respostas foram armazenadas separadamente.

## Resultados

Após a execução do experimento, foram obtidos os seguintes resultados médios para o tempo de resposta e o tamanho das respostas das APIs REST e GraphQL. Para a API REST, o tempo médio de resposta foi de 618,49 milissegundos, e o tamanho médio da resposta foi de 602.294 bytes. Em comparação, a consulta GraphQL 1 apresentou, para uma consulta básica, um tempo médio de resposta de 491,53 milissegundos, com um tamanho médio de resposta de 2.121,50 bytes. Por fim, a consulta GraphQL 2, para uma consulta que solicita mais campos na consulta, teve um tempo médio de resposta de 1.196,21 milissegundos, com um tamanho médio de resposta de 24.341 bytes.

| Tipo de Consulta | Tempo Médio de Resposta (ms) | Tamanho Médio da Resposta (bytes) |
| ---------------- | ---------------------------- | --------------------------------- |
| REST             | 618.49                       | 602294.00                         |
| GraphQL 1        | 491.53                       | 2121.50                           |
| GraphQL 2        | 1196.21                      | 24341.00                          |

## Discussão

Os resultados obtidos mostram diferenças claras entre o desempenho das APIs REST e GraphQL no que se refere tanto ao tempo de resposta quanto ao tamanho das respostas.

Em relação ao tempo de resposta, a API GraphQL apresentou desempenho superior à API REST na consulta básica (GraphQL 1), com um tempo médio de resposta de 491,53 ms, enquanto a API REST teve um tempo médio de resposta de 618,49 ms. Esse resultado pode ser atribuído à flexibilidade da GraphQL, que permite retornar apenas os campos específicos solicitados, reduzindo a quantidade de processamento necessário para consultas simples. Entretanto, na consulta mais complexa (GraphQL 2), que solicita um número maior de campos, o tempo médio de resposta aumentou significativamente para 1.196,21 ms. Isso sugere que, embora a GraphQL seja mais eficiente para consultas otimizadas, sua performance pode ser impactada negativamente por consultas complexas que exigem maior processamento no servidor.

Quanto ao tamanho da resposta, a diferença é ainda mais evidente. A API REST retornou respostas muito maiores (602.294 bytes em média) em comparação com a consulta GraphQL 1 (2.121,50 bytes em média). Essa discrepância ocorre porque, na API REST, o endpoint retorna todos os dados disponíveis de forma fixa, independentemente da necessidade do cliente. Já a GraphQL permite maior controle sobre os dados retornados, retornando apenas os campos solicitados, o que resulta em respostas significativamente menores. A consulta GraphQL 2, ao solicitar mais campos, teve um tamanho médio de resposta maior (24.341 bytes), mas ainda assim muito menor do que o da API REST.

Esses resultados indicam que a API GraphQL é superior no que diz respeito à eficiência de consultas básicas, apresentando menor tempo de resposta e tamanho de resposta mais otimizado. No entanto, à medida que a complexidade das consultas aumenta, o tempo de resposta da GraphQL também cresce, tornando-se menos eficiente em comparação com a REST para cenários com grande volume de dados ou campos a serem processados.

Portanto, a escolha entre essas duas tecnologias depende do tipo de aplicação e das necessidades específicas de cada projeto. Para consultas personalizadas e com menor volume de dados, a GraphQL é mais vantajosa. Entretanto, em aplicações onde o tempo de resposta é crítico e a estrutura de dados retornada é fixa e não possui filtros complexos, a API REST pode ser uma escolha mais adequada.