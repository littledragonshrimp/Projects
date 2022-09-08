string = 'The quick brown fox jumps over the lazy dog'
test = 'attach'
encode = string.encode()
print(test.__add__(' ' + encode.decode()))

