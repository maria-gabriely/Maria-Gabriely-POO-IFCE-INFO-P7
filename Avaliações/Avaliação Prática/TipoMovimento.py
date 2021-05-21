import enum

class TipoMovimento(enum.Enum):
    Provento = 'P'
    Desconto = 'D'
    
if __name__ == '__main__':
    print('As letras enum são:')
    for tipo in (TipoMovimento):
        print(type(tipo))
        print(tipo)