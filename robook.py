import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ChatMemberUpdated
import random

API_KEY = "CENSURADA POR RAZÕES DE SEGURANÇA"

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['apresentacao'])
def hello(message):
    bot.send_message(message.chat.id, '''Olá, eu me chamo Robook e sonho em ser ser um robô que ajude vários clubes do livro 🤖📚
    ❓ Eu tenho uma lista de comandos que podem ser acessados usando /ajuda (ou /help)
''')

@bot.message_handler(commands=['help', 'ajuda'])
def help(message):
  bot.send_message(message.chat.id, '''/ajuda ou /help - mensagem de ajuda com listagem de comandos
/apresentacao - permite que eu me apresenta e fale um pouco sobre minhas funcionalidades
/curiosidade - te contarei uma curiosidade aleatória da minha lista, infelizmente talvez repetida :(
/sorteio - eu posso sortear elementos de uma lista montada pelos membros do grupo
/sorteiaelimina - eu além de sortear já retiro esse elemento da lista
/pesquisa - eu posso criar uma pesquisa com opções dadas por membros do grupo
/escolha - eu posso escolher entre uma lista de coisas separadas entre virgula:
    exemplo: /escolha desventuras em série, Sherlock Holmes, It: a coisa
/lista - eu posso mostrar para você como está a lista
/tema - permite que eu crie uma mensagem interativa para acompanhar o progresso da leitura dos membros, se eu for adm eu posso até mesmo fixá-la.

Elementos podem ser adicionados à lista usando o comando /opcao, exemplos:
    /opcao Coraline
    /opcao E não sobrou nenhum
Essa lista pode ser limpa (zerada) usando o comando /limpa
''')

curiosidades = [
    #Sobre livros
    'A Índia é o país que mais lê no mundo, registrando uma média de 10 horas semanais para cada leitor.',
    '“Bibliosmia” é o nome dado ao prazer em que as pessoas sentem ao cheirar livros antigos.',
    'A frase mais longa impressa em um livro vem da obra “Os Miseráveis”, de Victor Hugo, com 823 palavras.',
    'Ler pode ajudar a prevenir doenças como o Alzheimer.',
    'O papel dos livros é feito com polpa de madeira e possui uma grande quantidade de substâncias orgânicas. Quando estas reagem à luz, ao calor e à humildade, libertam compostos orgânicos voláteis, que se traduzem num aroma a baunilha, a amêndoa ou flores, evocando memórias positivas, por isso os humanos gostam tanto do cheiro.',
    'Se a Wikipedia fosse um livro, teria 1133500 páginas, o equivalente a 2267 volumes.',
    'Em alguns países é mais barato comprar uma arma do que um livro.',
    'Até hoje, foram produzidos mais de 400 filmes baseados nas obras de William Shakespeare.',
    'Virginia Woolf, Goethe e Hemingway tinham o hábito de escrever em pé.',
    'Paulo Coelho é o escritor brasileiro que mais vendeu livros. Os números de exemplares ultrapassam 150 milhões.',
    'A caligrafia do escritor Machado de Assis era tão ruim que, às vezes, até ele tinha dificuldade de entender o que escrevia.',    

    #Sobre King
    'A mãe de Stephen King havia sido dada como estéril quando teve ele.',
    'O pai de Stephen King saiu para comprar cigarro e nunca mais voltou.',
    'King presenciou, quando criança, um atropelamento de um amigo, que o inspirou a escrever o conto “o corpo”.',
    'King já teve muitos problemas com drogas e mal se lembra de ter escrito “Cujo”',
    'King escreveu “The Running Man”, um romance de 304 páginas, em apenas dez dias.',
    'King está no Guinness book como o autor vivo com mais adaptações para o cinema.',
    'Carrie foi o primeiro livro publicado por King, graças aos esforços de sua esposa, Tabitha, que resgatou o manuscrito do lixo.',

    #Sobre Agatha
    'Segundo a UNESCO, Agatha Christie é considerada a escritora mais traduzida mundialmente.',
    'Agatha Christie é a autora do livro mais espesso do mundo, com mais de 30cm e 4032 páginas nas quais estão incluídos todos os 12 romances e 20 contos protagonizados por Miss Marple. É o livro mais raro da escritora.',
    'E não sobrou nenhum é o romance policial mais vendido da história e está na lista dos livros mais vendidos de sempre.',
    'O primeiro livro de Agatha Christie veio de um desafio feito pela irmã que dizia que ela incapaz de escrever um romance policial, ele foi rejeitado em 6 editoras.',
    'Agatha Christie tinha algumas manias estranhas, como comer maçãs na banheira, colecionar macacos de pelúcia e nadar no mar mesmo durante tempestades.'

    #Sobre J. K. Rowlling
    'J.K. Rowling, autora de “Harry Potter”, escreveu todos os livros da saga à mão.',
    'A Bíblia Sagrada, O Pequeno Livro Vermelho e a saga Harry Potter são as três obras mais lidas do mundo inteiro.',
    'J. K. Rowling baseou Hermione Granger em si mesma quando era adolescente.',
    'J. K. Rowling demorou 7 anos para lançar Harry Potter',
    'O manuscrito de Harry Potter foi rejeitado 12 vezes',
    'J. K. Rowling foi condecorada com o maior título da Inglaterra: recebeu o título de Oficial da Ordem do Império Britânico em 2000, e anos depois de membro da Ordem de Companheiros de Honra por seus serviços na literatura e filantropia.',
    'Vários dos estudantes de Hogwarts foram baseados em amigos de infância de J. K. Rowling',
    'Potter era o sobrenome de um dos vizinhos de J. K. Rowling com quem ela brincava de bruxos quando criança',
    'Os pais de J.K., Peter John Rowling e Anne Volant, conheceram-se na King’s Cross Station, a mesma onde Harry encontra a plataforma 9 3/4',

    #Sobre Sherlock
    'Nos livros de Sherlock Holmes, o protagonista nunca chega a dizer a célebre frase "Elementar, meu caro Watson".'
]

