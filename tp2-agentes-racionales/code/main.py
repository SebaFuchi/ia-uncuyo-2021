import environment
import agent
import agentRandom


env = environment.Environment
env.__init__(env,128,128,0.8)

agent01 = agentRandom.AgentRandom


agent01.__init__(agent01,env)

agent01.think(agent01)
print("")
env.get_performance(env)
print("")
