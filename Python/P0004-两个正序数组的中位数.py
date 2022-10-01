class FMSA:
  def findMedianSortedArrays(self, numList1:list, numList2:list) -> float:
    numList = sorted(numList1+numList2)
    if (numListLen:=len(numList))%2 == 0:
      Median = (numList[int(numListLen/2)-1]+numList[int(numListLen/2)]) / 2
    else:
      Median = numList[int(numListLen/2)]
    return Median
    

FMSA = FMSA()
print(FMSA.findMedianSortedArrays([1, 2], [3, 4]))