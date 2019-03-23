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