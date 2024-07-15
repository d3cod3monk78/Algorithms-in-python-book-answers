def removing_punctuation(string: str) -> str:
    punctuations = ['.', ',', '?', '!', '\'']
    new_string: [str] = []

    for x in string:
        if x not in punctuations:
            new_string.append(x)

    return ''.join(new_string)


print(removing_punctuation('what the is going on here bitches? what\' the reason for this thing? hey!!! we are done.'))
