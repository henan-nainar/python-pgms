def words_suffix(word):
    if word[-3:] == 'ing':
      print(word+ 'ly')
    else:
     print(word + 'ing')
     
word=input("enter the words:  ")
words_suffix(word)
