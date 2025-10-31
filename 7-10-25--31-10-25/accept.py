#accept a list of words and return length of longest word

n=int(input("enter the number of words: "))
words=[]
max_len=0
for i in range(n):
    word=input("enter the word: ")
    words.append(word)
for word in words:
    if len(word)>=max_len:
        max_len=len(word)
        lengthy_word=word
print("length of the longest word ",lengthy_word,max_len)        
