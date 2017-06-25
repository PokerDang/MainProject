# coding: utf-8

# Local application/library specific imports
import py_vollib
from py_vollib.black import black

F = 49
K = 50
r = .05
t = 0.3846
sigma = 0.2
flag = 'c'
discounted_call_price = black(flag, F, K, t, r, sigma)
print discounted_call_price