import discord

# Erstelle ein Discord Client-Objekt mit den notwendigen Intents
client = discord.Client(intents=discord.Intents.members)

# Erstelle ein CommandTree-Objekt, das für die Verwaltung von Befehlen verwendet wird
tree = discord.app_commands.CommandTree(client)


@client.event
async def on_ready():
    # Setze den Status des Bots auf "online" und seine Aktivität auf "Deine Entscheidung"
    activity = discord.Activity(
        type=discord.ActivityType.playing, name='Deine Entscheidung.')
    status = discord.Status.online
    await client.change_presence(activity=activity, status=status)

    # Synchronisiere den CommandTree mit dem Server, dessen ID in der Variable "guild" angegeben ist
    await tree.sync(guild=discord.Object(id="Deine Server ID."))
    print('Eingeloggt als {}#{}'.format(
        client.user.name, client.user.discriminator))


@tree.command()
async def role(interaction, role: discord.Role):
    # Sende eine Nachricht, in der die erwähnte Rolle angezeigt wird
    await interaction.response.send_message('{} wird jedem User im Server ab jetzt vergeben.'.format(role.mention))

    # Zähle die Anzahl der Mitglieder, denen die Rolle hinzugefügt wurde
    count = 0
    for member in client.get_guild(interaction.guild.id).members:
        try:
            # Versuche, die Rolle dem Mitglied hinzuzufügen
            await member.add_roles(role)
            count = count + 1
            print('{} wurde zu {} hinzugefügt.'.format(role.name, member))
        except:
            # Wenn das Hinzufügen der Rolle fehlschlägt, gebe eine entsprechende Nachricht aus
            print('{} konnte nicht zu {} hinzugefügt werden.'.format(
                role.name, member))

    # Sende eine Nachricht, die die Anzahl der Mitglieder anzeigt, denen die Rolle hinzugefügt wurde
    await interaction.channel.send('{} wurde an {} User vergeben.'.format(role.name, count))

# Starte den Bot mit dem angegebenen Token
client.run('DEIN TOKEN')