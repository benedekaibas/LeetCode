"""
Írjunk olyan python kódot, amely kitöröli egy listából a duplumokat pl. a = [10,20,30,20,10,50,60,40,80,50,40]

"""



def main():

    a = [10,20,30,20,10,50,60,40,80,50,40]

    for item in a:
        count = a.count(item)

        if count > 1:
            remove = a.remove(item)
            print(a)
        else:
            print("fhds")


    #print(new_list)
if __name__ == "__main__":
    main()