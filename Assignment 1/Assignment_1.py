import gymnasium as gym

# MountainCar-v0 Environment
env1 = gym.make("MountainCar-v0", render_mode="human")
observation, info = env1.reset()

for episode in range(5):  # Handle multiple episodes explicitly
    print(f"Episode {episode + 1}")
    for step in range(200):  # Match the episode duration to 200 steps
        action = env1.action_space.sample()  # Take a random action.
        observation, reward, terminated, truncated, info = env1.step(action)
        print(f"Step: {step + 1}, Action: {action}, Observation: {observation}, Reward: {reward}")  # Log details for debugging.
        if terminated or truncated:
            print("Episode ended. Resetting environment.")  # Log when the environment resets.
            observation, info = env1.reset()
            break

env1.close()

# Print details of MountainCar-v0
env1 = gym.make("MountainCar-v0")
print("MountainCar-v0")
print("Observation space:", env1.observation_space)
print("Action space:", env1.action_space)
env1.close()

# Pendulum-v1 Environment
env2 = gym.make("Pendulum-v1", render_mode="human")
observation, info = env2.reset(seed=42)

for _ in range(500):
    action = env2.action_space.sample()
    observation, reward, terminated, truncated, info = env2.step(action)
    if terminated or truncated:
        observation, info = env2.reset()

env2.close()

# Print details of Pendulum-v1
env2 = gym.make("Pendulum-v1")
print("\nPendulum-v1")
print("Observation space:", env2.observation_space)
print("Action space:", env2.action_space)
env2.close()
