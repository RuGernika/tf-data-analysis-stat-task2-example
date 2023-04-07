import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1902092480 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    n = len(x)
    mean = np.mean(x)
    std_error = np.std(x, ddof=1) / np.sqrt(n)
    t_value = t.ppf(1 - p / 2, n - 1)
    half_width = t_value * std_error
    return (mean - half_width, mean + half_width)
