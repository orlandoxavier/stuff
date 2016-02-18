from os import remove
from os.path import expanduser, isfile
from datetime import datetime
import argparse
import google


USER_HOME = expanduser('~')
LOG_FILE = '{}/.goopy.log'.format(USER_HOME) # Arquivo de log.
COOKIE_FILE = '{}/.google-cookie'.format(USER_HOME) # Arquivo de cookie criado pelo módulo 'google'

def search_it(text, stop):
    """
    Faz a busca propriamente dita.
    :param text:
    :param stop:
    :return:
    """
    results = []
    for r in google.search(query=text, stop=stop):
        results.append(r)
        print(r)

    log_it(args.text, args.stop, results)

def log_it(text, stop, result_list):
    """
    Salva a pesquisa no arquivo de log.
    :param text:
    :param stop:
    :return:
    """
    with open(LOG_FILE, 'a') as f:
        f.write('---- Em {} ----\n\n'.format(get_formatted_datetime()))
        f.write('Limite de {} registros\n'.format(stop))
        f.write('Buscado: {}\n\n'.format(text))
        f.write('Resultados: \n\n')

        for r in result_list:
            f.write('{}\n'.format(r))

        f.write('\n---- Fim da pesquisa {} ----\n\n\n\n'.format(get_formatted_datetime()))

def get_formatted_datetime():
    return datetime.now().strftime('%d/%m/%Y %H:%M:%S')

def remove_cookie():
    """
    Remove arquivo de cookie criado pelo módulo 'google'.
    :return:
    """
    if isfile(COOKIE_FILE):
        remove(COOKIE_FILE)


if __name__ == '__main__':
    # Configura os argumentos da linha de comando.
    parser = argparse.ArgumentParser()

    parser.add_argument('-t', action='store', dest='text',
                        default='', required=True,
                        help='Texto a ser buscado')

    parser.add_argument('-s', action='store', dest='stop',
                        default=15, required=False,
                        help='Máximo de resultados')

    args = parser.parse_args()
    search_it(args.text, int(args.stop))
    remove_cookie()