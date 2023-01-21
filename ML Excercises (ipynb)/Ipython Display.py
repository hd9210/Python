from IPython.display import display
from ipywidgets import interact,interactive
import ipywidgets as wid
def f(a, b):
    display(a + b)
    return a+b

w = interactive(f, a=10, b=20)

display(w)