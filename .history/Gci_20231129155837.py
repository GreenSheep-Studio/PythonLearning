import matplotlib.pyplot as plt
import numpy as np

ListIin = [eval(x) for x in input().split(" ")]
ListIout = [eval(x) for x in input().split(" ")]
ListR = [(4 / x * 1000) for x in ListIout]
ListB = []