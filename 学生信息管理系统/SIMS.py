# editor hc
# date: 2023/2/23 11:28
# StudentInformationManageSystem V0.0.0
import os

filename = 'student.txt'


# 定义主函数，实现基本框架
def main():  # 定义主函数
    while True:
        menu()  # 调用menu()函数，打印菜单界面
        choice = int(input('请选择'))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7, 8]:
            if choice == 0:
                answer = input('您确定要退出系统吗? Y/N')
                if answer == 'Y' or 'y':
                    print('感谢使用')
                    break  # 退出系统
                else:
                    continue  # 重新运行main()函数，再次进入菜单
            elif choice == 1:
                insert()  # 录入学生信息，调用insert()方法
            elif choice == 2:
                search()  # 查找学生信息，调用search()方法
            elif choice == 3:
                delete()  # 删除学生信息，调用delete()方法
            elif choice == 4:
                modify()  # 修改学生信息，调用modify()方法
            elif choice == 5:
                sort()  # 对学生成绩排序，调用sort()方法
            elif choice == 6:
                total()  # 统计人数，调用total()方法
            elif choice == 7:
                show()  # 显示所有信息，调用show()方法


# 定义用户界面
def menu():  # 定义菜单
    print('================学生信息管理系统====================')
    print('-------------------功能菜单----------------------')
    print('\t\t\t\t\t\t\t 1.录入学生信息')
    print('\t\t\t\t\t\t\t 2.查找学生信息')
    print('\t\t\t\t\t\t\t 3.删除学生信息')
    print('\t\t\t\t\t\t\t 4.修改学生信息')
    print('\t\t\t\t\t\t\t 5.排序')
    print('\t\t\t\t\t\t\t 6.统计学生总人数')
    print('\t\t\t\t\t\t\t 7.显示所有学生信息')
    print('\t\t\t\t\t\t\t 0.退出系统')
    print('-------------------------------------------------')


# 定义主函数中的七个重要函数
def insert():
    student_list = []
    while True:  # 循环录入学生信息
        id = input('请输入ID(如1001):')
        if not id:
            break
        name = input('请输入姓名:')
        if not name:
            break

        # 异常处理
        try:
            english = int(input('请输入英语成绩:'))
            python = int(input('请输入python成绩:'))
            java = int(input('请输入Java成绩:'))

        except:
            print('输入无效,请重新输入')
            continue
        # 将录入的学生信息保留在字典当中
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        # 将学生信息添加到列表当中
        student_list.append(student)
        answer = input('是否继续添加？y/n\n')
        if answer == 'y':
            continue
        else:
            break

    # 调用save()函数，存储学生信息
    save(student_list)
    print('学生信息录入完毕')


# 定义save()函数
def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    pass


def delete():
    while True:
        student_id = input('请输入要删除的学生的id:')
        if student_id != '':  # 如果学生id不为空
            if os.path.exists(filename):  # 判断文件是否存在
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != student_id:
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{student_id}的学生的信息已经被删除')
                    else:
                        print(f'没有找到{student_id}的学生信息')
            else:
                print('无学生信息')
                break
            show() #删除完之后要重新显示学生的信息
            answer = input('是否继续删除?y/n')
            if answer == 'y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input('请输入要修改的学员的ID:')
    with open(filename,'w',encoding='utf-8') as rfile:
        for item in student_old:
            d=dict(eval(item))
            if d['id']==student_id:
                print('找到学生信息，可以修改相关信息')
                while True:
                    try:
                        d['name']=input('请输入要修改的姓名')
                        d['english']=input('请输入要修改的英语成绩')
                        d['python']=input('请输入要修改的python成绩')
                        d['java']=input('请输入要修改的java成绩')
                    except:
                        print('您的输入有误，请重新输入')
                    else:
                        break
                wfile.write(str(d)+'\n')
                print('修改成功')
            else:
                wfile.write(str(d)+'\n')
        answer=input('是否继续修改其它信息?y/n')
        if answer =='y':
            modify()



def sort():
    pass


def total():
    pass


def show():
    pass



# 以主程序方式运行
if __name__ == '__main__':
    main()
