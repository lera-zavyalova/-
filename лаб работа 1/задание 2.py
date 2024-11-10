# TODO Найдите количество книг, которое можно разместить на дискете
disk_size = 1.44
pages = 100
lines = 50
chars = 25
byte_char = 4
disk = (disk_size * 1024 * 1024)
pamat = pages * lines * chars * byte_char
knigi = disk // pamat
print("Количество книг, помещающихся на дискету:", int(knigi))
