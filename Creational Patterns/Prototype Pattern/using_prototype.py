from game_object import GameObject

zombie_prototype = GameObject("Zombie", 100, 10, (0,0))

# Spawn new Zombies
zombie1 = zombie_prototype.clone()
zombie1.position = (5, 10)

zombie2 = zombie_prototype.clone()
zombie2.position = (-5, 10)

print(zombie_prototype)
print(zombie1)
print(zombie2)

