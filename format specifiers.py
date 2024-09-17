a: float = 10.98743
b: int = 1_000_000
text: str = "SAMPLE"
print(f"{text} hello")
print(f"{text:20} hello")
print(f"{text:_<20} hello")
print(f"{text:_>20} hello")
print(f"{text:_^20} hello")
print(f"a={a:,.2f}")  # 2 is value after decimal point
print(f"a={a:,.0f}")  # 0 is value after decimal point

""" 
1. 0 is value after decimal point . 
2. comma separator is to separate the digits with comma in thousands
"""
print(f"a={a:.3%}")  # 3 is value after decimal point in percentage
print(f"a={b:.0e}")  # 3 is value after decimal point in scientific notation
