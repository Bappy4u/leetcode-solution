def dvnc(nums1:List[int], nums2:List[int]):
    res = []
    
    i, j =0,0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            res.append(nums1[i])
            i +=1
        else:
            res.append(nums2[j])
            j +=1
        
    if j==len(nums2):
        return res + nums1[i:]
    else:
        return res + nums2[j:]
        


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        cnums = dvnc(nums1, nums2)    
        if len(cnums)%2==0:
            val = cnums[len(cnums)//2-1] + cnums[len(cnums)//2]
            return val/2
        return cnums[len(cnums)//2]

        