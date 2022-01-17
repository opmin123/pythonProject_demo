# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #============= 列表demo sorted , reverse , sort 用法==========
   place = ['北京','上海','云南','厦门','广东','台湾']
   print(place)
   print(sorted(place))
   print(place)
    #按字母顺序相反输出列表
   print(sorted(place,reverse=True))
   print(place)
   place.reverse()
   print(place)
   place.reverse()
   print(place)
   place.sort()
   print(place)
   print(len(place))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
