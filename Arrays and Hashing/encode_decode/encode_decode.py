class Solution:
  """
  Problem: Encode and Decode Strings
  Difficulty: Medium
  """

  # Time: O(M) where M is the total number of characters in all strings
  # Space: O(M) to hold the output string
  def encode(self, strs: list[str]) -> str:
    encodedWords = ""
    for word in strs:
      encodedWords += str(len(word)) + "#" + word

    return encodedWords

  # Time: O(M) | Space: O(M)
  def decode(self, s: str) -> list[str]:
    separated_words = []
    i = 0
    while i < len(s):
      if s[i].isdigit():
        index_of_symbol = s.find('#', i)
        length_of_word = int(s[i:index_of_symbol])
        index_to_start = int(index_of_symbol + 1)

        word = s[index_to_start: index_of_symbol + length_of_word + 1]
        separated_words.append(word)

        i = index_of_symbol + length_of_word + 1

    return separated_words

if __name__ == '__main__':
  words = ["neet", "my", "longing", "$", "55", "###"]

  encoded_string = Solution().encode(words)

  print("Encoded:", encoded_string)
  print("Decoded:", Solution().decode(encoded_string))
