#from string import ascii_letters, digits

def get_index_different_char(chars):
    alnum = [char for char in chars if str(char).isalnum()]
    not_alnum = [char for char in chars if not str(char).isalnum()]
    diff_char = min(alnum, not_alnum, key=len)
    return chars.index(diff_char[0])


sample1 = ['A', 'f', '.', 'Q', 2]  # returns index 2 (dot is non-alphanumeric among alphanumerics)
sample2 = ['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' is alphanumeric among non-alphanumerics)

print('sample1', get_index_different_char(sample1))
print('sample2', get_index_different_char(sample2))

