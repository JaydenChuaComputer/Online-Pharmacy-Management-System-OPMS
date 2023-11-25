
#CHUA YI XUAN
#TP068394


'''------------------------------------------------------------------------'''
# This function is for admin to delete the medicine
def delete_medicine():
    try:
        fileHandler = open('medicine.txt','r')
    except:
        print ('File cannot be opened:')
        exit()
    # This is to open the medicine text file so that the system can know what medicine is exist

    search_key = input('\n\tEnter name of medicine you want to delete: ')
    # This is to let the admin to type the medicine name which they wanted to be delete

    move = False
    for line in fileHandler:
        line = line.rstrip()
        if not search_key.lower() in line.lower(): # This is to search for the medicine 
            continue
        delete = line 
        move = True
        break
    # This is to read the line which is going to be deleted

    if (move):
        print("\n",search_key,'deleted successfully.')
    else:
        print("\nWe couldn't find anything for",search_key,", try to refine your search.")
        admin_what_do_you_want_to_do()
       
    fileHandler.close()

    a_file = open("medicine.txt", "r")
    lines = a_file.readlines()
    a_file.close()
    # This is to read the details exist in medicine text file

    new_file = open("medicine.txt", "w")
    for line_ in lines:
        if line_.strip("\n") != delete:
            new_file.write(line_)
    new_file.close()
    # This is to enter the details of the medicine back into the medicine text file but without the deleted medicine

    admin_what_do_you_want_to_do()    
'''------------------------------------------------------------------------'''
# This function is for admin to modify the medicine remark
def modify_medicine_remark():
    try:
        fileHandler = open('medicine.txt','r+')
    except:
        print ('File cannot be opened:')
        exit()
    # This is to open the medicine text file so that the system can know what medicine is exist and also let the system to add details

    search_key = input('Type medicine name: ')
    replace = input ("Type new medicine remark: ")
    # This is to let the admin to type the medicine name and the new remark

    move = False
    for line in fileHandler:
        line = line.rstrip()
        if not search_key.lower() in line.lower(): # This is to search whether the medicine exist
            continue
        lines=line.split('!')
        lines[5]= replace # This is to modify the remark
        for fs in lines:
            if len(fs)>0:
                fileHandler.write(fs)
                fileHandler.write('!')
        fileHandler.write('\n')
        move = True
        delete = line  # This is to read the line which is going to be deleted
        continue

    if (move):
        print("\n",'Medicine remark modified sucessfully!')
    else:
        print("\nWe couldn't find anything for",search_key,", try to refine your search.")
        admin_what_do_you_want_to_do()
       
    fileHandler.close()

    old_file = open("medicine.txt", "r")
    lines = old_file.readlines()
    old_file.close()
    # This is to read the details exist in medicine text file

    new_file = open("medicine.txt", "w")
    for line_ in lines:
        if line_.strip("\n") != delete:
            new_file.write(line_)
    new_file.close()
    # This is to enter the details of the medicine back into the medicine text file but without the medicine with the old remark

    admin_what_do_you_want_to_do() 
'''------------------------------------------------------------------------'''
# This function is for admin to modify the medicine direction of use
def modify_medicine_directions_of_use():
    try:
        fileHandler = open('medicine.txt','r+')
    except:
        print ('File cannot be opened:')
        exit()
    # This is to open the medicine text file so that the system can know what medicine is exist and also let the system to add details

    search_key = input('Type medicine name: ')
    replace = input ("Type new medicine directions of use: ")
    # This is to let the admin to type the medicine name and the new directions of use

    move = False
    for line in fileHandler:
        line = line.rstrip()
        if not search_key.lower() in line.lower(): # This is to search whether the medicine exist
            continue
        lines=line.split('!')
        lines[4]= replace # This is to modify the directions of use
        for fs in lines:
            if len(fs)>0:
                fileHandler.write(fs)
                fileHandler.write('!')
        fileHandler.write('\n')
        move = True
        delete = line # This is to read the line which is going to be deleted
        continue

    if (move):
        print("\n",'Medicine directions of use modified sucessfully!')
    else:
        print("\nWe couldn't find anything for",search_key,", try to refine your search.")
        admin_what_do_you_want_to_do()
       
    fileHandler.close()

    old_file = open("medicine.txt", "r")
    lines = old_file.readlines()
    old_file.close()
    # This is to read the details exist in medicine text file

    new_file = open("medicine.txt", "w")
    for line_ in lines:
        if line_.strip("\n") != delete:
            new_file.write(line_)
    new_file.close()
    # This is to enter the details of the medicine back into the medicine text file but without the medicine with the old direction of use

    admin_what_do_you_want_to_do() 
