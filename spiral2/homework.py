def spiralize(size, n=1):
    sum =[]
    while topRight < size:
      topRight = n**2 
      topLeft = n**2 - n + 1 
      bottomLeft = n**2 - 2*n + 2 
      bottomRight = n**2 - 3*n + 3
      currentSum = topRight + topLeft + bottomLeft + bottomRight
      sum.append(currentSum)
      return_value= sum(sum)
    return return_value
