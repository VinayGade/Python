def _is_palindrome_(str):
  # base case #1
    if len(str) == 1 or len(str) == 0:
        return True
  # recursive case
    else :
        reverse = str[::-1]
        return reverse == str

print(_is_palindrome_("AVAJAVA"))