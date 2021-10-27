import control_module
from datetime import date

def run():
    control_module.store_habit("Brush Teeth", 1, 1)
    control_module.store_habit("Run", 7, 1)
    habits_list = control_module.get_habits_list(1)
    for habit in habits_list:
        hid = habit[0]

    #control_module.update_habit_description(hid, "Boxing")
    #control_module.update_habit_frequency(hid, 10)

    habits_list = control_module.get_habits_list(1)
    for habit in habits_list:
        print(habit)

    print(control_module.habit_has_expired_by(hid, date.today()))

    control_module.deppreciate_habit(hid)
    habits_list = control_module.get_habits_list(1)
    for habit in habits_list:
        print(habit)


    control_module.appreciate_habit(hid)
    habits_list = control_module.get_habits_list(1)
    for habit in habits_list:
        print(habit)

    control_module.action_habit(hid)

    control_module.appreciate_habit(hid)
    habits_list = control_module.get_habits_list(1)
    for habit in habits_list:
        print(habit)

if __name__ == '__main__':
    run()