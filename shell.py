from ml.classify import classify

print(classify("server crashed need immediate fix"))      # expect "urgent"
print(classify("buy milk and bread for breakfast"))         # expect "personal"
print(classify("brainstorm a new feature for the app"))     # expect "idea"
print(classify("update the sprint board with new tickets")) # expect "work"