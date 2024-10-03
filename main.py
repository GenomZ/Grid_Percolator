#!usr/bin/env/python

import random
import numpy
import matplotlib.pyplot as plt


class grid_Percolator:
    def __init__(self, n, probability):
        self.probability = probability
        self.n = n
        self.x = 0
        self.y = 0
        self.path = []
        self.check_percolation = False
        self.flag = True
        digits = self.n*self.n
        obsticles = int((self.n*self.n)*self.probability)

        self.grid = []
        for i in range(obsticles):
            self.grid.append(1)
        while len(self.grid) < digits:
            self.grid.append(0)
        numpy.random.shuffle(self.grid)
        self.grid = numpy.reshape(self.grid, (n,n))
        self.grid = self.grid.tolist()

    def go_back(self):
        # self.path.pop(-1)
        for i in reversed(self.path):
            if i[0] == 0:
                if i[1] == 0:
                    if self.grid[i[0]+1][i[1]] == 0:
                        self.x = i[0]
                        self.y = i[1]
                        self.path.pop(-1)
                        break
                    elif self.grid[i[0]][i[1]+1] == 0 and self.y < self.n:
                        self.x = i[0]
                        self.y = i[1]
                        self.path.pop(-1)
                        break
                    else:
                        if i[0] == 0:
                            self.x = 0
                            self.y = 0
                            break
                elif i[1] == self.n-1:
                    if self.grid[i[0]+1][i[1]] == 0:
                        self.x = i[0]
                        self.y = i[1]
                        self.path.pop(-1)
                        break
                    elif self.grid[i[0]][i[1]-1] == 0 and i[1] >= 0:
                        self.x = i[0]
                        self.y = i[1]
                        self.path.pop(-1)
                        break
                    else:
                        if i[0] == 0:
                            self.x = 0
                            self.y = 0
                            break
                else:
                    if self.grid[i[0]+1][i[1]] == 0:
                        self.x = i[0]
                        self.y = i[1]
                        self.path.pop(-1)
                        break
                    elif self.grid[i[0]][i[1]-1] == 0 and i[1] >= 0:
                        self.x = i[0]
                        self.y = i[1]
                        self.path.pop(-1)
                        break
                    elif self.grid[i[0]][i[1]+1] == 0 and self.y < self.n:
                        self.x = i[0]
                        self.y = i[1]
                        self.path.pop(-1)
                        break
                    else:
                        if i[0] == 0:
                            self.x = 0
                            self.y = 0
                            break
                    self.path.pop(-1)
                    continue
            elif i[1] == 0:
                if self.grid[i[0]+1][i[1]] == 0:
                    self.x = i[0]
                    self.y = i[1]
                    self.path.pop(-1)
                    break
                elif self.grid[i[0]][i[1]+1] == 0 and self.y < self.n:
                    self.x = i[0]
                    self.y = i[1]
                    self.path.pop(-1)
                    break
                elif self.grid[i[0]-1][i[1]] == 0:
                    self.x = i[0]
                    self.y = i[1]
                    self.path.pop(-1)
                    break
                else:
                    if i[0] == 0:
                        self.x = 0
                        self.y = 0
                        break
                    self.path.pop(-1)
                    continue
            elif i[1] == self.n -1:
                if self.grid[i[0]+1][i[1]] == 0:
                    self.x = i[0]
                    self.y = i[1]
                    self.path.pop(-1)
                    break
                elif self.grid[i[0]][i[1]-1] == 0 and i[1] >= 0:
                    self.x = i[0]
                    self.y = i[1]
                    self.path.pop(-1)
                    break
                elif self.grid[i[0]-1][i[1]] == 0:
                    self.x = i[0]
                    self.y = i[1]
                    self.path.pop(-1)
                    break
                else:
                    if i[0] == 0:
                        self.x = 0
                        self.y = 0
                        break
                    self.path.pop(-1)
                    continue
            else:
                if self.grid[i[0]+1][i[1]] == 0:
                    self.x = i[0]
                    self.y = i[1]
                    self.path.pop(-1)
                    break
                elif self.grid[i[0]][i[1]-1] == 0 and i[1] >= 0:
                    self.x = i[0]
                    self.y = i[1]
                    self.path.pop(-1)
                    break
                elif self.grid[i[0]][i[1]+1] == 0 and self.y < self.n:
                    self.x = i[0]
                    self.y = i[1]
                    self.path.pop(-1)
                    break
                elif self.grid[i[0]-1][i[1]] == 0:
                    self.x = i[0]
                    self.y = i[1]
                    self.path.pop(-1)
                    break
                else:
                    if i[0] == 0:
                        self.x = 0
                        self.y = 0
                        break
                    self.path.pop(-1)
                    continue

    def percolate(self):
        while self.check_percolation == False:
            self.path.append([self.x, self.y])
            if self.y > self.n-1:
                print("no way out")
                break
            if self.x == self.n -1:
                if self.grid[self.x][self.y] == 0:
                    self.grid[self.x][self.y] = 0.5
                    print("percolation occurs")
                self.check_percolation = True
            elif self.x == 0:
                if self.grid[self.x][self.y] == 0.5:
                    self.y += 1
                elif self.grid[self.x][self.y] == 1:
                    self.y += 1
                elif self.grid[self.x][self.y] == 0 and self.grid[self.x+1][self.y] == 0.5:
                    self.grid[self.x][self.y] = 0.5
                    self.y += 1
                elif self.grid[self.x][self.y] == 0 and self.grid[self.x+1][self.y] == 1:
                    self.grid[self.x][self.y] = 0.5
                    self.y += 1
                elif self.grid[self.x+1][self.y] == 0:
                    self.grid[self.x][self.y] = 0.5
                    self.x += 1
            elif self.x != 0:
                if self.y == 0:
                    if self.grid[self.x+1][self.y] == 0:
                        self.grid[self.x][self.y] = 0.5
                        self.x += 1
                    elif self.grid[self.x][self.y+1] == 0:
                        self.grid[self.x][self.y] = 0.5
                        self.y += 1
                    elif self.grid[self.x-1][self.y] == 0:
                        self.grid[self.x][self.y] = 0.5
                        self.x -= 1
                    elif self.grid[self.x+1][self.y] != 0 and self.grid[self.x][self.y+1] != 0 and self.grid[self.x-1][self.y] != 0:
                        self.grid[self.x][self.y] = 0.5
                        self.go_back()
                if self.y == self.n-1:
                    if self.grid[self.x+1][self.y] == 0:
                        self.grid[self.x][self.y] = 0.5
                        self.x += 1
                    elif self.grid[self.x][self.y-1] == 0:
                        self.grid[self.x][self.y] = 0.5
                        self.y -= 1
                    elif self.grid[self.x-1][self.y] == 0:
                        self.grid[self.x][self.y] = 0.5
                        self.x -= 1
                    elif self.grid[self.x+1][self.y] != 0 and self.grid[self.x][self.y-1] != 0  and self.grid[self.x-1][self.y] != 0:
                        self.grid[self.x][self.y] = 0.5
                        self.go_back()
                if self.y > 0 and self.y < self.n -1:
                    if self.grid[self.x+1][self.y] == 0:
                        self.grid[self.x][self.y] = 0.5
                        self.x += 1
                    elif self.grid[self.x][self.y-1] == 0:
                        self.grid[self.x][self.y] = 0.5
                        self.y -= 1
                    elif self.grid[self.x][self.y+1] == 0:
                        self.grid[self.x][self.y] = 0.5
                        self.y += 1
                    elif self.grid[self.x-1][self.y] == 0:
                        self.grid[self.x][self.y] = 0.5
                        self.x -= 1
                    elif self.grid[self.x+1][self.y] != 0 and self.grid[self.x][self.y-1] != 0 and self.grid[self.x][self.y+1] != 0 and self.grid[self.x-1][self.y] != 0:
                        self.grid[self.x][self.y] = 0.5
                        self.go_back()
        #CHECK PERCOLATION IS TRUE OR FALSE FOR EACH GRID, THE VALUE IS TRANSFERED TO CALCULATE THE PROBABILITY OF PERCOLATION
        # return self.check_percolation
        #THE STATEMENT BELOW NEEDS TO BE HASHED TO PLOT A PARTICULAR GENERATED GRID WITH THE CODE AT THE END OF THIS TEXTFILE
        return self.grid

    def plot_Grid(self, grid):
        #CREATES A PNG FILE WHILE PLOTTING THE GRID
        img = plt.imshow(grid)
        img.set_interpolation('nearest')
        img.set_cmap("gist_heat")
        fig1 = plt.gcf()
        plt.show()
        plt.draw()
        fig1.savefig('PLOT.png', dpi=100)

    def plot_Graph(self, density, probability, size):
        value = size
        label = "Size"+str(value)+"X"+str(value)
        x = density
        y = probabilityGrid
        plt.plot(x, y)
        plt.show()


