def max_area(h_list:list[int]) -> int:
  hl_beg_idx = 0
  hl_end_idx = len(h_list)-1
  area_max = 0
  while hl_beg_idx < hl_end_idx:
    if (h_beg:=h_list[hl_beg_idx]) < (h_end:=h_list[hl_end_idx]):
      area = (hl_end_idx-hl_beg_idx) * h_beg
      if area > area_max:
        area_max = area
      hl_beg_idx += 1
    else:
      area = (hl_end_idx-hl_beg_idx) * h_end
      if area > area_max:
        area_max = area
      hl_end_idx -= 1
  return area_max

print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))