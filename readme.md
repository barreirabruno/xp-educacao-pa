  # XP Educação - Projeto aplicado

  Atende ao módulo final do curso de Pós-Graduação Arquitetura de software. [Veja página oficial do curso](https://www.xpeducacao.com.br/pos-graduacao/arquitetura-de-software)

  # Índice
  1. [Descrição](#Descrição)
  2. [Dados públicos](#Dados-públicos)
  3. [Entidades - descrição de negócio](#Entidades---descrição-de-negócio)
  4. [Endpoints - SALIC API](#Endpoints---SALIC-API)
  5. [Modelo de dados únicos](#Modelo-de-dados-únicos)

  ## Descrição 

  Utiliza dados de projetos incentivados na Lei de Incentivo a Cultura. Focado em atender os profissionais captadores de recursos dos projetos. O captador de recursos busca por incentivadores (ou patrocinadores) através das características do projeto ou (caso já aprovado em lei) pelo número PRONAC. A fonte de dados primárias são dados públicos em - http://leideincentivoacultura.cultura.gov.br/ferramentas/

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

  ## Endpoints - SALIC API

  Documenta a saída de endpoints da Salic API. Os endpoints documentados são relevantes para alimentar o sistema e gerar recomendação.

  **Base_url:** http://api.salic.cultura.gov.br/v1

  **Autenticação e Autorização:** A Salic API não possui nenhum tipo de Autenticação ou Autorização necessária para consumo.
  
  **Swagger:** [Acesse o swagger oficial - SALIC API](http://dados.cultura.gov.br/dataset/incentivos-da-lei-rouanet/resource/2bff8a52-14d5-48db-a970-ce30d0fb851d)

  ### Projetos - Dados relativos a Projetos

  **Endpoint:** /projetos/</br>
  **Descrição:** Busca projetos dado uma combinação de valores diversos de pesquisa</br>
  **Tipo:** GET</br>
  **Curl:**
  ```
  curl -X GET "http://api.salic.cultura.gov.br/v1/projetos/?limit=5&offset=1&area=1&UF=AM&format=json" -H  "accept: application/json"
  ```
  **Model:**
  |Propriedade   | Tipo   | Descrição  |
  |---|---|---|
  | PRONAC  | string ($int64) | Número do projeto no Programa Nacional de Apoio à Cultura  |
  | ano_projeto  | string  | Ano no qual o projeto foi apresentado  |
  | nome  | string  | Nome do projeto  |
  | cgccpf  | string ($int64)  | CNPJ ou CPF do proponente do projeto  |
  | proponente  | string  | Quem propõe o projeto  |
  | segmento  | string  | Código do Segmento do projeto |
  | area  | string  | Código da Área do projeto  |
  | UF  | string  | Estado de origem do projeto |
  | municipio  | string  | Munícipio do projeto  |
  | data_inicio  | string ($date)  | Data de início no formato AAAA-MM-DD  |
  | data_termino  | string ($date)  | Data de finalização no formato AAAA-MM-DD  |
  | situacao  | string  | Apresentou prestação de contas ou Autorizada a captação total dos recursos ou Projeto em execução - Encerrado prazo de captação ou Autorizada a captação total dos recursos ou Diligenciado - Readequação  |
  | mecanismo  | string  |  |
  | enquadramento  | string  | Artigo no qual o projeto se enquadra, por exemplo, Artigo 18  |
  | valor_projeto  | number ($double)  | [VALIDAR_COM_CAPTADORA_SIGNIFICADO_DO_CAMPO]  |
  | outras_fontes  | number ($double)  | [VALIDAR_COM_CAPTADORA_SIGNIFICADO_DO_CAMPO]  |
  | valor_captado  | number ($double)  | [VALIDAR_COM_CAPTADORA_SIGNIFICADO_DO_CAMPO]  |
  | valor_proposta  | number ($double)  | [VALIDAR_COM_CAPTADORA_SIGNIFICADO_DO_CAMPO]  |
  | valor_solicitado  | number ($double)  | [VALIDAR_COM_CAPTADORA_SIGNIFICADO_DO_CAMPO]  |
  | valor_aprovado  | number ($double)  |  [VALIDAR_COM_CAPTADORA_SIGNIFICADO_DO_CAMPO]  |
  | acessibilidade  | string  | Destaca quais medidas de acessibilidade serão adotadas no projeto  |
  | objetivos  | string  |  Descreve objetivos gerais e específicos do projeto |
  | justificativa  | string  | Justificativa para a realização do projeto  |
  | etapa  | string  | Descreve a etapa atual do projeto  |
  | ficha_tecnica  | string  | Lista os profissionais envolvidos na realização do projeto  |
  | impacto_ambiental  | string  | Descreve qual o impacto ambiental o projeto atual causa   |
  | especificacao_tecnica  | string  | Descreve a parte técnica do projeto  |
  | estrategia_execucao  | string  | Descreve o meios pelo qual o projeto é realizado  |
  | providencia  | string  | [VALIDAR_COM_CAPTADORA_SIGNIFICADO_DO_CAMPO]  |
  | democratizacao  | string  | Descreve a maneira como o projeto é democratizado para a sociedade  |
  | sinopse  | string  | Sintetiza, abrevia o que é o projeto em um texto  |
  | resumo  | string  |  Abreviação do projeto |  
  
  **Resposta:**
  ```
  {
    "count": 5,
    "_embedded": {
      "projetos": [
        {
          "etapa": "PRÉ-PRODUÇÃO – 3 meses - Contato com os municípios para firmar as parcerias; - Reuniões com equipes pedagógica, administrativa e artística; - Planejamento das aulas e organização de cronograma de f",
          "providencia": "PROJETO DILIGENCIADO DURANTE A ANÁLISE DA SOLICITAÇÃO DE READEQUAÇÃO.",
          "area": "Artes Cênicas",
          "enquadramento": "Artigo 18",
          "objetivos": "Objetivo Geral: Ampliar a capacidade de alcance do Liceu de Artes e Ofícios Claudio Santoro por meio do LICEU DIGITAL, para oferecer gratuitamente atividades artísticas formativas. Objetivos Específ",
          "ficha_tecnica": "EDVAL MACHADO JÚNIOR – Direção Geral Presidente da Agência Amazonense de Desenvolvimento Cultural - AADC, graduado em Comunicação Social e Direito, atuando há mais de 15 anos, tem experiência na área",
          "situacao": "Diligenciado - Readequação",
          "outras_fontes": 0,
          "acessibilidade": "Considerando o Art. 18 da IN 02/2019, destacamos abaixo as medidas que serão tomadas para garantir o acesso das pessoas com Deficiência às Atividades Artísticas Formativas:   Pela transmissão ser on",
          "sinopse": "O LICEU DIGITAL oferecerá cursos formativos em artes nas áreas de dança, teatro, música/canto para os municípios Silves, Anori, Caapiranga, Manaus, Benjamin Constant, Tefé, Boca do Acre, Coari, Codajás e Alvarães. Cada curso será oferecido por módulo de 03 meses e terá duração de 30 horas, com frequência mínima de 75%. A programação dos cursos está dividida em dois módulos de um trimestre cada, como segue:   Módulo I (3 meses de duração cada curso) Dança: Percepção Corporal Iniciação Teatral I (Módulo I) Iniciação ao Canto I (Módulo I)   Módulo II (3 meses de duração cada curso) Dança Contemporânea I Iniciação Teatral I (Módulo II) Iniciação ao Canto I (Módulo II)   Após a divulgação dos cursos nos municípios, realizaremos as inscrições. Posteriormente às inscrições, serão criados grupos no WhatsApp para cada turma/curso com os alunos matriculados, o instrutor e o monitor/tutor. Será aberta uma sala de aula virtual no Google Classroom, para cada turma/curso, onde os conteúdos, materiais, bibliografias estarão disponibilizadas aos alunos. As aulas serão ministradas via Google Meet, sendo o link disponibilizado no grupo de whatsapp de cada turma.   O instrutor do curso utilizará o Google Meet para aula expositiva, com utilização de slides, vídeos (produzidos para as aulas) e um bate papo com os participantes, assim como perguntas feitas pelo chat e/ou por áudio quando necessário.   Dentro de cada sala virtual, haverá um monitor/tutor a fim de registrar a aula e dar apoio a quaisquer ocorrências. Todas as atividades estarão dispostas no Google Classroom, acompanhadas pelo Google Agenda.   Após o encerramento de cada curso serão enviadas avaliações das atividades via Google Formulário, para avaliação dos alunos. Também será enviada uma avaliação para que os alunos possam avaliar os cursos oferecidos e, assim, auxiliar no planejamento de novos cursos.   Ao final será realizado um relatório com os resultados mensurados do projeto.   Como CONTRAPARTIDA SOCIAL, será realizada palestra para os municípios participantes, com a temática “Os cursos de formação artística do Liceu e perspectivas de futuro”.   MÓDULO I Dança: Percepção Corporal (Módulo I) – (Faixa etária a partir de 13 anos) O curso propõe atividades práticas e teóricas para construção de imagem corporal e estímulo à percepção do corpo e sua relação com o meio, visando o desenvolvimento de habilidades e aspectos inerentes ao movimento dançado. Teatro: Iniciação Teatral I (Faixa etária a partir de 13 anos) O curso de Iniciação Teatral propõe estimular a criatividade para a expressão de ideias por meio do teatro. Busca utilizar-se de jogos teatrais para construir caminhos prazerosos na relação ensino e aprendizagem. Música: iniciação ao Canto I (Faixa etária a partir de 13 anos) O Curso visa estimular e aprimorar o uso da voz cantada com técnicas vocais desenvolvidas para a realidade do estudante, propõe estudo de repertórios, técnica vocal, teoria musical e solfejo para prática musical de apresentações e concertos.   MÓDULO II Dança: Dança Contemporânea I (Faixa etária a partir de 13 anos) O curso propõe o estudo dos elementos que fazem parte do processo de desenvolvimento da dança (tempo, espaço, peso, fluência), a partir de métodos, experimentos e processos de pesquisa e improvisação. Propõe o estudo do corpo/físico, corpo/movimento, corpo/interativo, corpo/espaço. Teatro: Iniciação Teatral I (Módulo II) (Faixa etária a partir de 13 anos) Visa apresentar formas de criação cênica aos alunos que já cursaram o Módulo I, levando em consideração os estudos praticados, através de atividades relacionadas à história e preparação de elementos cênicos, como iluminação, cenografia, sonoplastia, figurino e dramaturgia, pensando no desenvolvimento prático e técnico, desenvolvendo o fazer teatral, criativo e artístico. Música: Iniciação ao Canto I (Módulo II) (Faixa etária a partir de 13 anos) O curso propõe um aprofundamento das questões levantadas no módulo anterior, aprimorando o uso da voz cantada com técnicas vocais desenvolvidas para a realidade do estudante, propõe estudo de repertórios, técnica vocal, teoria musical e solfejo para prática musical de apresentações e concertos.   CONTRAPARTIDAS Palestra “Os cursos de formação artística do Liceu e perspectivas de futuro” – a palestra poderá contribuir com uma reflexão sobre os cursos oferecidos pelo LICEU DIGITAL e os impactos desta formação na vida dos envolvidos e dos municípios participantes.",
          "nome": "LICEU DE ARTES E OFÍCIOS CLÁUDIO SANTORO - LICEU DIGITAL ",
          "cgccpf": "13659617000165",
          "mecanismo": "Mecenato",
          "_links": {
            "fornecedores": "http://api.salic.cultura.gov.br/v1/fornecedores/?PRONAC=212616",
            "self": "http://api.salic.cultura.gov.br/v1/projetos/212616",
            "incentivadores": "http://api.salic.cultura.gov.br/v1/incentivadores/?PRONAC=212616",
            "proponente": "http://api.salic.cultura.gov.br/v1/proponentes/68f003ce5b41c0b00565897f01dc98c362fe6ffd2b89a03e70f43d175e69"
          },
          "segmento": "Ações de capacitação e treinamento de pessoal",
          "PRONAC": "212616",
          "estrategia_execucao": "Devido a transmissão dos cursos serem pelo Google Meet, os alunos matriculados poderão acompanhar de suas próprias residências, desde que tenham internet. Entretanto, as prefeituras dos municípios dis",
          "valor_aprovado": 559309.52,
          "justificativa": "O Estado do Amazonas é uma região bastante peculiar comparada ao restante do país. O acesso aos seus municípios é, na sua maioria, por rios, o que contribui para prolongar as distâncias, visto que as",
          "resumo": "O projeto consiste na expansão das atividades artísticas formativas do LICEU DE ARTES E OFÍCIOS CLAUDIO SANTORO, localizado em Manaus/Amazonas, por meio da ampliação do seu LICEU DIGITAL. A possibilidade de ampliaçãodo LICEU DIGITALirábeneficiar, nesta etapa, outros municípios do Amazonas,por meio de tecnologias adequadas para aulas remotas, na perspectiva de proporcionar gratuitamente atividades artísticas formativas em Dança, Teatro e Música/Canto, para crianças e jovens destas localidades. Como CONTRAPARTIDA SOCIAL o projeto realizará uma palestra, por meio remoto, para as cidades participantes do projeto, com a temática “Os cursos de formação artística do Liceu e perspectivas de futuro”.",
          "valor_solicitado": 559309.52,
          "especificacao_tecnica": "Projeto pedagógico completo Com base nas possibilidades de atuação nos municípios, os cursos oferecidos nas áreas de Dança, Teatro e Música/Canto, são do nível Básico e visam o estimulo do fazer artí",
          "municipio": "Manaus",
          "data_termino": "2023-02-13",
          "UF": "AM",
          "impacto_ambiental": "",
          "democratizacao": "Todos os cursos e atividades do projeto são gratuitos. Serão oferecidas 900 vagas nos Cursos em dança, teatro, música/canto.   De acordo com o Art. 21 da IN n° 2/2019, serão adotadas as seguintes m",
          "valor_projeto": 559309.52,
          "proponente": "AGÊNCIA AMAZONENSE DE DESENVOLVIMENTO CULTURAL - AADC",
          "ano_projeto": "21",
          "data_inicio": "2022-02-14",
          "valor_captado": 0,
          "valor_proposta": 559309.52
        },
        ...
      ]
    },
    "total": 86,
    "_links": {
      "self": "http://api.salic.cultura.gov.br/v1/projetos/?limit=5&offset=1&area=1&UF=AM&format=json&",
      "first": "http://api.salic.cultura.gov.br/v1/projetos/?limit=5&offset=0&area=1&UF=AM&format=json&",
      "last": "http://api.salic.cultura.gov.br/v1/projetos/?limit=5&offset=85&area=1&UF=AM&format=json&",
      "next": "http://api.salic.cultura.gov.br/v1/projetos/?limit=5&offset=6&area=1&UF=AM&format=json&"
    }
  }
  ```

  </br>
  </br>

  **Endpoint:** /incentivadores/</br>
  **Descrição:** Busca incentivadores dado uma combinação de valores diversos de pesquisa</br>
  **Tipo:** GET</br>
  **Curl:**
  ```
  curl -X GET "http://api.salic.cultura.gov.br/v1/incentivadores/?limit=10&nome=Ita%C3%BA&tipo_pessoa=juridica&format=json" -H  "accept: application/json"
  ```
  **Model:**
  |Propriedade   | Tipo   | Descrição  |
  |---|---|---|
  | nome | string | Nome do incentivador |
  | responsavel | string | Nome do responsável vínculado a esse incentivador, pode estar vazio |
  | cgccpf | string ($int64) | Cgc/Cpf do incentivador |
  | tipo_pessoa | string | Física ou Jurídica |
  | UF | string | Estado do incentivador no formato EE |
  | municipio | string | Cidade do incentivador |
  | total_doado | number ($double) | Valor total doado por esse incentivador em N projetos [VALIDAR_COM_CAPTADORA_SIGNIFICADO_DO_CAMPO] |

  **Resposta:**
  ```
  {
    "count": 10,
    "_embedded": {
      "incentivadores": [
        {
          "nome": "ITAÚ Administradora de Consórcios Ltda,",
          "cgccpf": "00000776000101",
          "total_doado": 7168000,
          "_links": {
            "doacoes": "http://api.salic.cultura.gov.br/v1/incentivadores/6050fc669e500bf0292b246ec5a162cd46da2e6436e72f72591dab460410/doacoes/",
            "self": "http://api.salic.cultura.gov.br/v1/incentivadores/6050fc669e500bf0292b246ec5a162cd46da2e6436e72f72591dab460410"
          },
          "tipo_pessoa": "juridica",
          "responsavel": "",
          "UF": "SP",
          "municipio": "Poa"
        },
        ...
      ]
    },
    "total": 56,
    "_links": {
      "self": "http://api.salic.cultura.gov.br/v1/incentivadores/?limit=10&offset=0&nome=Itaú&tipo_pessoa=juridica&format=json&",
      "first": "http://api.salic.cultura.gov.br/v1/incentivadores/?limit=10&offset=0&nome=Itaú&tipo_pessoa=juridica&format=json&",
      "last": "http://api.salic.cultura.gov.br/v1/incentivadores/?limit=10&offset=50&nome=Itaú&tipo_pessoa=juridica&format=json&",
      "next": "http://api.salic.cultura.gov.br/v1/incentivadores/?limit=10&offset=10&nome=Itaú&tipo_pessoa=juridica&format=json&"
    }
  }
  ```
  
  </br>
  </br>

  **Endpoint:** /incentivadores/{incentivador_id}/doacoes</br>
  **Descrição:** Dado o id de um incentivador, retorna informações relativas a todas as doações por ele feitas</br>
  **Tipo:** GET</br>
  **Curl:**
  ```
  curl -X GET "http://api.salic.cultura.gov.br/v1/incentivadores/6050fc669e500bf0292b246ec5a162cd46da2e6436e72f72591dab460410/doacoes?limit=10&format=json" -H  "accept: application/json"
  ```
  **Model:**
  |Propriedade   | Tipo   | Descrição  |
  |---|---|---|
  | PRONAC | string ($int64) | Número do projeto no Programa Nacional de Apoio à Cultura |
  | valor | number ($double) | Valor doado para este projeto específico |
  | data_recibo | string ($date) | Data do recibo do aporte [VALIDAR_COM_CAPTADORA_SIGNIFICADO_DO_CAMPO] |
  | nome_projeto | string | Nome do projeto que recebeu o aporte |
  | cgccpf | 	string ($int64) | CNPJ ou CPF do incentivador |
  | nome_doador | string | Nome do incentivador |

  **Resposta:**
  ```
  {
    "count": 10,
    "_embedded": {
      "doacoes": [
        {
          "data_recibo": "2017-05-09",
          "cgccpf": "00000776000101",
          "nome_doador": "ITAÚ Administradora de Consórcios Ltda,",
          "nome_projeto": "Plano Anual de Atividades - MAM/SP 2017",
          "_links": {
            "projeto": "http://api.salic.cultura.gov.br/v1/projetos/163547 ",
            "incentivador": "http://api.salic.cultura.gov.br/v1/incentivadores/1b5552fe5eb3e4de7cfcd0bcc1bf81b1891aeca32fabf44eaf802181b66a"
          },
          "valor": 500000,
          "PRONAC": "163547 "
        }
      ]
    },
    "total": 31,
    "_links": {
      "self": "http://api.salic.cultura.gov.br/v1/incentivadores/6050fc669e500bf0292b246ec5a162cd46da2e6436e72f72591dab460410/doacoes/?limit=10&offset=0&format=json&",
      "first": "http://api.salic.cultura.gov.br/v1/incentivadores/6050fc669e500bf0292b246ec5a162cd46da2e6436e72f72591dab460410/doacoes/?limit=10&offset=0&format=json&",
      "last": "http://api.salic.cultura.gov.br/v1/incentivadores/6050fc669e500bf0292b246ec5a162cd46da2e6436e72f72591dab460410/doacoes/?limit=10&offset=30&format=json&",
      "next": "http://api.salic.cultura.gov.br/v1/incentivadores/6050fc669e500bf0292b246ec5a162cd46da2e6436e72f72591dab460410/doacoes/?limit=10&offset=10&format=json&"
    }
  }
  ```

  ## Modelo de dados únicos

  Descreve um modelo de dados único que é armazenado na base de dados do sistema.</br>

  ### Objetivo
  Garantir que o sistema retorne dados sobre projetos e incentivadores mesmo que a Salic API esteja intermitênte.
  Garantir que análises secundárias ocorram sem depender da Salic API.

  ### Modelo único

  ### Projeto

  |Propriedade   | Tipo   | Descrição  |
  |---|---|---|
  | nome  | string | Nome do projeto  |
  | area |  string | Código da Área do projeto  |
  | data_inicio | string ($date)  | Data de início no formato AAAA-MM-DD  |
  | data_termino | string ($date)  | Data de finalização no formato AAAA-MM-DD  |
  | UF | string  | Estado de origem do projeto  |
  | valor_projeto | number ($double)  | [VALIDAR_COM_CAPTADORA_SIGNIFICADO_DO_CAMPO]  |
  | outras_fontes | number ($double)  | [VALIDAR_COM_CAPTADORA_SIGNIFICADO_DO_CAMPO]  |
  | valor_captado | number ($double)  | [VALIDAR_COM_CAPTADORA_SIGNIFICADO_DO_CAMPO]  |
  | valor_proposta | number ($double)  | [VALIDAR_COM_CAPTADORA_SIGNIFICADO_DO_CAMPO]  |
  | valor_solicitado | number ($double)  | [VALIDAR_COM_CAPTADORA_SIGNIFICADO_DO_CAMPO]  |
  | valor_aprovado | number ($double)  | [VALIDAR_COM_CAPTADORA_SIGNIFICADO_DO_CAMPO]  |
  | metadata | string  | Resposta na integra vinda da requisição da SALIC Api |

  ### Dúvida | Enviar para o Professor orientador | APAGAR APÓS RESPOSTA
  Possível recomendar um incentivador para um projeto pelas propriedades de valor de aporte do modelo único?
  Propriedades relacionadas com valor de aporte no modelo único de projeto:
  - valor_projeto
  - outras_fontes
  - valor_captado
  - valor_proposta
  - valor_solicitado
  - valor_aprovado

  ### Incentivador

  |Propriedade   | Tipo   | Descrição  |
  |---|---|---|
  | nome  | string | Nome do incentivador  |
  | total_doado |  string | Valor total doado por esse incentivador em N projetos [VALIDAR_COM_CAPTADORA_SIGNIFICADO_DO_CAMPO] |
  | UF | string  | Estado do incentivador no formato EE  |
  | projetos_recentes | Projeto ($list)  | Lista de projetos recentes que esse incentivador aportou  |

  ### Dúvida | Enviar para o Professor orientador | APAGAR APÓS RESPOSTA
  Faz sentido manter uma lista de projetos recentes que esse incentivador aportou na propriedade **projetos_recentes**, penso em salvar os cinco aportes mais recentes desse incentivador nessa lista para fazer a recomendação inicial por valor de aporte.
