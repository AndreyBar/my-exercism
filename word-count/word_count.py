def word_count(phrase):
    r = dict()
    ns = ''
    for ch in phrase:
        if ch.isalnum():
            ns += ch
        else:
            ns += ' '
    ns = ns.lower().replace('  ', ' ')
    for word in ns.split():
        if word in r:
            r[word] += 1
        else:
            r[word] = 1
    return r