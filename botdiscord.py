import discord
from discord.ext import commands


    #Clientes
client = discord.Client()
client = commands.Bot(command_prefix="!")
client.remove_command('help')

    #Inicialização
@client.event
async def on_ready():
    print("-----Crommos-----")
    print('Bot Ligado!')


    #Comandos
@client.command()
async def info(ctx):
    await ctx.send("""Olá Garotinho(a)
    Meu nome é BotCrommos!
    Nome do meu pai é Sr.CrommosBR
    Tenho Exatamente todo tempo livre para lhe Atender!""")

@client.command()
async def comandos(ctx):
    embed = discord.Embed(title='COMANDOS',description='!info  **Para ver As Informações do BOT**\n!valor  **Valor de CORP&GANG**\n!ip  **Pegar o IP do nosso Servidor**', colour=0xf76200)
    await ctx.send(embed=embed)


@client.command()
async def valor(ctx):
    embed = discord.Embed(title='PREÇOS CORPS&GANGS', description='CORPORAÇÃO : 1 SKIN, 1 VTR, 1 BASE = 15R$\n'
    'GANG : 1 SKIN, 1 VTR, 1 BASE = 10R$\n'
    '\n**NO NOSSO SERVIDOR HÁ APENAS 2 CORPS&GANG GRATIS, FAVOR FALE COM O PRESIDENTE!**', colour=0xf76200)
    await ctx.send(embed=embed)

@client.command()
async def limpar(ctx, amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send("Chat Limpo!")

@client.command()
async def ip(ctx):
    embed = discord.Embed(title='CHROMA', description=':heavy_multiplication_x: Ok, IP do Nosso Servidor [CHROMARP] : mtasa://149.56.176.161:22853 :heavy_multiplication_x:',colour=0xc10000)
    await ctx.send(embed=embed)













@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Qual Membro deseja kickar ?")
        return
    await member.kick()
    await ctx.send(f"{member.mention} Kikado")
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Não foi kikado!")
 
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member = None):
    if not member:
        await ctx.send("Qual Membro deseja banir ?")
        return
    await member.ban()
    await ctx.send(f"{member.mention} Banido!")
@ban.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Não foi banido")
 
@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Qual Membro deseja mutar")
        return
    await member.mute()
    await ctx.send(f"{member.mention} Banido!")
@mute.error
async def mute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Não foi mutado!")
 
 
@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx, member: discord.Member=None):
    if not member:
        await ctx.send("Qual Membro deseja Mutar")
        return
    role = discord.utils.get(ctx.guild.roles, name="Unmute")
    await member.remove_roles(role)
@mute.error
async def unmute_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        await ctx.send("Não foi desmutado")







client.run('NTUyMjUzNTkxMTAxMTEyMzMw.XOU-wg.-HVHftL77StmJhaWXizubhu294o')

