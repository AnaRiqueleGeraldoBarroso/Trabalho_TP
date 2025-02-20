class UJCException(Exception):
    def __init__(self, mensagem='Usuário já cdastrado'):
        super().__init__(mensagem)


class UNCException(Exception):
    def __init__(self, mensagem='Usuário não cadastrado'):
        super().__init__(mensagem)


class PEException(Exception):
    def __init__(self, mensagem='Perfil já existente'):
        super().__init__(mensagem)


class PIException(Exception):
    def __init__(self, mensagem='Perfil não encontrado'):
        super().__init__(mensagem)


class PDException(Exception):
    def __init__(self, mensagem='Perfil desativado'):
        super().__init__(mensagem)


class MFPException(Exception):
    def __init__(self, mensagem='Mesagem fora do padrão (1 a 140 caracteres)'):
        super().__init__(mensagem)


class SIException(Exception):
    def __init__(self, mensagem='Não é possível seguir a si mesmo'):
        super().__init__(mensagem)
