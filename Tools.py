def Validate(text:str) -> str:
    if text.startswith('"') and text.endswith('"') or text.startswith("'") and text.endswith("'"):
        return text
    else:
        text = f'"{text}"'
        return text