'''------------------------------------------------------------------------'''
# This function is for admin to modify the medicine specifications
def modify_medicine_spec():
    try:
        fileHandler = open('medicine.txt','r+')
    except:
        print ('File cannot be opened:')
        exit()
    # This is to open the medicine text file so that the system can know what medicine is exist and also let the system to add details

    search_key = input('Type medicine name: ')
    replace = input ("Type new medicine specifications: ")
    # This is to let the admin to type the medicine name and the new specifications

    move = False
    for line in fileHandler:
        line = line.rstrip()
        if not search_key.lower() in line.lower(): # This is to search whether the medicine exist
            continue
        lines=line.split('!')
        lines[3]= replace # This is to modify the specifications
        for fs in lines:
            if len(fs)>0:
                fileHandler.write(fs)
                fileHandler.write('!')
        fileHandler.write('\n')
        move = True
        delete = line  # This is to read the line which is going to be deleted
        continue

    if (move):
        print("\n",'Medicine specifications modified sucessfully!')
    else:
        print("\nWe couldn't find anything for",search_key,", try to refine your search.")
        admin_what_do_you_want_to_do()
       
    fileHandler.close()

    old_file = open("medicine.txt", "r")
    lines = old_file.readlines()
    old_file.close()
    # This is to read the details exist in medicine text file

    new_file = open("medicine.txt", "w")
    for line_ in lines:
        if line_.strip("\n") != delete:
            new_file.write(line_)
    new_file.close()
    # This is to enter the details of the medicine back into the medicine text file but without the medicine with the old specifications

    admin_what_do_you_want_to_do() 
'''------------------------------------------------------------------------'''
# This function is for admin to modify the medicine price
def modify_medicine_price():
    try:
        fileHandler = open('medicine.txt','r+')
    except:
        print ('File cannot be opened:')
        exit()
    # This is to open the medicine text file so that the system can know what medicine is exist and also let the system to add details

    search_key = input('Type medicine name: ')
    replace = input ("Type new medicine price: ")
    # This is to let the admin to type the medicine name and the new medicine price

    move = False
    for line in fileHandler:
        line = line.rstrip()
        if not search_key.lower() in line.lower(): # This is to search whether the medicine exist
            continue
        lines=line.split('!')
        lines[2]= replace # This is to modify the medicine price
        for fs in lines:
            if len(fs)>0:
                fileHandler.write(fs)
                fileHandler.write('!')
        fileHandler.write('\n')
        move = True
        delete = line    # This is to read the line which is going to be deleted
        continue

    if (move):
        print("\n",'Medicine price modified sucessfully!')
    else:
        print("\nWe couldn't find anything for",search_key,", try to refine your search.")
        admin_what_do_you_want_to_do()
       
    fileHandler.close()

    old_file = open("medicine.txt", "r")
    lines = old_file.readlines()
    old_file.close()
    # This is to read the details exist in medicine text file

    new_file = open("medicine.txt", "w")
    for line_ in lines:
        if line_.strip("\n") != delete:
            new_file.write(line_)
    new_file.close()
    # This is to enter the details of the medicine back into the medicine text file but without the medicine with the old price

    admin_what_do_you_want_to_do() 
'''------------------------------------------------------------------------'''
# This function is for admin to modify the medicine expire date
def modify_medicine_expire_date():
    try:
        fileHandler = open('medicine.txt','r+')
    except:
        print ('File cannot be opened:')
        exit()
    # This is to open the medicine text file so that the system can know what medicine is exist and also let the system to add details

    search_key = input('Type medicine name: ')
    replace = input ("Type new expire date: ")
    # This is to let the admin to type the medicine name and the new expire date

    move = False
    for line in fileHandler:
        line = line.rstrip()
        if not search_key.lower() in line.lower(): # This is to search whether the medicine exist
            continue
        lines=line.split('!')
        lines[1]= replace # This is to modify the expire date
        for fs in lines:
            if len(fs)>0:
                fileHandler.write(fs)
                fileHandler.write('!')
        fileHandler.write('\n')
        move = True
        delete = line  # This is to read the line which is going to be deleted
        continue

    if (move):
        print("\n",'Expire date modified sucessfully!')
    else:
        print("\nWe couldn't find anything for",search_key,", try to refine your search.")
        admin_what_do_you_want_to_do()
       
    fileHandler.close()

    old_file = open("medicine.txt", "r")
    lines = old_file.readlines()
    old_file.close()
    # This is to read the details exist in medicine text file

    new_file = open("medicine.txt", "w")
    for line_ in lines:
        if line_.strip("\n") != delete:
            new_file.write(line_)
    new_file.close()
    # This is to enter the details of the medicine back into the medicine text file but without the medicine with the old expire date

    admin_what_do_you_want_to_do() 
