from nx.stock import *
from nx.utils import *
from nx.config import *

s1 = create_stock('Nutanix', Symbol.NX, 100, 10.3)
print_dict(s1)

s2 = create_stock('Nutanix', Symbol.NX, "Whatever", 5)
print_dict(s2)

# Problems
# Even if the operation fails, it's too late to provide such information.
# If does not fail, then it is worse. You get unexpected outcomes.