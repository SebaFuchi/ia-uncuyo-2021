import environment
import agent
import agentRandom


env = environment.Environment
env.__init__(env,32,32,1.0)

agent01 = agent.Agent

agent01.__init__(agent01,env)

agent01.think(agent01)
env.get_performance(env)


