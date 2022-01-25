space_junk = 100
spaceships = 40
aliens = 5
alien_hitchhikers = 30
space_in_spaceship = 5.0
ships_not_piloted = spaceships - aliens
ships_piloted = aliens
average_hitchhikers_per_spaceship = alien_hitchhikers/aliens
total_fleet_capacity = space_in_spaceship * ships_piloted

print("There are ", spaceships, " spaceships available")
print("There are ", aliens, " aliens willing to pick up hitchhikers")
print("There will be", ships_not_piloted, "empty spaceships")
print("We can transport", total_fleet_capacity, "hitchhikers")
print("We have", alien_hitchhikers, "hitchhikers to pick up")
print("We need", average_hitchhikers_per_spaceship, "in each ship")