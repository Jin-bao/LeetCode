def int_to_Roman(num:int) -> str:
  roman_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M', '', '']
  idx = 0
  roman = ''
  while num > 0:
    left   = roman_list[idx]
    middle = roman_list[idx+1]
    right  = roman_list[idx+2]
    roman_digit = ''

    digit = num % 10
    if digit == 0:
      pass
    elif 0 < digit < 4:
      while digit > 0:
        roman_digit += left
        digit -= 1
    elif 4 <= digit < 9:
      diff = digit - 5
      if diff < 0:
        roman_digit = left + middle
      else:
        roman_digit = middle
        while diff > 0:
          roman_digit += left
          diff -= 1
    else:
      roman_digit = left + right

    roman = roman_digit + roman
    num //= 10
    idx  += 2

  return roman

print(int_to_Roman(1994))