'''------------------------------------------------------------------------'''
# This function is for admin to modify the medicine name
def modify_medicine_name():
    try:
        fileHandler = open('medicine.txt','r+')
    except:
        print ('File cannot be opened:')
        exit()
    # This is to open the medicine text file so that the system can know what medicine is exist and also let the system to add details

    search_key = input('Type actual medicine name: ')
    replace = input ("Type new medicine name: ")
    # This is to let the admin to type the actual and new medicine name

    move = False
    for line in fileHandler:
        line = line.rstrip()
        if not search_key.lower() in line.lower(): # This is to search whether the medicine exist
            continue
        lines=line.split('!')
        lines[0]= replace # This is to enter the new medicine name
        for fs in lines:
            if len(fs)>0:
                fileHandler.write(fs)
                fileHandler.write('!')
        fileHandler.write('\n')
        move = True
        delete = line   # This is to read the line which is going to be deleted
        continue

    if (move):
        print("\n",'Medicine name modified sucessfully!')
    else:
        print("\nWe couldn't find anything for",search_key,", try to refine your search.")
        admin_what_do_you_want_to_do()
       
    fileHandler.close()

    old_file = open("medicine.txt", "r")
    lines = old_file.readlines()
    old_file.close()
    # This is to read the details exist in medicine text file

    new_file = open("medicine.txt", "w")
    for line_ in lines:
        if line_.strip("\n") != delete:
            new_file.write(line_)
    new_file.close()
    # This is to enter the details of the medicine back into the medicine text file but without the medicine with the old name

    admin_what_do_you_want_to_do()       
'''------------------------------------------------------------------------'''
# This function is for admin to choose how they want to modify the medicine in the system
def modify_medicine():
    print('\n\nWhat do you want to modify?')
    print('\n\t1. Medicine name \n\t2. Expire date \n\t3. Price \n\t4. Specification \n\t5. Directions of use \n\t6. Remark \n')
    choice = int(input('\nChoose the operation from the given options: '))
    # This is to let the admin to choose how they want to modify the medicine.

    if choice <= 0 or choice > 6:
        print('Invalid input')
        modify_medicine()
    elif choice == 1:
        modify_medicine_name()
    elif choice == 2:
        modify_medicine_expire_date()
    elif choice == 3:
        modify_medicine_price()
    elif choice == 4:
        modify_medicine_spec()
    elif choice == 5:
        modify_medicine_directions_of_use()         
    else:
        modify_medicine_remark()
'''------------------------------------------------------------------------'''
# This function is for admin to search the order by medicine name
def search_order_by_medicine_name():
    search = str(input('\n\tMedicine name: '))
    order = open('order.txt','r')# This is to open the order text file so that the system can know what order is exist

    move=False
    for line in order:
        name,address,email,phone,medicine,quantity = line.split('!')
        if medicine==search:
            print('\n\tCustomer username: ',name)
            print('\tHome address: ',address)
            print('\tEmail: ',email)
            print('\tContact number: ',phone)
            print('\tMedicine name: ',medicine)
            print('\tQuantity: ',quantity)
            move = True
        else:
            continue
    # This is to show the order with a specific medicine

    if (move):
        print('')
    else:
        print("\nMedicine doesn't exist or no customer place order to this medicine yet.")

    order.close
    
    admin_what_do_you_want_to_do()
