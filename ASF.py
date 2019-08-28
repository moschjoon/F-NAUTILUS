from river_pollution import RiverPollution
from Population import Population
from sklearn.cluster import KMeans
from weights import Referencepoints
# Problem =
class ASF:
    
    """Evaluate ASF function of individual.

    Returns ASF function of individuals.

    Parameters
    ----------
    problem: our MOP
    objectives: objectives value
    weights: the representative weights
    reference_p: the reference point
    """

    def __init__(self, problem, objectives, weight, reference_p):
        self.problem=problem
        self.objectives=objectives
        self.weight=weight
        self.reference_p=reference_p

    def asf_fun(self):

        rho=0.1
        first_term = max([self.weight[i] * (self.objectives[i] - self.reference_p[i])
            for i in range(self.problem.num_of_objectives)])
                
        second_term = sum([self.weight[i]*(self.objectives[i] - self.reference_p[i])
            for i in range(self.problem.num_of_objectives)]) * rho
        
        return first_term + second_term  

# problem = RiverPollution()
# znadir = [-4.07, -2.80, -0.32, 9.71] #Nadir point of Riverpollution problem
# filename = problem.name + "_" + str(problem.num_of_objectives)

# #----- Generating Uniform weights W ----#.
# lattice_resolution = 15
# Wi=Referencepoints(lattice_resolution, problem.num_of_objectives)

# ## Nµ Representative weights of objectives
# Nµ= 200 # The number of weights
# NS = 5 # Number of Solutions the DM wants to see in each iteration
# W=KMeans(Nµ).fit(Wi.values).cluster_centers_ # Selecting Nµ weights
# K=ASF(problem, Population(problem).objectives[0], W[0], znadir).asf_fun()
