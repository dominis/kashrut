#!/bin/env python
import yaml
from pprint import pprint as p

stream = open("kashrut.yaml", 'r')
config = yaml.load(stream)

p(config)