'''------------------------------------------------------------------------'''
# This function is for admin to search the order by customer name
def search_order_by_customer_name():
    search = str(input('\n\tCustomer name: '))
    order = open('order.txt','r')# This is to open the order text file so that the system can know what order is exist

    move=False
    for line in order:
        name,address,email,phone,medicine,quantity = line.split('!')
        if name==search:
            print('\n\tCustomer username: ',name)
            print('\tHome address: ',address)
            print('\tEmail: ',email)
            print('\tContact number: ',phone)
            print('\tMedicine name: ',medicine)
            print('\tQuantity: ',quantity)
            move = True
        else:
            continue
    # This is to show the order made by a specific customer
        
    if (move):
        print('')
    else:
        print("\nCustomer doesn't exist or Customer don't have any order.")
        
    order.close
    
    admin_what_do_you_want_to_do()
'''------------------------------------------------------------------------'''
# This function is for admin to choose how they want to search the order in the system
def search_orders():
    print('How do you want to search from?')
    print('\n\t1. Search by customer name \n\t2. Search by medicine name \n')
    choice = int(input('Choose the operation from the given options: '))
    # This is to let the admin to choose how they want to search the order.

    if choice <= 0 or choice > 2:
        print('Invalid input')
        search_orders()
    elif choice == 1:
        search_order_by_customer_name()
    else:
        search_order_by_medicine_name()    
'''------------------------------------------------------------------------'''
# This function is for admin to view all the order in the system
def view_orders():
    order = open('order.txt','r')
    # This is to open the order text file so that the system can know what order is exist

    for line in order:
        name,address,email,phone,medicine,quantity = line.split('!')
        print('\n\tCustomer username: ',name)
        print('\tHome address: ',address)
        print('\tEmail: ',email)
        print('\tContact number: ',phone)
        print('\tMedicine name: ',medicine)
        print('\tQuantity: ',quantity)
    # This is to show all the orders made by customer
    
    order.close
    
    admin_what_do_you_want_to_do()    
'''------------------------------------------------------------------------'''
# This function is for registered customer to view their order
def view_order():
    order = open('order.txt','r')
    # This is to open the order text file so that the system can know what order is exist

    move=False
    for line in order:
        name,address,email,phone,medicine,quantity = line.split('!')
        if (name==cus_username):
            print('\n\tUsername: ',name)
            print('\tHome address: ',address)
            print('\tEmail: ',email)
            print('\tContact number: ',phone)
            print('\tMedicine name: ',medicine)
            print('\tQuantity: ',quantity)
            move=True
        else:
            continue
    # This is to show the order made by a specific customer

    order.close

    if (move):
        print('')
    else:
        print("\nYou have not order anything yet.")
        
    registered_customer_what_do_you_want_to_do()
'''------------------------------------------------------------------------'''
# This function is for registered customer to place an order
## assumptions: Roxithromycin & Isotretinoin & Alendronate
def place_order():
    print("\n\nEnter the details of your order.")

    try:
        fileHandler = open('medicine.txt','r')
    except:
        print ('File cannot be opened:')
        exit()
    # This is to open the medicine text file so that the system can know what medicine is exist

    medicine_name = str(input("\n\tMedicine name: "))
    quantity = str(input("\tQuantity: "))

    move = False
    for line in fileHandler:
        line = line.rstrip()
        if not medicine_name.lower() in line.lower(): 
            continue
        move = True
    # This is to search weather the medicine typed by the customer is exist in the system

    if (move):
        print('')
    else:
        print("\nMedicine doesn't exist.")
        place_order()
       
    fileHandler.close()

    database = open('database.txt','r')
    # This is to open the database text file so that the system can know the details of the customer

    for line in database:
        user_id,user_name,user_password,user_address,user_email,user_phone,user_gender,user_dob = line.split('!')
        if (user_name==cus_username and user_password==cus_password):
            address = user_address
            email = user_email
            phone = user_phone
            break
        else:
            continue
    # This is for the system to know the details of the customer
    
    database.close
    
    order = open('order.txt','a')# This is to open the order text file so that the system can add a new order
    order.write(cus_username + '!' + address + '!' + email + '!' + phone + '!' + medicine_name + '!' + quantity + '\n')
    print ('\nYou have placed an order successfully!')
    order.close()
    
    registered_customer_what_do_you_want_to_do()
