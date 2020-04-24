# s = 'My Name is Julia'
# #
# # if 'Name' in s:
# #     print('Substring found')
#
# index = s.find('Name')
# if index != -1:
#     print(f'Substring found at index {index}')
# #возвращает индекс первого вхождения подстроки в строку

def test_substring(full_string, substring):
    assert substring in full_string, "expected '{0}' to be substring of '{1}'".format(substring, full_string)

test_substring('fulltext', 'some_value')
