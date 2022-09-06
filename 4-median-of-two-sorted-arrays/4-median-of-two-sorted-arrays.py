class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        resarr = nums1 + nums2
        resarr.sort()
        
        if len(resarr)%2==1:
            return resarr[len(resarr)//2]
        else:
            return (resarr[len(resarr)//2] + resarr[len(resarr)//2-1])/2
            
        