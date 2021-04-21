# This is  module for file 47

def a1():
    print('from a1',__name__)   #gunakan __name__ agar fungsi ini bisa dipanggil

def a2():
    print('from a2')
    print(__name__) #ini akan menghasilkan __main__ sehingga fungsi bisa dipanggil

def main():
    a1()
    a2()

# jika kita hanya ingin menggunakan salah satu fungsinya, maka gunakan:
if __name__ == '__main__':
    main()