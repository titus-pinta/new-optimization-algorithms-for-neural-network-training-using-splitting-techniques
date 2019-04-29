"""
:mod:`torch.optim` is a package implementing various optimization algorithms.
Most commonly used methods are already supported, and the interface is general
enough, so that more sophisticated ones can be also easily integrated in the
future.
"""

from .adadelta import Adadelta
from .adagrad import Adagrad
from .adam import Adam
from .sparse_adam import SparseAdam
from .adamax import Adamax
from .asgd import ASGD
from .sgd import SGD
from .rprop import Rprop
from .rmsprop import RMSprop
from .optimizer import Optimizer
from .lbfgs import LBFGS
from .ssa1 import SSA1
from .ssa2 import SSA2
from .ssa1-ada import SSA1-ADA
from .ssa2-ada import SSA2-ADA
from . import lr_scheduler

del adadelta
del adagrad
del adam
del sparse_adam
del adamax
del asgd
del sgd
del rprop
del rmsprop
del optimizer
del lbfgs
del ssa1
del ssa2
del ssa1-ada
del ssa1-ada
#del a3titus
