[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/fSKWLlat)
# Atividade Unidade I

# Cadastro Geral de Aparelhos Celulares do Mercosul para Rastreamento Antifurto

## Objetivo: 
* Reforçar a importância do estudo da análise de sua complexidade na avaliação de algoritmos;
* Analisar os requisitos de um problema real, propondo uma solução computacional;
* Construir um protótipo de teste baseado na solução proposta;
* Entender os processos de manipulação de arquivos em *Python*.


## Contexto e Motivação

Todo o celular possui um número identificador chamado ***IMEI - International Mobile Equipment Identity***, que consiste em uma sequência de 15 dígitos, geralmente organizado no formato ***WW-XXXXXX-YYYYYY-Z***, como mostra a Figura 1, onde: 

- WW: descreve o identificador do órgão de registro, mostrando o Código de Alocação de Tipo (TAC) pelo grupo de aprovação GSMA 
- XXXXXX: representa os dígitos reais do TAC 
- YYYYYY: age como um identificador para o dispositivo específico 
- Z: é o dígito de verificação. Em dispositivos GSM, este é 0 

O **IMEI** é garantidamente único em todo o mundo, o que significa que dispositivos com dois *SIM Cards* têm dois números **IMEI** devido aos dois *slots* individuais para *SIM Cards*.

O IMEI não desempenha apenas um papel central quando o seu dispositivo for roubado. O fabricante do dispositivo ou o provedor de conectividade pode precisar da combinação de números em caso de reclamação ou para análise de erros em consultas de suporte.

Existem várias opções para determinar o IMEI do seu dispositivo. Na maioria dos casos, o número está impresso na embalagem do dispositivo. Se o seu dispositivo tiver uma bateria removível, vale a pena procurar sob a tampa da bateria. Os fabricantes frequentemente colocam um adesivo com as informações relevantes aqui. Com a ajuda do código especial *#06#, o número IMEI também pode ser consultado pelo teclado do dispositivo, quando disponível. 

Se for roubado ou perdido, você precisa dessa combinação de números para denunciá-lo à polícia, por exemplo. Com a ajuda do **IMEI**, o dispositivo também pode ser completamente bloqueado pelo operador de rede. Por esse motivo, você nunca deve divulgar o IMEI de seus dispositivos celulares a terceiros.

O Brasil possui um projeto muito interessante, criado pela Anatel, com a participação das operadoras móveis, fabricantes e fornecedores de equipamentos, chamado *Celular Legal*. Este projeto tem por objetivo fortalecer o combate a equipamentos adulterados, roubados e extraviados e inibir o uso de aparelhos não certificados pela Anatel. 

Além do bloqueio, há uma crescente pressão social para que as autoridades consigam rastrear celulares furtados por meio da associação do aparelho ao seu proprietário original. Para isso, a existência de um cadastro armazenando não apenas o **IMEI**, mas também informações sobre o dono (CPF) e o local de registro (CEP) permitiria que, em caso de furto, um aparelho fosse identificado e vinculado ao seu legítimo proprietário mesmo após múltiplas trocas de chip.

### O Desafio

Os países do Mercosul decidiram criar um **Cadastro Geral de Aparelhos Celulares** unificado. O objetivo principal é combater o roubo e a clonagem de dispositivos, permitindo que um celular bloqueado em um país seja automaticamente bloqueado em todos os demais países.

Cada país participante forneceu uma base de dados com milhões de registros de aparelhos homologados. Cada registro originalmente continha: **IMEI (15 dígitos)**, **fabricante**, **modelo**, **ano de fabricação**, **ID do proprietário** (no caso brasileiro, o CPF com 11 dígitos) e **CEP de registro** (8 dígitos).

No cadastro unificado haverá a necessidade de se manter todos os registros ordenados por **IMEI**. Estima-se que o volume de dados ultrapasse os **50 milhões de registros**!  Portanto, o tempo de processamento e o custo de armazenamento serão fatores importantes para o sistema. 

Os tomadores de decisão responsáveis pelo projeto foram avisados de que o processo de ordenação da base de dados é crucial para o sucesso do projeto. E que, no caso de chaves de tamanho fixo, como o **IMEI**, é possível utilizar algoritmos mais eficientes que consideram essa característica [1][2]. Por isso, não serão aceitas soluções que envolvam algoritmos das classes O(n²) ou O(n log n).

Outro problema que a base de dados integrada pode apresentar é a existência de **registros duplicados** (o mesmo **IMEI** pode ter sido enviado por mais de um país, especialmente em regiões de fronteira, com informações de proprietário conflitantes). Esses casos precisam ser identificados e removidos da base de dados, também em tempo linear. 

