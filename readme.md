# GiveEveryoneRole

Dies ist ein Discord Bot, der mit der Python Discord API entwickelt wurde. Er verfügt über einen Befehl, der jedem Mitglied einer bestimmten Rolle im Server hinzufügt.

## Funktionsweise

1. Der Bot wird gestartet und verbindet sich mit dem Discord-API-Server.
2. Der Bot setzt seinen Status auf "online" und ändert seine Aktivität auf "Deine Entscheidung".
3. Der Bot synchronisiert das Kommandobaum-Objekt mit dem Server, dessen ID in der Variable "guild" angegeben ist.
4. Wenn der Befehl "role" im Chat eingegeben wird, sendet der Bot eine Nachricht, in der die erwähnte Rolle angezeigt wird.
5. Der Bot fügt dann der Rolle jedes Mitglied im Server hinzu und zählt die Anzahl der hinzugefügten Mit

## Benötigte Bibliotheken

- [discord.py](https://github.com/Rapptz/discord.py)

## Einrichtung

1. Stelle sicher, dass du über eine aktuelle Version von Python 3.5 oder höher verfügst.
2. Installiere die notwendigen Bibliotheken mit dem Befehl `pip install -r requirements.txt`.
3. Erstelle einen Discord-Bot und kopiere den Token, den du von der Discord Developer Portal erhältst.
4. Ersetze `DEIN TOKEN` in der letzten Zeile des Codes durch deinen eigenen Token.
5. Ersetze die Server-ID in der Zeile `await tree.sync(guild=discord.Object(id="Deine Server ID."))` mit der ID deines Servers.
6. Führe den Code mit dem Befehl `python bot.py` aus.

## Verwendung

Um den Bot zu verwenden, tippe einfach `/role @Rolle` in einen Chat-Kanal, wobei `@Rolle` durch die erwünschte Rolle ersetzt werden sollte. Der Bot wird dann jedem Mitglied im Server die Rolle hinzufügen und eine Nachricht senden, die die Anzahl der hinzugefügten Mitglieder anzeigt.
