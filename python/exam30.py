fete_list = ['太后','皇后','纯妃','小嘉嫔','舒妃','皇上']

print(f'春节将至，请{fete_list}过来延禧宫小聚。')

for name in fete_list:
    print(f'春节将至，请{name}过来延禧宫小聚')

print(f'春节将至，请{fete_list[0]}过来延禧宫小聚。')
print(f'春节将至，请{fete_list[1]}过来延禧宫小聚。')
print(f'春节将至，请{fete_list[2]}过来延禧宫小聚。')
print(f'春节将至，请{fete_list[3]}过来延禧宫小聚。')
print(f'春节将至，请{fete_list[4]}过来延禧宫小聚。')
print(f'春节将至，请{fete_list[5]}过来延禧宫小聚。')

garden_name = fete_list.copy()
garden_name.insert(0,'哥哥')
garden_name.append('傅恒')
print(f'参加宴会的前三个人人员是{garden_name[:3]}')
print(f'参加宴会的前三个人人员是{garden_name[-3:]}')

