def numReverse(num: int) -> int:
  numR = 0
  if num >= 0:
    while num != 0:
      numR = numR*10 + num%10
      num = int(num/10)
    if numR >= 2**31-1:
      return 0
    return numR
  else:
    num = -num
    while num != 0:
      numR = numR*10 + num%10
      num = int(num/10)
    if numR >= 2**31:
      return 0
    return -numR

if __name__ == '__main__':
  print(numReverse(-2147483648))