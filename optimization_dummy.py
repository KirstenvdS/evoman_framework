###############################################################################
# EvoMan FrameWork - V1.0 2016  			                                  #
# DEMO : Neuroevolution - Genetic Algorithm  neural network.                  #
# Author: Karine Miras        			                                      #
# karine.smiras@gmail.com     				                                  #
###############################################################################

# imports framework
import sys

from evoman.environment import Environment
from demo_controller import player_controller

# imports other libs
import numpy as np
import os

# runs simulation
def simulation(env,x):
    f,p,e,t = env.play(pcont=x)
    return f

# evaluation
def evaluate(env, x):
    return np.array(list(map(lambda y: simulation(env,y), x)))


def main():
    # choose this for not using visuals and thus making experiments faster
    headless = True
    if headless:
        os.environ["SDL_VIDEODRIVER"] = "dummy"


    experiment_name = 'optimization_test'
    if not os.path.exists(experiment_name):
        os.makedirs(experiment_name)

    n_hidden_neurons = 10

    # initializes simulation in individual evolution mode, for single static enemy.
    env = Environment(experiment_name=experiment_name,
                    enemies=[2],
                    playermode="ai",
                    player_controller=player_controller(n_hidden_neurons), # you  can insert your own controller here
                    enemymode="static",
                    level=2,
                    speed="fastest",
                    visuals=False)


    # number of weights for multilayer with 10 hidden neurons
    n_vars = (env.get_num_sensors()+1)*n_hidden_neurons + (n_hidden_neurons+1)*5

    # start writing your own code from here

    # constants
    POP_SIZE = 10

    # our own functions
    def new_pop(pop_size, n_vars):
        new_population = np.random.uniform(-1.0, 1.0, (pop_size, n_vars))
        return new_population

    def discrete_crossover(parent_1, parent_2):
        offspring_1 = []
        offspring_2 = []
        for i in range(len(parent_1)):
            if np.random.uniform() > 0.5:
                offspring_1.append(parent_1[i])
                offspring_2.append(parent_2[i])
            else:
                offspring_1.append(parent_2[i])
                offspring_2.append(parent_1[i])

        return offspring_1, offspring_2

    def intermediate_crossover (parent_1, parent_2):
        a = np.random.uniform()
        offspring_1 = []
        offspring_2 = []
        for i in range(len(parent_1)):
            offspring_1_new_value = a * parent_1[i] + (1 - a) * parent_2 [i]
            offspring_1.append(offspring_1_new_value)

            offspring_2_new_value = (1 - a) * parent_1[i] + a * parent_2 [i]
            offspring_2.append(offspring_2_new_value)

        return offspring_1, offspring_2



    #this is where our working code starts
    #create new population
    population = new_pop(POP_SIZE, n_vars)
    generation = 0

    #evaluate population (probably also put in a documentation and termination mechanism in here)

    #selection

    #select parents



    #some test values I used
    #parent_1 = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]
    #parent_2 = [8.0, 9.0, 6.0, 7.0, 3.0, 4.0, 5.0, 1.0, 2.0]

    #crossover (use to create offspring)

    # discrete crossover
    #offspring_1, offspring_2 = discrete_crossover(parent_1, parent_2)

    # intermediate crossover
    offspring_1, offspring_2 = intermediate_crossover(parent_1, parent_2)

    #print(parent_1)
    #print(parent_2)
    #print(offspring_1)
    #print(offspring_2)

    #mutation (use to create offspring)

    #replace parent generation with new generation


if __name__ == '__main__':
    main()
