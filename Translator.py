#print("hello this is a new repo".split())


dict = {
    "smile" : "😁",
    "dog" : "🐶",
    "sky" : "🌄",
    "heart" : "🫀",
    "red" : "🔴",


}
while True:
    s = input()
    l = ""
   # put my forloop here 
    for word in s.split():
        if word in dict:
            l = l + dict[word]  
        else:
            l = word + l

        
    print(l)
    
























#1 how to store a map of certain words to certain emoji??
# 2 How to retrieve those emojis 
#  start? get user input using input()
