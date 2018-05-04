import discord
import asyncio
import btid

VERMELHO = 0x86080E
TOKEN = btid.seu_token()
msg_id = None
msg_user = None


client = discord.Client()

@client.event
async def on_ready():
    print('BOT ONLINE - Olá MUNDO!')
    print(client.user.name)
    print(client.user.id)
    print('--------PR--------')

@client.event
async def on_member_join(member):
 canal = client.get_channel("441620373914517504")
 regras = client.get_channel("441620558849769472")
 msg = "Seja bem-vindo, {} , leia as {}".format(member.mention, regras.mention)
 await client.send_message(canal, msg)

@client.event
async def on_message(message):
    if message.content.lower().startswith("!cargos"):
        embed =discord.Embed(
            title = "Escolha seu cargo!",
            color = VERMELHO,
            description = "- Sniper = 🗡\n"
                          "- Fuzileiro = ⚔\n"
                          "- SMG = ⚙\n"
                          "- Suporte = 🛡",
        )
        botmsg = await client.send_message(message.channel,embed=embed)
        await client.add_reaction(botmsg, "🗡")
        await client.add_reaction(botmsg, "⚔")
        await client.add_reaction(botmsg, "⚙")
        await client.add_reaction(botmsg, "🛡")

    global msg_id
    msg_id = botmsg.id
    global msg_user
    msg_user = message.author



@client.event
async def on_reaction_add(reaction, user):
    msg = reaction.message
    if reaction.emoji == "🗡" and msg.id == msg_id and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Sniper", msg.server.roles)
        await client.add_roles(user, role)
    if reaction.emoji == "⚔" and msg.id == msg_id and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Fuzileiro", msg.server.roles)
        await client.add_roles(user, role)
    if reaction.emoji == "⚙" and msg.id == msg_id and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "SMG", msg.server.roles)
        await client.add_roles(user, role)
    if reaction.emoji == "🛡" and msg.id == msg_id and user == msg_user:
        role = discord.utils.find(lambda r: r.name == "Suporte", msg.server.roles)
        await client.add_roles(user, role)

@client.event
async def on_reaction_remove(reaction, user):
    msg = reaction.message
    if reaction.emoji == "🗡" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Sniper", msg.server.roles)
        await client.remove_roles(user, role)
    if reaction.emoji == "⚔" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Fuzileiro", msg.server.roles)
        await client.remove_roles(user, role)
    if reaction.emoji == "⚙" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "SMG", msg.server.roles)
        await client.remove_roles(user, role)
    if reaction.emoji == "🛡" and msg.id == msg_id:
        role = discord.utils.find(lambda r: r.name == "Suporte", msg.server.roles)
        await client.remove_roles(user, role)



client.run(TOKEN)
