import polars as pl
import time
import resource 

time_start = time.perf_counter()

def isSame(ind1, ind2): #checks if they are same by comparing a definitely unique data (TC)
    tc1=file1.get_column("TC")[ind1]
    tc2=file2.get_column("TC")[ind2]
    if tc1==tc2:
        return True
    else:
        return False

def dateChecker(ind1, ind2, col): #compares two given data's dates
    date1=file1.get_column("DATE")[ind1]
    date2=file2.get_column("DATE")[ind2]
    for i in range(0, 10):
        while(str(date1)[i]!=str(date2)[i]):
            if(int(date1[i])>int(date2[i])):
                print("File1 is derived from File2. (According to " + file1.get_column("FIRST NAME")[ind1] + " " + file1.get_column("LAST NAME")[ind1] + "'s "+ col +")")
                return
            else:
                print("File2 is derived from File1. (According to " + file1.get_column("FIRST NAME")[ind1] + " " + file1.get_column("LAST NAME")[ind1] + "'s "+ col +")")
                return
    print("Dates are same.")
    return
        
def columnTraverser(col1, col2, col): #goes through the same column looking for same data
    x=0
    while x<len(col1):
        y=0
        while y<len(col2):
            if col1[x] == col2[y] and isSame(x, y):
                dateChecker(x, y, col)
            y+=1
        x+=1
    return
        
def traverser(data1, data2): #goes through the columns looking for a same
    for i in data1.columns:
        for j in data2.columns:
            if i=="DATE" or j=="DATE":
                continue
            if i==j:
                columnTraverser(data1.get_column(i),data2.get_column(i),i)
    return

#main

print("enter a path or copy the file into the same directory and enter the name")
file1=pl.read_excel(input("File1: "))
file2=pl.read_excel(input("File2: "))

traverser(file1, file2)

time_elapsed = (time.perf_counter() - time_start)
memKb=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss/1024.0
print ("%5.1f secs %5.1f KByte" % (time_elapsed,memKb))
