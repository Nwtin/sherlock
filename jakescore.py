import telebot, requests, re, json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

FULL = [779455996,1625562699,-1001509745317,-1001472038306,-1001558388459,-1001443222542,-1001312766377,-1001588604830]

bot = telebot.TeleBot("5043800716:AAGx5aJcCWq3xmqQmp7HNEOOaeeuCnQ0mB8")

def back_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("⬅Voltar⬅", callback_data="back"))
    return markup 

def back9_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("⬅Voltar⬅", callback_data="back9"))
    return markup 
    
def clear_markup(id):
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("🗑APAGAR🗑", callback_data=f"delete {id}"))
    return markup 
    
def busca_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("BUSCAS", callback_data="testee"))
    markup.add(InlineKeyboardButton("⬅Voltar⬅", callback_data="back"))
    return markup 
    
def veiculo_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("VEICULO", callback_data="veiculoo"))
    markup.add(InlineKeyboardButton("⬅Voltar⬅", callback_data="back"))
    return markup 

def back2_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("⬅Voltar⬅", callback_data="back2"))
    return markup 

def back3_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("⬅Voltar⬅", callback_data="back3"))
    return markup 
    
def fisica_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("fisica", callback_data="fisicaa"))
    return markup 
    
def back4_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("◀VOLTAR◀", callback_data="back4"))
    return markup 
    
def empresa_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("empresa", callback_data="empresaa"))
    return markup 

def back5_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("◀VOLTAR◀", callback_data="back5"))
    return markup 

