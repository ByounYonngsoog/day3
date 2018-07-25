person={'name':'Nick','address':'cheonan','email':'nick@gmail.com'}
print(person)
print(person['name'])
print(person['email'])
print(person.items())
person['name']='James'
for key, value in person.items():
    print("\nKey : " + key)
    print("Value : " + value)

    print("\nKey \\'" + key + "'")
    print("Value \\'" + value + "'")

    print('\nKey \\"' + key + '"')
    print('Value \\"' + value + '"')

# Key \ 'name'
# Value \ 'Nick'



