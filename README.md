# Case de **Engenharia de Dados e Analytics** | FEA.dev

## Introdução

Este case foi desenvolvido pela **FEA.dev** com o objetivo de capacitar seus membros em **Engenharia de Dados e Analytics**, utilizando **dados financeiros públicos** de fontes como o **Banco Central**, **CVM** e **B3**. O projeto integra **conceitos técnicos e de negócios**, aplicando ferramentas modernas de **coleta, processamento, análise e visualização de dados**, com foco em **serviços AWS gratuitos** e ferramentas de visualização como **Streamlit**, **Power BI** ou **Looker Studio**.

---

## Objetivo

O objetivo deste case é:

1. Criar uma **plataforma de análise de dados financeiros** para auxiliar na **tomada de decisões estratégicas**;
2. Capacitar os membros da **FEA.dev** em **Engenharia de Dados e Analytics**;
3. Desenvolver **habilidades técnicas e de negócios** através de um projeto **prático e didático**.

---

## Resumo do Case

O case consiste em:

1. Coletar **dados financeiros** de **APIs públicas** (Banco Central, CVM, B3);
2. Processar e transformar os dados utilizando **serviços AWS** como **Lambda**, **Glue** e **RDS**;
3. Visualizar os dados em **dashboards interativos** usando ferramentas como **Streamlit**, **Power BI** ou **Looker Studio**;
4. Automatizar **notificações e interações** via **Telegram Bot**;
5. Desenvolver **habilidades técnicas e de negócios** ao longo do projeto.

---

### Pré-requisitos

Para realizar este case, é necessário:

- Conhecimento básico de **Python**;
- Familiaridade com conceitos de **banco de dados** e **SQL**;
- Noções de **APIs** e **integração de sistemas**;
- Conta na **AWS** para utilizar serviços gratuitos;
- Conta no **Telegram** para criar e configurar o bot.

---

## Competências desenvolvidas até completar o Case

### Hard Skills

- **Engenharia de Dados:**
  - Coleta de dados via **APIs**;
  - Processamento e transformação de dados (**ETL**);
  - Armazenamento e consulta em **bancos de dados relacionais** (RDS);
  - Automação de **pipelines de dados** com **AWS Lambda** e **Glue**.
 
- **Engenharia de Analytics:**
  - **Análise exploratória de dados (EDA)**;
  - Criação de **métricas e indicadores financeiros**;
  - Visualização de dados com ferramentas modernas (**Streamlit**, **Power BI**, **Looker Studio**);
  - Desenvolvimento de **dashboards interativos**;
  - Uso de **modelos preditivos** para análise de tendências (opcional).

### Soft Skills

- **Trabalho em equipe** para dividir tarefas e resolver problemas;
- **Comunicação clara** para apresentar resultados e insights;
- **Gestão de tempo** para cumprir prazos e entregas.

### Human Skills

- **Pensamento crítico** para analisar dados e gerar insights;
- **Adaptabilidade** para lidar com mudanças e desafios técnicos;
- **Aprendizado contínuo** para dominar novas ferramentas e conceitos.

---

## Conhecimentos técnicos adquiridos com o Case

### Conceitos de negócios

- Análise de **indicadores econômicos** (taxa Selic, inflação, câmbio);
- Interpretação de **dados financeiros** (demonstrações contábeis, desempenho de ações);
- Geração de **insights** para **tomada de decisões estratégicas**.

### Ferramentas

- **AWS:** Lambda, Glue, S3, RDS, CloudWatch, API Gateway;
- **Visualização de dados:** Streamlit, Power BI, Looker Studio;
- **Automação:** Telegram Bot, Python;
- **Banco de dados:** MySQL/PostgreSQL (Amazon RDS);
- **Linguagem de programação:** Python.

### Conceitos técnicos

- **Engenharia de Dados:** ETL, pipelines de dados, data warehousing;
- **Engenharia de Analytics:** Dashboards, métricas, visualização de dados;
- **Integração de sistemas:** APIs, automação, bots;
- **Cloud computing:** Uso de serviços AWS.

---

## Valor Gerado para o Negócio - Hipótese

Este projeto gera valor ao abordar um problema crítico no contexto de **gerenciamento de risco**:

- **Problema:** Empresas e investidores enfrentam dificuldades para **monitorar e prever riscos financeiros**, como variações abruptas na **taxa de juros**, **inflação** ou **desempenho de ativos**. A falta de acesso a **dados atualizados** e **insights acionáveis** pode levar a **decisões inadequadas**, expondo o negócio a **perdas financeiras** e **oportunidades desperdiçadas**;
- **Valor Gerado:** A plataforma desenvolvida neste case permite:
  - **Monitorar indicadores econômicos** em tempo real;
  - **Identificar tendências e anomalias** nos dados financeiros;
  - **Tomar decisões informadas** para **mitigar riscos** e **aproveitar oportunidades**;
  - **Automatizar alertas** sobre mudanças críticas (ex.: aumento da taxa Selic ou queda no preço de ações);
  - **Reduzir a incerteza** e **aumentar a confiança** nas decisões estratégicas.

---

## Programa do conteúdo

### 1. **Introdução ao Case e Planejamento**
   - Apresentação do case e objetivos;
   - Definição de **papéis e responsabilidades**;
   - Planejamento das etapas do projeto.

### 2. **Coleta de Dados**
   - Introdução a **APIs** e coleta de dados públicos;
   - Configuração do **AWS Lambda** para automatizar a coleta;
   - Armazenamento dos dados brutos no **Amazon S3**.

### 3. **Processamento e Transformação de Dados**
   - Introdução ao **ETL** com **AWS Glue**;
   - Transformação e limpeza dos dados;
   - Armazenamento dos dados processados no **Amazon RDS**.

### 4. **Visualização de Dados**
   - Escolha da ferramenta de visualização (**Streamlit**, **Power BI**, **Looker Studio**);
   - Criação de **dashboards interativos**;
   - Publicação e compartilhamento dos dashboards.

### 5. **Automação e Notificações**
   - Criação de um **bot no Telegram**;
   - Integração do bot com **AWS Lambda** e **API Gateway**;
   - Configuração de **notificações automáticas**.

### 6. **Machine Learning (Opcional)**
   - Introdução a **modelos preditivos** com **Amazon SageMaker**;
   - Criação de um modelo simples para **previsão de tendências**;
   - Integração do modelo ao **pipeline de dados**.

### 7. **Monitoramento e Gestão**
   - Configuração do **Amazon CloudWatch** para monitoramento;
   - Criação de **alertas** para falhas ou gargalos.

### 8. **Apresentação e Conclusão**
   - Apresentação dos **resultados** e **dashboards**;
   - Discussão dos **insights gerados**;
   - Feedback e **próximos passos**.

---

## Como contribuir

1. Faça um **fork** deste repositório.
2. Crie uma **branch** para sua contribuição (`git checkout -b feature/nova-feature`).
3. **Commit** suas alterações (`git commit -m 'Adiciona nova feature'`).
4. **Push** para a branch (`git push origin feature/nova-feature`).
5. Abra um **Pull Request**.

---

## Licença

Este projeto está licenciado sob a licença **MIT**. 

---

## Contato

Para dúvidas ou sugestões, entre em contato com:
- **Gabriel Braz:** gabriel_braz@usp.br
- **Igor Pires:** igorpires@usp.br
- **Gabriel Navarro:** gbnavarro@usp.br
