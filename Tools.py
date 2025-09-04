# Essa função desempenha o papel de adicionar aspas duplas ao texto/variavel inserido
def Validate(text:str) -> str:
    if text.startswith('"') and text.endswith('"') or text.startswith("'") and text.endswith("'"):
        return text
    else:
        text = f'"{text}"'
        return text
    
# Essa função desempenha o papel de remover as aspas (simples e/ou duplas) do texto/variavel inserido
def Safe_Remove(text:str) -> str:
    if text.startswith('"') and text.endswith('"') or text.startswith("'") and text.endswith("'"):
        text = text.replace("'", "")
        text = text.replace('"', "")
        return text
    else:
        return text