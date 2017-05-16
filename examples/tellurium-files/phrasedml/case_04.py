"""
More complex compute change.
"""

from __future__ import print_function
import os
from tellurium.sedml.case_template import run_case

antimonyStr = '''
model case_04()
  J0: S1 -> S2; k1*S1-k2*S2
  S1 = 10.0; S2 = 0.0;
  k1 = 0.5; k2=0.4
end
'''

phrasedmlStr = '''
  mod1 = model "case_04"
  mod2 = model mod1 with S2=S1+4
  mod3 = model mod2 with S1=20.0
  sim1 = simulate uniform(0, 10, 100)
  task1 = run sim1 on mod1
  task2 = run sim1 on mod2
  task3 = run sim1 on mod3
  plot "Example plot" task1.time vs task1.S1, task1.S2, task2.S1, task2.S2, task3.S1, task3.S2
  report task1.time vs task1.S1, task1.S2, task2.S1, task2.S2, task3.S1, task3.S2
'''

run_case(os.path.realpath(__file__), antimonyStr, phrasedmlStr)