import unittest

from MyTwitter import Perfil, Tweet, PessoaFisica, PessoaJuridica

class PerfilTest(unittest.TestCase):

    def test_init(self):
        perfil = Perfil('usuario1')
        self.assertEqual(perfil.get_usuario(), 'usuario1')
        self.assertTrue(perfil.is_ativo())
        self.assertEqual(len(perfil.get_seguidores()), 0) #Inicia com 0 seguidores
        self.assertEqual(len(perfil.get_seguidos()), 0) #Inicia com 0 seguidos
        self.assertEqual(len(perfil.get_tweets()), 0) #Inicia com 0 tweet

    def test_add_seguidor(self):
        perfil1 = Perfil('usuario1')
        perfil2 = Perfil('usuario2')

        #adiciona perfil2 como seguidor de perfil1
        perfil1.add_seguidor(perfil2)

        #verifica se um valor está presente em uma lista
        self.assertIn(perfil2, perfil1.get_seguidores())

    def test_add_seguidos(self):
        perfil1 = Perfil('usuario1')
        perfil2 = Perfil('usuario2')

        #adiciona perfil2 a lista de seguidos do perfil1
        perfil1.add_seguidos(perfil2)

        self.assertIn(perfil2, perfil1.get_seguidos())

    def test_add_tweet(self):
        perfil1 = Perfil('usuario1')
        tweet = Tweet(1, 'Teste de tweet', '2025-02-20 12:00:00')

        #adiciona um tweet ao perfil
        perfil1.add_tweet(tweet)

        #verifica se o tweet foi adicionado
        self.assertIn(tweet, perfil1.get_tweets())

    def test_get_tweets(self):
        perfil1 = Perfil('usuario1')

        tweet1 = Tweet(1, 'Primeiro tweet', '2025-02-20 12:00:00')
        tweet2 = Tweet(2, 'Segundo tweet', '2025-02-21 12:00:00')

        perfil1.add_tweet(tweet1)
        perfil1.add_tweet(tweet2)

        tweets = perfil1.get_tweets()

        self.assertEqual(tweets[0], tweet2)
        self.assertEqual(tweets[1], tweet1)

    '''def test_get_tweet(self):
        perfil1 = Perfil('usuario1')
        tweet1 = Tweet(1, 'Primeiro tweet', '2025-02-20 12:00:00')
        perfil1.add_tweet(tweet1)

        tweet = perfil1.get_tweet(1)
        self.assertEqual(tweet, tweet1)

        tweet_inexistente = perfil1.get_tweet(999)
        self.assertIsNone(tweet_inexistente)'''

    def test_get_timeline(self):
        perfil1 = Perfil('usuario1')
        perfil2 = Perfil('usuario2')

        tweet1 = Tweet(1, 'Tweet do usuario1', '2025-02-20 12:00:00')
        tweet2 = Tweet(2, 'Tweet do usuario2', '2025-02-21 12:00:00')

        perfil1.add_tweet(tweet1)
        perfil2.add_tweet(tweet2)

        perfil1.add_seguidos(perfil2)

        timeline = perfil1.get_timeline()

        self.assertEqual(timeline[0], tweet2)
        self.assertEqual(timeline[1], tweet1)

    def test_set_ativo(self):
        perfil1 = Perfil('usuario1')

        perfil1.set_ativo(False)

        self.assertFalse(perfil1.is_ativo())

        perfil1.set_ativo(True)

        self.assertTrue(perfil1.is_ativo())

    def test_set_usuario(self):
        perfil1 = Perfil('usuario1')

        perfil1.set_usuario('novo_usuario')

        self.assertEqual(perfil1.get_usuario(), 'novo_usuario')

class PessoaFisicaTest(unittest.TestCase):
    def teste_init(self):
        pessoa = PessoaFisica('usuario1', '123')
        self.assertEqual(pessoa.get_usuario(), 'usuario1')
        self.assertEqual(pessoa.get_cpf(), '123')
        self.assertTrue(pessoa.is_ativo())

    def test_get_cpf(self):
        # Cria uma pessoa física com um CPF específico
        pessoa = PessoaFisica('usuario2', '987')

        # Verifica se o método get_cpf retorna o CPF correto
        self.assertEqual(pessoa.get_cpf(), '987')

    def test_add_seguidor(self):
        # Testa o método de adicionar seguidores, que vem da classe base Perfil
        pessoa1 = PessoaFisica('usuario1', '123')
        pessoa2 = PessoaFisica('usuario2', '987')

        pessoa1.add_seguidor(pessoa2)

        # Verifica se o perfil2 foi adicionado à lista de seguidores do perfil1
        self.assertIn(pessoa2, pessoa1.get_seguidores())

    def test_add_tweet(self):
        # Testa a adição de tweets na classe base Perfil
        pessoa1 = PessoaFisica('usuario1', '123.456.789-00')
        tweet = Tweet(1, 'Teste de tweet', '2025-02-20 12:00:00')

        pessoa1.add_tweet(tweet)

        # Verifica se o tweet foi adicionado à lista de tweets de pessoa1
        self.assertIn(tweet, pessoa1.get_tweets())

class TestPessoaJuridica(unittest.TestCase):

    def test_init(self):
        # Cria uma pessoa jurídica com o usuário e CNPJ
        pessoa = PessoaJuridica('usuarioPJ', '12')

        # Verifica se o nome de usuário foi corretamente atribuído
        self.assertEqual(pessoa.get_usuario(), 'usuarioPJ')
        # Verifica se o CNPJ foi corretamente atribuído
        self.assertEqual(pessoa.get_cnpj(), '12')
        # Verifica se o perfil está ativo
        self.assertTrue(pessoa.is_ativo())

    def test_get_cnpj(self):
        # Cria uma pessoa jurídica com um CNPJ específico
        pessoa = PessoaJuridica('usuarioPJ', '98')

        # Verifica se o método get_cnpj retorna o CNPJ correto
        self.assertEqual(pessoa.get_cnpj(), '98')

    def test_add_seguidor(self):
        # Testa o método de adicionar seguidores, que vem da classe base Perfil
        pessoa1 = PessoaJuridica('usuarioPJ1', '12')
        pessoa2 = PessoaJuridica('usuarioPJ2', '23')

        pessoa1.add_seguidor(pessoa2)

        # Verifica se o perfil2 foi adicionado à lista de seguidores do perfil1
        self.assertIn(pessoa2, pessoa1.get_seguidores())

    def test_add_tweet(self):
        # Testa a adição de tweets na classe base Perfil
        pessoa1 = PessoaJuridica('usuarioPJ', '12')
        tweet = Tweet(1, 'Tweet da pessoa jurídica', '2025-02-20 12:00:00')

        pessoa1.add_tweet(tweet)

        # Verifica se o tweet foi adicionado à lista de tweets de pessoa1
        self.assertIn(tweet, pessoa1.get_tweets())


if __name__ == '__main__':
    unittest.main()