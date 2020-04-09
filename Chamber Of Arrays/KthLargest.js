/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
function sortNumber(a, b) {
    return a - b;
  }
  
var findKthLargest = function(nums, k) {
    let l = nums.length
    nums=nums.sort(sortNumber)
    return nums[l-k]
};

findKthLargest([3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6],2)