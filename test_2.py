data = (3, None, 'Leha', None, '33333333333', 'Saratov', 2000,)

a = ("SELECT * from update_user(%s, %s, %s, %s, %s, %s, %s)" % (data))
print(a)