if __name__ == '__main__':
    ######################################################################
    # PROGRAM TO GENERATE N GRIDS FOR 30 VALUES OF THE DENSITY, AND CALCULATING THE PROBABILITY OF PERCOLATION
    # FOR GRID SIZES 10, 20, 40 and 80.
    # size = 10
    # stepps = 30
    # size_values = dict()
    # robocza_density = 0.2
    # density_for_plot = []
    # for n in xrange(stepps+1):
    #     density_for_plot.append(round(robocza_density, 2))
    #     robocza_density += 0.02
    # for k in xrange(4):
    #     density_values = dict()
    #     density = 0.2
    #     for i in xrange(stepps+1):
    #         range = random.randint(50, 200)
    #         density_plot = []
    #         for j in xrange(range):
    #             check_percolation = False
    #             g = grid_Percolator(size, density)
    #             grid = g.percolate()
    #             if grid == False:
    #                 density_plot.append(0.0)
    #             elif grid == True:
    #                 density_plot.append(1.0)
    #         density_values[round(density, 2)] = sum(density_plot)/range
    #         density += 0.02
    #     size_values[size] = density_values
    #     size *= 2
    #
    # print_size = 10
    # for l in xrange(4):
    #     print_density = 0.2
    #     densities = size_values[print_size]
    #     probability_values_for_plot = []
    #     for m in xrange(stepps+1):
    #         probability_values_for_plot.append(densities[round(print_density, 2)])
    #         print_density += 0.02
    #     g.plot_Graph(density_for_plot, probability_values_for_plot, print_size)
    #     print_size *= 2

    #TEST CODE, AND PLOTTING
    size = 100
    density = 0.4
    g = grid_Percolator(size, density)
    grid = g.percolate()
    g.plot_Grid(grid)
