# Problem 1
def tennis_balls2(num):
  if num%3 == 0:
      return num/3
  elif num%2 != 0:
      return num*4+2
  else:
      return num+1
def tennis_ball(num):
  for i in range(0,5):
    num = tennis_balls2(num)
  return num

# Problem 2
def remove_duplicates(num):
  num2 = str(num)
  array = ""
  i = 0
  while i < len(num2):
    #print("I"+str(i))
    if i < len(num2):
      #print("I"+str(i))
      if num2[i] in array :
        
        #print("in"+num2[i])
        #print(num2)
        if i < len(num2):
          num2 = num2[:i]+num2[i+1:]
        else:
          num2 = num2[:i-1]
        #num2 = num2.split(num2[i])
        #print(num2)
        i -= 1
      else:
        #print("Array"+array)
        array += num2[i]
    i+= 1
  return(int(num2))

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

#Problem 4
def next_fib(num):
  i = 0;
  j = 1;
  if num == 0:
    return 0
  elif num == 1:
    return 1
  while (j<num):
    temp = j
    j = i + j
    i = temp
    
  return j

# Problem 5
def most_common (inputnum):
  outs = []
  zeroArr = []
  for i in range(10):
    outs.append(0)
    zeroArr.append(0)

  for i in str(inputnum):
    outs[int(i)]+=1

# Problem 6
def get_coins(num):
  q = (int) (num / 25)
  num = num % 25
  n = (int) (num / 5)
  num = num % 5

return int(str(q)+str(n)+str(num))