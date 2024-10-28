import discord
from discord.ext import commands
import requests
from config import TOKEN, GUILD_ID, FIVEM_SERVER_URL

# Configuración de permisos e inicialización del bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Evento que se dispara cuando el bot está listo
@bot.event
async def on_ready():
    guild = discord.Object(id=GUILD_ID)
    await bot.tree.sync(guild=guild)
    print(f"{bot.user} se ha conectado a Discord y está listo.")
    print(f"Comandos slash sincronizados en el servidor con ID {GUILD_ID}")

# Slash command para obtener el estado del servidor de FiveM
@bot.tree.command(name="estado_servidor", description="Obtiene el estado del servidor de FiveM.")
async def estado_servidor(interaction: discord.Interaction):
    try:
        # Envía una solicitud al servidor de FiveM para verificar su estado
        response = requests.get(f"{FIVEM_SERVER_URL}/info.json")
        if response.status_code == 200:
            server_info = response.json()
            server_name = server_info["vars"]["sv_projectName"]
            online_players = server_info["clients"]
            max_players = server_info["sv_maxclients"]
            
            embed = discord.Embed(title="Estado del Servidor FiveM", color=discord.Color.green())
            embed.add_field(name="Nombre del Servidor", value=server_name, inline=False)
            embed.add_field(name="Jugadores Conectados", value=f"{online_players}/{max_players}", inline=False)
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message("No se pudo conectar al servidor de FiveM.", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"Error al obtener el estado: {e}", ephemeral=True)

# Slash command para obtener la lista de jugadores conectados en el servidor de FiveM
@bot.tree.command(name="jugadores", description="Muestra la lista de jugadores conectados en el servidor de FiveM.")
async def jugadores(interaction: discord.Interaction):
    try:
        # Envía una solicitud al servidor de FiveM para obtener la lista de jugadores
        response = requests.get(f"{FIVEM_SERVER_URL}/players.json")
        if response.status_code == 200:
            players = response.json()
            player_names = [player["name"] for player in players]
            
            if player_names:
                embed = discord.Embed(title="Jugadores Conectados", color=discord.Color.blue())
                embed.add_field(name="Jugadores", value="\n".join(player_names), inline=False)
                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message("No hay jugadores conectados en el servidor.", ephemeral=True)
        else:
            await interaction.response.send_message("No se pudo conectar al servidor de FiveM.", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"Error al obtener la lista de jugadores: {e}", ephemeral=True)

# Slash command para enviar un mensaje de saludo a un jugador específico
@bot.tree.command(name="saludar", description="Envía un mensaje de saludo a un jugador.")
async def saludar(interaction: discord.Interaction, nombre: str):
    await interaction.response.send_message(f"Hola, {nombre}! Bienvenido al servidor de FiveM.")

# Inicia el bot con el token proporcionado en config.py
bot.run(TOKEN)
