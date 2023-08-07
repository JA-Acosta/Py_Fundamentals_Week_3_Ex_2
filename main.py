'''
>>> JAAR
>>> 8/7/2023
>>> Practicing Fundamentals Program 14
>>> Version 1
'''

'''
>>> Generates a program that takes a text file and copies the contents of that file to another file.
'''

def main() :
    with open('the_little_prince.txt', 'r') as file :
        with open('copy.txt', 'w') as new_file :
            for line in file.readlines() :
                new_file.write(line)

    with open('copy.txt', 'r') as copy :
        print(copy.read())

if __name__ == '__main__' :
    main()