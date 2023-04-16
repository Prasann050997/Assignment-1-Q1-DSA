#Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?
def printPairs(arr, sum):
    s = set()
    for i in range(len(arr)):
        temp = sum - arr[i]
        if (temp in s):
            print("(", temp, ",", arr[i], ")")
        s.add(arr[i])
arr = [1, 5, 7, -1, 2, 4]
sum = 6
printPairs(arr, sum)

#Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverseList(arr):
        print( arr[::-1])
	
arr = [1, 2, 3, 4, 5, 6]
print(arr)
print("Reversed list is")
reverseList(arr)
 
 
#Q3. Write a program to check if two strings are a rotation of each other?

def areRotations(string1, string2):
	size1 = len(string1)
	size2 = len(string2)
	temp = ''

	if size1 != size2:
		return 0

	temp = string1 + string1

	if (temp.count(string2) > 0):
		return 1
	else:
		return 0


# Driver code
if __name__ == "__main__":
	string1 = "AACD"
	string2 = "ACDA"

	# Function call
	if areRotations(string1, string2):
		print("Strings are rotations of each other")
	else:
		print("Strings are not rotations of each other")


 #Q4. Write a program to print the first non-repeated character from a string?

string = "characters"
index = -1
fnc = ""
for i in string:
	if string.count(i) == 1:
		fnc += i
		break
	else:
		index += 1
if index == 1:
	print("Either all characters are repeating or string is empty")
else:
	print("First non-repeating character is", fnc)
 
 

#Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
  
N = 3
  
# A, C, B are the name of rods
TowerOfHanoi(N, 'A', 'C', 'B')

#Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

def isOperator(x):

	if x == "+":
		return True

	if x == "-":
		return True

	if x == "/":
		return True

	if x == "*":
		return True

	return False

# Convert postfix to Prefix expression

def postToPre(post_exp):

	s = []

	# length of expression
	length = len(post_exp)

	# reading from right to left
	for i in range(length):

		# check if symbol is operator
		if (isOperator(post_exp[i])):

			op1 = s[-1]
			s.pop()
			op2 = s[-1]
			s.pop()

			temp = post_exp[i] + op2 + op1

			s.append(temp)

		else:

			s.append(post_exp[i])

	ans = ""
	for i in s:
		ans += i
	return ans

if __name__ == "__main__":

	post_exp = "AB+CD-"
	print("Prefix : ", postToPre(post_exp))

#Q7. Write a program to convert prefix expression to infix expression.

def prefixToInfix(prefix):
	stack = []
	
	i = len(prefix) - 1
	while i >= 0:
		if not isOperator(prefix[i]):
			
			stack.append(prefix[i])
			i -= 1
		else:
		
			str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
			stack.append(str)
			i -= 1
	
	return stack.pop()

def isOperator(c):
	if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
		return True
	else:
		return False

# Driver code
if __name__=="__main__":
	str = "*-A/BC-/AKL"
	print(prefixToInfix(str))
 
 
#Q8. Write a program to check if all the brackets are closed in a given code snippet.

def are_brackets_balanced(s):
	stack = []
	for ch in s:
		if ch in ('(', '{', '['):
			stack.append(ch)
		else:
			if stack and ((stack[-1] == '(' and ch == ')') or
						(stack[-1] == '{' and ch == '}') or
						(stack[-1] == '[' and ch == ']')):
				stack.pop()
			else:
				return False
	return not stack

expr = "{()}[]"

# Function call
if are_brackets_balanced(expr):
	print("Balanced")
else:
	print("Not Balanced")

#Q9. Write a program to reverse a stack.

class Stack:

	def __init__(self):
		self.Elements = []
		
	def push(self, value):
		self.Elements.append(value)
	
	def pop(self):
		return self.Elements.pop()
	
	def empty(self):
		return self.Elements == []
	
	def show(self):
		for value in reversed(self.Elements):
			print(value)

def BottomInsert(s, value):

	# check the stack is empty or not
	if s.empty():
		
		# if stack is empty then call
		s.push(value)
		
	# if stack is not empty then execute
	else:
		popped = s.pop()
		BottomInsert(s, value)
		s.push(popped)

# Reverse() reverse the stack
def Reverse(s):
	if s.empty():
		pass
	else:
		popped = s.pop()
		Reverse(s)
		BottomInsert(s, popped)

stk = Stack()

stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)

print("Original Stack")
stk.show()

print("\nStack after Reversing")
Reverse(stk)
stk.show()


#Q10. Write a program to find the smallest number using a stack.

# Python program for the above approach
class MinStack:
	
	# initialize your data structure here.
	def __init__(self):
		self.s = []

	class Node:
		def __init__(self, val, Min):
			self.val = val
			self.min = Min

	def push(self, x):
		if not self.s:
			self.s.append(self.Node(x, x))
		else:
			Min = min(self.s[-1].min, x)
			self.s.append(self.Node(x, Min))

	def pop(self):
		return self.s.pop().val

	def top(self):
		return self.s[-1].val

	def getMin(self):
		return self.s[-1].min

s = MinStack()

# Function calls
s.push(-1)
s.push(10)
s.push(-4)
s.push(0)
print(s.getMin())
print(s.pop())
print(s.pop())
print(s.getMin())


	
