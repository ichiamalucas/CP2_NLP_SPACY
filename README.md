# Análise de Sentimento com spaCy e Regras Personalizadas

Este script Python demonstra como utilizar a biblioteca spaCy para realizar uma análise de sentimento simples em frases, baseada em regras personalizadas definidas com o `Matcher` e armazenando o resultado usando `Doc.set_extension`.

## Requisitos

* Python 3.6 ou superior.
* Biblioteca spaCy.
* Modelo de português `pt_core_news_sm` para spaCy.

## Instalação

1.  **Instalar spaCy:**
    ```bash
    pip install spacy
    ```

2.  **Baixar o modelo de português:**
    ```bash
    python -m spacy download pt_core_news_sm
    ```

## Como Executar

1.  Salve o código Python fornecido (na seção **Código Python** do guia) em um arquivo chamado `sentiment_analyzer.py`.
2.  Salve este conteúdo em um arquivo chamado `README.md` no mesmo diretório.
3.  Abra um terminal ou prompt de comando e navegue até o diretório onde você salvou os arquivos.
4.  Execute o script Python:
    ```bash
    python sentiment_analyzer.py
    ```

## Funcionamento do Código

1.  **Carregamento do Modelo:** O script carrega o modelo pequeno de português `pt_core_news_sm` do spaCy, que fornece funcionalidades básicas de Processamento de Linguagem Natural (PLN), como tokenização e lematização.
2.  **Extensão Personalizada (`Doc.set_extension`):** Uma extensão personalizada chamada `sentimento` é adicionada ao objeto `Doc` do spaCy. Isso permite que cada documento processado pelo spaCy tenha um atributo `.sentimento` onde o resultado da análise pode ser armazenado. O valor padrão é definido como "Neutro".
3.  **Regras com `Matcher`:** O `Matcher` do spaCy é utilizado para encontrar padrões de palavras no texto. Definimos listas de palavras positivas e negativas comuns em português. Padrões são criados para detectar qualquer token (palavra) cuja forma em minúscula esteja em uma dessas listas. As regras são adicionadas ao matcher com os IDs "POSITIVO" e "NEGATIVO".
4.  **Análise das Frases:** Uma lista de frases de exemplo é definida. O script itera sobre cada frase:
    * A frase é processada pelo spaCy (`nlp(phrase)`), criando um objeto `Doc`.
    * O `matcher` é aplicado ao `Doc` para encontrar as correspondências definidas nas regras.
    * As correspondências encontradas são verificadas para determinar se palavras positivas ou negativas (ou ambas) estão presentes na frase.
    * Com base na presença de palavras positivas e/ou negativas, o sentimento da frase é classificado como "Positivo", "Negativo", "Neutro" (se nenhuma for encontrada) ou "Conflitante" (se ambas forem encontradas).
    * O sentimento determinado é armazenado no atributo `._.sentimento` do objeto `Doc`.
5.  **Impressão dos Resultados:** O script imprime a frase original e o sentimento detectado que foi armazenado na extensão personalizada do `Doc`.

Este é um exemplo básico de análise de sentimento baseado em léxico (listas de palavras). Para tarefas mais complexas, modelos de aprendizado de máquina treinados em grandes datasets de sentimento são geralmente mais eficazes.