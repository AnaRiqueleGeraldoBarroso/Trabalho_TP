from datetime import datetime

from execoes import UJCException, UNCException, PEException, PIException, SIException, MFPException, PDException


def gerador_id():
    id_atual = 1
    while True:
        yield id_atual
        id_atual += 1

gerador = gerador_id()

class Tweet:
    def __init__(self,usuario, mensagem, data_postagem):
        self.__usuario = usuario
        self.__mensagem = mensagem
        self.__data_postagem = data_postagem

        self.__id = next(gerador)

    def get_id(self):
        return self.__id

    def get_usuario(self):
        return self.__usuario

    def get_mensagem(self):
        return self.__mensagem

    def get_data_postagem(self):
        return self.__data_postagem

class Perfil:
    def __init__(self, usuario):
        self.__usuario = usuario
        self.__seguidos = [] #Lista de perfils que o usuários segue
        self.__seguidores = [] #Lista de perfils que segue o usuário
        self.__tweets = [] #Lista de tweets do usuário
        self.__ativo = True #Perfil inicia como ativo

    def add_seguidor(self, perfil):
        if perfil not in self.__seguidores:
            self.__seguidores.append(perfil)

    def add_seguidos(self, perfil):
        if perfil not in self.__seguidos:
            self.__seguidos.append(perfil)

    def add_tweet(self, tweet):
        self.__tweets.append(tweet)

    def get_tweets(self):
        return sorted(self.__tweets, key=lambda t:t.get_data_postagem(), reverse=True)

    def get_tweet(self, tweet_id):
        for tweet in self.__tweets:
            if tweet.get_id() == tweet_id:
                return tweet
        return None

    #Não entendi
    def get_timeline(self):
        timeline = self.__tweets[:]

        for perfil in self.__seguidos:
            timeline.extend(perfil.get_tweets())
        return sorted(timeline, key=lambda t: t.get_data_postagem(), reverse=True)

    def set_usuario(self, usuario):
        self.__usuario = usuario

    def get_usuario(self):
        return self.__usuario

    def set_ativo(self, ativo):
        self.__ativo = ativo

    def is_ativo(self):
        return self.__ativo

    #Não foi pedido
    def get_seguidores(self):
        return self.__seguidores

    #Não foi pedido
    def get_seguidos(self):
        return self.__seguidos

class PessoaFisica(Perfil):
    def __init__(self, usuario, cpf):
        super().__init__(usuario)
        self.__cpf = cpf

    def get_cpf(self):
        return self.__cpf

class PessoaJuridica(Perfil):
    def __init__(self, usuario, cnpj):
        super().__init__(usuario)
        self.__cnpj = cnpj

    def get_cnpj(self):
        return self.__cnpj

class RepositorioUsuarios:
    def __init__(self):
        self.__usuario = []

    def cadastrar(self, perfil):
        for usuario in self.__usuario:
            if usuario.get_usuario == perfil.get_usuario():
                raise UJCException('Usuário já cadastrado')

    def buscar(self, nome_usuario):
        for usuario in self.__usuario:
            if usuario.get_usuario() == nome_usuario:
                return usuario
        return None

    def atualizar(self, perfil):
        for i, usuario in enumerate(self.__usuario):
            if usuario.get_usuario() == perfil.get_usuario():
                self.__usuario[i] = perfil
                return
        raise UNCException('Usuário não cadastrado')

class MyTwitter:
    def __init__(self):
        self.repositorio = RepositorioUsuarios

    def criar_perfil(self, perfil):
        if self.repositorio.buscar(perfil.get_usuario()):
            raise PEException('Já existe perfil com esse nome')

        self.repositorio.cadastrar(perfil)

    def cancelar_perfil(self, nome_usuario):
        perfil = self.repositorio.buscar(nome_usuario)

        if perfil is None:
            raise PIException('Perfil não encontrado')
        if not perfil.is_ativo():
            raise PDException('Perfil desativado')

        perfil.set_ativo(False)

    def tweetar(self, nome_usuario, mensagem):
        perfil = self.repositorio.buscar(nome_usuario)

        if perfil is None:
            raise PIException('Perfil não encontrado')
        if not perfil.is_ativo():
            raise PDException('Perfil desativado')
        if len(mensagem) < 1 or len(mensagem) > 140:
            raise MFPException('Mensagem fora do padrão (1 a 140 caracteres)')

        tweet = Tweet(nome_usuario, mensagem, gerador_id())
        perfil.add_tweet(tweet)

    def timeline(self, nome_usuario):
        perfil = self.repositorio.buscar(nome_usuario)

        if perfil is None:
            raise PIException('Perfil não encontrado')
        if not perfil.is_ativo():
            raise PDException('Perfil desativado')

        timeline_tweets = perfil.get_tweets()

        for seguido in perfil.get_seguidos():
            timeline_tweets.extend(seguido.get_tweets())

        timeline_tweets.sort(key=lambda x:x.get_data_postagem(), reverse=True)
        return timeline_tweets

    def tweets(self, nome_usuario):
        perfil = self.repositorio.buscar(nome_usuario)

        if perfil is None:
            raise PIException('Perfil não encontrado')
        if not perfil.is_ativo():
            raise PDException('Perfil desativado')

        return perfil.get_tweets()

    def seguir(self, seguidor_nome, seguido_nome):
        seguidor = self.repositorio.buscar(seguidor_nome)
        seguido = self.repositorio.buscar(seguido_nome)

        if seguidor is None or seguido is None:
            raise PIException('Perfil não encontrado')
        if not seguidor.is_ativo() or not seguido.is_ativo():
            raise PDException('Perfil desativado')

        if seguidor_nome == seguido_nome:
            raise SIException('Não é possível seguir a si mesmo')

        seguidor.add_seguidos(seguido)
        seguido.add_seguidor(seguidor)

    def numero_seguidores(self, nome_usuario):
        perfil = self.repositorio.buscar(nome_usuario)
        if perfil is None:
            raise PIException('Perfil não encontrado')
        if not perfil.is_ativo():
            raise PDException('Perfil desativado')
        return len([seguidor for seguidor in perfil.get_seguidores() if seguidor.is_ativo()])

    def seguidores(self, nome_usuario):
        perfil = self.repositorio.buscar(nome_usuario)
        if perfil is None:
            raise PIException('Perfil não encontrado')
        if not perfil.is_ativo():
            raise PDException('Perfil desativado')
        return [seguidor for seguidor in perfil.get_seguidores() if seguidor.is_ativo()]

    def seguidos(self, nome_usuario):
        perfil = self.repositorio.buscar(nome_usuario)
        if perfil is None:
            raise PIException('Perfil não encontrado')
        if not perfil.is_ativo():
            raise PDException('Perfil desativado')
        return [seguido for seguido in perfil.get_seguidos() if seguido.is_ativo()]