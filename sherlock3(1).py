import telebot, requests, re, json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

privado = [779455996,1625562699]

grupos = [-1001558388459,-1001443222542]

EXCEPT = []

NETIN = [] # OFF

bot = telebot.TeleBot("2008119402:AAEuHtFOcircHprGAYGF1c30WcDenMyFYaY")

def back_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("Voltar", callback_data="back"))
    return markup 

@bot.message_handler(commands=['cnpj'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = privado + grupos + NETIN + EXCEPT + [-1001414552721,-1001278553553,-1001588604830]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>consultando...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split('/cnpj')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://www.receitaws.com.br/v1/cnpj/' + ip)
                    req = url.json()
                    response = f'🔍 <b>CONSULTA DE CNPJ</b> 🔍\n\n<b>• CNPJ</b>: <code>{req["cnpj"]}</code>\n<b>• MATRIZ</b>: <code>{req["tipo"]}</code>\n\n<b>• ABERTURA</b>: <code>{req["abertura"]}</code>\n\n<b>• NOME</b>: <code>{req["nome"]}</code>\n\n<b>• NOME DA FANTASIA</b>: <code>{req["fantasia"]}</code>\n<b>• PORTE</b>: <code>{req["porte"]}</code>\n\n<b>• ATIVIDADE PRINCIPAL</b>: <code>{req["atividade_principal"]}</code>\n\n<b>• ATIVIDADES SEGUNDARIAS</b>: <code>{req["atividades_secundarias"]}</code>\n\n<b>• CÓDIGO NATUREZA JUDICIÁRIAS</b>: <code>{req["natureza_juridica"]}</code>\n\n<b>• QUEDRO DE SÓCIOS E ADMINISTRADORES</b>: <code>{req["nome"]}</code>\n\n<b>• LOGRADOURO</b>: <code>{req["logradouro"]}</code>\n<b>• NÚMERO</b>: <code>{req["numero"]}</code>\n<b>• COMPLEMENTO</b>: <code>{req["complemento"]}</code>\n\n<b>• CEP</b>: <code>{req["cep"]}</code>\n<b>• BAIRRO</b>: <code>{req["bairro"]}</code>\n<b>• MUNICÍPIO</b>: <code>{req["municipio"]}</code>\n<b>• ESTADO</b>: <code>{req["uf"]}</code>\n\n<b>• TELEFONE</b>: <code>{req["telefone"]}</code>\n<b>• EMAIL</b>: <code>{req["email"]}</code>\n\n<b>• By</b>: @Bernadar_robot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CNPJ NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''VOCE NÄO TEM PERMISSÃO''', parse_mode='html')




@bot.message_handler(commands=['vizinhos'])
def byti(men):
            chtid = men.chat.id
            permitidos = privado + grupos + EXCEPT + NETIN + [-1001414552721,-1001278553553,-1001588604830]
            if int(chtid) in permitidos:
                if men.text == '/vizinhos':
                    bot.reply_to(men, 'VIZINHOS Checker - Consulta de VIZINHOS, obtém os nomes dos vizinhos do portador do número de CPF.' + '\n\n' + 'Formato' + '\n' + '27867260854' + '\n' + 'ou' + '\n' + '278.672.608-54' + '\n\n' + '/vizinhos 27867260854')

                else:
                    header = {'Host': 'tudosobretodos.info', 'cache-control': 'max-age=0',
                              'upgrade-insecure-requests': '1', 'save-data': 'on',
                              'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36',
                              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                              'sec-fetch-site': 'cross-site', 'sec-fetch-mode': 'navigate',
                              'sec-fetch-user': '?1',
                              'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br',
                              'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                              'cookie': '__cfduid=dc3ac236c5f39888dbd7f585eedf6feb11596724421',
                              'cookie': '_ga=GA1.2.971515152.1596724424',
                              'cookie': '_gid=GA1.2.109978583.1596724424'}
                    num = re.sub('[^0-9]', '', men.text)
                    envia = requests.get("https://tudosobretodos.info/{}".format(num), headers=header).text

                    if "itemMoradores" in envia:
                        try:
                            bot.reply_to(men, '<code>consultando...</code>', parse_mode='html')

                            viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                                   str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40]) + '\n' + \
                                   str(envia.split("<div class='itemMoradores'>")[3].split("<")[0][3:40]) + '\n' + str(envia.split("<div class='itemMoradores'>")[4].split("<")[0][3:40]) +'\n'+ \
                                   str(envia.split("<div class='itemMoradores'>")[5].split("<")[0][3:40])

                            bot.reply_to(men, '<b>' '🔍CONSULTA DE VIZINHOS 🔍' '</b>' + '\n\n' + '<b>' '• VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' '• By: @Bernadar_robot' '</b>' , parse_mode='html')
                        except:
                            try:
                                viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                                       str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40])

                                bot.reply_to(men,
                                             '<b>' '🔍CONSULTA DE VIZINHOS 🔍' '</b>' + '\n\n' + '<b>' '• VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' '• By: @Bernadar_robot' '</b>',
                                             parse_mode='html')
                            except:
                                bot.reply_to(men, '<b>⚠️VIZINHOS NÃO ENCONTRADO!⚠️</b>', parse_mode='HTML')



                    else:
                        bot.reply_to(men, '<b>⚠️VIZINHOS NÃO ENCONTRADO!⚠️</b>️', parse_mode='html')

            else:
                bot.reply_to(men, '''SEM PERMISSÃO
━━━━━━━━━━━━━━━━━''', parse_mode='html')

