  # XP Educação - Projeto aplicado

  Atende ao módulo final do curso de Pós-Graduação Arquitetura de software. [Veja página oficial do curso](https://www.xpeducacao.com.br/pos-graduacao/arquitetura-de-software)

  ## Descrição 

  Utiliza dados de projetos incentivados na Lei de Incentivo a Cultura. Focado em atender os profissionais captadores de recursos dos projetos. O captador de recursos busca pelo projeto através das características do projeto ou (caso já aprovado em lei) pelo número PRONAC. A fonte de dados primárias são dados públicos em - http://leideincentivoacultura.cultura.gov.br/ferramentas/

  ## Dados públicos

  Os dados abaixo são extraídos do SALIC - Sistema de Apoio às Leis de Incentivo à Cultura, o sistema é utilizado para apoiar todo o processo de incentivo, desde a submissão de propostas culturais até sua avaliação pela Comissão Nacional de Incentivo à Cultura.

  Os dados estão disponíveis em nossa API de dados abertos, que contemplam essas entidades:
  - Projetos Culturais
  - Propostas (de projetos culturais)
  - Proponentes
  - Incentivadores
  - Fornecedores

  **Fonte:**</br>
  [Projetos do Programa Nacional de Apoio à Cultura - Lei Rouanet - SALIC](http://dados.cultura.gov.br/dataset/incentivos-da-lei-rouanet)

   ## Entidades - descrição de negócio

   Apresenta a descrição de negócio para cada entidade envolvida com projetos incentivados na Lei de incentivo à cultura.

   <details>
   <summary>Projetos Culturais</summary>
   Um projeto cultural é um documento que deve reunir todo o planejamento de um evento ou de uma série de apresentações artística, como mostras de quadros, shows musicais, peças de teatro etc.
   Descreve fontes de captação de recursos, remuneração do captador e relevância do projeto para a comunidade local.
   </br>
   <b>Fontes:</b></br>
   <a href="https://consultoriasquadra.com.br/lei-rouanet/como-fazer-um-projeto-cultural/#:~:text=Um%20projeto%20cultural%20%C3%A9%20um,musicais%2C%20pe%C3%A7as%20de%20teatro%20etc.">Squadra Consultoria</a></br>   
   </details>

   <details>
   <summary>Propostas (de projetos culturais)</summary>
   Apresentada pelo proponente (aquele que propõe o projeto), é submetida de forma eletrônica no Sistema de Apoio às Leis de Incentivo à Cultura (Salic).
   Avaliada por critérios objetivos estabelecidos pela <a href="https://www.planalto.gov.br/ccivil_03/leis/l8313cons.htm">Lei 8.313/91</a>.
   </br>
   <b>Fontes:</b></br>
   <a href="https://consultoriasquadra.com.br/lei-rouanet/quais-as-etapas-de-um-projeto-na-lei-de-incentivo-a-cultura/">Squadra Consultoria</a></br>
   <a href="https://www.planalto.gov.br/ccivil_03/leis/l8313cons.htm">Site oficial do Planalto</a>
   </details>
   
   <details>
   <summary>Proponente</summary>
   É a pessoa física ou jurídica responsável pela gestão do projeto – apresentação, execução e prestação de contas.</br>
   Definição no Dicionário - Que ou aquele que propõe algo.
   </br>
   <b>Fontes:</b></br>
   <a href="https://www.proac.sp.gov.br/faq_icms/o-que-e-o-proponente/#:~:text=%C3%89%20a%20pessoa%20f%C3%ADsica%20ou,execu%C3%A7%C3%A3o%20e%20presta%C3%A7%C3%A3o%20de%20contas.">PROAC - site oficial</a><br>
   <a href="https://michaelis.uol.com.br/moderno-portugues/busca/portugues-brasileiro/proponente/">Dicionário Michaellis</a>
   </details>

  <details>
  <summary>Incentivadores</summary>
  Quem fornece os recursos é chamado de incentivador e, com a Lei Rouanet, tem parte ou o total do valor do apoio deduzido no Imposto de Renda devido.
  </br>
  Há duas formas de financiar um projeto: por meio de doação ou de patrocínio. A doação é um repasse sem retorno de imagem para o incentivador. É um apoio que resulta apenas da decisão de aplicar parcela do imposto de renda devido em um projeto cultural para o qual a pessoa ou empresa queira contribuir. O patrocínio é um repasse com retorno de imagem. Além de viabilizar a realização de um projeto, o patrocinador se beneficia de estratégias de comunicação, assinando o patrocínio com sua marca e inserindo sua imagem associada ao projeto selecionado, conforme Artigo 23, da Lei 8.313/91. A doação ou patrocínio não pode ser feita a projeto de pessoa ou instituição vinculada ao apoiador, de acordo com o Artigo 27 da Lei 8.313/91.
  </br>
  <b>Fontes:</b></br>
  <a href="https://consultoriasquadra.com.br/como-elaborar-projetos-para-lei-rouanet/#:~:text=Quem%20fornece%20os%20recursos%20%C3%A9,meio%20de%20doa%C3%A7%C3%A3o%20ou%20patroc%C3%ADnio.">Squadra Consultoria</a></br>
  <a href="http://leideincentivoacultura.cultura.gov.br/como-funciona/">Lei de incentivo a cultura - site oficial</a></br>
  </details>

  <details>
  <summary>Fornecedores</summary>
  Presentes na fase de execução do projeto, quando o proponente entra em contato com fornecedores, artistas e outros prestadores de serviço que irão executar a proposta. Também envolve a realização em si do espetáculo, show, festival, montagem e visitação de exposições, impressão de livros, etc.
  </br>
  <b>Fontes:</b></br>
  <a href="http://leideincentivoacultura.cultura.gov.br/como-funciona/">Lei de incentivo a cultura - site oficial</a>
  </details>

  ## Entidades - descrição de dados

  Apresenta a descrição do modelo de dados das entidades envolvidas com projetos incentivados na Lei de incentivo à cultura.

  [Documentação da API - fonte primária de dados](http://dados.cultura.gov.br/dataset/incentivos-da-lei-rouanet/resource/2bff8a52-14d5-48db-a970-ce30d0fb851d)