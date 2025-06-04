####Random Checkname System####
####This is a Python code , You must use the Python Decoder to run it!####
####这是Python文件，请使用python解读它




import os
import sys
import pygame,random
##随机点名系统2.1.2.9.pre3
bbh = "2.1.2.9.pre3"
##重制版


def get_base_path():
    """
    获取基础路径，区分开发环境和打包后的环境
    """
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))
def resource_path(relative_path,last=0):
    return os.path.join(get_base_path(), relative_path)


# 导入 dlc.py
try:
    
    # 尝试在开发模式下导入
    import dlc.dlc as dlc
    mode = "开发"
except ImportError:
    # 如果开发模式导入失败，尝试在打包模式下导入
    sys.path.append(resource_path("dlc/dlc",last=0))
    import dlc as dlc  # 假设打包后的模块名称为 dlc，并且在 dlc 文件夹中
    mode = "封闭"


def get_class_files():
    """获取 class 文件夹中的所有文件名称"""
    class_folder = resource_path('class')
    if os.path.exists(class_folder):
        return os.listdir(class_folder)
    return []
def fg(a):
    b=[]
    c=''
    for i in a:
        if i!=" ":
            c+=i
        else:
            b.append(c)
            c=''
    b.append(c)
    return b

if __name__ == "__main__":
    pygame.init()
    language = "CN"
    flag = pygame.RESIZABLE
    
    dlc.text_output_yes()
    # 获取 class 文件夹中的文件名称
    files = get_class_files()
    screen = pygame.display.set_mode((1000, 800), flag)
    pygame.display.set_caption(f'随机点名系统   v{bbh}')
    dlc.fontupload(resource_path('dlc/font.ttf',0),66,1)
    dlc.fontupload(resource_path('dlc/font.ttf',0),30,2)
    dlc.fontupload(resource_path('dlc/font.ttf',0),18,3)
    dlc.fontupload(resource_path('dlc/font.ttf',0),9,4)
    dlc.fontupload(resource_path('dlc/font.ttf',0),23,5)
    dlc.fontupload(resource_path('dlc/font.ttf',0),22,6)

    clock = pygame.time.Clock()
    class_now_chosen = ""
    random_student=""
    random_student_last=""
    random_student_lastsec=""
    random_y = 290
    run_random = 0
    random_speed = 8
    students = [""]
    students_score=[]
    page = "main"
    kfzmode = 0
    kfztime = 0
    student_scoreg=0
    lousinhuimode = "#H关"
    lxhnum=0
    random_time =0
    bichongmode = "#H关"
    students_all = [""]
    xz='None'
    guibimode="#H关"
    guibi = "#R/"
    gbnum=0
    none = "#R/"
    log = []
    keyincode=""
    andlistmode=0
    notnamelist = []
    kfzmodecan=0
    andlistrs=0
    ##从dlc/set中读取指令
    try:
        with open(resource_path('dlc/dlc.py'), 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if line.startswith("#") or line.startswith("\n") or line.startswith("'"):
                    if line[:5]=='#格式："':
                        break
                    continue
                
                else:
                    linea = fg(line)
                    print(linea)
                    if linea[0]=="open":
                                with open(resource_path(f'class/{files[int(linea[1])]}'), 'r', encoding='utf-8') as file:
                                    students = file.readlines()
                                    students = [student.strip() for student in students]
                                    students_all = [student.strip() for student in students]
                    elif linea[0]=="not":
                                notnamelist.append(students_all[int(linea[1])])
                                #print(notnamelist)
                    else:
                        try:
                            eval(line)
                        except:
                                exec(line.strip())
                            

    except Exception as e:
        print("读取dlc/set失败,不影响操作 \n错误信息: ",e,"\n代码: ",line)
        pass



    while 1:
        #try:
            screen.fill((5, 255, 125))
            if page == "main":
            ##绘制一个矩形中线
                pygame.draw.rect(screen, (0,0,0), (399,40,2,720), 2)
                ##绘制班级选择框
                classy=60
                for i in files:
                    if class_now_chosen != i:
                        pygame.draw.rect(screen, (240,190,240), (50,classy,300,90))
                        pygame.draw.rect(screen, (200,20,125), (50,classy,300,90),4)
                    else:
                        pygame.draw.rect(screen, (240,180,130), (50,classy,300,90))
                        pygame.draw.rect(screen, (200,125,55), (50,classy,300,90),4)
                    dlc.moutput(screen,i,(0,0,0),(152-dlc.mlength(i,2)//2,classy+28),num=2)
                    with open(resource_path(f'class/{i}'), 'r', encoding='utf-8') as file:
                        studentsnum = len(file.readlines())
                    if language == "CN":
                        dlc.moutput(screen,f"人数：{studentsnum}",(0,0,0),(274-dlc.mlength(f"人数：{studentsnum}",3)//2,classy+58),num=3)
                    elif language == "EN":
                        dlc.moutput(screen,f"Number of students：{studentsnum}",(0,0,0),(244-dlc.mlength(f"Number of students：{studentsnum}",3)//2,classy+58),num=3)
                    elif language == "HK":
                        dlc.moutput(screen,f"學生人數：{studentsnum}",(0,0,0),(274-dlc.mlength(f"學生人數：{studentsnum}",3)//2,classy+58),num=3)
                    elif language == "JP":
                        dlc.moutput(screen,f"生徒数：{studentsnum}",(0,0,0),(274-dlc.mlength(f"生徒数：{studentsnum}",3)//2,classy+58),num=3)
                    #dlc.moutput(screen,f"人数：{studentsnum}",(0,0,0),(274-dlc.mlength(f"人数：{studentsnum}",3)//2,classy+58),num=3)
                    classy+=100
                ##右侧横向3:5区域绘制分割线
                pygame.draw.rect(screen, (100,240,160), (410,40,540,250))

                ##绘制随机点名的对象（动态）
                if run_random:
                    random_y -= random_speed*(1.1+random_speed * 0.2)*2
                    dlc.moutput(screen,random_student,(0,0,0),(650-dlc.mlength(random_student,1)//2,random_y-20),num=1)
                    dlc.moutput(screen,random_student_last,(0,0,0),(650-dlc.mlength(random_student_last,1)//2,random_y-165),num=1)
                    dlc.moutput(screen,random_student_lastsec,(0,0,0),(650-dlc.mlength(random_student_lastsec,1)//2,random_y-310),num=1)
                    if random_speed > 2:
                        random_time +=1
                        if random_time > 130-random_speed*22 :
                            random_time=0
                            random_speed -= 1
                    
                    

                        
                    if random_y<145:
                        random_y=290
                        random_student_lastsec=random_student_last
                        random_student_last=random_student
                        random_student = random.choice(students) 
                        if random_speed == 2:
                            #print(1,random_student,lousinhuimode,"楼忻慧" in students)
                            random_time += 1
                            if random_time == 3:
                                random_speed = 1
                                random_time = 0
                            if lousinhuimode == "#B开"  and none in students and random_time == 2 and random.randint(1,2)==1:
                                #print(2,random_student)
                                random_student = none
                            if ((guibimode == "#B开"  and random_student == guibi) or random_student in notnamelist)and random_time == 2:
                                #print(2,random_student)
                                
                                if bichongmode != "#H关" and random_student in students:
                                    students.remove(random_student)
                                    try:
                                        dd=0
                                        while random_student == guibi or random_student in notnamelist:
                                            random_student = random.choice(students)
                                            dd+=1
                                            if dd>50:
                                                students = list(students_all)
                                    except:
                                        random_student = students[0]
                                else:
                                    try:
                                        dd=0
                                        while random_student == guibi or random_student in notnamelist:
                                            random_student = random.choice(students)
                                            dd+=1
                                            if dd>50:
                                                0/0
                                    except:
                                        random_student = students_all[0]
                        if random_speed == 1:
                            random_speed=8
                            run_random=0
                            random_student_lastsec=""
                            
                else:
                    dlc.moutput(screen,random_student_last,(0,0,0),(650-dlc.mlength(random_student_last,1)//2,random_y-165),num=1)
                    if bichongmode != "#H关":

                        if random_student_last in students:
                            students.remove(random_student_last)
                            bichongmode = "#O    重置"
                        if len(students)<=15:
                            students = list(students_all)
                if bichongmode != "#H关":
                    if language == "CN":
                        dlc.moutput(screen,f"#R避重模式·剩余#H{len(students)}#R人",(50,150,225),(760,261),num=3)
                    elif language == "EN":
                        dlc.moutput(screen,f"#RAvoidance mode#n     Remaining#H{len(students)}#Rstudents",(50,150,225),(722,231),num=3)##通过换行等操作实现语言适配
                    elif language == "HK":
                        dlc.moutput(screen,f"#R避重模式·剩餘#H{len(students)}#R人",(50,150,225),(760,261),num=3)
                    elif language == "JP":
                        dlc.moutput(screen,f"#R重複を避けるパターン·残り#H{len(students)}#R人",(50,150,225),(682,261),num=3)
                try:
                    if andlistmode!=0:
                        if language == "CN":
                            dlc.moutput(screen,f"#P交集模式·#Z<{class_now_chosen}>#P与#Z<{files[andlistmode-1]}>#P交叉",(50,150,225),(930-dlc.mlength(f"#R交集模式·<{class_now_chosen}>与<{files[andlistmode-1]}>交叉",3),231),num=3)
                
                
                except Exception as e:
                    print(e)
                    pass

                ##绘制1组方框挡住多余的部分
                pygame.draw.rect(screen,(5, 255, 125),(405,0,550,43))
                pygame.draw.rect(screen,(5, 255, 125),(405,295,550,260))
                pygame.draw.rect(screen, (240,140,120), (405,35,550,260),10)
                pygame.draw.rect(screen, (0,0,0), (400,299,560,2), 2)

                ##快速切换页面
                ##设置页面
                pygame.draw.rect(screen, (255,190,61), (420,310,115,75))
                pygame.draw.rect(screen, (230,230,117), (420,310,115,75),7)
                if language == "CN":
                    dlc.moutput(screen,"设 置",(0,0,0),(440,331),num=2)
                elif language == "EN":
                    dlc.moutput(screen,"Settings",(0,0,0),(430,333),num=2)
                elif language == "HK":
                    dlc.moutput(screen,"設 定",(0,0,0),(440,331),num=2)
                elif language == "JP":
                    dlc.moutput(screen,"設 定",(0,0,0),(440,331),num=2)

                pygame.draw.rect(screen, (0,0,0), (400,394,560,2), 2)

                ##保存score_class
                """
                if students_score!=[] and student_scoreg == 1:
                    with open(resource_path(f'score—class/{class_now_chosen}'), 'w', encoding='utf-8') as file:
                        for student_sc in students_score:
                            file.write(f"{student_sc}\n")
                    student_scoreg=0
                """
                
                ##测试项 andlistmode(交集模式)
                
                    


                

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:  # 鼠标左键
                            mouse_x, mouse_y = event.pos
                            if 1:#读取班级（前四个）
                                try:
                                    if 50 <= mouse_x <= 350 and 60 <= mouse_y <= 150:
                                        class_now_chosen = files[0]
                                        with open(resource_path(f'class/{files[0]}'), 'r', encoding='utf-8') as file:
                                            students = file.readlines()
                                        students = [student.strip() for student in students]
                                        students_all = [student.strip() for student in students]
                                        '''
                                        try:
                                            with open(resource_path(f'score—class/{files[0]}'), 'r', encoding='utf-8') as file:
                                                students_score = file.readlines()
                                                students_score = [student.strip() for student in students_score]
                                        except:
                                            students_score = ["0"]*len(students)
                                            student_scoreg=1
                                        '''
                                    elif 50 <= mouse_x <= 350 and 160 <= mouse_y <= 250:
                                        class_now_chosen = files[1]
                                        with open(resource_path(f'class/{files[1]}'), 'r', encoding='utf-8') as file:
                                            students = file.readlines()
                                        students = [student.strip() for student in students]
                                        students_all = [student.strip() for student in students]
                                        '''
                                        try:
                                            with open(resource_path(f'score—class/{files[1]}'), 'r', encoding='utf-8') as file:
                                                students_score = file.readlines()
                                                students_score = [student.strip() for student in students_score]
                                        except:
                                            students_score = ["0"]*len(students)
                                            student_scoreg=1
                                        '''
                                    elif 50 <= mouse_x <= 350 and 260 <= mouse_y <= 350:
                                        class_now_chosen = files[2]
                                        with open(resource_path(f'class/{files[2]}'), 'r', encoding='utf-8') as file:
                                            students = file.readlines()
                                        students = [student.strip() for student in students]
                                        students_all = [student.strip() for student in students]
                                        '''
                                        try:
                                            with open(resource_path(f'score—class/{files[2]}'), 'r', encoding='utf-8') as file:
                                                students_score = file.readlines()
                                                students_score = [student.strip() for student in students_score]
                                        except:
                                            students_score = ["0"]*len(students)
                                            student_scoreg=1
                                        '''
                                    elif 50 <= mouse_x <= 350 and 360 <= mouse_y <= 450:
                                        class_now_chosen = files[3]
                                        with open(resource_path(f'class/{files[3]}'), 'r', encoding='utf-8') as file:
                                            students = file.readlines()
                                        students = [student.strip() for student in students]
                                        students_all = [student.strip() for student in students]
                                        '''
                                        try:
                                            with open(resource_path(f'score—class/{files[3]}'), 'r', encoding='utf-8') as file:
                                                students_score = file.readlines()
                                                students_score = [student.strip() for student in students_score]
                                        except:
                                            students_score = ["0"]*len(students)
                                            student_scoreg=1
                                        '''
                                    elif 50 <= mouse_x <= 350 and 460 <= mouse_y <= 550:
                                        class_now_chosen = files[4]
                                        with open(resource_path(f'class/{files[4]}'), 'r', encoding='utf-8') as file:
                                            students = file.readlines()
                                        students = [student.strip() for student in students]
                                        students_all = [student.strip() for student in students]
                                        '''
                                        try:
                                            with open(resource_path(f'score—class/{files[4]}'), 'r', encoding='utf-8') as file:
                                                students_score = file.readlines()
                                                students_score = [student.strip() for student in students_score]
                                        except:
                                            students_score = ["0"]*len(students)
                                            student_scoreg=1
                                        '''
                                    elif 50 <= mouse_x <= 350 and 560 <= mouse_y <= 650:
                                        class_now_chosen = files[5]
                                        with open(resource_path(f'class/{files[5]}'), 'r', encoding='utf-8') as file:
                                            students = file.readlines()
                                        students = [student.strip() for student in students]
                                        students_all = [student.strip() for student in students]
                                        """
                                        try:
                                            with open(resource_path(f'score—class/{files[5]}'), 'r', encoding='utf-8') as file:
                                                students_score = file.readlines()
                                                students_score = [student.strip() for student in students_score]
                                        except:
                                            students_score = ["0"]*len(students)
                                            student_scoreg=1
                                        """
                                except:
                                    if language == "CN":
                                        dlc.addts("无效的班级选择")
                                    elif language == "EN":
                                        dlc.addts("Invalid class selection")
                                    elif language == "HK":
                                        dlc.addts("無效的班級選擇")
                                    elif language == "JP":
                                        dlc.addts("無効なクラス選択")
                                    #dlc.addts("无效的班级选择")
                                    
                            if 1:#随机点名
                                if 410 <= mouse_x <= 950 and 40 <= mouse_y <= 300:
                                    random_y = 290
                                    run_random = 1
                                    random_speed = 8
                                    random_student = random.choice(students)
                                if 0 <= mouse_x <= 10 and 0 <= mouse_y <= 10:
                                    if kfzmode == 1:
                                        page = "kfzsetting"
                                        log=[]
                                        if not kfzmodecan:
                                            log.append("#ZDeveloper mode unlocked: #Rplease enter the password!")
                                    else:
                                        kfztime += 1
                                        if kfztime == 7:
                                            kfzmode = 1
                                            if language == "CN":
                                                dlc.addts("恭喜解锁高级设置")
                                            elif language == "EN":
                                                dlc.addts("Congratulations, you have unlocked the advanced settings")
                                            elif language == "HK":
                                                dlc.addts("恭喜解鎖高級設置")
                                            elif language == "JP":
                                                dlc.addts("おめでとうございます、高級設定を解錠しました")
                                if 970 <= mouse_x <= 1000 and 0 <= mouse_y <= 10:
                                    if language == "CN":
                                        language = "EN"
                                        dlc.addts("Language set to English",color=(0,128,255))
                                    elif language == "EN":
                                        language = "CN"
                                        dlc.addts("语言设置为简体中文",color=(0,128,255))
                            if mouse_x >= 410 and mouse_y>300 and mouse_y < 395:#工具条
                                if 420 <= mouse_x <= 535 and 310 <= mouse_y <= 385:
                                    page = "setting"
                    if event.type == pygame.VIDEORESIZE:
                        screen = pygame.display.set_mode((1000,800), flag)
            if page == "setting":
                if andlistmode!=0 and andlistrs:
                    andlistrs=0
                    set1 = set(students)
                    with open(resource_path(f'class/{files[andlistmode-1]}'), 'r', encoding='utf-8') as file:
                        set2 = file.readlines()
                        set2 = [set2.strip() for set2 in set2]
                        set2=set(set2)
                    students_all = list(set1&set2)
                    students = list(students_all)
                    dlc.addts(f"交集模式数据已重置")
                if lousinhuimode=="#B开":
                    none=students_all[lxhnum]  
                else:
                    none="#R/"
                if guibimode=="#B开":
                    guibi=students_all[gbnum]  
                else:
                    guibi="#R/"
                if language == "CN":
                    dlc.moutput(screen,"#P按下ESC退出",(0,0,0),(500-dlc.mlength("按下ESC退出",2)//2,0),num=2)
                    dlc.moutput(screen,f"指定模式#x280{lousinhuimode}#x520{none}",(0,0,0),(40,40),num=2)
                    dlc.moutput(screen,f"避重模式#x280{bichongmode}",(0,0,0),(40,80),num=2)
                    dlc.moutput(screen,f"小窗口模式#x280#H关",(0,0,0),(40,120),num=2)
                    dlc.moutput(screen,f"语言设置#x280#5#R简体中文 #HEnglish #H繁體中文[Beta] #H日本語#H[Beta]",(0,0,0),(40,160),num=2)
                    dlc.moutput(screen,f"规避模式#x280{guibimode}#x520{guibi}",(0,0,0),(40,200),num=2)
                    if andlistmode!=0:
                        dlc.moutput(screen,f"交集模式#x280#Z与<{files[andlistmode-1]}>交叉#x520#O退出",(0,0,0),(40,240),num=2)
                    else:
                        dlc.moutput(screen,f"交集模式#x280#H关",(0,0,0),(40,240),num=2)
                elif language == "EN":
                    bichongEng = "#Hoff" if bichongmode == "#H关" else ("#Bon" if bichongmode == "#B开" else "#O    reset")
                    lousinhuiEng = "#Hoff" if lousinhuimode == "#H关" else ("#Bon" if lousinhuimode == "#B开" else "#R    incompatible")
                    guibiEng = "#Hoff" if guibimode == "#H关" else "#Bon"
                    dlc.moutput(screen,"#PPress ESC key to exit",(0,0,0),(500-dlc.mlength("Press ESC key to exit",2)//2,0),num=2)
                    dlc.moutput(screen,f"Specified mode#x280{lousinhuiEng}#x520{none}",(0,0,0),(40,40),num=2)
                    dlc.moutput(screen,f"Avoidance mode#x280{bichongEng}",(0,0,0),(40,80),num=2)
                    dlc.moutput(screen,f"Small window mode#x280#Hoff",(0,0,0),(40,120),num=2)
                    dlc.moutput(screen,f"Language#x280#5#H简体中文 #BEnglish #H繁體中文[Beta] #H日本語#H[Beta]",(0,0,0),(40,160),num=2)
                    dlc.moutput(screen,f"Avoid mode#x280{guibiEng}#x520{guibi}",(0,0,0),(40,200),num=2)
                elif language == "HK":#繁体中文
                    bichongHK = "#H關" if bichongmode == "#H关" else ("#B開" if bichongmode == "#B开" else "#O    重置")
                    dlc.moutput(screen,f"避重模式#x280{bichongHK}",(0,0,0),(40,80),num=2)
                    dlc.moutput(screen,f"小窗口模式#x280#H關",(0,0,0),(40,120),num=2)
                    dlc.moutput(screen,f"语言设置#x280#5#H简体中文 #HEnglish #O繁體中文#H[Beta] #H日本語#H[Beta]",(0,0,0),(40,160),num=2)
                elif language == "JP":#日语
                    bichongJP = "#Hオフ" if bichongmode == "#H关" else ("#Bオン" if bichongmode == "#B开" else "#O    リセット")
                    dlc.moutput(screen,f"避重モード#x280{bichongJP}",(0,0,0),(40,80),num=2)
                    dlc.moutput(screen,f"小窓モード#x280#Hオフ",(0,0,0),(40,120),num=2)
                    dlc.moutput(screen,f"言語設定#x280#5#H简体中文 #HEnglish #H繁體中文#H[Beta] #W日本語#H[Beta]",(0,0,0),(40,160),num=2)

                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.VIDEORESIZE:
                        screen = pygame.display.set_mode((1000,800), flag)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:  # 鼠标左键
                            mouse_x, mouse_y = event.pos
                            if 1:
                                if 0 <= mouse_x <= 10 and 0 <= mouse_y <= 10:
                                        page = "main"     
                                if 40 <= mouse_x <= 240 and 40 <= mouse_y <= 80:
                                    if lousinhuimode == "#H关":
                                        lousinhuimode = "#B开"
                                        xz="lxh"
                                        if bichongmode == "#B开":
                                            dlc.addts("系统警告:模式互斥",color=(255,128,10))
                                            lousinhuimode = "#R    互斥"
                                    else:   
                                        lousinhuimode = "#H关"   
                                if 40 <= mouse_x <= 240 and 80 <= mouse_y <= 120:
                                    if bichongmode == "#H关":
                                        bichongmode = "#B开"
                                        xz="lxh"
                                        if lousinhuimode == "#B开":
                                            if language == "CN":
                                                dlc.addts("系统警告:模式互斥",color=(255,128,10))
                                            elif language == "EN":
                                                dlc.addts("System warning: mutual exclusion",color=(255,128,10))
                                            elif language == "HK":#繁体中文
                                                dlc.addts("系統警告:模式互斥",color=(255,128,10))
                                            #dlc.addts("系统警告:模式互斥",color=(255,128,10))
                                            lousinhuimode = "#R    互斥"
                                    else:
                                        bichongmode = "#H关" 
                                        students = students_all
                                if 40 <= mouse_x <= 240 and 120 <= mouse_y <= 160:
                                    page = "small"
                                    screen = pygame.display.set_mode((200, 1), flag)
                                    pygame.display.set_caption('最小化模式')
                                if 40 <= mouse_x <= 240 and 160 <= mouse_y <= 200:
                                    if language == "CN":
                                        language = "EN"
                                    elif language == "EN":
                                        language = "HK"#繁体中文
                                    elif language == "HK":#繁体中文
                                        language = "JP"#日语
                                    else:
                                        language = "CN"
                                if 40 <= mouse_x <= 240 and 200 <= mouse_y <= 240:
                                    if guibimode == "#H关":
                                        guibimode = "#B开"
                                        xz="gb"
                                    elif guibimode == "#B开":
                                        guibimode="#H关"
                                if 40 <= mouse_x <= 240 and 240 <= mouse_y <= 280:
                                    if andlistmode==0:
                                        xz="andlist"
                                        dlc.addts("激活<交集模式>输入，请输入要与的班级编号",color=(210,88,125))
                                    else:
                                        andlistmode=0
                    elif event.type == pygame.KEYDOWN:
                        if event.key >= pygame.K_0 and event.key <= pygame.K_9 or event.key == pygame.K_BACKSPACE:
                            if xz=="lxh":
                                if event.key == pygame.K_BACKSPACE:
                                    lxhnum //= 10
                                else:
                                    lxhnum*=10
                                    lxhnum += event.key - pygame.K_0
                                    if lxhnum>=len(students):
                                        lxhnum=0
                            if xz=="gb":
                                if event.key == pygame.K_BACKSPACE:
                                    gbnum //= 10
                                else:
                                    gbnum*=10
                                    gbnum += event.key - pygame.K_0
                                    if gbnum>=len(students):
                                        gbnum=0
                            if xz=="andlist":
                                if event.key == pygame.K_BACKSPACE:
                                    andlistmode //= 10
                                else:
                                    andlistmode*=10
                                    andlistmode += event.key - pygame.K_0
                                    if andlistmode>=len(files)+1:
                                        andlistmode=0
                                        dlc.addts("无效的班级选择，请重新输入",color=(255,128,10))

                                andlistrs=1
                        if event.key == pygame.K_ESCAPE:
                            page="main"
            if page == "small":
                if language == "CN":
                    dlc.moutput(screen,"#B当前处于#H最小化#B模式#n#P    点按任意处返回主页",(0,0,0),(40,40),num=2)
                elif language == "EN":
                    dlc.moutput(screen,"#BCurrent is in#H Minimize #Bmode#n#P    Press anywhere to return to the homepage",(0,0,0),(40,40),num=2)
                elif language == "HK":#繁体中文
                    dlc.moutput(screen,"#B目前處於#H最小化#B模式#n#P    點按任意處返回主頁",(0,0,0),(40,40),num=2)
                elif language == "JP":#日语
                    dlc.moutput(screen,"#BCurrent is in#H Minimize #Bmode#n#P    Press anywhere to return to the homepage",(0,0,0),(40,40),num=2)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:  # 鼠标左键
                            screen = pygame.display.set_mode((1000,800), flag)
                            page = "main"
                    elif event.type == pygame.WINDOWMINIMIZED or event.type == pygame.VIDEORESIZE or event.type == pygame.WINDOWMINIMIZED:
                        screen = pygame.display.set_mode((1000,800), flag)
            if page == "kfzsetting":
                logy=30
                for i in log:
                    dlc.moutput(screen,i,(0,0,0),(40,logy),num=6)
                    logy+=25
                dlc.moutput(screen,"#W"+keyincode,(0,0,0),(40,logy),num=6)
                if len(log)>52:
                    log=log[1:]
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        sys.exit()
                    elif e.type == pygame.MOUSEBUTTONDOWN:
                        if e.button == 1:  # 鼠标左键
                            page = "main"
                    elif e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_ESCAPE:
                            page = "main"
                        ##对所有字母数字按键进行输入
                        if e.key >= pygame.K_0 and e.key <= pygame.K_9 or e.key == pygame.K_BACKSPACE:
                            if e.key == pygame.K_BACKSPACE:
                                keyincode = keyincode[:-1]
                            else:
                                keyincode += str(e.key - pygame.K_0)
                        if e.key >= pygame.K_a and e.key <= pygame.K_z:
                            keyincode += chr(e.key)
                        if e.key >= pygame.K_KP0 and e.key <= pygame.K_KP9:
                            keyincode += str(e.key - pygame.K_KP0)
                        if e.key >= pygame.K_KP_MULTIPLY and e.key <= pygame.K_KP_DIVIDE:
                            if e.key == pygame.K_KP_MULTIPLY:
                                keyincode += "*"
                            elif e.key == pygame.K_KP_DIVIDE:
                                keyincode += "/"
                            elif e.key == pygame.K_KP_PLUS:
                                keyincode += "+"
                            elif e.key == pygame.K_KP_MINUS:
                                keyincode += "-"
                        if e.key == pygame.K_EQUALS:
                            keyincode += "="
                        if e.key == pygame.K_PERIOD:
                            keyincode += "."
                        if e.key == pygame.K_COMMA:
                            keyincode += ","
                        if e.key == pygame.K_SEMICOLON:
                            keyincode += ";"
                        if e.key == pygame.K_SPACE:
                            keyincode += " "
                        if e.key == pygame.K_MINUS:
                            keyincode += "-"
                        if e.key == pygame.K_RETURN:
                            try:
                                if kfzmodecan == 1:
                                    try:
                                        keyincode = str(eval(keyincode))
                                        log.append(keyincode)
                                    except:
                                        exec(keyincode)
                                        log.append("#YThe code '"+keyincode+"' is successfully run.")
                                    keyincode=""
                                else:
                                    if keyincode == "yamgchenghu008":
                                        log.append("#YYou can use the Developer Mode of the programme")
                                        kfzmodecan=1
                                        keyincode=''
                                    else:
                                        log.append("#RWrong password ! #HYou cannot use the Developer Mode of the programme")
                                        log.append("#BIf you want to set the programme , please click 'Settings' on the main page")
                            except Exception as e:
                                #拆分字符串
                                keyincodelst = keyincode.split(" ")
                                try:
                                    if keyincodelst[0] == "andlist":
                                        andlistmode = int(keyincodelst[1])
                                        log.append(f"#RYour command has been redirected to 'andlistmode = {int(keyincodelst[1])}'")
                                    elif keyincodelst[0] == "print":
                                        print(keyincodelst[1])
                                        log.append(f"#RYour command has been redirected to 'print({int(keyincodelst[1])})'")
                                    elif keyincodelst[0] == "notname":
                                        notnamelist.append(students_all[int(keyincodelst[1])])
                                        log.append(f"#RYour command has been redirected to 'notnamelist.append({students_all[int(keyincodelst[1])]})'")
                                    elif keyincodelst[0] == "notnameclear":
                                        notnamelist=[]
                                        log.append(f"#RYour command has been redirected to 'notnamelist=[]'")
                                    elif keyincodelst[0] == "open":
                                        try: 
                                            opennum = int(keyincodelst[1])
                                            with open(resource_path(f'class/{files[opennum]}'), 'r', encoding='utf-8') as file:
                                                students = file.readlines()
                                                students = [student.strip() for student in students]
                                                students_all = [student.strip() for student in students]
                                            log.append(f"#RYour command has been redirected to 'open('class/{files[int(opennum)]}','r')' and the programme try to read it")
                                        except:
                                            exec(f"{keyincodelst[1]}='#B开'")
                                            log.append(f"#RYour command has been redirected to '{keyincodelst[1]}='#$B开'" )
                                
                                except:
                                    log.append(f"#RError exception: {e}")

            if page == "#B开":
                page = "main"
                dlc.addts("谁允许你把page变量设置成开启状态的")
            dlc.outputts(screen,2)
            if language == "CN":
                dlc.moutput(screen,f"#H随机点名系统 v{bbh}",(100,100,100),(0,0),num=4)
                dlc.moutput(screen,f"#HEng",(100,100,100),(960,0),num=4)
            elif language == "EN" or language == "JP":
                dlc.moutput(screen,f"#HRandom Calling System v{bbh}",(100,100,100),(0,0),num=4)
                dlc.moutput(screen,f"#HChn",(100,100,100),(960,0),num=4)
            elif language == "HK":#繁体中文
                dlc.moutput(screen,f"#H隨機點名系統 v{bbh}",(100,100,100),(0,0),num=4)
            dlc.moutput(screen,resource_path(""),(100,100,100),(10,780),num=4)
            pygame.display.update()
            clock.tick(50)  
        