Você quer se candidatar a desenvolvedor para esse projeto, e para participar do processo seletivo voce deverá projetar o processo de integração das bases de dados. Para tanto, deverá submeter um protótipo para avaliação da sua solução, capaz de comprovar que seu algoritmo é capaz de processar diferentes bases de dados, ordenar seus registros e remover registros duplicados. 

Além disso, sua proposta deve conter um relatório técnico[^1] simples, no qual você demonstrará sua capacidade de comunicação, deixando claros os critérios de escolha do algoritmo de ordenação, o quanto ele é aderente aos requisitos do problema e sua complexidade teórica [^2].

## Requisitos Técnicos e Restrições

- O protótipo deve ser escrito em *Python*, sem dependências externas [^3].
- Seu código será avaliado quanto ao processo de desenvolvimento e ao conhecimento de boas práticas de programação e de documentação [3]. Portanto, o código deve ser modular, bem documentado e, sempre que possível, implementar o conceito de **Tipo Abstrato de Dados (TAD)**, por meio do uso de **Classes** e **Objetos**.
- O processo de seleção quer identificar sua capacidade de projetar e desenvolver estruturas de dados e algoritmos, portanto, não será permitido o uso de estruturas de dados nativas da linguagem *Python* [^4]. 

- As bases de dados serão simuladas no protótipo por arquivos em formato de texto, nomeados pelo país, que contêm as informações dos registros.
- A saída será a base de dados integrada, também em formato de arquivo de texto.
- Seu protótipo deve calcular estatísticas que informem o número de registros lidos em cada arquivo de entrada e o número total de registros processados nas etapas de ordenação e remoção de duplicidade. Os resultados esperados dos algoritmos e o número efetivo de comparações devem ser calculados e apresentados ao final do processo. 

- Os produtos (protótipo e relatório[^1]) devem ser disponibilizados em repositório indicado no *github Classroom*. 
- O prazo de entrega da atividade será o dia 20/04 (2ª feira). Entregas fora do prazo sofrerão uma penalidade de 1,0 ponto por dia de atraso. 
- Como etapa final do processo de avaliação, você será entrevistado para fornecer mais detalhes sobre a solução apresentada e esclarecer quaisquer dúvidas sobre o seu desenvolvimento. 
- Para facilitar o processo de testes, alguns arquivos com conjuntos de registros serão disponibilizados, com volumes de dados distintos. 

## A Avaliação:

Seu protótipo será avaliado pelos seguintes critérios:

| Critério | Pontuação |
| :--- | :---: |
| 1. Relatório Técnico em Markdown[4] (README) e Documentação | 1,0 |
| 2. Modularização do código | 1,0 | 
| 3. Uso de TAD | 1,0 |
| 4. Leitura e gravação dos arquivos | 1,0  |
| 5. Escolha/justificativa/análise da complexidade do algoritmo | 1,0 |
| 6. Implementação correta do algoritmo de ordenação | 5,0 |

A pontuação de cada item pode ser alterada com base nas respostas na etapa de entrevista. 

## Observações Gerais:

> Plágio não é uma prática aceitável, nem na academia nem no mercado de trabalho. Uma vez detectada, **TODOS** os envolvidos serão penalizados com zero na avaliação. 

> Não presuma nada! Pergunte ao professor ou aos monitores. 

> **Não compartilhe seu código nos canais do *Discord***
> Discussões conceituais podem ser feitas por lá, mas dúvidas específicas relacionadas a sua solução ou ao seu código devem ser encaminhadas de forma privada no *Discord* ou como *issues* no *github Classroom*.

# Referências Bibliográficas:

[1]     Cormen,T.H., Leiserson,C.E., Rivest,R.L., Stein,C. **Algoritmos – Teoria e Prática**. Editora Campus. 3ª edição, 2012.

[2]     Canning, J., Broder, A., Lafore, R. **Data Structures & Algorithms in Python**. Addison-Wesley. 2022.

[3]     Erica Vartanian, **"6 coding best practices for beginner programmers"**. Disponível em:  https://www.educative.io/blog/coding-best-practices

[4]     Matt Cone, **Markdown Cheat Sheet - A quick reference to the Markdown syntax**. Disponível em: https://www.markdownguide.org/cheat-sheet/

[^1]: Renomeio o README original do seu repositório, e crie um novo arquivo README com o seu relatório em *Markdown* [4] 
[^2]: Não há necessidade de provas formais, mas você deve indicar as referências bibliográficas consultadas que respaldem seus argumentos.
[^3]: Considere dependências externas de pacotes que precisariam ser instaladas no ambiente *Python* via *pip*, por exemplo. 
[^4]: Você deve criar seu TAD, definindo atributos e construindo os métodos necessários à sua manipulação, tal como no exemplo do vetor analisado nas aulas.  
