#!/usr/bin/env python
# -*- coding: utf-8 -*-
import yaml
from pprint import pprint as p
import argparse

__author__ = "dominis"
__version__ = "0.1"


class Kashrut(object):
  def __init__(self, action, run=False, yml='kashrut.yml'):
    self._action = action
    self._run = run
    self._config = self.parse_yaml(yml)

    try:
      run = getattr(self, self._action)
      run()
    except AttributeError:
      raise NotImplementedError("%s not implemeted" % self._action)


  def parse_yaml(self, yml):
    stream = open(yml, 'r')
    return yaml.load(stream)


  def validate(self):
    rules_yml = self.parse_yaml('rules.yml')

    self.iterate(rules_yml)


  def iterate(self, x):
    for k, v in x.items():
      if isinstance(v , dict):
        self.iterate(v)
      else:
        #print "key: {}, val: {}".format(k, v) 
        pass

  def build(self):
    p(self._config['build'])



if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Kashrut')
  parser.add_argument('action', choices=['init', 'deploy', 'build', 'validate'])
  parser.add_argument('--run', help='make it real', action='store_true')
  parser.add_argument('-v', action='count', help='verbose output', default=0)
  parser.add_argument('--yml', help='YML file location', default='kashrut.yml')
  args = parser.parse_args()

  K = Kashrut(action=args.action, run=args.run, yml=args.yml)