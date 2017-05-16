"""
Simple report & report of repeated tasks.
"""

from __future__ import print_function
import os
from tellurium.sedml.case_template import run_case

antimonyStr = '''
model case_07()
  J0: S1 -> S2; k1*S1-k2*S2
  S1 = 10.0; S2 = 0.0;
  k1 = 0.5; k2=0.4
end
'''

phrasedmlStr = '''
  mod1 = model "case_07"
  sim1 = simulate uniform(0, 10, 100)
  task1 = run sim1 on mod1
  repeat1 = repeat task1 for S1 in [1, 3, 5], reset=True
  report task1.time, task1.S1, task1.S2, task1.S1/task1.S2
  report repeat1.time, repeat1.S1, repeat1.S2, repeat1.S1/repeat1.S2
'''

run_case(os.path.realpath(__file__), antimonyStr, phrasedmlStr)
