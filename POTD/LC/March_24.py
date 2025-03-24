class Solution:
    def countDays(self, days: int, arr: List[List[int]]) -> int:
        arr.sort()
        rem_days=arr[0][0]-1
        n=len(arr)
        max_day=arr[0][1]
        print(arr)
        print(rem_days)
        for i in range(1,n):
            if arr[i][0]<=max_day:
                max_day=max(max_day,arr[i][1])
            else:
                rem_days+=arr[i][0]-(max_day+1)
                max_day=arr[i][1]
                print(rem_days,arr[i][0],arr[i][0]-(max_day+1))
        if max_day<days:
            rem_days+=days-(max_day)
        return rem_days
# TC : O ( N Log N )
# SC : O ( 1 )
#  Approach : sort the array find the gaps between the days 