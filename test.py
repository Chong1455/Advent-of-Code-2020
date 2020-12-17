import os
import sys

def manipulate(sequence,start,end,fs,ls):
    for ch in sequence:
        mid=(start+end)//2
        if(ch==fs):
            end=mid
        else:
            start=mid+1
    return start

def findmissing(n):
    return n*(n+1)//2

total=0
start=1023
end=0
with open('day5.txt','r') as f:
    for line in f:
        line=line.strip()
        row=manipulate(line[:7],0,127,'F','B')
        col=manipulate(line[7:],0,7,'L','R')
        seat=row*8+col
        start=min(start,seat)
        end=max(end,seat)
        total+=seat
    missing=findmissing(end)-findmissing(start-1)-total
    print(end)
    print(missing)
    f.close()