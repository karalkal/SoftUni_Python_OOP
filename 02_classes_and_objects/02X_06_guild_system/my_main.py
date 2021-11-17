from project.player import Player
from project.guild import Guild

player = Player("George", 50, 100)
player2 = Player("Ivan", 40, 110)

print(player.add_skill("Shield Break", 20))
print(player2.add_skill("Whatever", 21))
print()
print(player.player_info())
print()
print(player2.player_info())
print()

guild = Guild("UGT")
guild2 = Guild("Lokomotiv")

print(guild.assign_player(player))
print(guild.assign_player(player))
print(guild2.assign_player(player2))
print(guild.assign_player(player2))
print()

print(player.player_info())
print()
print(player2.player_info())
print()

print(guild2.kick_player("Bay Huy"))
print(guild2.kick_player("Ivan"))
print(player2.player_info())  # guy is now unaffiliated
print()

print(guild.assign_player(player2))  # and is now affiliated to the other team
print()
print(guild.guild_info())
print()

player3 = Player("Nick Cave", 40, 110)
print(guild2.assign_player(player3))
print(guild2.assign_player(player3))
print(guild.assign_player(player3))

print(guild2.guild_info())

print()  # original test input follows
print()
player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())

print()  # another test input
player88 = Player("Pesho", 90, 90)
print(player88.add_skill("A", 3))
print(player88.add_skill("A", 3))
print(player88.player_info())

guild101 = Guild("GGXrd")
print(guild101.guild_info())
print(guild101.assign_player(player88))
print(guild101.assign_player(player88))


