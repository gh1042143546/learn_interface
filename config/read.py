import os
import yaml
proDir = os.path.split(os.path.realpath(__file__))[0]
configPath = os.path.join(proDir, "config.yml")

f = open(configPath)
cf = yaml.load(f)
print(cf["http"][1])