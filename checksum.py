from hashlib import md5
from subprocess import getoutput
from datetime import datetime
from sys import argv
from os.path import exists, isdir


def md5sum(file):
    hash = md5()
    print('\n# Iniciando algoritmo')
    initial_time = datetime.now()
    print('Início.................{}'.format(str(initial_time)))

    with open(file, 'rb') as f:
        for piece in iter(lambda: f.read(4096), b""):
            hash.update(piece)

    final_time = datetime.now()
    print('Fim....................{}'.format(str(final_time)))
    print('Total..................{}'.format(str(final_time - initial_time)))
    print('# Algorotmo finalizado!\n')

    return 'Resultado.............{}'.format(hash.hexdigest())


def md5sum_system_command(file):
    print('\n# Iniciando comando do sistema')
    initial_time = datetime.now()
    print('Início.................{}'.format(str(initial_time)))

    output = getoutput('md5sum {}'.format(file)).split(' ')[0]

    final_time = datetime.now()
    print('Fim....................{}'.format(str(final_time)))
    print('Total..................{}'.format(str(final_time - initial_time)))
    print('# Comando do sistema finalizado!\n')

    return 'Resultado.............{}'.format(output)


if __name__ == '__main__':
    if len(argv) <= 1:
        print('Qual é o arquivo?')
        print('Uso correto: python checksum.py <arquivo>')
        exit(0)

    file = argv[1]
    if not exists(file) or isdir(file):
        print('Pode mandar um arquivo válido?')
        exit(0)

    print(md5sum(file))
    print(md5sum_system_command(file))