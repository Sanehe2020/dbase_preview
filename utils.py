def grep(text, nmax):
    size = len(text)
    if (size<nmax):
        return text
    else:
        return text[0:nmax]
