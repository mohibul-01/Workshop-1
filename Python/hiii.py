email = 'alice.johnson@company.com'
print(f'Email: {email}')

#Now, call the .find() method on email and pass it '@' to find the position of the at sign in the email string. Assign the result to a variable named at_position.
# Then print at_position so that the output reads: Position of @: 13.

at_position = email.find('@')
print(f'Position of @: {at_position}')

#Use slicing on email to extract everything before at_position, and store the result in a variable named username.
#Then print username so that the output reads Username: alice.johnson.

username = email[:at_position]
print(f'Username:{username}')

#Create a variable named has_at that checks if the character @ is in email.
#Then print has_at so that the output reads: Has @ symbol: True.

has_at = '@' in email
print(f'Has @ symbol: {has_at}')

#Create another variable named has_com that checks if .com is in email.
#Then print has_com so that the output reads: Has .com: True.

has_com = '.com' in email
print(f'Has .com: {has_com}')

#Create a variable messy_name and assign it the string sARaH dAVis with two leading spaces and two trailing spaces. Then print it so that the output reads: messy Name:   sARaH dAVis  

messy_name = '  sARaH dAVis  '
print(f"Original name: '{messy_name}'")

#Create a variable named clean_name and assign it the result of calling .title() on messy_name.

clean_name = messy_name.title()

#Update the value of clean_name to call .strip() on messy_name before .title().
#After that, print clean_name so that the output reads Cleaned name: 'Sarah Davis'.

clean_name = messy_name.strip().title()
print(f"Cleaned name: '{clean_name}'")

#Create a variable messy_email and assign it the string SARAH.DAVIS@COMPANY.COM with two leading spaces and two trailing spaces.
#Also, call .strip().lower() on messy_email and assign the result to a variable clean_email.

messy_email = '  SARAH.DAVIS@COMPANY.COM  '
print(f"Original email: '{messy_email}'")
clean_email = messy_email.strip().lower()
print(f"Cleaned email: '{clean_email}'")

#Create a variable named name_badge and assign it the result of calling the .upper() method on clean_name.
#Then print name_badge so that the output reads: Name badge: SARAH DAVIS.

name_badge = clean_name.upper()
print(f"Name badge: '{name_badge}'")

#Find the position of the @ character in clean_email and store it in at_pos. Then use slicing to extract everything before @ and store it in email_user.
#Then print clean_email and email_user

at_pos = clean_email.find('@')
email_user = clean_email[:at_pos]
print(f"Clean email: '{clean_email}'")
print(f"Email user: '{email_user}'")

#Replace . with a single space in email_user, and then call .title() on the result. Assign the result to a variable named display_name.
#Then print display_name so that the output reads: Display name: Sarah Davis.

display_name = email_user.replace('.', ' ').title()
print(f"Display name: '{display_name}'")

#Create a variable phone and assign it the string 123-456-7890. Then replace - with an empty string and assign the result to a variable named phone_clean.

phone = '123-456-7890'
phone_clean = phone.replace('-', '')
print(f"Phone with dashes: {phone}")
print(f"Phone without dashes: {phone_clean}")

#Create a variable full_address and assign it the string 123 Main Street, Springfield, IL. Then create address_parts by splitting on a comma followed by a single space.
#Then print address_parts so that the output reads Address parts: ['123 Main Street', 'Springfield', 'IL'].

full_address = '123 Main Street, Springfield, IL'
address_parts = full_address.split(', ')
print(f"Address parts: {address_parts}")

#Join the elements from address_parts with a | character surrounded by spaces and assign the result to a variable named rejoined.
#Then print rejoined so that the output reads: Rejoined: 123 Main Street | Springfield | IL.

rejoined = ' | '.join(address_parts)
print(f'Rejoined: {rejoined}')

#Create a variable employee_code and assign it the string EMP-2024-SD. Then create a starts_with_emp variable that checks if employee_code starts with EMP.

employee_code = 'EMP-2024-SD'
starts_with_emp = employee_code.startswith('EMP')

#Create a variable ends_with_com that checks if clean_email ends with .com.

ends_with_com = clean_email.endswith('.com')

#Now print employee_code, starts_with_emp, clean_email, and ends_with_com so that the output reads:
#Example Code
#Code: EMP-2024-SD
#Starts with EMP: True
#Clean email: sarah.davis@company.com
#Ends with .com: True

print(f"Code: {employee_code}")
print(f"Starts with EMP: {starts_with_emp}")
print(f"Clean email: {clean_email}")
print(f"Ends with .com: {ends_with_com}")

#Create two variables named dot_count and dash_count. dot_count should count how many . characters appear in clean_email, and dash_count should count how many - characters appear in employee_code.

dot_count = clean_email.count('.')
dash_count = employee_code.count('-')

#Now print dot_count and dash_count so that the output reads:
#Dot count in email: 2
#Dash count in employee code: 2

print(f"Dot count in email: {dot_count}")
print(f"Dash count in employee code: {dash_count}")



#With that, your employee profile validator workshop is complete!