@bot.message_handler(commands=['placa2'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = privado + grupos + NETIN + EXCEPT + [-1001414552721,-1001278553553,-1001588604830, 1270552935]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>consultando...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split(' ')
                    nome2 = str(fl[1:])
                    nome2 = nome2.replace('[', '')
                    nome2 = nome2.replace(']', '')
                    nome2 = nome2.replace("'", "")
                    nome2 = nome2.replace(',', '')
                    print(nome2)
                    url = requests.get('https://netinapi.space/Netinadmtokenfds/Api%20json/placasv2.php?consulta='+ nome2, verify=False)
                    req = url.json()
                    response = f'{req}'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>PLACA2 NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                  bot.reply_to(nome, '''VOCÊ NÃO TEM AUTORIZAÇÃO
                  
<SEM PERMISSÃO
━━━━━━━━━━━━━━━━━''', parse_mode='html')


@bot.message_handler(commands=['nome'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = privado + grupos + NETIN + EXCEPT + [-1001414552721,-1001278553553,-1001588604830, 1270552935]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>consultando...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split(' ')
                    nome2 = str(fl[1:])
                    nome2 = nome2.replace('[', '')
                    nome2 = nome2.replace(']', '')
                    nome2 = nome2.replace("'", "")
                    nome2 = nome2.replace(',', '')
                    print(nome2)
                    url = requests.get('https://netinapi.space/Netinadmtokenfds/Api%20json/nome.php?consulta='+ nome2, verify=False)
                    req = url.json()
                    response = f'{req}'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>NOME NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                  bot.reply_to(nome, '''VOCÊ NÃO TEM AUTORIZAÇÃO
                  
SEM PERMISSÃO
━━━━━━━━━━━━━━━━━''', parse_mode='html')



@bot.message_handler(commands=['cpf1','!cpf'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = privado + grupos + NETIN + EXCEPT + [-1001414552721,-1001278553553,-1001588604830]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>consultando...</code>', parse_mode='HTML')
                    msg = nome.text.replace('cpf1','')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://netinmakerapi.000webhostapp.com/Netinadmtokenfds/Api%20json/Cpf.php?cpf=' + ip)
                    req = url.json()
                    response = f'🔍 <b>CONSULTA DE CPF</b> 🔍\n\n<b>• CPF</b>: <code>{req["retorno"]["CPF"]}</code>\n<b>• NOME</b>: <code>{req["retorno"]["Nome"]}</code>\n\n<b>• SEXO</b>: <code>{req["retorno"]["Sexo"]}</code>\n\n<b>• NASCIMENTO</b>: <code>{req["retorno"]["AnoNascimento"]}</code>\n\n<b>• By</b>: @Bernadar_robot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CPF NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''VOCE NÄO TEM PERMISSÃO''', parse_mode='html')



@bot.message_handler(commands=['cpf2'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = privado + grupos + NETIN + EXCEPT + [-1001414552721,-1001278553553,-1001588604830, 1270552935]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>consultando...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split(' ')
                    nome2 = str(fl[1:])
                    nome2 = nome2.replace('[', '')
                    nome2 = nome2.replace(']', '')
                    nome2 = nome2.replace("'", "")
                    nome2 = nome2.replace(',', '')
                    print(nome2)
                    url = requests.get('http://hospen.tk/Melirolaspeagape/cpf.php?consulta='+ nome2, verify=False)
                    req = url.json()
                    response = f'{req}'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CPF2 NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                  bot.reply_to(nome, '''VOCÊ NÃO TEM AUTORIZAÇÃO
                  
SEM PERMISSÃO
━━━━━━━━━━━━━━━━━''', parse_mode='html')




@bot.message_handler(commands=['cnpj'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = privado + grupos + NETIN + EXCEPT + [-1001414552721,-1001278553553,-1001588604830]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>consultando...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split('/cnpj')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://www.receitaws.com.br/v1/cnpj/' + ip)
                    req = url.json()
                    response = f'🔍 <b>CONSULTA DE CNPJ</b> 🔍\n\n<b>• CNPJ</b>: <code>{req["cnpj"]}</code>\n<b>• MATRIZ</b>: <code>{req["tipo"]}</code>\n\n<b>• ABERTURA</b>: <code>{req["abertura"]}</code>\n\n<b>• NOME</b>: <code>{req["nome"]}</code>\n\n<b>• NOME DA FANTASIA</b>: <code>{req["fantasia"]}</code>\n<b>• PORTE</b>: <code>{req["porte"]}</code>\n\n<b>• ATIVIDADE PRINCIPAL</b>: <code>{req["atividade_principal"]}</code>\n\n<b>• ATIVIDADES SEGUNDARIAS</b>: <code>{req["atividades_secundarias"]}</code>\n\n<b>• CÓDIGO NATUREZA JUDICIÁRIAS</b>: <code>{req["natureza_juridica"]}</code>\n\n<b>• QUEDRO DE SÓCIOS E ADMINISTRADORES</b>: <code>{req["nome"]}</code>\n\n<b>• LOGRADOURO</b>: <code>{req["logradouro"]}</code>\n<b>• NÚMERO</b>: <code>{req["numero"]}</code>\n<b>• COMPLEMENTO</b>: <code>{req["complemento"]}</code>\n\n<b>• CEP</b>: <code>{req["cep"]}</code>\n<b>• BAIRRO</b>: <code>{req["bairro"]}</code>\n<b>• MUNICÍPIO</b>: <code>{req["municipio"]}</code>\n<b>• ESTADO</b>: <code>{req["uf"]}</code>\n\n<b>• TELEFONE</b>: <code>{req["telefone"]}</code>\n<b>• EMAIL</b>: <code>{req["email"]}</code>\n\n<b>• By</b>: @Bernadar_robot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CNPJ NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''VOCE NÄO TEM PERMISSÃO''', parse_mode='html')

def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("➕ADICIONE-ME A UM GRUPO➕", url="https://t.me/bernadar_robot?startgroup=start")
        ,InlineKeyboardButton("🔎BUSCAS🔍", callback_data="cb_yes")
        ,InlineKeyboardButton("📎CHECKERS📎", callback_data="cb_no")
        ,InlineKeyboardButton("🛠GERADORES🛠", callback_data="cb_cnpj")
        ,InlineKeyboardButton("🖱PLANOS🖱", callback_data="cb_nome")
    )
    return markup
    
   


@bot.message_handler(commands=['menu', 'help', 'start'])
def bniio(men):
    notbin = []
    bid = men.chat.id
    mensagem = men.text
    if men.text == '/menuu':
        bot.reply_to(men, '<b>' + '⚠️ ERRADO BURRO ⚠️' + '</b>')
    else:
        try:
         menu = f'olá, <pre>{men.from_user.first_name}</pre>\n<b>VEJA MEUS COMANDOS</b>\n\n<b>ESCOLHA UMA OPIÇÃO:</b>\n\n'
         bot.reply_to(men, menu, reply_markup=gen_markup() ,parse_mode='HTML')
        except:
                    bot.reply_to(men, 'start', reply_markup=gen_markup())


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    
    if call.data == 'back':
        return bot.edit_message_text(
            f'olá, <pre>{call.from_user.first_name}</pre>\n<b>VEJA MEUS COMANDOS</b>\n\n<b>ESCOLHA UMA OPIÇÃO:</b>\n\n', call.message.chat.id, call.message.message_id, 
            reply_markup=gen_markup()
        )

    if call.data == "cb_yes":
        return bot.edit_message_text(
            "🔍BUSCAS🔍\n\n↕ PLACA2: /placa2 abc1234\n↕ NOME: /nome CARINA ALVES MAIESKY\n↕ CPF: /cpf1 34592913892\n↕ CNPJ: /cnpj 27865757000102\n↕ VIZINHOS:/vizinhos 27867260854\n↕ PLACA:/placa ATJ8617\n\n", call.message.chat.id, call.message.message_id, 
            reply_markup=back_markup()
        )
    if call.data == "cb_no":
        return bot.edit_message_text(
            "NENHUM NO MOMENTO", call.message.chat.id, call.message.message_id,
            reply_markup=back_markup()    
        )
    if call.data == "cb_cpf":
        return bot.edit_message_text("CONSULTA CPF /CPF1", call.message.chat.id, call.message.message_id,
            reply_markup=back_markup()
        )
    if call.data == "cb_cnpj":
        return bot.edit_message_text("CONSULTA CNPJ /CNPJ", call.message.chat.id, call.message.message_id,
            reply_markup=back_markup()
        )
    if call.data == "cb_placa":
        return bot.edit_message_text("CONSULTA PLACA /PLACA", call.message.chat.id, call.message.message_id, 
            reply_markup=back_markup()
        )
    if call.data == "cb_nome":
        return bot.edit_message_text("CONSULTA NOME /NOME", call.message.chat.id, call.message.message_id,
            reply_markup=back_markup()
        )
    if call.data == "cb_lgpd":
        bot.answer_callback_query(
            call.id, "ESTAMOS DE ACORDO COM A LEI LGPD VOCÊ É RESPONSAVEL PELO SEU USO")
    if call.data == "cb_cad":
        return bot.edit_message_text("CONSULTA PLACA2 /PLACA2", call.message.chat.id, call.message.message_id, 
            reply_markup=back_markup()
        )
    if call.data == "cb_cpf2":
        return bot.edit_message_text("CONSULTA cpf2 /cpf2", call.message.chat.id, call.message.message_id, 
            reply_markup=back_markup()
        )
        

                                                                                                                                                                                                                                   
@bot.message_handler(commands=['vibbvcffdf'])
def byti(men):
            chtid = men.chat.id
            permitidos = privado + grupos + EXCEPT + NETIN + [-1001414552721,-1001278553553,-1001588604830]
            if int(chtid) in permitidos:
                if men.text == '/vizinhos':
                    bot.reply_to(men, 'VIZINHOS Checker - Consulta de VIZINHOS, obtém os nomes dos vizinhos do portador do número de CPF.' + '\n\n' + 'Formato' + '\n' + '27867260854' + '\n' + 'ou' + '\n' + '278.672.608-54' + '\n\n' + '/vizinhos 27867260854')

                else:
                    header = {'Host': 'tudosobretodos.info', 'cache-control': 'max-age=0',
                              'upgrade-insecure-requests': '1', 'save-data': 'on',
                              'user-agent': 'Mozilla/5.0 (Linux; Android 10; SM-A107M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.111 Mobile Safari/537.36',
                              'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                              'sec-fetch-site': 'cross-site', 'sec-fetch-mode': 'navigate',
                              'sec-fetch-user': '?1',
                              'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br',
                              'accept-language': 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7',
                              'cookie': '__cfduid=dc3ac236c5f39888dbd7f585eedf6feb11596724421',
                              'cookie': '_ga=GA1.2.971515152.1596724424',
                              'cookie': '_gid=GA1.2.109978583.1596724424'}
                    num = re.sub('[^0-9]', '', men.text)
                    envia = requests.get("https://tudosobretodos.info/{}".format(num), headers=header).text

                    if "itemMoradores" in envia:
                        try:
                            bot.reply_to(men, '<code>consultando...</code>', parse_mode='html')

                            viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                                   str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40]) + '\n' + \
                                   str(envia.split("<div class='itemMoradores'>")[3].split("<")[0][3:40]) + '\n' + str(envia.split("<div class='itemMoradores'>")[4].split("<")[0][3:40]) +'\n'+ \
                                   str(envia.split("<div class='itemMoradores'>")[5].split("<")[0][3:40])

                            bot.reply_to(men, '<b>' '🔍CONSULTA DE VIZINHOS 🔍' '</b>' + '\n\n' + '<b>' '• VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' '• By: @Bernadar_robot' '</b>' , parse_mode='html')
                        except:
                            try:
                                viz1 = str(envia.split("<div class='itemMoradores'>")[1].split("<")[0][3:40]) + '\n' + \
                                       str(envia.split("<div class='itemMoradores'>")[2].split("<")[0][3:40])

                                bot.reply_to(men,
                                             '<b>' '🔍CONSULTA DE VIZINHOS 🔍' '</b>' + '\n\n' + '<b>' '• VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' '• By: @Bernadar_robot' '</b>',
                                             parse_mode='html')
                            except:
                                bot.reply_to(men, '<b>⚠️VIZINHOS NÃO ENCONTRADO!⚠️</b>', parse_mode='HTML')



                    else:
                        bot.reply_to(men, '<b>⚠️VIZINHOS NÃO ENCONTRADO!⚠️</b>️', parse_mode='html')

            else:
                bot.reply_to(men, '''SEM PERMISSÃO
━━━━━━━━━━━━━━━━━''', parse_mode='html')




@bot.message_handler(commands=['cpfndn','!cpf'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = privado + grupos + NETIN + EXCEPT + [-1001414552721,-1001278553553,-1001588604830]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>consultando...</code>', parse_mode='HTML')
                    msg = nome.text.replace('cpf1','')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://netinmakerapi.000webhostapp.com/netinadmf/CONSULTA%20CPF1/api.php?cpf=' + ip)
                    req = url.json()
                    response = f'🔍 <b>CONSULTA DE CPF</b> 🔍\n\n<b>• CPF</b>: <code>{req["retorno"]["CPF"]}</code>\n<b>• NOME</b>: <code>{req["retorno"]["Nome"]}</code>\n\n<b>• SEXO</b>: <code>{req["retorno"]["Sexo"]}</code>\n\n<b>• NASCIMENTO</b>: <code>{req["retorno"]["AnoNascimento"]}</code>\n\n<b>• By</b>: @Bernadar_robot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, parse_mode='HTML')

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CPF NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''VOCE NÄO TEM PERMISSÃO''', parse_mode='html')





@bot.message_handler(commands=['placa','placa3','veiculo','placa4'])
def zbsn(nome):
            id1 = nome.chat.id

            ltnome = privado + grupos + EXCEPT + NETIN + [-1001414552721,-1001278553553,-1001588604830]
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split('/placa')
                    ipp = re.sub('[^A-Z]', '', msg)
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get("https://apicarros.com/v1/consulta/" + ipp + ip + "/json", verify=False)
                    req = url.json()
                    response = f'🔍<b>PLACA ENCONTRADA</b>🔍\n\n<b>• PLACA</b>: <code>{req["placa"]}</code>\n<b>• ANO</b>: <code>{req["ano"]}</code>\n<b>• CHASSI</b>: <code>{req["chassi"]}</code>\n<b>• COR</b>: <code>{req["cor"]}</code>\n<b>• DATA</b>: <code>{req["data"]}</code>\n<b>• ALERME</b>: <code>{req["dataAtualizacaoAlarme"]}</code>\n<b>• VEICULO</b>: <code>{req["dataAtualizacaoCaracteristicasVeiculo"]}</code>\n<b>• ROUBO/FURTO</b>: <code>{req["dataAtualizacaoRouboFurto"]}</code>\n<b>• MARCA</b>: <code>{req["marca"]}</code>\n<b>• MODELO</b>: <code>{req["modelo"]}</code>\n<b>• MUNICÍPIO</b>: <code>{req["municipio"]}</code>\n<b>• UF</b>: <code>{req["uf"]}</code>\n<b>• SITUAÇÃO</b>: <code>{req["situacao"]}</code>\n\n<b>• By</b>: @Bernadar_robot'
                    bot.reply_to(nome, response, parse_mode="html")
                except:
                	bot.reply_to(nome, '<b>PLACA NÃO FOI ENCONTRADA</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''VOCÊ NÃO TEM AUTORIZAÇÃO

<SEM PERMISSÃO
━━━━━━━━━━━━━━━━━''', parse_mode='html')   		
bot.polling()
