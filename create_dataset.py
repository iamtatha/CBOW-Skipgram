import nltk

analogy = open("Analogy_dataset.txt")
s = analogy.read()

words = []
word = ''

for i in s:
    if(i == " " or i == "\n"):
        if(word not in words):
            words.append(word)
        word = ''
    
    else:
        word += i

print(len(words))
print(words[:50])
print(words)
print(words[50:100])
print(words[100:])


"""

['Riga', 'Latvia', 'India', 'Asia', 'Paris', 'Europe', 'Nigeria', 'Africa', 'France', 'Kenya', 'Netherlands', 'Mumbai', 
'Nairobi', 'Maharastra', 'Karnataka', 'Bengaluru', 'Telengana', 'Hyderabad', 'Odisha', 'Bhubaneswar', 'Gujurat', 'Gandhinagar', 
'Bihar', 'Patna', 'Chhattisgarh', 'Raipur', 'Assam', 'Dispur', 'Goa', 'Panaji', 'Rajasthan', 'Jaipur', 'Jharkhand', 'Ranchi', 
'Punjab', 'Chandigarh', 'Tripura', 'Agartala', 'Kerala', 'Thiruvananthapuram', 'Delhi', 'Serbia', 'Belgrade', 'Spanish', 'Arabic', 
'Syria', 'English', 'Mouse', 'Squeak', 'Elephant']



"""