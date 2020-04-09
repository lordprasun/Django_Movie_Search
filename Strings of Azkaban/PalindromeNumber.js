/**
 * @description Determine whether an integer is a palindrome.
 * @description An integer is a palindrome when it reads the same backward as forward.
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome_2 = function(x) {
    strx = x.toString();
    len = strx.length - 1
    limit = Math.floor(strx.length/2)    
    for(let i=0;i<limit;i++){
        if(strx[i]!==strx[len-i]){
          return false  
        }
    }  
    return true
};

var isPalindrome = function(x) {
    strx = x.toString();
    if(strx==reversex(strx)){
        return true
    }else{
        return false
    }
};
function reversex(x){
    return x.split('').reverse().join('')
}

console.log(isPalindrome(121))
console.log(isPalindrome(-121))