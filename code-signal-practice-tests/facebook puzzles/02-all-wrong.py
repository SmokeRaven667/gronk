# Write any import statements here

def getWrongAnswers(N: int, C: str) -> str:
  # Write your code here
  answers = []
  for letter in C:
    answer = 'B' if (letter == 'A') else 'A'
    answers.append(answer)
  return ''.join(answers)


print(getWrongAnswers(3, 'ABA'))
print(getWrongAnswers(3, 'BBBBBB'))