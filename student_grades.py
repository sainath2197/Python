# Keep this is small app to find grades by entering your marks 
def avg(list1):
    if any(mark>100 for mark in list1):
        return "DOnt cheat us by giving wrong marks"

    average=sum(list1)/len(list1)
    if average>90:
        return "a"
    elif average>80:
        return "b"
    elif average>70:
        return "c"
    elif average>60:
        return "d"
    else:
        return "fail"


def main():
    list1=list(map(int ,input('Give me your marks for 100 in all subjects ').split()))
    grade=avg(list1)
    print('\nResult:',grade)
if __name__ == "__main__":
    main()

# map function built in function of higher order which 


