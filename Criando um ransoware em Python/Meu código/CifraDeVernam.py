# inicia variaveis
# Só para teste, mas em um cenario real, a senha deve ser idepedente do algoritmo
def EncriptarDecriptar(txt:str, mode:str):
    # sourcery skip: convert-to-enumerate, move-assign-in-block, use-join
    key = "BtJrHKrr1\}p36`8"

    # Aramazena a posição de uma letra na palavra
    keyidx = 0

    # resutado
    xored = ''
    msg = ''
    
    # codifica ou decodifica a mensage
    if mode == 'enc':
        msg = txt
    elif mode == 'dec':
        msg = txt.decode('utf8', 'strict')

    for msgchar in msg:
        # Operação XOR:
        # chr() - transforma um caracter em decimal para ascii
        # ord() - transforma um caractere ascii em decimal
        xored += chr(ord(key[keyidx % len(key)]) ^ ord(msgchar))

        # Controla qual a letra da palavra-secreta será usada no próximo loop
        keyidx += 1

    msgenc = ''
    # Transforma o resultado em hexadecimal letra
    if mode == 'enc':
        msgenc = xored.encode(encoding='utf8')
    elif mode == 'dec':
        msgenc = xored
    return msgenc
