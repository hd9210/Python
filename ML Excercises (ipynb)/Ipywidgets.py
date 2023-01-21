from ipywidgets import interact,interactive
import ipywidgets as wid
from IPython import display

def func(x):
    display(x)
    return x

w=interactive(func,x=5)

print(type(w))

print(w.children)
print(w)

display(w)