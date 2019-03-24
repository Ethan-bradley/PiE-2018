# Problem 3
def rotate(num):
  num = str(num)

  big = 0;
  for i in num:
    if int(i) > big:
      big = int(i)


  for i in range(big):
    lastnum = num[-1:]
    num = num[:-1]
    num = lastnum + num

  return(int(num))

  # Problem 6
def get_coins(num):
  q = (int) (num / 25)
  num = num % 25
  n = (int) (num / 5)
  num = num % 5

  return int(str(q)+str(n)+str(num))
