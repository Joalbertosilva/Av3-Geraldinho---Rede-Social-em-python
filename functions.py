class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.amigos = {}
        self.interesses = set()
        self.mensagens = [] 

    def adicionar_amigo(self, amigo):
        if amigo not in self.amigos:
            self.amigos[amigo] = "nenhum"
            amigo.amigos[self] = "nenhum"

    def remover_amigo(self, amigo):
        if amigo in self.amigos:
            del self.amigos[amigo]
            del amigo.amigos[self]

    def adicionar_interesse(self, interesse):
        self.interesses.add(interesse)

    def enviar_mensagem(self, amigo, mensagem):
        if amigo in self.amigos:
            amigo.mensagens.append((self.nome, mensagem))
            print(f"Mensagem enviada para {amigo.nome} com sucesso!")
        else:
            print(f"{amigo.nome} não é amigo de {self.nome}, não é possível enviar mensagem.")

class RedeSocial:
    def __init__(self):
        self.usuarios = {}

    def adicionar_usuario(self, nome, interesses):
        if nome not in self.usuarios:
            usuario = Usuario(nome)
            for interesse in interesses:
                usuario.adicionar_interesse(interesse)
            self.usuarios[nome] = usuario
            print(f"Usuário {nome} adicionado com sucesso!")
        else:
            print(f"Usuário {nome} já existe na rede!")

    def remover_usuario(self, nome):
        if nome in self.usuarios:
            usuario_a_remover = self.usuarios[nome]
            for amigo in list(usuario_a_remover.amigos.keys()):
                usuario_a_remover.remover_amigo(amigo)
            del self.usuarios[nome]
            print(f"Usuário {nome} removido com sucesso!")
        else:
            print(f"Usuário {nome} não encontrado na rede!")

    def adicionar_amizade(self, usuario1, usuario2):
        if usuario1 in self.usuarios and usuario2 in self.usuarios:
            self.usuarios[usuario1].adicionar_amigo(self.usuarios[usuario2])
            print(f"Amizade entre {usuario1} e {usuario2} adicionada com sucesso!")
        else:
            print(f"Um ou ambos os usuários não encontrados na rede!")

    def remover_amizade(self, usuario1, usuario2):
        if usuario1 in self.usuarios and usuario2 in self.usuarios:
            if self.usuarios[usuario2] in self.usuarios[usuario1].amigos:
                self.usuarios[usuario1].remover_amigo(self.usuarios[usuario2])
                print(f"Amizade entre {usuario1} e {usuario2} removida com sucesso!")
            else:
                print(f"Amizade entre {usuario1} e {usuario2} não encontrada!")
        else:
            print(f"Um ou ambos os usuários não encontrados na rede!")

    def visualizar_rede(self):
        print("Rede Social:")
        for usuario in self.usuarios.values():
            print(f"{usuario.nome}:")
            for amigo, sentimento in usuario.amigos.items():
                print(f"  Amigo: {amigo.nome}, Sentimento: {sentimento}")

    def enviar_mensagem(self, usuario1, usuario2, mensagem):
        if usuario1 in self.usuarios and usuario2 in self.usuarios:
            self.usuarios[usuario1].enviar_mensagem(self.usuarios[usuario2], mensagem)
        else:
            print(f"Um ou ambos os usuários não encontrados na rede!")

    def buscar_usuario(self, nome):
        if nome in self.usuarios:
            usuario = self.usuarios[nome]
            print(f"Usuário {nome} encontrado!")
            print(f"Amigos: {', '.join([amigo.nome for amigo in usuario.amigos])}")
            print(f"Interesses: {', '.join(usuario.interesses)}")
            print("Mensagens:")
            for i, (remetente, mensagem) in enumerate(usuario.mensagens, 1):
                print(f"{i}. De {remetente}: {mensagem}")
            if usuario.mensagens:
                escolha = input("Deseja responder alguma mensagem? (s/n): ")
                if escolha.lower() == 's':
                    indice = int(input("Digite o número da mensagem que deseja responder: ")) - 1
                    if 0 <= indice < len(usuario.mensagens):
                        remetente = usuario.mensagens[indice][0]
                        resposta = input("Digite sua resposta: ")
                        self.usuarios[nome].enviar_mensagem(self.usuarios[remetente], resposta)
                    else:
                        print("Número de mensagem inválido.")
        else:
            print(f"Usuário {nome} não encontrado na rede!")

    def sentimentos(self):
        print("Análise de sentimentos:")
        amizades = []
        for usuario in self.usuarios.values():
            for amigo in usuario.amigos:
                if usuario.nome < amigo.nome:  # Avoid duplicating the pair
                    amizades.append((usuario.nome, amigo.nome))
        
        print("Amizades existentes:")
        for i, (usuario1, usuario2) in enumerate(amizades):
            print(f"{i + 1}. {usuario1} e {usuario2}")
        
        escolha = int(input("Escolha o número da amizade para alterar o sentimento: ")) - 1
        if 0 <= escolha < len(amizades):
            usuario1, usuario2 = amizades[escolha]
            sentimento = input(f"Digite o sentimento da interação entre {usuario1} e {usuario2}: ")
            self.usuarios[usuario1].amigos[self.usuarios[usuario2]] = sentimento
            self.usuarios[usuario2].amigos[self.usuarios[usuario1]] = sentimento
            print(f"Sentimento entre {usuario1} e {usuario2} atualizado com sucesso!")
        else:
            print("Escolha inválida!")
        
        self.visualizar_rede()

    def centralidade(self):
        print("Cálculo de centralidade:")
        for usuario in self.usuarios.values():
            print(f"{usuario.nome}:")
            centralidade = len(usuario.amigos)
            print(f"  Centralidade: {centralidade}")

    def comunidades(self):
        print("Identificação de comunidades por interesses:")
        interesses_map = {}

        for usuario in self.usuarios.values():
            for interesse in usuario.interesses:
                if interesse not in interesses_map:
                    interesses_map[interesse] = set()
                interesses_map[interesse].add(usuario)

        for interesse, usuarios in interesses_map.items():
            print(f"Interesse '{interesse}': {', '.join([u.nome for u in usuarios])}")


    
