def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None

def scan(user):
    user = user.lower()
    words = user.split()
    sentence = []
    
    directions = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
    verb = ['go', 'stop', 'kill', 'eat']
    stop = ['the', 'in', 'of', 'from', 'at', 'it']
    noun = ['door', 'bear', 'princess', 'cabinet']
    
    for word in words:
        if word in directions:
            sentence.append(('direction', word))
        elif word in verb:
            sentence.append(('verb', word))
        elif word in stop:
            sentence.append(('stop', word))
        elif word in noun:
            sentence.append(('noun', word))
        else:
            last = convert_number(word)
            if last == None:
                sentence.append(('error', word))
            else:
                sentence.append(('number', last))
    return sentence
    
if __name__ == '__main__':
    test = raw_input('> ')
    print scan(test)