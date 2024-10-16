'''
    Lesson: Else If
    Author: Eric Fang
    Date Created: October 16th, 2024
    Date Last Modified: October 16th, 2024
'''

def q1(): 
  #Write Assignment code here
  word = input("In: ")
  if word[-3:] == "ife":
    print("-ives")
  elif word[-2:] == "ey":
    print("-eys")
  elif word[-1:] == "y":
    print("-ies")
  else:
    print("-s")


def q2(): 
  #Write Assignment code here
  num = int(input("In: "))
  if num > 0:
    print(f"{num} is positive")
  elif num < 0:
    print(f"{num} is negative")

def q3():
  s1 = float(input("Input a number: "))
  s2 = float(input("Input a number: "))
  s3 = float(input("Input a number: "))
  if s1 + s2 < s3 or s2 + s3 < s1 or s3 + s1 < s2:
    print("No Triangle")
  elif s1 == s2 and s2 == s3:
    print("Equilateral")
  elif s1 == s2 or s2 == s3 or s1 == s3:
    print("Isosceles")
  else:
    print("Scalene")


#Do not alter the following code
#Comment out the following code when running your tests
'''
q1()
q2()
q3()
'''