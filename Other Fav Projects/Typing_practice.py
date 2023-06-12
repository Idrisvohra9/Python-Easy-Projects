import time
import random
import os
import trmnl_colors as clr
list1=["The","army","in","India","are","the","only","ones","in","the","whole","world","who","get","undying","respect","form","the","civils","residing","in","the","country.","The","color","of","the","Indian","flag","consists","of","orange,","white,","green","and","a","blue","cycle","tyre","like","symbol","is","called","Ashok","chakra."]

list2=["Germany","is","one","of","beautiful,","richest","and","Popular","nation","that","everyone","knows","and","want","to","visit","Germany","is","a","part","of","central","europe.","Germany","has","common","border","with","Denmark,","the","Netherlands,","Belgium","Poland","etc.","The","government","is","a","fedral","republic","system.","The","country","is","full","of","river","valley","and","rising","and","falling","hills","also","the","snow","covered","alps","and","bushy","mountains."]

str1="One of the most known civilizations that thrived in Mexico was called the Mayans. The Mayans where considered to be pre-Columbian America's most brilliant civilization. They thrived between 250 and 900 A.D. Thanks to the Mayans we are able to say that we have a calendar and a writing system. They also built cities that functioned as hubs for the surrounding farm towns."

str2="Japan is an island country in the North Pacific Ocean. It lies off the northeast coast of mainland Asia and faces Russia, Korea, and China. Four large islands and thousands of smaller ones make up Japan. The four major islands- Hokkaido, Honshu, Kyushu and Shikoku form a curve that extends for about 1,900 kilometres. Topography Japan is a land of great natural beauty. mountains and hills cover about 70% of the country. IN fact, Japanese islands consist of the rugged upper part of a great mountain range that rises from the floor of the North Pacific Ocean."

list3=str1.split(" ")
list4=str2.split(" ")

list_all=[list1,list2,list3,list4]

sel_list=random.choices(list_all)

sel_list = [ item for elem in sel_list for item in elem] # List comprehension will convert the nested list to simple list so that it could be written in the file.
# print(len(sel_list))
mistakes=0
correct=0
i=0
start=time.time()
while i<=len(sel_list)-1:
    clr.cyanbg()
    print(sel_list[i],end="")
    print()
    clr.reset()
    clr.magentaB()
    inp=input()
    os.system("cls")
    if inp!=sel_list[i]:
        mistakes+=1
    else:
        correct+=1
    i+=1

end=time.time()
minutes=int(end-start)/60
wpm=len(sel_list)/minutes
accuracy=(correct/len(sel_list))*100
clr.reset()
clr.yellowB()
print(f"Total mistakes: {mistakes} \nWPM: {wpm} \nAccuracy: {accuracy} \nTotal minutes: {minutes}")
clr.reset()