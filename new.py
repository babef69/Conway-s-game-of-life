import random
size = 20
def create_grid(size):
    grid = [[random.randrange(0, 2) for i in range(size)] for i in range(size)]
             
    return grid
grid =create_grid(size)

def show_grid(grid):
    for ligne in grid:
        print(ligne)


show_grid(grid)    
            
def dead_or_alive(grid):
    new_grid = [[0 for i in range(size)]for i in range(size)]
    for x in range(size):
        for y in range(size):
            alive_neighbors = 0
            
            
            for dx in [-1,0,1]:
                for dy in [-1,0,1]:
                    if dx == 0 and dy == 0:
                        continue
                    if 0 <= x + dx < size and 0 <= y + dy < size and grid[x + dx][y + dy] == 1:
                        alive_neighbors += 1
            
            
            
            if grid[x][y] ==1:
                if alive_neighbors <2 or alive_neighbors > 3:
                    grid[x][y] = 0
                else:
                    grid[x][y] = 1
            else:
                if alive_neighbors ==3:
                    grid[x][y] =1
                else:
                    grid[x][y] = 0       
    return grid
print("Initial Grid:")
show_grid(grid)

new_grid = dead_or_alive(grid)

print("Next Generation:")
show_grid(new_grid)
           



