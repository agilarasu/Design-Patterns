from game_object import GameObject, GameObjectRegistry

registry = GameObjectRegistry()

zombie_prototype = GameObject("zombie", 100, 10, (0, 0))
registry.register("zombie", zombie_prototype)

ally_prototype = GameObject("ally", 100, 50, (0, 0))
registry.register("ally", ally_prototype)


# Spawn New Zombies
z1 = registry.clone("zombie", position=(10, 5))
z2 = registry.clone("zombie", name="Fast Zombie", attack=20, position=(20, 5))

# Spawn New Allies
a1 = registry.clone("ally", position=(15, 5))
a2 = registry.clone("ally", name="Gun Man", attack=70, position=(25, 5))


print(z1)
print(z2)
print(a1)
print(a2)