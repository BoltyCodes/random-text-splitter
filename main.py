mytext = "I need to write a really long string so that I can see where it splits it. I don't have a great imagination so this is a rather boring sentence."
def shortener(text: str, length: int = 97, dots: bool = False) -> str:
    if len(text) > length:
        if dots == True:
            output = text[:length] + "..."
        else:
            output = text[:length]
    else:
        output = text
    return output
call = shortener(text=mytext, length=97, dots=True)
print(call)
