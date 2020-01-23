import csv
import time
import datetime

def cmp_datetime(a, b):             #时间比较函数
    a_datetime = datetime.datetime.strptime(a, '%Y-%m-%d %H:%M:%S')
    b_datetime = datetime.datetime.strptime(b, '%Y-%m-%d %H:%M:%S')

    if a_datetime > b_datetime:
        return -1
    elif a_datetime < b_datetime:
        return 1
    else:
        return 0

def TimeSort(deal):                  #时间排序函数
	tempList=[]
	for i in range(0,len(deal)):
		for j in range(i+1,len(deal)):
			if(cmp_datetime(deal[i][0],deal[j][0])==-1):
				tempList=deal[i][0]
				deal[i][0]=deal[j][0]
				deal[j][0]=tempList
	print(deal)
	for A in deal:
		writer.writerow(A)

	

#print("读取CSV文件内容：")
file=open("data.csv","r")
reader=csv.reader(file)

file2=open("output.csv","w",newline='')    #newline去写空行
writer=csv.writer(file2)

sign=1    #总条目
tag=1     #处理完条目
deal=[]
tempBefore=''
for A in reader:
	if(sign!=1):    #从第二行处理
		timeStamp = int(A[0])/1000
		timeArray = time.localtime(timeStamp)
		A[0] = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
	else:
		sign+=1
		writer.writerow(A[0:4])    #写入指定文件
		continue;


	if(A[1]!='' and A[2]!='' and A[3]!='' and not('#' in A[1]) and not('*' in A[1]) 
		and not('^' in A[1]) and A[0][0:10]=='2018-10-03'):    #非空且无特殊符号,在10-03
	#	writer.writerow(A[0:4])    #写入指定文件

	    #时间排序操作
		if(tempBefore!=A[1] and sign!=2):
			print(tempBefore)
			print(A[1])
			TimeSort(deal)
			deal.clear()    #清空list
	#	print(A[0:4])
		deal.append(A[0:4])
		tempBefore=A[1]       #需放在判定条件之内
		tag+=1

	sign+=1
	#print(type(A))
TimeSort(deal)   #处理最后一行

print(sign)      #总条目
print(tag)       #处理完条目
file.close()
file2.close()