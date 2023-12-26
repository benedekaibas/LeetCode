"""
Írjunk olyan python kódot, amely kitöröli egy listából a duplumokat pl. a = [10,20,30,20,10,50,60,40,80,50,40]

"""



def main():

    a = [10,20,30,20,10,50,60,40,80,50,40]

    for item in a:
        count = a.count(item)

        if count <= 1:
            print(item)
        elif count >= 1:
            print(f"This item appears multiple times: {item}")
        else:
            print("not working")
        
if __name__ == "__main__":
    main()