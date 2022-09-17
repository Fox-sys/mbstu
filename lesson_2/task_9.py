n = int(input())

hours = n // 60
minutes = n % 60

days = hours // 24
hours -= days * 24
print(f'{hours}:{minutes}')
