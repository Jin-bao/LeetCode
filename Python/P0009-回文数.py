def palindromeQ(x: int) -> bool:
  if (xStr := str(x)) == xStr[::-1]:
    return True
  else:
    return False

print(palindromeQ(1221))