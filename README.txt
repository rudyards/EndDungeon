Programmers: Piper Summers, Rhody Kaner

Features:
Random World (3 Points) (Piper)
Made the dungeon randomly place additional rooms that pop up around it when the game starts. Those rooms have a chance of being interconnected. Each room is also randomly assigned a description and name. Names are unique, descriptions are not.

Complex Rooms (3 Points) (Piper)
Limited implementation but two rooms, Monster Den and Old Armory, have things that are different about them due to their names.While they still use the same Room class, all rooms named Old Armory start with a broken sword in them, and all rooms named Monster Den have a 3x higher rate of spawning monsters.

Bigger World (2 Points) (Piper)
The world is by default 10 rooms large, and on average is 14 rooms large (due to 50/50 chance of randomly spawning additional rooms with a total of 8 bonus rooms).

Victory Condition (2 points) (Rhody)
The last room in the dungeon contains a final boss, a dragon which, when you kill it, gives you loot and then prints a victory screen.

More Monsters (3 Points) (Piper)
This dungeon is filled with 4 types of monsters: Trolls which regenerate while you fight them, Giant Rats, Velociraptors that move up to two rooms at a time, and Giant Spiders, which poison players when they bite them.

Auto-generating monsters (2 points) (Rhody)
Each room in the dungeon has a chance of spawning a monster each time it is updated. The more rooms, the more monsters on average spawn each turn.
-Bonus (Piper): Each monster that spawns has a random name, and a random level. Higher level monsters are stronger but give more loot. It’s more common for monsters to spawn at low levels and increasingly unlikely for them to spawn at higher ones.

Loot (3 Points) (Piper)
Whenever a monster is killed, in addition to dropping gold and xp, they have a chance of dropping a random item out of the list of items in the game.

Currency (4 Points) (Rhody)
Players can acquire gold by selling items to Characters and spend it by buying items from them.

Characters (4 Points) (Rhody)
There are two types of characters: Merchants and Blacksmiths. Both of them behave functionally the same, in that they both have a list of items in their inventory to sell, but they have different starting inventories. You can talk to them, which gives you information on how to further interact with them, view their inventory, or buy and sell items to them.

Leveling Up (4 Points) (Piper)
In addition to gold and items, killing monsters gives you xp. If you collect sufficient xp, 250 per level you currently are, then you level up! Leveling up increases your stats randomly, either of them by +0 or +1.

Player Attributes (3 Points) (Piper)
Players have 6 stats, which randomly start as -1, 0, or +1. These stats are Strength, Constitution, Dexterity, Intelligence, Wisdom, Charisma. Strength increases your damage, Constitution increases your health, Dex increases your defense,Intelligence increases your xp gain, Wisdom and Charisma increase nothing, since we didn’t get around to implementing features for them.

Inventory Maximum Size (2 Points) (Piper)
Players can only carry a certain number of items, but that is increased by their strength. Players have to drop items in order to pick additional ones up.

Drop (1 point) (Piper)
Players can drop any item that they have in their inventory. If they have an item equipped, they have to unequal it first.

Stacking Items (2 points) (Rhody)
If you pick up multiple items with the same name, they stack up in <name> x2 pattern. One of items are displayed as <name> x1

Weapons (2 points) (Piper)
Players can find weapons and equip them to fight monsters. Weapons increase the players damage by a set value based on the weapon.

Armor (2 points) (Piper)
Players can also find armor. Armor reduces the damage the player takes overtime they are attacked.

Healing Items (2 points) (Rhody)
Players can also find a Healing Potion which they can consume using the heal command. That restores 15 HP to them.

Regeneration (2 Points) (Piper)
Players get 1 point of regeneration per 5 points of constitution they have. This is very unlikely, but technically possible. Once they have that, they’ll regenerate 1 each time they update.

Wait (1 Point) (Piper)
Player can wait 1 turn by typing wait in order to pass the current turn, allowing more monsters to spawn, events to occur, regeneration to happen, and monsters to move.

Events (3 Points) (Rhody)
Every turn, there’s a chance a random event will happen in the player’s room. You might trip over a rock, or encounter a healing mist, or a swarm of radioactive bees.

Me (2 Points) (Piper)
The me command displays the players current stats, health, xp, and gp.

Inspect (2 points) (Rhody)
Players can inspect items in their room or inventory to display the item description.

Command Abbreviations (3 Points) (Rhody)
Players can type any letter(s) that is the first letter(s) of a command in order to do that command. If that abbreviation describes two commands, it’ll ask the players to differentiate between them.

Saving the Game (Rhody)
BONUS: Players can save their game and choose to resume it when they boot up the game. 