'''------------------------------------------------------------------------'''
# This function is for registered customer to view all their personal information
def view_personal_information():
    database = open('database.txt','r')
    # This is to open the database text file so that the system can know the personal information of the customer

    for line in database:
        user_id,user_name,user_password,user_address,user_email,user_phone,user_gender,user_dob = line.split('!')
        if (user_name==cus_username and user_password==cus_password):
            print('\n\tUser ID: ',user_id)
            print('\tUsername: ',user_name)
            print('\tPassword: ',user_password)
            print('\tHome address: ',user_address)
            print('\tEmail address: ',user_email)
            print('\tContact number: ',user_phone)
            print('\tGender: ',user_gender)
            print('\tDate of birth: ',user_dob)
            break
        else:
            continue
    # The details of the personal information would be displayed here
    
    database.close
    
    registered_customer_what_do_you_want_to_do()
'''------------------------------------------------------------------------'''
# This function is for registered customer to search medicine in the system
def search_medicine_customer():
    try:
        fileHandler = open('medicine.txt','r')
    except:
        print ('File cannot be opened:')
        exit()
    # This is to open the medicine text file so that the registered customer can search for the details of medicine

    search_key = input('Type what you want to search: ')
    # Registered customer can type medicine details they wanted to search for

    move = False
    for line in fileHandler:
        line = line.rstrip()
        if not search_key.lower() in line.lower(): 
            continue
        name,expire_date,price,specifications,directions_of_use,remark,empty = line.split('!')
        print("\n\tMedicine name: ",name)
        print("\tExpire date: ",expire_date)
        print("\tPrice: ",price)
        print("\tSpecifications: ",specifications)
        print("\tDirections of use: ",directions_of_use)
        print("\tRemark: ",remark)
        print('\n')
        move = True
    # The system is searching for the medicine

    if (move):
        print('')
    else:
        print("\nWe couldn't find anything for",search_key,", try to refine your search.")
       
    fileHandler.close()
    
    registered_customer_what_do_you_want_to_do()
'''------------------------------------------------------------------------'''
# This function is for admin to search medicine in the system
def search_medicine_admin():
    try:
        fileHandler = open('medicine.txt','r')
    except:
        print ('File cannot be opened:')
        exit()
    # This is to open the medicine text file so that the admin can search for the details of medicine

    search_key = input('Type what you want to search: ')
    # Admin can type medicine details they wanted to search for

    move = False
    for line in fileHandler:
        line = line.rstrip()
        if not search_key.lower() in line.lower(): 
            continue
        name,expire_date,price,specifications,directions_of_use,remark,empty = line.split('!')
        print("\n\tMedicine name: ",name)
        print("\tExpire date: ",expire_date)
        print("\tPrice: ",price)
        print("\tSpecifications: ",specifications)
        print("\tDirections of use: ",directions_of_use)
        print("\tRemark: ",remark)
        print('\n')
        move = True
    # The system is searching for the medicine

    if (move):
        print('')
    else:
        print("\nWe couldn't find anything for",search_key,", try to refine your search.")
       
    fileHandler.close()
    
    admin_what_do_you_want_to_do()
'''------------------------------------------------------------------------'''
# This function is for new customer to view all the medicine in the system
def new_customer_view_medicine():
    try:
        fileHandler = open('medicine.txt','r')
    except:
        print ('File cannot be opened:')
        exit()
    # This is to open the medicine text file so that the new customer can view the details of all medicine

    for line in fileHandler:
        line = line.rstrip()
        name,expire_date,price,specifications,directions_of_use,remark,empty = line.split('!')
        print("\n\tMedicine name: ",name)
        print("\tExpire date: ",expire_date)
        print("\tPrice: ",price)
        print("\tSpecifications: ",specifications)
        print("\tDirections of use: ",directions_of_use)
        print("\tRemark: ",remark)
        print('\n')
    fileHandler.close()
    # This is to display the details of all medicine
    
    new_customer_what_do_you_want_to_do()
'''------------------------------------------------------------------------'''
# This function is for registered customer to view all the medicine in the system
def reg_customer_view_medicine():
    try:
        fileHandler = open('medicine.txt','r')
    except:
        print ('File cannot be opened:')
        exit()
    # This is to open the medicine text file so that the registered customer can view the details of all medicine

    for line in fileHandler:
        line = line.rstrip()
        name,expire_date,price,specifications,directions_of_use,remark,empty = line.split('!')
        print("\n\tMedicine name: ",name)
        print("\tExpire date: ",expire_date)
        print("\tPrice: ",price)
        print("\tSpecifications: ",specifications)
        print("\tDirections of use: ",directions_of_use)
        print("\tRemark: ",remark)
        print('\n')
    fileHandler.close()
    # This is to display the details of all medicine
    
    registered_customer_what_do_you_want_to_do()
