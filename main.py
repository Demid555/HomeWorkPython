def work_with_phonebook():
	

    choice=show_menu()

    phone_book=read_txt('phonebook.txt')

    while (choice!=7):

        if choice==1:
            print_result(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new  number ')
            print(change_number(phone_book,last_name,new_number))
	    	
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            # write_txt('phonebook.txt',phone_book)


        choice=show_menu()









def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Поменять абоненту номер телефона\n"
          "4. Удалить абонента из справочника\n"
          "5. Найти абонента по телефону\n"
          "6. Добавить абонента в справочник")
    choice = int(input())
    return choice








def read_txt(filename): 

    phone_book=[]

    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']

	

    with open(filename,'r',encoding='utf-8') as phb:

        for line in phb:

           record = dict(zip(fields, line.split(',')))

			#dict(( (фамилия,Иванов),(имя, Точка),(номер,8928) ))
	     
    phone_book.append(record)	

    return phone_book








def write_txt(filename , phone_book):

    with open('phonebook.txt','w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):

            s=''
            for v in phone_book[i].values():

                s = s + v + ','

            phout.write(f'{s[:-1]}\n')





def print_result(filename):
    with open('phonebook.txt','r',encoding='utf-8') as file:
        for i in file:
            print('\n', i.strip())
    
    
def find_by_lastname(filename, last_name):
    with open('phonebook.txt','r',encoding='utf-8') as file:
        s = ''
        for v in file:
            if last_name in v:
                s = s + v + ','
                return f'\n{s[:-1]}\n'
                    
            
def change_number(filename, last_name, new_number):
    
    
    updated = False
    with open('phonebook.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
    with open('phonebook.txt', 'w', encoding='utf-8') as file:
        for line in lines:
            lines = line.strip().split(',')
            if lines[0] == last_name:
                lines[2] = new_number  
                updated = True
            file.write(''.join(lines) + '\n')

    return updated



def delete_by_lastname(phone_book,last_name):
     updated = False
     with open('phonebook.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    
     with open('phonebook.txt', 'w', encoding='utf-8') as file:
        for line in lines:
            lines = line.strip().split(' ')
            if last_name in line:
                lines.clear()  
                updated = True
            file.write(''.join(lines) + '\n')

     return updated

def find_by_number(phone_book,number):
     with open('phonebook.txt','r',encoding='utf-8') as file:
        s = ''
        for v in file:
            if number in v:
                s = s + v + ','
                return f'\n{s[:-1]}\n'

def add_user(phone_book,user_data):
    data = open('phonebook.txt', 'a', encoding='utf-8')  
    user = user_data.strip().split()
    data.write(' , '.join(user) + '\n')

work_with_phonebook()