/*
 * @lc app=leetcode id=9 lang=rust
 *
 * [9] Palindrome Number
 */

// @lc code=start
impl Solution {
    pub fn is_palindrome(x: i32) -> bool {
        let x_string : String = x.to_string();
        let x_string_rev: String = x_string.chars().rev().collect();

        if x_string == x_string_rev {
            return true;
        } else {
            return false;
        }
    }
}
// @lc code=end

