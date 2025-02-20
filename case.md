# **Módulo 1: Introdução à Engenharia de Dados**

## **1.1 O que é Engenharia de Dados ?**

Engenharia de Dados é a área responsável por **construir e manter a infraestrutura** que permite coletar, armazenar, processar e disponibilizar dados de forma eficiente. Pense nela como a "construção de estradas" para os dados: o engenheiro de dados cria os caminhos por onde os dados vão trafegar, garantindo que eles cheguem ao destino certo, no formato certo e no momento certo.

### **Engenharia de Dados vs Ciência de Dados**

#### **Engenharia de Dados:**

- Foca na construção e manutenção da infraestrutura de dados.
- Responsável pela coleta, armazenamento e processamento de grandes volumes de dados.
- Se os dados fossem água, o engenheiro de dados seria responsável por construir canos, reservatórios e sistemas de filtragem para que a água chegue limpa e pronta para uso.

#### **Ciência de Dados:**

- Foca na análise e interpretação dos dados para extrair insights e tomar decisões informadas.
- Utiliza técnicas estatísticas, algoritmos de machine learning e visualização de dados.
- Envolve a criação de modelos preditivos e a realização de experimentos para testar hipóteses.
- Se os dados fossem água, o cientista de dados seria responsável por analisar a qualidade da água, descobrir de onde ela vem e prever se vai faltar no futuro.

### **O papel do Engenheiro de Dados dentro de um time de dados**

O papel do engenheiro de dados dentro de um time de dados é fundamental para garantir que os dados estejam disponíveis, acessíveis e em um formato utilizável para os cientistas de dados e outros stakeholders. As principais responsabilidades incluem:

- **Coleta de Dados**: Coletar dados de diferentes fontes, como APIs, bancos de dados, planilhas, sensores, etc.
- **Armazenamento de Dados**: Implementar processos de validação e limpeza de dados para assegurar a precisão e a integridade dos dados.
- **Armazenamento e gerenciamento de dados**: Escolher e configurar onde os dados serão armazenados (bancos de dados, data lakes, data warehouses).
- **Processamento e Transformação de Dados**: Limpar, organizar e transformar os dados brutos em um formato útil para análise.
- **Criação de Pipelines de Dados**: Desenvolver fluxos automatizados para mover e processar dados entre diferentes sistemas.
- **Garantia de Qualidade dos Dados**: Verificar se os dados estão completos, consistentes e livres de erros.

### **Visão geral do pipeline de dados: Extração, Transformação e Carregamento (ETL)**

#### **Pipeline de Dados**

Um pipeline de dados é um conjunto de processos que move dados de uma fonte para um destino, passando por etapas de coleta, processamento e armazenamento. É como uma "linha de montagem" para dados, onde cada etapa tem um propósito específico.

#### **(ETL) Extração, Transformação e Carregamento**

É um tipo de pipeline de dados que envolve três etapas principais:

1. **Extração (Extract):**

    - Coleta de dados
    - Exemplo: Extrair dados de vendas de um site de e-commerce.

2. **Transformação (Transform):**

    - Processamento dos dados
    - Exemplo: Converter datas para um formato padrão, remover dados duplicados ou calcular valores totais.

3. **Carregamento (Load):**

    - Armazenamento dos dados
    - Exemplo: Carregar os dados de vendas processados em um banco de dados para que os analistas possam acessá-los.