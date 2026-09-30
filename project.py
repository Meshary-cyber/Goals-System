"""
Welcome!


this application is a first version of orgnization tasks beigning from small 
like wash your face to hug thing such as make a lab-paper or a project in 
acadimc or job filed.

 - make the project without app                     --> 0.0 version
 - make the project still same but test the code    --> 0.1 version
 - make the project with app                        --> 0.2 version
 - make the project with AI withoit app             --> 0.3 version
 - make the project with AI + App                   --> 0.4 version

To 0.0 version ther are many versions in 0.0:-
 - just build classes and function just Empty       --> 0.00 version
 - classes and functions fielld                     --> 0.01 version
 - add ability to the project like input and submit --> 0.02 version
 - improve 0.02 + add stuts that user maybe do      --> 0.03 version
 - improve 0.03 + add optins to user to input       --> 0.04 version
 - |       |   -  |        | 


Enjoy

class Task:
    def __init__(self, name, classification):
        self.name = name
        self.classification = classification
        self.is_finished = False



    def mark_done(self, done:bool):
        self.is_finished = done
        
            
    


class OrganizationApp:
    def __init__(self):
        self.tasks = []
        self.classification = ['easy', 'medium', 'hard']

    def add_task(self, stut, name):
        if stut in self.classification:
            new_task = Task(name, stut)
            self.tasks.append(new_task)
    
        else:
            print("Wrong in classification")

    def remove_task(self):
        pass

    def list_tasks(self):
        pass

    def show_daily_summary(self):
        pass



"""
import time
class System:
    def __init__(self):
        self.info = [
            {
                'user_name': '',
                'user_stus_focus':'',
                'user_time_using': 0,
                'days_user_use': 0,
            },
            {
                'goals': [],
                'number_of_goals': 0,
                'goals_that_done':[],
                'goals_did_not_done': [],
                'checkbocks_amout': [],
                'checkbocks_amout_done': [],
                'checkbocks_amout_not_done': [],
                'accrency_goals': 0,
                'Probability_of_non-progression_based_on_data': {},

            }
        ]
        self.command_welcome_goal = 0
    def add_info(self, goal_name, total_checkboxes):
        """دالة لإضافة هدف جديد وتهيئة البيانات الخاصة به"""
        goals_dict = self.info[1]
        
        # إضافة الهدف وتحديث العدد
        goals_dict['goals'].append(goal_name)
        goals_dict['number_of_goals'] = len(goals_dict['goals'])
        
        # إضافة كمية تشيك بوكس المحددة لهذا الهدف (كمثال)
        goals_dict['checkboxes_amount'].append(total_checkboxes)
        
        # وضعه مؤقتاً في قائمة الأهداف غير المكتملة
        goals_dict['goals_incomplete'].append(goal_name)
        print(f"تم إضافة الهدف: {goal_name}")
    
    def run(self):
        self.welcome()
    def welcome(self):
        size_screen = 100
        print("-" * size_screen)
        time.sleep(0.3)
        print("*" * size_screen)
        time.sleep(0.3)
        print("-"* size_screen)
        time.sleep(0.2)
        print("Welcome to my application")
        name = input("Type your name: ")
        print(f"hello {name} how can I help you")
        print("this list choose what you want")
        stat = input("""
                [1] put schedual for goals,
                [2] type your moving in goals,
        
        """)
        if stat == 1:
            self.command_welcome_goal = 0
        elif stat == 2:
            self.command_welcome_goal = 1
        else:
            print("Wrong number Please write 1 or 2")
            print("If you want the first command please type 1")
            print("If you want the first command please type 2")

    def cmnd_1St_condition(self):
        print()

    def logic_welcom(self):
        if self.command_welcome_goal == 0:
            pass
        elif self.command_welcome_goal == 1:
            pass




sys = System()
sys.run()


    
