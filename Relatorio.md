# Comparação de Desempenho entre APIs GraphQL e REST

Daniel Leão, Juliana Serra e Letícia Fraga

## Introdução

Este trabalho tem como objetivo comparar o desempenho de APIs GraphQL e REST em termos de tempo de resposta e tamanho das respostas. Com o crescimento do uso de APIs em aplicações modernas, entender as diferenças entre esses dois modelos é essencial para decisões arquiteturais. Para isso, serão realizadas medições do desempenho de ambos os modelos para responder às seguintes perguntas de pesquisa:

- RQ1: As respostas das consultas GraphQL são mais rápidas que as respostas das consultas REST?
- RQ2: As respostas das consultas GraphQL têm tamanho menor que as respostas das consultas REST?

### Hipóteses Iniciais

-   Hipótese Nula (H₀): Não há diferença significativa entre o tempo de resposta e o tamanho das respostas das APIs GraphQL e REST.
-   Hipótese Alternativa (H₁): Há uma diferença significativa no tempo de resposta e no tamanho das respostas entre APIs GraphQL e REST.

## Metodologia

Para conduzir este experimento, foram desenvolvidos scripts automatizados para executar endpoints das APIs GraphQL e REST, com o objetivo de realizar consultas e medir o tempo de resposta e o tamanho das respostas das APIs. A variável independente considerada foi o tipo de API (GraphQL ou REST), enquanto as variáveis dependentes foram o tempo de resposta, medido em milissegundos, e o tamanho das respostas, medido em bytes.

O experimento foi realizado por meio de múltiplas medições, totalizando 50 consultas para cada tipo de API, com o objetivo de obter uma amostra significativa para análise estatística.

Foram definidas consultas que pudessem ser realizadas tanto em GraphQL, quanto em REST, visto que a API REST possui algumas limitações em relação a filtros e ordenação. Foram selecionados os seguintes dados para a coleta:

-   Repositórios do GitHub de um usuário específico, "torvalds" (Linus Torvalds)
-   Coleta configurada para ser ordenada pelo campo `updated_at`
-   Limite de 100 repositórios por página

Além de uma consulta básica em GraphQL, chamada de GraphQl 1, foi implementado um script, chamado de GraphQl 1, que realiza a mesma consulta, porém com um número maior de campos solicitados, o que pode afetar o tempo de resposta. Este script retorna dados adicionais sobre os repositórios, como datas de criação, atualização e push, contagem de forks, estrelas, visibilidade e outras informações.

Os dados coletados foram registrados em um arquivo CSV, enquanto as médias de tempo de resposta e tamanho das respostas foram armazenadas separadamente.

## Resultados

Após a execução do experimento, foram obtidos os seguintes resultados médios para o tempo de resposta e o tamanho das respostas das APIs REST e GraphQL. Para a API REST, o tempo médio de resposta foi de 359,68 milissegundos, e o tamanho médio da resposta foi de 36.311 bytes. Em comparação, a consulta GraphQL 1 apresentou, para uma consulta básica, um tempo médio de resposta de 506,27 milissegundos, com um tamanho médio de resposta de 1.006 bytes. Por fim, a consulta GraphQL 2, para uma consulta que solicita mais campos na consulta, teve um tempo médio de resposta de 1.597,20 milissegundos, com um tamanho médio de resposta de 21.604 bytes.

| Tipo de Consulta | Tempo Médio de Resposta (ms) | Tamanho Médio da Resposta (bytes) |
| ---------------- | ---------------------------- | --------------------------------- |
| REST             | 359.68                       | 36311.00                          |
| GraphQL 1        | 506.27                       | 1006.00                           |
| GraphQL 2        | 1597.20                      | 21604.00                          |

## Discussão e Conclusões Finais

Os resultados obtidos mostram diferenças claras entre o desempenho das APIs REST e GraphQL no que se refere tanto ao tempo de resposta, quanto ao tamanho das respostas.

Em relação ao tempo de resposta, a API REST apresentou um desempenho superior, com um tempo médio de resposta de 359.68 ms, enquanto a consulta API GraphQL 1 teve um tempo médio de resposta de 506.27 ms. Esse resultado pode ser atribuído ao fato de que a API REST, geralmente, possui um modelo de requisição mais direto, em que o servidor retorna a resposta completa para o endpoint solicitado, sem necessidade de processamento adicional de filtros ou operações de agregação, como ocorre na API GraphQL. Embora a GraphQL possa ser mais eficiente em termos de otimização de consultas em cenários complexos, neste caso, a necessidade de processar os dados de maneira mais dinâmica pode ter impactado o tempo de resposta.

Além disso, o maior impacto foi observado na consulta API GraphQL 2, com um número maior de campos em comparação à consulta anterior. O tempo médio de resposta desta API foi significativamente mais alto, atingindo 1.597,20 milissegundos. Esse aumento pode ser explicado pelo fato de que, ao solicitar mais campos de dados (como datas de criação, atualização, contagem de forks, estrelas, entre outros), a complexidade da consulta aumenta, e o servidor precisa processar mais informações para gerar a resposta. Portanto, embora a GraphQL seja flexível e poderosa em termos de personalização da consulta, consultas mais complexas naturalmente acarretam maior tempo de resposta.

Quanto ao tamanho da resposta, a diferença é ainda mais notável: a API REST retornou respostas significativamente maiores (36.311 bytes em média) em comparação com a API GraphQL 1 (1.006 bytes em média). Esse contraste ocorre porque, na API REST, o endpoint retorna todos os dados disponíveis para os repositórios de forma fixa, enquanto na API GraphQL, apenas os campos específicos solicitados (nome, descrição e URL) são retornados, o que resulta em respostas muito menores. A consulta API GraphQL 2 com um número maior de campos resultou em uma resposta significativamente maior, com 21.604 bytes, por retornar mais dados, mas se manteve menor do que a resposta da API REST.

Esses resultados reforçam a ideia de que a API REST tende a ser mais simples e direta, com respostas maiores, enquanto a API GraphQL, embora mais flexível e eficiente no uso de dados, pode exigir mais processamento e, portanto, ter tempos de resposta mais altos. A escolha entre essas duas abordagens depende do tipo de aplicação e das necessidades específicas de desempenho e utilização de dados.

Além disso, é importante observar que a diferença no tamanho das respostas pode ser vantajosa em cenários em que a minimização do tráfego de dados seja uma prioridade. A GraphQL, ao retornar apenas os dados solicitados, oferece uma solução mais eficiente para redes com largura de banda limitada ou para otimização de performance em dispositivos móveis, onde o consumo de dados pode ser uma preocupação.

Por fim, esses resultados indicam que, embora a GraphQL ofereça vantagens em termos de controle sobre os dados retornados, a API REST pode ser uma escolha mais eficiente quando o desempenho, em termos de tempo de resposta, for a prioridade.
