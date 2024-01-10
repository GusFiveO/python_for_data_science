import time
from datetime import datetime

timestamp = time.time()

print(f"Seconds since Junary 1, 1970: {timestamp:,.3f} or {timestamp:.3g} in scientific notation")
print(datetime.now().strftime("%b %d %Y"))
