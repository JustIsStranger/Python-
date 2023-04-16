book = ("三国演义", "红楼梦", "西游记", "水浒传", "哈利波特·魔法石",)
books = ["三国演义", "红楼梦", "西游记", "水浒传", "哈利波特·魔法石"]

while True:
    a = input('欢迎使用图书管理系统，查阅书籍请按1，借书请按2，还书请按3，结束服务请按4:  ')
    print()
    if a == "4":
        out = input("真的要退出吗？（退出请按1，取消退出请按2）")
        print()
        if out == "1":
            break
        elif out == "2":
            print()
        else:
            print("无效数字！您是要退出还是取消退出呢？本系统就自动选择取消退出了。")
            print()
    elif a == "1":
        print("目前书籍名单：")
        print()
        for i in books:
            print(i)
        print()
    elif a == "2":
        book001 = input("请输入所借书籍的名称:  ")
        print()
        if book001 in books:
            books.remove(book001)
            print("借书成功！")
            print()
        else:
            print("未有此书或已被借走")
            print()
    elif a == "3":
        d = input("请输入所还书籍的名称:  ")
        if d in book:
            print("此书不是本系统录入过的书籍，无法归还，请确认书籍名称！",end='') 
            
        elif d in books:
            print("此书已存在于目前书籍名单中，无法归还！")
            print()
        else:
            books.append(d)
            print("还书成功！")
            print()
    else:
        print("本系统未有此功能，请按“1”查看本系统功能")   
        print()



