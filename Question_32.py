#Write a function to find in which line of file does the word "Learning" occure first print -1 if word not found.

def check_for_line():
    word = "dev"
    data = True
    line_no= 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return 
            line_no += 1
    return -1
print(check_for_line())

        