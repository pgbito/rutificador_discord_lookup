from utils import *
try:
    config = json.loads(open('config.json','r').read())
    config['token']
    if type(config['token']) is int:
        raise KeyError('')
except (FileNotFoundError, KeyError, json.decoder.JSONDecodeError):
    print('Please create a config.json file with a valid "token" attribute set.')
    quit(1)
# refactor
try:
    c = open('config.json','r').read()
    open('config.json','w').write(json.dumps(json.loads(c),indent=4))
except:
    quit(1)

client = discord.Client(intents=discord.Intents.all())
formatos = list()
@client.event

async def on_message(message:discord.Message):
    if message.content.startswith('/formatorutificador'):
        
        content = message.content.replace('/formatorutificador','')

        if content.startswith(' add'):
            def check(author):
             def inner_check(message):
              return message.author == author
             return inner_check
            await message.reply('Por favor enviar el formato a continuacion!')
            msg = await client.wait_for('message', check=check(message.author)) or discord.Message
            if msg.content.__contains__(r'%(direccion)s') and msg.content.__contains__(r'%(comuna)s') and\
                msg.content.__contains__(r'%(nombre)s') and msg.content.__contains__(r'%(rut)s'):
                          formatos.append(msg.content)
                          await msg.add_reaction('✅')
            else:
                await message.reply('Error. no hay un formato valido. ejemplo: \n  ```txt\nMi abuelo siempre decia %(nombre)s %(rut)s%(direccion)s%(comuna)s```''')
            return
       
        if formatos.__len__() ==0:
            await message.reply('Por favor añadir formatos primero con /formatorutificador add')
            return
        isblockcode = content.startswith('```')
        if isblockcode:
            if content.__contains__('```json'):

             content = content.replace('```json','')
             content = content.replace('```','')
        # isjson? 
        try:
           datos = json.loads(content)
        except json.JSONDecodeError:
            await message.reply('Por favor mandar los datos del usuario en json!')
            return
        
        content = (random.choice(formatos) % {
                'rut': datos['RUT'],
                'nombre': datos['Nombre'],
                'direccion': datos['Direcci\u00f3n'],
                'comuna': datos['Ciudad/Comuna']
            })
        
        await message.channel.send(embed=embedify(content,blockcode=True, blockcodeFormat='txt'))
     
client.run(config['token'])  

# if else for del while yield def pass continue break return await async lambda elif raise with and assert class not nonlocal global
# str tuple list dict function
