def test(nums1,nums2,*arr):
    sum=0
    for num in arr:
        print(num)
        sum+=num
    return sum
total=test(45,46,89,11,82,5,34,55)
print("all sum ",total)