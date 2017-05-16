"""
    tellurium 1.3.5

    auto-generated code
    sedmlDoc: L1V2  
    workingDir: /home/mkoenig/git/tellurium/examples/tellurium-files/phrasedml/results/_te_case_08
    inputType: COMBINE_FILE
"""
from __future__ import print_function, division
import tellurium as te
from roadrunner import Config
from tellurium.sedml.mathml import *
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import libsedml
import pandas
import os.path
Config.LOADSBMLOPTIONS_RECOMPILE = True

workingDir = r'/home/mkoenig/git/tellurium/examples/tellurium-files/phrasedml/results/_te_case_08'

# --------------------------------------------------------
# Models
# --------------------------------------------------------
# Model <mod1>
mod1 = te.loadSBMLModel(os.path.join(workingDir, 'case_08.xml'))
# Model <mod2>
mod2 = te.loadSBMLModel(os.path.join(workingDir, 'case_08.xml'))

# --------------------------------------------------------
# Tasks
# --------------------------------------------------------
# Task <task1>
# not part of any DataGenerator: task1

# Task <task2>
# not part of any DataGenerator: task2

# Task <repeat1>

repeat1 = []
__range__uniform_linear_for_S2 = np.linspace(start=0.0, stop=10.0, num=10)
for __k__uniform_linear_for_S2, __value__uniform_linear_for_S2 in enumerate(__range__uniform_linear_for_S2):
    if __k__uniform_linear_for_S2 == 0:
        mod1.reset()
    # Task: <task1>
    task1 = [None]
    mod1.setIntegrator('cvode')
    mod1['init([S2])'] = __value__uniform_linear_for_S2
    __value__S2 = mod1['init([S2])']
    mod1['init([S1])'] = __value__S2 + 3
    mod1.timeCourseSelections = ['[S1]', '[S2]', 'time']
    task1[0] = mod1.simulate(start=0.0, end=10.0, steps=20)
    # Task: <task2>
    task2 = [None]
    mod1.setIntegrator('cvode')
    mod1['init([S2])'] = __value__uniform_linear_for_S2
    __value__S2 = mod1['init([S2])']
    mod1['init([S1])'] = __value__S2 + 3
    mod1.timeCourseSelections = ['[S1]', '[S2]', 'time']
    task2[0] = mod1.simulate(start=0.0, end=3.0, steps=10)

    task1.extend(task2)

    repeat1.extend(task1)

# --------------------------------------------------------
# DataGenerators
# --------------------------------------------------------
# DataGenerator <plot_0_0_0>
__offsets__repeat1 = np.cumsum(np.array([sim['time'][-1] for sim in repeat1]))
__offsets__repeat1 = np.insert(__offsets__repeat1, 0, 0)
__var__repeat1_____mod1_____time = np.transpose(np.array([sim['time']+__offsets__repeat1[k] for k, sim in enumerate(repeat1)]))
__var__repeat1_____mod1_____time = np.concatenate(np.transpose(__var__repeat1_____mod1_____time))
if len(__var__repeat1_____mod1_____time.shape) == 1:
     __var__repeat1_____mod1_____time.shape += (1,)
plot_0_0_0 = __var__repeat1_____mod1_____time

# DataGenerator <plot_0_0_1>
__var__repeat1_____mod1_____S1 = np.transpose(np.array([sim['[S1]'] for sim in repeat1]))
__var__repeat1_____mod1_____S1 = np.concatenate(np.transpose(__var__repeat1_____mod1_____S1))
if len(__var__repeat1_____mod1_____S1.shape) == 1:
     __var__repeat1_____mod1_____S1.shape += (1,)
plot_0_0_1 = __var__repeat1_____mod1_____S1

# DataGenerator <plot_0_1_1>
__var__repeat1_____mod1_____S2 = np.transpose(np.array([sim['[S2]'] for sim in repeat1]))
__var__repeat1_____mod1_____S2 = np.concatenate(np.transpose(__var__repeat1_____mod1_____S2))
if len(__var__repeat1_____mod1_____S2.shape) == 1:
     __var__repeat1_____mod1_____S2.shape += (1,)
plot_0_1_1 = __var__repeat1_____mod1_____S2

# --------------------------------------------------------
# Outputs
# --------------------------------------------------------
# Output <plot_0>
plt.figure(num=None, figsize=(9, 5), dpi=80, facecolor='w', edgecolor='k')
from matplotlib import gridspec
__gs = gridspec.GridSpec(1, 2, width_ratios=[3, 1])
plt.subplot(__gs[0])
for k in range(plot_0_0_0.shape[1]):
    if k == 0:
        plt.plot(plot_0_0_0[:,k], plot_0_0_1[:,k], marker = '.', color='r', linewidth=1.5, markersize=3.0, alpha=0.8, label='repeat1.mod1.S1')
    else:
        plt.plot(plot_0_0_0[:,k], plot_0_0_1[:,k], marker = '.', color='r', linewidth=1.5, markersize=3.0, alpha=0.8)
for k in range(plot_0_0_0.shape[1]):
    if k == 0:
        plt.plot(plot_0_0_0[:,k], plot_0_1_1[:,k], marker = '.', color='b', linewidth=1.5, markersize=3.0, alpha=0.8, label='repeat1.mod1.S2')
    else:
        plt.plot(plot_0_0_0[:,k], plot_0_1_1[:,k], marker = '.', color='b', linewidth=1.5, markersize=3.0, alpha=0.8)
plt.title('Repeated Multiple Subtasks', fontweight='bold')
plt.xlabel('repeat1.mod1.time', fontweight='bold')
__lg = plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
__lg.draw_frame(False)
plt.setp(__lg.get_texts(), fontsize='small')
plt.setp(__lg.get_texts(), fontweight='bold')
plt.savefig(os.path.join(workingDir, 'plot_0.png'), dpi=100)
plt.show()

