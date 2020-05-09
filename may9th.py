def twoSum(nums: [int], target: int) -> [int]:
    mergesort(nums)
    print(nums)
    for i in range(0, len(nums)):
        result = binarysearch(nums[i+1:],target-nums[i])
        print(i,result)
        if result[0]:
            return [i,result[1]]
        i+=1
        
        
def binarysearch(inputlist, target):
    first = 0
    last = len(inputlist)-1
    found = False
    while( first<= last and not found):
        mid = (first + last)//2
        if inputlist[mid] == target :
            found = True
        else:
            if target < inputlist[mid]:
                last = mid - 1
            else:
                first = mid + 1	
    return [found,mid]
        
def mergesort(nlist):
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]

        mergesort(lefthalf)
        mergesort(righthalf)
        i=j=k=0       
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                nlist[k]=lefthalf[i]
                i=i+1
            else:
                nlist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            nlist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            nlist[k]=righthalf[j]
            j=j+1
            k=k+1


#print(twoSum([3,2,4],6))



def two_Sum( nums: [int], target: int) -> [int]:
        index = 0 
        while index < len(nums)-1:
            for i in range(index+1,len(nums)):
                if nums[index]+nums[i] == target:
                    return[index,i]
            index += 1
        

print(two_Sum([3,2,4],6))


def addtwonumbers(list1,list2):
    