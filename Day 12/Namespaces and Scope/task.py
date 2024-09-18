enemies = 1

def outer_wall_maria():
    def increase_enemies():
        enemies = 2
        print(f"enemies inside function: {enemies}")
    increase_enemies()
    print(f"enemies middle function: {enemies}")
    
outer_wall_maria()

print(f"enemies outside function: {enemies}")
