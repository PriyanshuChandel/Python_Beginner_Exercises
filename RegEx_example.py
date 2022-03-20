"""Given a string with a lot of phone number, search for number which is starting with +91 and having 10 digits"""
Mystr2 = '''+91 99999-99999 , +91 55555-55555 , +65 98938929 , +65 294428 +91 33333-33333'''
Pattern2 = re.compile(r'\+91 \d{5}-\d{5}')
Matches = Pattern2.finditer(Mystr2)
for Match in Matches:
    print(Match)
