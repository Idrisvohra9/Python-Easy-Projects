print("SUBJECTS WISE MARKS:")
english=int(input("ENG->"))
hindi=int(input("HIN->"))
gujarati=int(input("GUJ->"))
grade = (english + hindi +gujarati)/3
if grade>=40:
  print("Pass")
else:
  print("Fail")
