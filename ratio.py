def AGbyTC(data):
	k = []
	for i in range(len(data)):
		l = data[i]
		result = (l[1]+l[2])/(l[3]+l[4])
		k.append(result)
		print(l[0] + "- " + str(result))
	return k
def ATbyCG(data):
	k = []
	for i in range(len(data)):
		l = data[i]
		result = (l[1]+l[4])/(l[2]+l[3])
		k.append(result)
		print(l[0] + "- " + str(result))
	return k
def varAGbyTC(l1):
	mean = sum(l1)/len(l1)
	for i in range(len(l1)):
		l1[i] = abs(l1[i] - mean)
	summer = sum(l1)/len(l1)
	print("mean variation = "+str(summer))
def main():
	n = int(input("number of data "))
	data = []
	print("enter data")
	for i in range(n):
		string = list(map(str, input().strip().split(" ")))
		T = float(string[-1])
		C = float(string[-2])
		G = float(string[-3])
		A = float(string[-4])
		K = string[:-4]
		NAME = ""
		for i in range(len(K)):
			NAME += K[i] + " "
		data.append([NAME,A,G,C,T])
	print("\n(A + G) / (T + C) ratio\n")
	l1 = AGbyTC(data)
	varAGbyTC(l1)
	print("\n")
	print("(A + T) / (C + G) ratio\n")
	l2 = ATbyCG(data)
	varAGbyTC(l2)
main()