@bot.message_handler(commands=['cnpj'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL + [-1001414552721,-1001278553553,-1001588604830]
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split('/cnpj')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://www.receitaws.com.br/v1/cnpj/' + ip)
                    req = url.json()
                    response = f'🔍 <b>CONSULTA DE CNPJ</b> 🔍\n\n<b>• CNPJ</b>: <code>{req["cnpj"]}</code>\n<b>• MATRIZ</b>: <code>{req["tipo"]}</code>\n\n<b>• ABERTURA</b>: <code>{req["abertura"]}</code>\n\n<b>• NOME</b>: <code>{req["nome"]}</code>\n\n<b>• NOME DA FANTASIA</b>: <code>{req["fantasia"]}</code>\n<b>• PORTE</b>: <code>{req["porte"]}</code>\n\n<b>• ATIVIDADE PRINCIPAL</b>: <code>{req["atividade_principal"]}</code>\n\n<b>• ATIVIDADES SEGUNDARIAS</b>: <code>{req["atividades_secundarias"]}</code>\n\n<b>• CÓDIGO NATUREZA JUDICIÁRIAS</b>: <code>{req["natureza_juridica"]}</code>\n\n<b>• QUEDRO DE SÓCIOS E ADMINISTRADORES</b>: <code>{req["nome"]}</code>\n\n<b>• LOGRADOURO</b>: <code>{req["logradouro"]}</code>\n<b>• NÚMERO</b>: <code>{req["numero"]}</code>\n<b>• COMPLEMENTO</b>: <code>{req["complemento"]}</code>\n\n<b>• CEP</b>: <code>{req["cep"]}</code>\n<b>• BAIRRO</b>: <code>{req["bairro"]}</code>\n<b>• MUNICÍPIO</b>: <code>{req["municipio"]}</code>\n<b>• ESTADO</b>: <code>{req["uf"]}</code>\n\n<b>• TELEFONE</b>: <code>{req["telefone"]}</code>\n<b>• EMAIL</b>: <code>{req["email"]}</code>\n\n<b>• By</b>: @SHERLOCK_rbot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=clear_markup(nome.from_user.id))

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CNPJ NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''VOCE NÄO TEM PERMISSÃO''', reply_markup=planos_markup())
                		
@bot.message_handler(commands=['pf'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL + [-1001414552721,-1001278553553,-1001588604830]
            if id1 in ltnome:
                try:
                    bot.reply_to(nome, '<code>consultando...</code>', parse_mode='HTML')
                    msg = nome.text
                    fl = msg.split('/cnpj')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('https://netinmakerapi.000webhostapp.com/cpfreceita738teste/Api%20json/Cpf.php?consulta=' + ip)
                    req = url.json()
                    response = f'🔍 <b>CONSULTA DE CPF</b> 🔍\n\n<b>• CNPJ</b>: <code>{req["dataNascimento"]}</code>\n<b>• MATRIZ</b>: <code>{req["id"]}</code>\n\n<b>• ABERTURA</b>: <code>{req["idUnidadeAdministrativa"]}</code>\n\n<b>• NOME</b>: <code>{req["nomeMae"]}</code>\n\n<b>• NOME DA FANTASIA</b>: <code>{req["numeroTituloEleitor"]}</code>\n<b>• PORTE</b>: <code>{req["pessoa"]}</code>\n\n<b>• ATIVIDADES SEGUNDARIAS</b>: <code>{req["dataProcessamento"]}</code>\n\n<b>• CÓDIGO NATUREZA JUDICIÁRIAS</b>: <code>{req["id"]}</code>\n\n<b>• QUEDRO DE SÓCIOS E ADMINISTRADORES</b>: <code>{req["idMunicipioIbge"]}</code>\n\n<b>• LOGRADOURO</b>: <code>{req["nome"]}</code>\n<b>• NÚMERO</b>: <code>{req["nomeBairro"]}</code>\n<b>• COMPLEMENTO</b>: <code>{req["nomeLogradouro"]}</code>\n\n<b>• CEP</b>: <code>{req["nomeMunicipio"]}</code>\n<b>• BAIRRO</b>: <code>{req["numeroCep"]}</code>\n<b>• MUNICÍPIO</b>: <code>{req["numeroDdd"]}</code>\n<b>• ESTADO</b>: <code>{req["numeroLogradouro"]}</code>\n\n<b>• TELEFONE</b>: <code>{req["numeroTelefone"]}</code>\n<b>• EMAIL</b>: <code>{req["siglaUf"]}</code>\n<b>• EMAIL</b>: <code>{req["situacaoRegistroAtivo"]}</code>\n<b>• EMAIL</b>: <code>{req["sexo"]}</code>\n<b>• EMAIL</b>: <code>{req["situacaoEstrangeiro"]}</code>\n<b>• EMAIL</b>: <code>{req["situacaoResidenteExterior"]}</code>\n<b>• EMAIL</b>: <code>{req["tipoSexo"]}</code>\n<b>• EMAIL</b>: <code>{req["tipoSituacaoCPF"]}</code>\n\n<b>• By</b>: @SHERLOCK_rbot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=clear_markup(nome.from_user.id))

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CNPJ NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''VOCE NÄO TEM PERMISSÃO''', reply_markup=planos_markup())


@bot.message_handler(commands=['telefone'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL + [-1001414552721,-1001278553553,-1001588604830]
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split('/cnpj')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('http://143.110.149.76:8888?tim=' + ip)
                    req = url.json()
                    response = f'🔍 CONSULTA DE TELEFONE 🔍\n\n• SEXO : {req["Sexo"]}\n\n• CPF : {req["CPF"]}\n\n • NOME : {req["Nome"]}\n\n • TIPOLGD : {req["Tipolgd"]}\n\n• LOGRADOURO : {req["Logradouro"]}\n\n• NUMERO : {req["Numero"]}\n\n• COMPLEMENTO : {req["Complemento"]}\n\n• BAIRRO : {req["Bairro"]}\n\n• CIDADE : {req["Cidade"]}\n\n• CEP : {req["CEP"]}\n\n•TELEFONE : {req["Telefone"]}\n\n• By: @SHERLOCK_rbot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=clear_markup(nome.from_user.id))

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>TEL NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''VOCE NÄO TEM PERMISSÃO''', reply_markup=planos_markup())
                		


@bot.message_handler(commands=['cpf2'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL + [-1001414552721,-1001278553553,-1001588604830]
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split('/cnpj')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('http://143.110.149.76:8888?timCpf=' + ip)
                    req = url.json()
                    response = f'🔍 CONSULTA DE CPF/CNPJ🔍\n\n• SEXO : {req["Sexo"]}\n\n• CPF : {req["CPF"]}\n\n • NOME : {req["Nome"]}\n\n • TIPOLGD : {req["Tipolgd"]}\n\n• LOGRADOURO : {req["Logradouro"]}\n\n• NUMERO : {req["Numero"]}\n\n• COMPLEMENTO : {req["Complemento"]}\n\n• BAIRRO : {req["Bairro"]}\n\n• CIDADE : {req["Cidade"]}\n\n• CEP : {req["CEP"]}\n\n•TELEFONE : {req["Telefone"]}\n\n• By: @SHERLOCK_rbot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=clear_markup(nome.from_user.id))

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CPF/CNPJ NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''VOCE NÄO TEM PERMISSÃO''', reply_markup=planos_markup())



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

                            bot.reply_to(men, '<b>' '🔍CONSULTA DE VIZINHOS 🔍' '</b>' + '\n\n' + '<b>' '• VIZINHOS: ' '</b>' + '\n\n' + '<code>' + viz1 + '</code>' + '\n\n' + '<b>' '• By: @SHERLOCK_rbot' '</b>' , parse_mode='html')
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

            ltnome = FULL + [-1001414552721,-1001278553553,-1001588604830, 1270552935]
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
                    bot.reply_to(nome, response, reply_markup=clear_markup(nome.from_user.id))

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>PLACA2 NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                  bot.reply_to(nome, '''VOCÊ NÃO TEM AUTORIZAÇÃO
                  
<SEM PERMISSÃO
━━━━━━━━━━━━━━━━━''', reply_markup=planos_markup())

@bot.message_handler(commands=['cpf4'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL + [-1001414552721,-1001278553553,-1001588604830, 1270552935]
            if id1 in ltnome:
                try:
                    msg = nome.text
                    fl = msg.split(' ')
                    nome2 = str(fl[1:])
                    nome2 = nome2.replace('[', '')
                    nome2 = nome2.replace(']', '')
                    nome2 = nome2.replace("'", "")
                    nome2 = nome2.replace(',', '')
                    print(nome2)
                    url = requests.get('http://143.110.149.76/receita/'+ nome2, verify=False)
                    person = url.json()
                    response = dedent(f"""
                    🔍 <b>CPF ENCONTRADO </b>🔍

                    • <b>CPF</b>: <code>{person["id"]}</code>
                    • <b>Nome</b>: <code>{person["pessoa"]["nome"]}</code>
                    • <b>Nome da mãe</b>: <code>{person["nomeMae"]}</code>
                    • <b>Título de eleitor</b>: <code>{person["numeroTituloEleitor"]}</code>
                    • <b>Nascimento</b>: <code>{person["dataNascimento"]}</code>
                    • <b>Sexo</b>: <code>{person["sexo"]}</code>

                    •<b> Contato </b>•

                    • <b>Telefone</b>: <code>{person["pessoa"]["numeroDdd"]} {person["pessoa"]["numeroTelefone"]}</code>

                    •<b> Endereço </b>•

                    • <b>Estado</b>: <code>{person["pessoa"]["siglaUf"]}</code>
                    • <b>Município</b>: <code>{person["pessoa"]["nomeMunicipio"]}</code>
                    • <b>Bairro</b>: <code>{person["pessoa"]["nomeBairro"]}</code>
                    • <b>CEP</b>: <code>{person["pessoa"]["numeroCep"]}</code>
                    • <b>Logradouro</b>: <code>{person["pessoa"]["nomeLogradouro"]}</code>
                    • <b>Nº</b>: <code>{person["pessoa"]["numeroCep"]}</code>
                    """)
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=clear_markup(nome.from_user.id), parse_mode="HTML")

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b> INFORME UM CPF...</b>', parse_mode='html')
            else:
                  bot.reply_to(nome, '''VOCÊ NÃO TEM AUTORIZAÇÃO
                  
<SEM PERMISSÃO
━━━━━━━━━━━━━━━━━''', reply_markup=planos_markup())


@bot.message_handler(commands=['norme'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL + [-1001414552721,-1001278553553,-1001588604830, 1270552935]
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
                    url = requests.get('https://webservice.previnity.com.br/?usuario=webservice@previnity.com.br&senha=WEBSERVICE123&ws=S&tipocons=pnn008&cpfcnpj='+ nome2, verify=False)
                    req = url.xml()
                    response = f'{req}'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=clear_markup(nome.from_user.id))

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>NOME NÃO ENCONTRADO</b>', reply_markup=clear_markup(nome.from_user.id))
            else:
                  bot.reply_to(nome, '''VOCÊ NÃO TEM AUTORIZAÇÃO
                  
SEM PERMISSÃO
━━━━━━━━━━━━━━━━━''', reply_markup=planos_markup())



@bot.message_handler(commands=['cpf1','cpf'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL + [-1001414552721,-1001278553553,-1001588604830]
            if id1 in ltnome:
                try:
                    msg = nome.text.replace('cpf1','')
                    ip = re.sub('[^0-9]', '', msg)
                    url = requests.get('http://nettinn.000webhostapp.com/Consulta.php?cpf=' + ip)
                    req = url.json()
                    response = f'🔍 CONSULTA DE CPF 🔍\n\n🔍 CPF: {req["cpf"]}\n🔍  NOME : {req["nome"]}\n🔍 SEXO : {req["sexo"]}\n🔍 NASCIMENTO : {req["anoNasc"]}\n🔍 VIZINHOS : {req["vizinhos"]}\n\n• By : @SHERLOCK_rbot'
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.send_chat_action(nome.chat.id, 'typing')
                    bot.reply_to(nome, response, reply_markup=clear_markup(nome.from_user.id))

                except Exception as e:
                    print(e)
                    bot.reply_to(nome, '<b>CPF NÃO ENCONTRADO</b>', parse_mode='html')
            else:
                		bot.reply_to(nome, '''VOCE NÄO TEM PERMISSÃO''', reply_markup=planos_markup())
                		
                		









@bot.message_handler(commands=['cnpj'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL + [-1001414552721,-1001278553553,-1001588604830]
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
    markup.add(InlineKeyboardButton("🔍BUSCAS", callback_data="cb_yes")
        ,InlineKeyboardButton("👥CONSULTAS GP", url="https://t.me/consultassss")
    )
    return markup
    
def api_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🗒PLACA🗒", callback_data="cb_apiplaca")
    
        ,InlineKeyboardButton("⬅VOLTAR⬅", callback_data="back")
    )
    return markup
    

    
def gen2_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("🚗VEICULOS🚗", callback_data="cb_veiculo")
        ,InlineKeyboardButton("👥PESSOA FISICA👥", callback_data="cb_fisicaa")
        ,InlineKeyboardButton("📰PESSOA JURITICA📰", callback_data="cb_empresa")
       ,InlineKeyboardButton("⬅voltar⬅", callback_data="back")
    )
    return markup
    
def veiculo_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("🚗PLACA🚗", callback_data="cb_placa")
        ,InlineKeyboardButton("🚙PLACA2🚙", callback_data="cb_placa2")
        ,InlineKeyboardButton("◀VOLTAR◀", callback_data="back3")
    )
    return markup
    
def back2_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("◀VOLTAR◀", callback_data="back2")
    )
    return markup

def fisica_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("👤CPF👤", callback_data="cb_cpf")
        ,InlineKeyboardButton("🗣VIZINHOS🗣", callback_data="cb_vizinhos")
        ,InlineKeyboardButton("📄NOME📄", callback_data="cb_nomee")
        ,InlineKeyboardButton("📲TIM TELEFONE📲", callback_data="cb_tim")
        ,InlineKeyboardButton("👥TIM CPF👥", callback_data="cb_timcpf")
        ,InlineKeyboardButton("◀VOLTAR◀", callback_data="back3")
    )
    return markup
    
def empresa_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("📃CNPJ📃", callback_data="cb_cnpjj")
        ,InlineKeyboardButton("◀VOLTAR◀", callback_data="back3")
    )
    return markup
    
def planos_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(InlineKeyboardButton("♠PLANOS♠", callback_data="cb_nome")
        ,InlineKeyboardButton("👥GRUPO DO BOT👥", url="https://t.me/consultassss")
        ,InlineKeyboardButton("👥GRUPO2 DO BOT👥", url="https://t.me/consultassss2")
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
         menu = f'<a href="https://lojasrevyton.000webhostapp.com/unnamed.jpg"> </a>olá, <pre>{men.from_user.first_name}</pre>!\n<b>Meu nome é @Sherlock_rbot.\n\nESCOLHA UMA OPÇÃO:</b>\n\n'
         bot.reply_to(men, menu, reply_markup=gen_markup() ,parse_mode='HTML')
        except:
                    bot.reply_to(men, 'start', reply_markup=gen_markup())




@bot.callback_query_handler(func=lambda call: 'delete' in call.data)
def delete_handler(call):
    chat_id = call.message.chat.id
    if call.from_user.id == int(call.data.split(' ')[1]):
        try:
            bot.delete_message(chat_id, call.message.message_id)
            bot.delete_message(
                chat_id, call.message.reply_to_message.message_id)
            bot.answer_callback_query(call.id, 'Mensagem deletada')
            return
        except Exception as err:
            print('Erro ao apagar mensagem', err)
            return
    bot.answer_callback_query(call.id, 'Você não tem autorização para isso')
        
        
        
@bot.callback_query_handler(func=lambda call: not "delte" in call.data)
def callback_query(call):
    
    if call.data == 'back':
        return bot.edit_message_text(
            f'✅ MENU DE COMANDOS\n\nEscolha uma das opções a baixo e clique no botão correspondente.', call.message.chat.id, call.message.message_id, 
            reply_markup=gen_markup()
        )
    if call.data == 'back3':
        return bot.edit_message_text(
            f'🔍BASES DISPONIVEIS🔎', call.message.chat.id, call.message.message_id, 
            reply_markup=gen2_markup()
        )
    if call.data == 'back9':
        return bot.edit_message_text(
            f'🔍APIS NB🔍\n\n 🔔PLACA > 50R$ MENSAL\n\n🔔NOME > 60R$\n\n🔔CPF SIMPLES > 55R$\n\nCPF FULL 95R$\n\n\n🔍RETORNANDO EM JSON🔍\n\n\nVEJA OS RETORNOS👇', call.message.chat.id, call.message.message_id, 
            reply_markup=api_markup()
        )
        
        
    if call.data == 'back2':
        return bot.edit_message_text(
            f'🔍BASES DISPONIVEIS🔎', call.message.chat.id, call.message.message_id, 
            reply_markup=veiculo_markup()
        )

    if call.data == 'back4':
        return bot.edit_message_text(
            f'🔍BASES DISPONIVEIS🔎', call.message.chat.id, call.message.message_id, 
            reply_markup=fisica_markup()
        )        
        
    if call.data == 'back5':
        return bot.edit_message_text(
            f'🔍BASES DISPONIVEIS🔎', call.message.chat.id, call.message.message_id, 
            reply_markup=empresa_markup()
        )        
                                
    if call.data == 'testee':
        return bot.edit_message_text(
            f'⛏ESCOLHA UMA OPIÇÃO:', call.message.chat.id, call.message.message_id, 
            reply_markup=busca_markup()
        )
        
    if call.data == 'veiculo':
        return bot.edit_message_text(
            f'⛏ESCOLHA UMA OPIÇÃO:', call.message.chat.id, call.message.message_id, 
            reply_markup=busca_markup()
        )

    if call.data == 'fisica':
        return bot.edit_message_text(
            f'⛏ESCOLHA UMA OPIÇÃO:', call.message.chat.id, call.message.message_id, 
            reply_markup=fisica_markup()
        )
    if call.data == 'empresa':
        return bot.edit_message_text(
            f'⛏ESCOLHA UMA OPIÇÃO:', call.message.chat.id, call.message.message_id, 
            reply_markup=fisica_markup()
        )
        

    if call.data == "cb_yes":
        return bot.edit_message_text(
            "🔍BASES DISPONIVEIS🔎", call.message.chat.id, call.message.message_id, 
            reply_markup=gen2_markup()
        )
    if call.data == "cb_no":
        return bot.edit_message_text(
            "NENHUM NO MOMENTO", call.message.chat.id, call.message.message_id,
            reply_markup=back_markup()    
        )
    if call.data == "cb_veiculo":
        return bot.edit_message_text("escolha:", call.message.chat.id, call.message.message_id,
            reply_markup=veiculo_markup()
        )
    if call.data == "cb_cnpj":
        return bot.edit_message_text("🔍API'S NB🔍\n\n 🔔PLACA > 50R$ MENSAL\n\n🔔NOME > 60R$\n\n🔔CPF SIMPLES > 55R$\nCPF FULL 95R$\n\n\nVEJA OS RETORNOS👇", call.message.chat.id, call.message.message_id,
            reply_markup=api_markup()
        )
    if call.data == "cb_cnpjj":
        return bot.edit_message_text("CONSULTA CNPJ /cnpj 000000000000", call.message.chat.id, call.message.message_id,
            reply_markup=back5_markup()
        )
    if call.data == "cb_empresa":
        return bot.edit_message_text("🔍BASES DISPONIVEIS🔎", call.message.chat.id, call.message.message_id,
            reply_markup=empresa_markup()
        )
    if call.data == "cb_fisicaa":
        return bot.edit_message_text("🔍BASES DISPONIVEIS🔎", call.message.chat.id, call.message.message_id,
            reply_markup=fisica_markup()
        )
    if call.data == "cb_placa":
        return bot.edit_message_text("CONSULTA PLACA /PLACA ABC1234", call.message.chat.id, call.message.message_id, 
            reply_markup=back2_markup()
        )
    if call.data == "cb_apiplaca":
        return bot.edit_message_text("[] placa: CVD1354\n[] ano: 1983\n[] DATA: 2021-11-03 20:36:30.000000\n[] cor: Outros ou Desconhecido\n[] chassi: 5K08SCB019275\n[] municipio: ARARAQUARA\n[] anoModelo: 1983\n[] modelo: MONZA\n[] marca: GM\n[] uf placa: SP\n[] dataAtualizacaoAlarme: 2005-04-28 00:00:00\n[] dataAtualizacaoRouboFurto: 2005-04-28 00:00:00\n[] dataAtualizacaoCaracteristicasVeiculo: 2005-04-28 00:00:00\n[] codigoRetorno: 0\n[] mensagemRetorno: Sem erros.\n[] codigoSituacao: 0\n[] situacao: Sem informaÃ§Ã£o\n[] id: 587372223\n[] data atualiacao: 2000-10-13 00:00:00\n[] chassi: 5K08SCB019275\n[] placa: CVD1354\n[] faturado: Sem informaÃ§Ã£o\n[] ano fabricacao: 1983\n[] municipio: ARARAQUARA\n[] uf: SP\n[] uf placa: SP\n[] modelo: MONZA\n[] marca: GM\n[] segmento: Auto\n[] sub segmento: AU - SEDAN COMPACTO\n[] grupo: MONZA\n[] version: Sem informaÃ§Ã£o\n[] combustivel: Indeterminado\n[] potencia: 0\n[] capacidade carga: 0\n[] nacionalidade: Nacional\n[] linha: 6845326\n[] carroceria: Sem informaÃ§Ã£o\n[] caixa cambio: Sem informaÃ§Ã£o\n[] eixo traseiro dif: Sem informaÃ§Ã£o\n[] terceiro eixo: Sem informaÃ§Ã£o\n[] motor: Sem informaÃ§Ã£o\n[] tipo pessoa: Outros\n[] uf faturado: Sem informaÃ§Ã£o\n[] tipo pessoa: Fisica\n[] ano modelo: 0\n[] tipo veiculo: Nao Identificado\n[] especie veiculo: 0\n[] tipo carroceria: Sem informaÃ§Ã£o\n[] cor: Outros ou Desconhecido\n[] quantidade passageiro: 0\n[] situacao chassi: N\n[] eixos: 0\n[] tipo montagem: 1\n[] tipo doc importadora: 0\n[] ident importadora: Sem informaÃ§Ã£o\n[] di: 0\n[] registro di: Sem informaÃ§Ã£o\n[] unidade local srf: 0000000\n[] ultima atualizacao: 2005-04-28 00:00:00\n[] id: Sem informaÃ§Ã£o\n[] restricao: SEM RESTRICAO\n[] id: Sem informaÃ§Ã£o\n[] restricao: SEM RESTRICAO\n[] id: Sem informaÃ§Ã£o\n[] restricao: SEM RESTRICAO\n[] id: Sem informaÃ§Ã£o\n[] restricao: SEM RESTRICAO\n[] limite restricao trib: Sem informaÃ§Ã£o\n[] cilindradas: 0\n[] cap maxima tracao: 0\n[] peso bruto total: 0\n[] situacao veiculo: S\n[] placa modelo antigo: CVD1354\n[] placa modelo novo: CVD1D54\n[] placa nova: f\n[] renavam: 00377366552", call.message.chat.id, call.message.message_id, 
            reply_markup=back9_markup()
        )
    if call.data == "cb_placa2":
        return bot.edit_message_text("CONSULTA PLACA /PLACA2 ABC1234", call.message.chat.id, call.message.message_id, 
            reply_markup=back2_markup()
        )
    if call.data == "cb_nome":
        return bot.edit_message_text("BOT FREE", call.message.chat.id, call.message.message_id,
            reply_markup=back_markup()
        )
    if call.data == "cb_cpf":
        return bot.edit_message_text("CONSULTA CPF /CPF 00000000353\n\nCONSULTA CPF /CPF1 00000000353", call.message.chat.id, call.message.message_id,
            reply_markup=back4_markup()
        )
    if call.data == "cb_vizinhos":
        return bot.edit_message_text("CONSULTA VIZINHOS /vizinhos 00000000353", call.message.chat.id, call.message.message_id,
            reply_markup=back4_markup()
        )
    if call.data == "cb_timcpf":
        return bot.edit_message_text("CONSULTA CPF /timcpf 00000000353", call.message.chat.id, call.message.message_id,
            reply_markup=back4_markup()
        )
    if call.data == "cb_tim":
        return bot.edit_message_text("CONSULTA TELEFONE /tim 13981266580", call.message.chat.id, call.message.message_id,
            reply_markup=back4_markup()
        )
    if call.data == "cb_nomee":
        return bot.edit_message_text("CONSULTA NOME /NOME LUCIO FELIPE", call.message.chat.id, call.message.message_id,
            reply_markup=back4_markup()
        )
    if call.data == "cb_lgpd":
        bot.answer_callback_query(
            call.id, "ESTAMOS DE ACORDO COM A LEI LGPD VOCÊ É RESPONSAVEL PELO SEU USO")
    if call.data == "cb_fisbbbvca":
        return bot.edit_message_text("🔍BASES DISPONIVEIS🔎", call.message.chat.id, call.message.message_id, 
            reply_markup=fisica_markup()
        )
    if call.data == "cb_fisica":
        return bot.edit_message_text("CONSULTA cpf2 /cpf2", call.message.chat.id, call.message.message_id, 
            reply_markup=fisica_markup()
        )


@bot.message_handler(commands=['nome'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = FULL + [-1001414552721,-1001278553553,-1001588604830, 1270552935]
            if id1 in ltnome:

                bot.reply_to(nome, '<code>CONSULTANDO...</code>', parse_mode='HTML')
                msg = nome.text
                fl = msg.split('/nome')
                ip = re.sub('[^0-9]', '', msg)
                
                msg2 = msg.replace("/nome ","")

                try:
                    url = requests.get(f'http://hardsearch.tk/nome.php?token=buffalobuscas&nome={msg2}').json()

                    if url['status'] != "200":
                        bot.reply_to(nome, "NOME NAO ENCONTRADO")
                        return

                    text = "🔍CONSULTA DE NOME\n"

                    for v in url['pessoas']:
                        text += (f"\n🔍NOME: {v['nome']}")
                        text += (f"\n🔍CPF: {v['cpf']}")
                        text += (f"\n🔍SEXO: {v['sexo']}")
                        text += (f"\n🔍NASCIMENTO: {v['nascimento']}\n")

                    bot.reply_to(nome, text)
                except Exception:
                    bot.reply_to(nome, "NOME NAO ENCONTRADO")

bot.polling()                                                                                                                                                                                                                                   
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

            ltnome = FULL + [-1001414552721,-1001278553553,-1001588604830]
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




@bot.message_handler(commands=['nomee'])
def zn(nome):
            id1 = nome.chat.id

            ltnome = PRIVADO + GRUPO + ANONY + EXCEPT + [-1001414552721,-1001369485386]
            if id1 in ltnome:

                msg = nome.text
                fl = msg.split('/nomee')
                ip = re.sub('[^0-9]', '', msg)
                
                msg2 = msg.replace("/nome ","")

                try:
                    url = requests.get(f'http://hardsearch.tk/nome.php?token=buffalobuscas&nome={msg2}').json()

                    if url['status'] != "200":
                        bot.reply_to(nome, "NOME NAO ENCONTRADO")
                        return

                    text = "CONSULTA DE NOME\n"

                    for v in url['pessoas']:
                        text += (f"\nNOME: {v['nome']}")
                        text += (f"\nCPF: {v['cpf']}")
                        text += (f"\nSEXO: {v['sexo']}")
                        text += (f"\nNASCIMENTO: {v['nascimento']}\n")

                    bot.reply_to(nome, text)
                except Exception:
                    bot.reply_to(nome, "NOME NAO ENCONTRADO")

bot.polling()