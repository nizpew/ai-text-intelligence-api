def summarize_text(text: str) -> str:
    """
    Resumo simples: Pega a primeira frase do texto.
    """
    if not text:
        return ""
        
    # Divide por ponto final e pega a primeira parte
    sentences = text.split(".")
    return sentences[0].strip()