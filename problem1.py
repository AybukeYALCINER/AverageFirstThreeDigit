import sys
inputfile=sys.argv[1]

file=open("integers.txt","r")

line=file.readline()
ListIntegersfirst=line.split(';')
ListIntegers=[]
print("ListIntegers=",ListIntegersfirst)
output=[]

i=len(ListIntegersfirst)

while (i > 0):
   i = i - 1
   ListIntegers.append(ListIntegersfirst[i])

for item in ListIntegers:
    count=0
    print(*item,sep=(','))
    count=count+1

def firstdigit(item):
    firstdigit=item[0]


def seconddigit(item):
    seconddigit=item[1]


def thirddigit(item):
    thirddigit=item[2]

def avgFirstThreeDigit(item):
    return (float(item[0])+float(item[1])+float(item[2]))/3

for item in ListIntegers:
    count=0
    print(avgFirstThreeDigit(item))
    output.append(float(avgFirstThreeDigit(item)))
    count=count+1

print("output=",output)

file.close()
