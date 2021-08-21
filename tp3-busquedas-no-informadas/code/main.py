import environment
import agent
import time

env = environment.Environment()

ag = agent.Agent(env)

print("START")
env.print_enviroment()
start = time.time()
ag.seekBF()
print("------")
print("SOLVED")
env.print_enviroment()
end = time.time()
print("")

print("Time: "+str(end-start))