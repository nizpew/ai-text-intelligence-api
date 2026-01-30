def classify_text(text: str) -> str:
    """
    Classifica o texto em categorias baseadas em palavras-chave.
    """
    text = text.lower()

    if "dinheiro" in text or "preço" in text or "venda" in text:
        return "finanças"
    if "python" in text or "código" in text or "ia" in text:
        return "tecnologia"
    if "futebol" in text or "jogo" in text:
        return "esportes"

    return "geral"