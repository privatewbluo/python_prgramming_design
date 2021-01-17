###
### 练习str   list
### 2021-01-16

### function :将用户输入的日期转


def main():
    month ,date ,year = input('please input your date (mm-dd-yyyy):').split('-')
    month = int(month)
    months = ['Jan','Feb','Mar','May','Apr','June','July','Aug','Sep','Oct','Nov','Dec']
    print(month)
    print('the data is',months[month-1],date,',',year)
    print('the data is {0}{1},{2}'.format(months[month-1],date,year))
    print('the data is {}'.format(date))
main()

