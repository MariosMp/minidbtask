Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
from database import Database
command = input("Enter command:")
a = command.split()
if a[0] == "CREATE" and a[1] == "DATABASE":
    print("create_database")
    db_object = Database(a[2], load=False)
elif a[0] == "CREATE" and a[1] == "TABLE":
    name = input("Name of Database for the Table")
    x = Database(name, load=True)
    tk = len(a[3])
    x.create_table(a[2], )
    print("create_table")
elif a[0] == "CREATE" and a[1] == "INDEX":
    nq = input("Name of Database for the Index")
    q = Database(nq, load=True)
    q.create_index(a[4], a[2])
elif a[0] == "DROP" and a[1] == "TABLE":
    '''print("drop_table")'''
    n = input("Name of Database of the Table")
    ps = Database(n, load=True)
    ps.unlock_table(a[2])
    ps.drop_table(a[2])
elif a[0] == "INSERT" and a[1] == "INTO" and a[3] == "VALUES":
    named = input("Name of Database of the Table")
    db = Database(named, load=True)
    db.unlock_table(a[2])
    x2 = a[2]
    a.pop(0)
    a.pop(1)
    a.pop(0)
    a.pop(0)
    db.insert(x2, x)
    db.show_table(x2)
    '''print("insert_into")'''
elif a[0] == "DELETE" and a[1] == "FROM" and a[3] == "WHERE":
    nam = input("Name of Database of the Table")
    p = Database(nam, load=True)
    p.unlock_table(a[2])
    p.delete(a[2], a[4])
    '''print("delete_from")'''
elif a[0] == "UPDATE":
    na = input("Name of Database of the Table")
    st = Database(na, load=True)
    st.update(a[1], a[5], a[3], a[7])
    st.show_table(a[1])

elif a[0] == "SELECT" and a[4] == "WHERE":
    tr = input("Name of Database of the Table")
    km = Database(tr, load=True)
    km.unlock_table(a[3])
    if a[1] == '*':
        km.select(a[3], a[1], a[5])
    else:
        lix3 = a[3]
        lix5 = a[5]
        a.pop(0)
        a.pop(1)
        a.pop(1)
        a.pop(1)
        a.pop(1)
        '''print(lix2)'''
        km.select(lix3, x, lix5)
elif a[0] == "SELECT" and a[5] == "JOIN":
    cv = input("Name of Database of the Table")
    xc = Database(cv, load=True)
    xc.inner_join(a[3], a[6], a[8])
else:
    print("wrong command")