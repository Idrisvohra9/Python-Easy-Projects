# Ok so basically the aim of this python file is that the user enters a name of an organization or an object that has a big name of more than one word, the code makes the short form of that organization's name.

# # for example if the user entered the Name of a organization as World Health Organization the code will translate it to 'WHO'.

sf=""
ff = input("Enter the Full form to convert into short form: ")

words = ff.split(" ")

for i in range(len(words)):
    sf += words[i][0].upper()

    if(i<len(words)):
        sf+="."

print("The Short Form: " + sf)