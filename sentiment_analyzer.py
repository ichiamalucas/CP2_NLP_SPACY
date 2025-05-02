import spacy
from spacy.matcher import Matcher
from spacy.tokens import Doc

# 1. Carregar o modelo de português
try:
    nlp = spacy.load("pt_core_news_sm")
    print("Modelo pt_core_news_sm carregado com sucesso!")
except OSError:
    print("Modelo pt_core_news_sm não encontrado. Por favor, execute:")
    print("python -m spacy download pt_core_news_sm")
    exit()

# 2. Adicionar uma extensão personalizada ao objeto Doc
# Define a extensão 'sentimento' com valor padrão 'Neutro'
if not Doc.has_extension("sentimento"):
    Doc.set_extension("sentimento", default="Neutro")
    print("Extensão 'sentimento' adicionada ao Doc.")

# 3. Criar regras com Matcher
matcher = Matcher(nlp.vocab)

# Listas simples de palavras para sentimentos (em minúsculas)
positive_words = ["bom", "boa", "ótimo", "ótima", "feliz", "amo", "gosto",
                  "excelente", "maravilhoso", "maravilhosa", "positivo", "bem", "legal"]
negative_words = ["ruim", "péssimo", "péssima", "triste", "odeio", "detesto",
                  "terrível", "negativo", "mal", "chato", "chata", "não gosto"]

# Padrões para o Matcher (correspondência por token em minúsculas)
# [{"LOWER": {"IN": [...]}}] - Corresponde a um token cuja forma em minúscula está na lista
pattern_pos = [{"LOWER": {"IN": positive_words}}]
pattern_neg = [{"LOWER": {"IN": negative_words}}]

# Adicionar os padrões ao Matcher com IDs
matcher.add("POSITIVO", [pattern_pos])
matcher.add("NEGATIVO", [pattern_neg])

# 4. Analisar uma lista de frases
phrases = [
    "Eu amo programar em Python, é ótimo!",
    "Este serviço foi péssimo e o atendimento ruim.",
    "O céu está azul hoje, um dia normal.",
    "A comida estava boa, mas o atendimento foi ruim.",
    "Preciso comprar pão no mercado.",
    "Que dia maravilhoso tivemos!",
    "Não gosto de chuva."
]

print("\nAnalisando frases:")

# Processar e analisar cada frase
for phrase in phrases:
    doc = nlp(phrase)

    # Encontrar correspondências usando o Matcher
    matches = matcher(doc)

    # Determinar o sentimento baseado nas correspondências encontradas
    is_positive = False
    is_negative = False

    for match_id, start, end in matches:
        match_name = nlp.vocab.strings[match_id]
        if match_name == "POSITIVO":
            is_positive = True
        elif match_name == "NEGATIVO":
            is_negative = True

    # Definir o sentimento no objeto Doc usando a extensão personalizada
    sentiment = "Neutro"
    if is_positive and not is_negative:
        sentiment = "Positivo"
    elif is_negative and not is_positive:
        sentiment = "Negativo"
    elif is_positive and is_negative:
        sentiment = "Conflitante" # Ou "Misto", ou priorizar um, dependendo da regra de negócio

    doc._.sentimento = sentiment

    # 5. Imprimir o sentimento de cada frase
    print(f"Frase: \"{phrase}\"")
    print(f"Sentimento: {doc._.sentimento}")
    print("-" * 20)