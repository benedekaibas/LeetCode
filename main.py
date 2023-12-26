"""
Írjunk olyan python kódot, amely kitöröli egy listából a duplumokat pl. a = [10,20,30,20,10,50,60,40,80,50,40]

"""



def main():

    a = [10,20,30,20,10,50,60,40,80,50,40]

    for item in a:
        count = a.count(item)
        print(count)
        

if __name__ == "__main__":
    main()