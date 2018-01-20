f=open("train_20171215.txt")
data=f.read()
rows=data.split('\n')
full_data=[]
for i in range(1,len(rows)):
    rowdata=[]
    row_data=rows[i].split("	")
    for j in row_data:
  #      j=int(j)
        rowdata.append(j)
    full_data.append(rowdata)

data_1_1=[]
data_1_2=[]
data_1_3=[]
data_1_4=[]
data_1_5=[]
data_1_6=[]
data_1_7=[]
data_2_1=[]
data_2_2=[]
data_2_3=[]
data_2_4=[]
data_2_5=[]
data_2_6=[]
data_2_7=[]
data_3_1=[]
data_3_2=[]
data_3_3=[]
data_3_4=[]
data_3_5=[]
data_3_6=[]
data_3_7=[]
data_4_1=[]
data_4_2=[]
data_4_3=[]
data_4_4=[]
data_4_5=[]
data_4_6=[]
data_4_7=[]
data_5_1=[]
data_5_2=[]
data_5_3=[]
data_5_4=[]
data_5_5=[]
data_5_6=[]
data_5_7=[]

for i in range(0,len(full_data)-1):
    if full_data[i][1]=='1':
        if full_data[i][2]=='1':
            data_1_1.append(full_data[i][3])
            continue
        if full_data[i][2]=='2':
            data_2_1.append(full_data[i][3])
            continue
        if full_data[i][2]=='3':
            data_3_1.append(full_data[i][3])
            continue
        if full_data[i][2]=='4':
            data_4_1.append(full_data[i][3])
            continue
        if full_data[i][2]=='5':
            data_5_1.append(full_data[i][3])
            continue
    if full_data[i][1]=='2':
        if full_data[i][2]=='1':
            data_1_2.append(full_data[i][3])
            continue
        if full_data[i][2]=='2':
            data_2_2.append(full_data[i][3])
            continue
        if full_data[i][2]=='3':
            data_3_2.append(full_data[i][3])
            continue
        if full_data[i][2]=='4':
            data_4_2.append(full_data[i][3])
            continue
        if full_data[i][2]=='5':
            data_5_2.append(full_data[i][3])
            continue
    if full_data[i][1]=='3':
        if full_data[i][2]=='1':
            data_1_3.append(full_data[i][3])
            continue
        if full_data[i][2]=='2':
            data_2_3.append(full_data[i][3])
            continue
        if full_data[i][2]=='3':
            data_3_3.append(full_data[i][3])
            continue
        if full_data[i][2]=='4':
            data_4_3.append(full_data[i][3])
            continue
        if full_data[i][2]=='5':
            data_5_3.append(full_data[i][3])
            continue
    if full_data[i][1]=='4':
        if full_data[i][2]=='1':
            data_1_4.append(full_data[i][3])
            continue
        if full_data[i][2]=='2':
            data_2_4.append(full_data[i][3])
            continue
        if full_data[i][2]=='3':
            data_3_4.append(full_data[i][3])
            continue
        if full_data[i][2]=='4':
            data_4_4.append(full_data[i][3])
            continue
        if full_data[i][2]=='5':
            data_5_4.append(full_data[i][3])
            continue
    if full_data[i][1]=='5':
        if full_data[i][2]=='1':
            data_1_5.append(full_data[i][3])
            continue
        if full_data[i][2]=='2':
            data_2_5.append(full_data[i][3])
            continue
        if full_data[i][2]=='3':
            data_3_5.append(full_data[i][3])
            continue
        if full_data[i][2]=='4':
            data_4_5.append(full_data[i][3])
            continue
        if full_data[i][2]=='5':
            data_5_5.append(full_data[i][3])
            continue
    if full_data[i][1]=='6':
        if full_data[i][2]=='1':
            data_1_6.append(full_data[i][3])
            continue
        if full_data[i][2]=='2':
            data_2_6.append(full_data[i][3])
            continue
        if full_data[i][2]=='3':
            data_3_6.append(full_data[i][3])
            continue
        if full_data[i][2]=='4':
            data_4_6.append(full_data[i][3])
            continue
        if full_data[i][2]=='5':
            data_5_6.append(full_data[i][3])
            continue
    if full_data[i][1]=='7':
        if full_data[i][2]=='1':
            data_1_7.append(full_data[i][3])
            continue
        if full_data[i][2]=='2':
            data_2_7.append(full_data[i][3])
            continue
        if full_data[i][2]=='3':
            data_3_7.append(full_data[i][3])
            continue
        if full_data[i][2]=='4':
            data_4_7.append(full_data[i][3])
            continue
        if full_data[i][2]=='5':
            data_5_7.append(full_data[i][3])
            continue

print("1_1")
for i in data_1_1:
    print(i)
print("1_2")
for i in data_1_2:
    print(i)
print("1_3")
for i in data_1_3:
    print(i)
print("1_4")
for i in data_1_4:
    print(i)
print("1_5")
for i in data_1_5:
    print(i)
print("1_6")
for i in data_1_6:
    print(i)
print("1_7")
for i in data_1_7:
    print(i)
print("2_1")
for i in data_2_1:
    print(i)
print("2_2")
for i in data_2_2:
    print(i)
print("2_3")
for i in data_2_3:
    print(i)
print("2_4")
for i in data_2_4:
    print(i)
print("2_5")
for i in data_2_5:
    print(i)
print("2_6")
for i in data_2_6:
    print(i)
print("2_7")
for i in data_2_7:
    print(i)
print("3_1")
for i in data_3_1:
    print(i)
print("3_2")
for i in data_3_2:
    print(i)
print("3_3")
for i in data_3_3:
    print(i)
print("3_4")
for i in data_3_4:
    print(i)
print("3_5")
for i in data_3_5:
    print(i)
print("3_6")
for i in data_3_6:
    print(i)
print("3_7")
for i in data_3_7:
    print(i)
print("4_1")
for i in data_4_1:
    print(i)
print("4_2")
for i in data_4_2:
    print(i)
print("4_3")
for i in data_4_3:
    print(i)
print("4_4")
for i in data_4_4:
    print(i)
print("4_5")
for i in data_4_5:
    print(i)
print("4_6")
for i in data_4_6:
    print(i)
print("4_7")
for i in data_4_7:
    print(i)
print("5_1")
for i in data_5_1:
    print(i)
print("5_2")
for i in data_5_2:
    print(i)
print("5_3")
for i in data_5_3:
    print(i)
print("5_4")
for i in data_5_4:
    print(i)
print("5_5")
for i in data_5_5:
    print(i)
print("5_6")
for i in data_5_6:
    print(i)
print("5_7")
for i in data_5_7:
    print(i)