'''------------------------------------------------------------------------'''
# This function is for admin to view all the medicine in the system
## assumptions: Roxithromycin & Isotretinoin & Alendronate
def admin_view_medicine():
    try:
        fileHandler = open('medicine.txt','r')
    except:
        print ('File cannot be opened:')
        exit()
    # This is to open the medicine text file so that the admin can view the details of all medicine

    for line in fileHandler:
        line = line.rstrip()
        name,expire_date,price,specifications,directions_of_use,remark,empty = line.split('!')
        print("\n\tMedicine name: ",name)
        print("\tExpire date: ",expire_date)
        print("\tPrice: ",price)
        print("\tSpecifications: ",specifications)
        print("\tDirections of use: ",directions_of_use)
        print("\tRemark: ",remark)
        print('\n')
    fileHandler.close()
    # This is to display the details of all medicine
    
    admin_what_do_you_want_to_do()
'''------------------------------------------------------------------------'''
# This function is for admin to upload medicine into the system
## assumptions: Roxithromycin & Isotretinoin & Alendronate
def upload_medicine():
    try:
        fileHandler = open('medicine.txt','a+')
    except:
        print ('File cannot be opened:')
        exit()
    # This is to open the medicine text file so that the admin can upload medicine to the system

    number = int(input("\n\nHow many medicine do you want to upload?"))
    medicine = []
    for line_ in range(number):
        med = []
        medicine_name = input('\n\n\tMedicine name: ')
        med.append(medicine_name)
        expire_date = input('\tExpire date (DD/MM/YYYY): ')
        med.append(expire_date)
        price = input('\tPrice: ')
        med.append(price)
        specification = input('\tSpecification: ')
        med.append(specification)
        directions_of_use = input('\tDirections of use: ')
        med.append(directions_of_use)
        remark = input('\tRemark: ')
        med.append(remark)
        medicine.append(med)
    # The admin can upload the details of the medicine here

    for med in medicine:
        for me in med:
            fileHandler.write(me)
            fileHandler.write('!')
        fileHandler.write('\n')
    fileHandler.close()
    
    print ('\nYou have added a new medicine!')
    admin_what_do_you_want_to_do()      
'''------------------------------------------------------------------------'''
# This function is for registered customer to choose what operation they want to do
def registered_customer_what_do_you_want_to_do():
    print('\n\nWhat do you want to do by using OPMS?')
    print('\n\t1. View all medicine')
    print('\n\t2. Place order')
    print('\n\t3. View order')
    print('\n\t4. View Personal Information')
    print('\n\t5. Search medicine')
    print('\n\t6. Logout')
    choice = int(input('\nChoose the operation from the given options: '))
    # Customer can choose what they want to do using this system

    if choice <=0 or choice > 6:
        print('Invalid input')
        registered_customer_what_do_you_want_to_do()
    else:
        if choice == 1:
            reg_customer_view_medicine()
        elif choice == 2:
            place_order()
        elif choice == 3:
            view_order()
        elif choice == 4:
            view_personal_information()
        elif choice == 5:
            search_medicine_customer()
        else:
            menu()
'''------------------------------------------------------------------------'''
# This function is for admin to choose what operation they want to do
def admin_what_do_you_want_to_do():
    print('\n\nWhat do you want to do by using OPMS?')
    print('\n\t1. Upload medicine detail in system')
    print('\n\t2. View all medicine')
    print('\n\t3. Modify medicine information')
    print('\n\t4. Delete medicine')
    print('\n\t5. Search medicine')
    print('\n\t6. View orders of customers')
    print('\n\t7. Search orders of customers')
    print('\n\t8. Logout')
    choice = int(input('\nChoose the operation from the given options: '))
    # Admin can choose what they want to do using this system

    if choice <=0 or choice > 8:
        print('Invalid input')
        admin_what_do_you_want_to_do()
    else:
        if choice == 1:
            upload_medicine()
        elif choice == 2:
            admin_view_medicine()
        elif choice == 3:
            modify_medicine()
        elif choice == 4:
            delete_medicine()
        elif choice == 5:
            search_medicine_admin()
        elif choice == 6:
            view_orders()
        elif choice == 7:
            search_orders()
        else:
            menu()

