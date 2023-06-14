import setup_path
import airsim
import time

client = airsim.MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)

client.armDisarm(True)

print("Setting wind to 10m/s in forward direction") # NED
wind = airsim.Vector3r(-100, 0, 0)
client.simSetWind(wind)
