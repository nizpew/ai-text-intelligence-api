def analyze_sentiment(text: str) -> dict:
    """
    Análise simples de sentimento (Lógica baseada em regras).
    """
    text = text.lower()
    
    # Listas de palavras (você pode aumentar depois)
    # Dicionários expandidos
    positive_words = [
        "bom", "ótimo", "excelente", "feliz", "maravilhoso", "lucro", "ganhar", 
        "gostei", "adorei", "amo", "incrível", "top", "legal", "show"
    ]
    negative_words = [
        "ruim", "péssimo", "horrível", "triste", "perda", "erro", "falha", 
        "odiei", "detestei", "lento", "travando", "bug", "caro"
    ]
    score = 0

    # Conta pontos
    for word in positive_words:
        if word in text:
            score += 1
            
    for word in negative_words:
        if word in text:
            score -= 1

    # Decide o sentimento
    if score > 0:
        sentiment = "positivo"
    elif score < 0:
        sentiment = "negativo"
    else:
        sentiment = "neutro"

    return {
        "sentiment": sentiment,
        "score": score
    }