'''------------------------------------------------------------------------'''
# This function is for registered customer to login to the system
## assumptions: username-Admin, password-12345678
def customer_login():
    global cus_username
    global cus_password
    print('\nPlease enter your username and password.')
    cus_username = str(input('\n\tUsername: '))
    cus_password = str(input('\tPassword: '))
    # Customer can provide their details here and login into the system.
    
    move = False
    file = open('database.txt','r')
    for line in file:
        user_id,user_name,user_password,user_address,user_email,user_phone,user_gender,user_dob = line.split('!')
        if (user_name==cus_username and user_password == cus_password):
            move = True
            break
    file.close()
    
    if(move):
        print('\nLogin Successful!!!')
        registered_customer_what_do_you_want_to_do()
    else:
        print('\nWrong username or password')
        customer_login()
'''------------------------------------------------------------------------'''
# This function is for admin to login to the system
## assumptions: username-admin, password-admin
def admin_login():
    print('\nPlease enter your username and password.')
    admin_username = str(input('\n\tUsername: '))
    admin_password = str(input('\tPassword: '))
    # Admin can provide their details here and login into the system.
    
    move = False
    file = open('admin.txt','r')
    for line in file:
        user_name,user_password = line.split(',')
        if (user_name == admin_username and user_password == admin_password):
            move = True
            break
    file.close()
    
    if(move):
        print('\nLogin Successful!!!')
        admin_what_do_you_want_to_do()
    else:
        print('\nWrong username or password')
        admin_login()
'''------------------------------------------------------------------------'''
# This function is for new customer to register themselves into the system
def register():
    database = open('database.txt','r') # This is to open the database and so that the system can count how many customer had already been recorded and the current registering user id

    print('\nCreate Your OPMS Account \n')

    count = 0
    for line in database:
        count = count + 1
        Userid = count + 1
        userid = str(Userid)

    cus_username = str(input('\tUsername: '))
    cus_password = str(input('\tPassword: '))
    password = str(input('\tConfirm password: '))
    address = str(input('\tHome address: '))
    email = str(input('\tEmail address: '))
    phone = str(input('\tContact number: '))
    gender = str(input('\tGender (F/M): '))
    dob = str(input('\tDate of birth (DD/MM/YYYY): '))

    database = open('database.txt','r') 
    for line in database:
        user_id,user_name,user_password,user_address,user_email,user_phone,user_gender,user_dob = line.split('!')
        if (user_name == cus_username):
            print('\nThat username is taken. Try another.')
            register()
            break
        else:
            continue
    database.close()
     # This is to open the database and so that the system can check weather the current registering username had been registered before into the system

    
    if cus_password != password:
        print ("\nBoth passwords didn't match. Try again.")
        register()
    elif len(password) < 6:
        print('\nSorry, your password must be at least 6 characters long. Try again.')
        register()
    else:
        database = open('database.txt','a')
        database.write(userid + '!' + cus_username + '!' + password + '!' + address + '!' + email + '!' + phone + '!' + gender + '!' + dob + '\n')
        print ('\nYou have created an account successfully!')
        print ('\n'+cus_username+',your user ID is', userid+'.')
        print('\nPlease login from registered customer.')
        database.close()
    # These is to check weather the details given by the customer is valid
    
        menu()      
'''------------------------------------------------------------------------'''
# This function is for new customer to choose what operation they want to do
def new_customer_what_do_you_want_to_do():
    print('\nWhat do you want to do by using OPMS?')
    print('\n\t1. View all medicine')
    print('\t2. Register')
    print('\t3. Menu')
    choice = int(input('\nChoose the operation from the given options: '))
    # Customer can choose what they want to do by using the system without logging in or to register an account

    if choice <=0 or choice > 3:
        print('Invalid input')
        new_customer_what_do_you_want_to_do()
    else:
        if choice == 1:
            new_customer_view_medicine()
        elif choice == 2:
            register()
        else:
            menu()
'''------------------------------------------------------------------------'''
# This function is the menu to let the system know who is the user
def menu():
    print('\n\nWho are you?')
    print('\n\t1. Admin \n\t2. New Customer \n\t3. Registered Customer \n')
    choice = int(input('\nChoose the operation from the given options: '))
    # User can choose who are them here

    if choice <= 0 or choice > 3:
        print('\nInvalid input')
        menu()
    elif choice == 1:
        admin_login()
    elif choice == 2:
        new_customer_what_do_you_want_to_do()
    else:
        customer_login()
'''------------------------------------------------------------------------'''                     
menu()

