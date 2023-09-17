from pathlib import Path


LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg): 
        raise NotImplementedError('Implemente o método log')
    
    """
    Esse aqui é um metodo obrigatoria que todas as sub classes tem que ter
    """

    def log_error(self, msg):
        return self._log(f'Error: {msg}')

    """
    Esse self é o objeto que está chamando log_error
    e ._log é o metodo da classe que fez o objeto 
    """

    def log_success(self, msg):
        return self._log(f'Success: {msg}')


class LogFileMixin(Log):
    def _log(self, msg):
        msg_format = f'{msg} ({self.__class__.__name__})'
        with LOG_FILE.open('a', encoding='utf8') as arquivo:
            arquivo.write(f'{msg_format}\n')


class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')


if __name__ == '__main__':
    l1 = LogPrintMixin()
    l2= LogFileMixin()
    l2.log_error('deu errado cara (-_-*)')
    l2.log_success('yes yes yes (*-*)')
    l1.log_success('Que legal')