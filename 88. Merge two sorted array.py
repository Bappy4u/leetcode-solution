def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        temp1 = nums1[:m]
        nums1[:] = sorted(temp1+nums2)