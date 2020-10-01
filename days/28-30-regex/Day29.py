import re

string = '''
abcdefgh acddef abcdedfg ABCDEFGH !a!b!c@d#e 619-514-4975 www.dasadfa.com awodkwapodk@yapjkdw.com
456-123-7895
dawopkda@hoakwh.com
https://dopawkjdaw.com
https://dwajdpoawdwa.net
weliadjwaoidjuwa.com
google.com
yourdawdawdom.com
https://yourmom.com

123-456-7890
123.456.7890
123*456*7890
(619)492-3891
222-222-2222
'''

matches = re.findall('\(?\d{3}.\d{3}.\d{4}', string)
for match in matches:
    print(match)

print(f'{"-" * 60}')

matches = re.findall(r'(https://)?\w*\.(com|net)', string)
print(matches)
for match in matches:
    print(match)

print(re.sub('\(?\d{3}.\d{3}.\d{4}', 'Phone number', string))

# for match in matches:
#     print(match)
