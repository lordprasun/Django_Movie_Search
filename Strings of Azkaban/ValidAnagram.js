/**
 * @description Given two strings s and t , write a function to determine if t is an anagram of s.
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(sorted(s) == sorted(t)){
        return true
    }else{
        return false
    }
};
function sorted(str){
    return str.split('').sort().join('')
}


console.log(isAnagram("anagram", "nagaram"))
console.log(isAnagram("rat","car"))