@bot.message_handler(commands=['curiosidade'])
def manda_curiosidades(message):
    curiosidade = random.choice(curiosidades)
    bot.send_message(message.chat.id, curiosidade)

opcoes = []

@bot.message_handler(commands=['opcao'])
def add_opcao(message):
    option = message.text.replace('/opcao', '')
    if (len(option.replace(' ', '')) == 0):
        bot.reply_to(message, 'Insira uma opção válida.')
    else:
        opcoes.append(option)
        bot.reply_to(message, f'opção "{option}" foi adicionada à lista')

@bot.message_handler(commands=['pesquisa'])
def create_poll(message):
    if(len(opcoes) <= 1):
        bot.reply_to(message, "Opções insuficientes, use o comando /opcao seguido do nome da sua opcao para adicioná-la à lista")
    else:
        msg = message.text
        msg = msg.replace('/pesquisa', '')
        if len(msg.replace(' ', '')) == 0:
            bot.send_poll(message.chat.id, "pesquisa", opcoes)
        else:
            bot.send_poll(message.chat.id, f'{msg}', opcoes)


@bot.message_handler(commands=['limpa'])
def limpa_opcoes(message):
    opcoes.clear()
    bot.reply_to(message, "lista limpa!")

@bot.message_handler(commands=['sorteio'])
def sorteio(message):
    if(len(opcoes) <= 0):
        bot.send_message(message.chat.id, "Opções insuficientes, use o comando /opcao seguido do nome da sua opcao para adicioná-la à lista")
    else:
        opcao = random.choice(opcoes)
        bot.send_message(message.chat.id, f'Parabéns, o resultado do sorteio foi: {opcao}')

@bot.message_handler(commands=['sorteiaelimina'])
def sorteiaelimina(message):
    if(len(opcoes) <= 0):
        bot.send_message(message.chat.id, "Opções insuficientes, use o comando /opcao seguido do nome da sua opcao para adicioná-la à lista")
    else:
        opcao = random.choice(opcoes)
        opcoes.remove(opcao)
        bot.send_message(message.chat.id, f'Parabéns, o resultado do sorteio foi: {opcao}')

@bot.message_handler(commands=['escolha'])
def escolha(message):
    choices = message.text.replace('/escolha', '')
    choices = choices.split(',')
    if(len(choices) <= 0):
        bot.reply_to(message, "Opções insuficientes, se quiser que eu escolha entre opções use como: /escolha a, b, c")
    else:
        c = random.choice(choices)
        bot.reply_to(message, f'Eu escolho: {c}')

