mytext = "The quick brown fox jumped over the lazy dogs last Friday morning in my neighbor's yard when the "
def shortener(text: str, length: int = 100, dots: bool = False) -> str:
    if len(text) >= length:
        if dots == True:
            output = text[:length - 3] + "..."
        else:
            output = text[:length]
    else:
        output = text
    return output
call = shortener(text=mytext, length=97, dots=True)
print(call)
