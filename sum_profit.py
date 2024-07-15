import re

# extract number from str using generator function
def generator_numbers(text):
  pattern = re.compile(r'\d+\.?\d+')
  matches = pattern.findall(text)
  for match in matches:
    yield float(match)

# calculate total sum of number in text using func in attrs
def sum_profit(text, func):
  total = 0
  for number in func(text):
    total += number
  
  return total

text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")