
def encrypt(message,rot):
    uppers = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowers = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for char in message:
        if char == ' ':
            encrypted = encrypted + ' '
        else:
            if char in uppers:
                rotatedIndex = uppers.index(char) + rot
                if rotatedIndex < 26:
                    encrypted = encrypted + uppers[rotatedIndex]
                else:
                    encrypted = encrypted + uppers[rotatedIndex % 26]
            elif char in lowers:
                rotatedIndex = lowers.index(char) + rot
                if rotatedIndex < 26:
                    encrypted = encrypted + lowers[rotatedIndex]
                else:
                    encrypted = encrypted + lowers[rotatedIndex % 26]
            else:
                encrypted = encrypted + char
    return encrypted