@bot.message_handler(commands=['escolha'])
def escolha(message):
    choices = message.text.replace('/escolha', '')
    choices = choices.split(',')
    if(len(choices) <= 0):
        bot.reply_to(message, "Opções insuficientes, se quiser que eu escolha entre opções use como: /escolha a, b, c")
    else:
        c = random.choice(choices)
        bot.reply_to(message, f'Eu escolho: {c}')

@bot.message_handler(commands=['lista'])
def lista(message):
    if(len(opcoes) == 0):
        bot.reply_to(message, 'Lista vazia')
    elif(len(opcoes) == 1):
            bot.reply_to(message, f'{opcoes[0]}')
    else:
        l = ','.join(opcoes[:-1])
        l = f'{l} e {opcoes[-1]}'
        bot.reply_to(message, f'{l}')

@bot.message_handler(commands=["lembrete"])
def lembrete(message):
    msg = message.text
    msg.replace('/lembrete ', '')
    data, hora = msg.split(' - ')

def markup_tema():
    markup = InlineKeyboardMarkup(row_width=3)
    itembtn1 = InlineKeyboardButton(text="🔴 não", callback_data="não comecei")
    itembtn2 = InlineKeyboardButton(text="🟡 lendo", callback_data="estou lendo")
    itembtn3 = InlineKeyboardButton(text="🟢 terminei", callback_data="terminei")
    markup.add(itembtn1, itembtn2, itembtn3)
    return markup

@bot.message_handler(commands=["tema"])
def tema(message):
    if(len(message.text.replace("/tema", "").replace(" ", "")) == 0):
        bot.reply_to(message, "por favor, escreva o nome do tema")
    else:
        msg = message.text
        msg = msg.replace('/tema ', '')
        markup = markup_tema()
        theme_msg = bot.send_message(message.chat.id,
            f'Novo tema: {msg}\nMembros que participam do tema:',
            reply_markup=markup)

        bot_id = theme_msg.from_user.id
        bot_member = bot.get_chat_member(theme_msg.chat.id, bot_id)

        if(bot_member.status == "administrator"):
            bot.pin_chat_message(theme_msg.chat.id, theme_msg.message_id)
        else:
            bot.reply_to(theme_msg, "Não pude fixar a mensagem, precisaria ser administrador para isso")

def replace_state(text, nome, estado):
    t = text.replace(f'\n🔴 {nome}', f'\n{estado} {nome}')
    t = t.replace(f'\n🟡 {nome}', f'\n{estado} {nome}')
    t = t.replace(f'\n🟢 {nome}', f'\n{estado} {nome}')
    return t

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    msg_id = call.message.message_id
    chat_id = call.message.chat.id
    texto = call.message.text
    nome = call.from_user.first_name
    markup = markup_tema()

    if(nome in texto):
        if call.data == "não comecei":
            novo_texto = replace_state(texto, nome,'🔴')
        elif call.data == "estou lendo":
            novo_texto = replace_state(texto, nome, '🟡')
        elif call.data == "terminei":
            novo_texto = replace_state(texto, nome, '🟢')
        if(novo_texto != texto):
            bot.edit_message_text(f'{novo_texto}', chat_id, msg_id, reply_markup=markup)
    else:
        if call.data == "não comecei":
            bot.edit_message_text(f'{texto} \n🔴 {nome}', chat_id, msg_id, reply_markup=markup)
        elif call.data == "estou lendo":
            bot.edit_message_text(f'{texto} \n🟡 {nome}', chat_id, msg_id, reply_markup=markup)
        elif call.data == "terminei":
            bot.edit_message_text(f'{texto} \n🟢 {nome}', chat_id, msg_id, reply_markup=markup)

#Quando o robô for adicionado no grupo
@bot.my_chat_member_handler()
def my_chat_m(message: ChatMemberUpdated):
    old = message.old_chat_member
    new = message.new_chat_member
    if new.status == "member":
        bot.send_message(message.chat.id, '''Olá, sou o novo membro desse grupo!
    Eu me chamo Robook e sonho em ser ser um robô que ajuda vários clubes do livro 🤖📚
    ❓ Eu tenho uma lista de comandos que podem ser acessados usando o comando /ajuda (ou /help)
    Para me chamar basta usar um comando, eles começam com uma barra (/) logo atrás.
''')

bot.polling()