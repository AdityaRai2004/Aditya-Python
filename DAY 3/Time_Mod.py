import time
start_time = time.time()
import math
end_time = time.perf_counter() 
print(f"Time taken for single import (math): {end_time - start_time:.4f} seconds")

start_time = time.time()
from math import *
end_time = time.perf_counter()
print(f"Time taken for 'from math import *': {end_time - start_time:.4f} seconds")