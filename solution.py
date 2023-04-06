import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1902092480 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    
    alpha = 1 - p
    loc = x.mean()
    degree_freedom = len(x)
    x_expon = 0.5 - x / 89 ** 2
    a = chi2.ppf(1 - alpha / 2, 2 * degree_freedom)
    b = chi2.ppf(alpha / 2, 2 * degree_freedom)
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return loc - scale * norm.ppf(1 - alpha / 2), \
           loc - scale * norm.ppf(alpha / 2)
