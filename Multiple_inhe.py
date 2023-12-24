class LU:
    def course1(self, s, t, d):
        Sub = {1: "AI & ML", 2: "Web 3.0", 3: "UI/UX", 4: "AR/VR"}
        Tra = {1: "Sai Sir", 2: "Prasad Sir"}
        Dur = {1: "2yr", 2: "3yr", 3: "4yr"}
        print("\nCourse1:", "\n",Sub,"\n", Tra,"\n", Dur,"\n")


class ITM:
    def course2(self, s, t, d):
        Sub = {1: "AI & ML", 2: "Web 3.0", 3: "UI/UX", 4: "AR/VR"}
        Tra = {1: "Sumit Sir", 2: "Sheetal Ma'am"}
        Dur = {1: "2yr", 2: "3yr", 3: "4yr"}
        print("\nCourse2:", "\n",Sub,"\n", Tra,"\n", Dur,"\n")


class Btech(LU, ITM):
    def displayc(self):
        self.course1("s1", "t1", "d1") 
        self.course2("s2", "t2", "d2")

    def choose(self):
        cho = int(input("Select the Course (1/2): "))
        if cho == 1:
            self.course1("s1", "t1", "d1") 
            ch = int(input("Choose the Subject (1-4): "))
            ch1 = int(input("Choose the Trainer (1-2): "))
            ch2 = int(input("Choose the Duration (1-3): "))
            if ch in range(1, 5):
                so={ch}
            if ch1 in range(1,3):
                tr={ch2}
            if ch2 in range(1,4):
                du={ch2}
            print("Elected Course:\n*------------------------------*\n|Subject | Trainer | Duration \n*------------------------------*\n|",so  ,"|", tr,"|",du,"|","\n*------------------------------*")

        elif cho == 2:
            self.course2("s2", "t2", "d2") 
            ch = int(input("Choose the Subject (1-4): "))
            ch1 = int(input("Choose the Trainer (1-2): "))
            ch2 = int(input("Choose the Duration (1-3): "))
            if ch in range(1, 5):
                so={ch}
            if ch1 in range(1,3):
                tr={ch2}
            if ch2 in range(1,4):
                du={ch2}
            print("Elected Course:\n*------------------------------*\n|Subject | Trainer | Duration \n*------------------------------*\n|",so  ,"|", tr,"|",du,"|","\n*------------------------------*")
        else:
            print("Invalid course choice")



obj = Btech()

obj.displayc()
obj.choose()
