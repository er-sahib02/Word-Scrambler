import random
def scramble(a):
    allowed_marks = [".", ";", "!", ",", "?"]
    new = []
    for i in a:
        length = len(i)
        
        if length <= 2:
            new.append(i)
            
        elif i[length-1] in allowed_marks:
            start = i[0]
            if i[length-3] == "'":
                end = i[length-3:]
                middle = i[1:length-3]
            else:
                end = i[length-2:]
                middle = i[1:length-2]
            temp = list(middle)
            random.shuffle(temp)
            shuffle = ''.join(temp)
            

            if shuffle == middle:
                random.shuffle(temp)
                shuffle = ''.join(temp)
        
            new_word = start + shuffle + end
            new.append(new_word)
            
        else:
            if i[length-2] == "'":
                end = i[length-2:]
                middle = i[1:length-2]
            else:
                end = i[length-1:]
                middle = i[1:length-1]
            start = i[0]
            temp = list(middle)
            random.shuffle(temp)
            shuffle = ''.join(temp)
            if shuffle == middle:
                random.shuffle(temp)
                shuffle = ''.join(temp)
        
            new_word = start + shuffle + end
            new.append(new_word)
    return (new)

name = input("Enter the file name to be scrambled (E.g. abc.txt): ")
with open(name, "r") as file:
    content = file.readlines()
for i in content:
    a = i.split(" ")


shuffled_file = scramble(a)

shuffled_file_name = "Scrambled_" + name


with open(shuffled_file_name, "w") as new:
    for word in shuffled_file:
        new.write(word + " ")

