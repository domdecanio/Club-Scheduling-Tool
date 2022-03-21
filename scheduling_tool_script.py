import pandas as pd

# Building Dataframe
file_location = input('Enter the file location: ')
source_file = input('Enter the file name: ')
avail_df = pd.read_csv(f'{file_location}{source_file}',
                       usecols=["mon", "tues", "wed", "thur", "friM", "friA", "penalty"])
names_info_df = pd.read_csv(f'{file_location}{source_file}', usecols=["First Name", "Last Name"])

names_info_df['Full_Name'] = names_info_df["First Name"] + "_" + names_info_df["Last Name"]
names_df = pd.DataFrame(names_info_df, columns=["Full_Name"])

member_data = pd.concat([names_df, avail_df], axis=1)
print(member_data)
drop_last = str(input('Drop the last row from the table? (enter: yes or no) '))
if drop_last == 'yes':
    member_data.drop(member_data.tail(1).index, inplace=True)
print('Data to use: ')
print(member_data)

# Building Member Objects
class Member:
    _registry = []

    def __init__(self, name, mon, tues, wed, thur, friM, friA, penalty):
        self._registry.append(self)
        self.name = name
        self.total_sessions = 0
        self.scheduled_weeks = {}
        self.scheduled_days = {}
        self.avail = {"mon": mon, "tues": tues, "wed": wed, "thur": thur, "friM": friM, "friA": friA}
        self.penalty = penalty


members = []
members_counter = 0

for i in member_data.itertuples():
    member = Member(str(i.Full_Name), i.mon, i.tues, i.wed, i.thur, i.friM, i.friA, i.penalty)
    members.append(member)
    members_counter += 1

# Week and Day Info / Analysis
number_of_weeks = int(input('How many weeks are you scheduling for? '))
sessions_per_week = int(input('How many sessions per week will there be? (enter: 2 or 3) '))

constant_sessions = []
alternating_sessions = []
if sessions_per_week == 2:
    num_alternating = int(input('How many session times will be alternating? (enter: 0, 1, or 2) '))
    if num_alternating == 0:
        print('In the following input fields, enter one of the following: mon, tues, wed, thur, friM, or friA.')
        day1 = str(input('Day 1 (every week): '))
        constant_sessions.append(day1)
        day2 = str(input('Day 2 (every week): '))
        constant_sessions.append(day2)

    if num_alternating == 1:
        print('In the following input fields, enter one of the following: mon, tues, wed, thur, friM, or friA.')
        day1 = str(input('Day 1 (every week): '))
        constant_sessions.append(day1)
        day21 = str(input('Day 2 option 1 (every other week): '))
        alternating_sessions.append(day21)
        day22 = str(input('Day 2 option 2 (every other week): '))
        alternating_sessions.append(day22)

    if num_alternating == 2:
        print('In the following input fields, enter one of the following: mon, tues, wed, thur, friM, or friA.')
        day11 = str(input('Day 1 option 1 (every other week): '))
        alternating_sessions.append(day11)
        day12 = str(input('Day 1 option 2 (every other week): '))
        alternating_sessions.append(day12)
        day21 = str(input('Day 2 option 1 (every other week): '))
        alternating_sessions.append(day21)
        day22 = str(input('Day 2 option 2 (every other week): '))
        alternating_sessions.append(day22)

if sessions_per_week == 3:
    num_alternating = int(input('How many session times will be alternating? (enter: 0, 1, 2, or 3) '))
    if num_alternating == 0:
        print('In the following input fields, enter one of the following: mon, tues, wed, thur, friM, or friA.')
        day1 = str(input('Day 1 (every week): '))
        constant_sessions.append(day1)
        day2 = str(input('Day 2 (every week): '))
        constant_sessions.append(day2)
        day3 = str(input('Day 3 (every week): '))
        constant_sessions.append(day3)

    if num_alternating == 1:
        print('In the following input fields, enter one of the following: mon, tues, wed, thur, friM, or friA.')
        day1 = str(input('Day 1 (every week): '))
        constant_sessions.append(day1)
        day2 = str(input('Day 2 (every week): '))
        constant_sessions.append(day2)
        day31 = str(input('Day 3 option 1 (every other week): '))
        alternating_sessions.append(day31)
        day32 = str(input('Day 3 option 2 (every other week): '))
        alternating_sessions.append(day32)

    if num_alternating == 2:
        print('In the following input fields, enter one of the following: mon, tues, wed, thur, friM, or friA.')
        day1 = str(input('Day 1 (every week): '))
        constant_sessions.append(day1)
        day21 = str(input('Day 2 option 1 (every other week): '))
        alternating_sessions.append(day21)
        day22 = str(input('Day 2 option 2 (every other week): '))
        alternating_sessions.append(day22)
        day31 = str(input('Day 3 option 1 (every other week): '))
        alternating_sessions.append(day31)
        day32 = str(input('Day 3 option 2 (every other week): '))
        alternating_sessions.append(day32)

    if num_alternating == 3:
        print('In the following input fields, enter one of the following: mon, tues, wed, thur, friM, or friA.')
        day11 = str(input('Day 1 option 1 (every other week): '))
        alternating_sessions.append(day11)
        day12 = str(input('Day 1 option 2 (every other week): '))
        alternating_sessions.append(day12)
        day21 = str(input('Day 2 option 1 (every other week): '))
        alternating_sessions.append(day21)
        day22 = str(input('Day 2 option 2 (every other week): '))
        alternating_sessions.append(day22)
        day31 = str(input('Day 3 option 1 (every other week): '))
        alternating_sessions.append(day31)
        day32 = str(input('Day 3 option 2 (every other week): '))
        alternating_sessions.append(day32)

ticker = 1
scheduled_days = []

for i in range(0, number_of_weeks):
    week_sessions = []

    if ticker % 2 == 1:
        if len(alternating_sessions) == 2:
            week_sessions.append(alternating_sessions[0])
        if len(alternating_sessions) == 4:
            week_sessions.append(alternating_sessions[0])
            week_sessions.append(alternating_sessions[2])
        if len(alternating_sessions) == 6:
            week_sessions.append(alternating_sessions[0])
            week_sessions.append(alternating_sessions[2])
            week_sessions.append(alternating_sessions[4])

    if ticker % 2 == 0:
        if len(alternating_sessions) == 2:
            week_sessions.append(alternating_sessions[1])
        if len(alternating_sessions) == 4:
            week_sessions.append(alternating_sessions[1])
            week_sessions.append(alternating_sessions[3])
        if len(alternating_sessions) == 6:
            week_sessions.append(alternating_sessions[1])
            week_sessions.append(alternating_sessions[3])
            week_sessions.append(alternating_sessions[5])

    week_sessions.extend(constant_sessions)
    scheduled_days.append(week_sessions)
    ticker += 1

# Number of Members Available By Session Time
alternating_sessions.extend(constant_sessions)
sessions = alternating_sessions
session_availability = {}
members_available = 0
for a in sessions:
    for b in range(0, members_counter):
        members_available += members[b].avail[a]
    session_availability[a] = members_available
    members_available = 0


# Building 'Week' and 'Day' Object Classes
class Week:
    _registry = []

    def __init__(self, week):
        self._registry.append(self)
        self.week_number = week
        self.times_scheduled = []
        self.sessions_scheduled = []


class Day:
    _registry = []

    def __init__(self, day):
        self._registry.append(self)
        self.day_of_week = day
        self.members_scheduled = []


# Assigning Week and Day ids
# 'weeks_in_schedule' is a list of class objects 'Week', indicating attributes for that week in the schedule
weeks_in_schedule = []
# 'days_in_schedule' is a list of class objects 'Day', indicating attributes for that day in the schedule
days_in_schedule = []

for i in range(0, number_of_weeks):
    week = Week(i)
    week.times_scheduled = scheduled_days[i]
    weeks_in_schedule.append(week)

for each in weeks_in_schedule:
    for i in each.times_scheduled:
        day = Day(str(i))
        each.sessions_scheduled.append(day)
        days_in_schedule.append(day)


# Building Scheduling Functions
def schedule(week, day, member_object):
    """
    This function will schedule a given member for a given slot of a given week.
    :param member_object: the club member to be scheduled
    :param week: the week object of the semester that the individual will be scheduled for
    :param day: The day object of the semester that the individual will be scheduled for
    :return: This function should return updated values for the club member's
            "total_sessions" and "week_schedule" parameters. It will also update
            the corresponding "day" and "week" objects to reflect the fact that
            the individual is scheduled for the slot.
    """
    day.members_scheduled.append(member_object)
    member_object.total_sessions += 1
    member_object.scheduled_days[f'Week: {week.week_number} Day: {day.day_of_week}'] = 1
    member_object.scheduled_weeks[f'Week: {week.week_number}'] = 1


def no_schedule_dy(week, day, member_object):
    """
    This function indicates that a given member has not been scheduled for a given slot.
    :param member_object: the club member to be scheduled
    :param week: the week object of the semester that the individual will not be scheduled for
    :param day: The day object of the semester that the individual will not be scheduled for
    :return: This function should return the updated value for the club member's
            "schedule," indicating that the member is not scheduled for the corresponding
            session.
    """
    member_object.scheduled_days[f'Week: {week.week_number} Day: {day.day_of_week}'] = 0


def no_schedule_wk(week, member_object):
    """
    This function indicates that a given member has not been scheduled for a given week.
    :param member_object: the club member to be scheduled
    :param week: the week object of the semester that the individual will not be scheduled for
    :param day: The day object of the semester that the individual will not be scheduled for
    :return: This function should return the updated value for the club member's
            "schedule," indicating that the member is not scheduled for the corresponding
            session.
    """
    member_object.scheduled_weeks[f'Week: {week.week_number}'] = 0


def blank_schedule(week, member_object):
    """
    This function indicates that a given member has not yet been scheduled for a slot in a given week.
    :param member_object: the club member to be scheduled
    :param week: the week object of the semester that the individual will not be scheduled for
    :param day: The day object of the semester that the individual will not be scheduled for
    :return: This function should return the updated value for the club member's
            "schedule," indicating that the member is not scheduled for the corresponding
            session.
    """
    member_object.scheduled_weeks[f'Week: {week.week_number}'] = 9


# Scheduling Algorithm
for i in weeks_in_schedule:
    for session in i.sessions_scheduled:
        slots_open_counter = 6

        if session_availability[session.day_of_week] <= 6:
            for k in members:
                if k.avail[session.day_of_week] == 1:
                    schedule(i, session, k)
                    slots_open_counter -= 1
                if k.avail[session.day_of_week] == 0:
                    blank_schedule(i, k)

        if session_availability[session.day_of_week] > 6:
            eligible_for_session = []
            eligible_weekly = []

            for k in members:
                if k.avail[session.day_of_week] == 1:
                    scheduled_weeks_dict_key = list(k.scheduled_weeks.keys())

                    if len(scheduled_weeks_dict_key) == 0:
                        # in this scenario, the member: 1. is available for a session that has >6 availability,
                        #                               2. has NOT BEEN scheduled for a single session
                        eligible_for_session.append(k)
                        k.scheduled_weeks[f'Week: {i.week_number}'] = 9  # is a code for "blank"

                    else:
                        if len(scheduled_weeks_dict_key) <= i.week_number:
                            k.scheduled_weeks[f'Week: {i.week_number}'] = 9
                            # in this scenario, the member is: 1.available for a session that has >6 availability,
                            #                                  2.has BEEN scheduled for a session this week
                        if k.scheduled_weeks[f'Week: {i.week_number}'] == 1:
                            # in this scenario, the member is: 1.available for a session that has >6 availability,
                            #                                  2.has BEEN scheduled for a session this week
                            no_schedule_dy(i, session, k)
                        else:
                            eligible_for_session.append(k)
                            # in this scenario, the member is: 1.available for a session that has >6 availability,
                            #                                  2.has NOT BEEN scheduled for a session this week

            # This section is for individuals who have not had a session at all, or have not had one last week.
            for l in eligible_for_session:
                if slots_open_counter > 0:

                    if l.total_sessions == 0:
                        schedule(i, session, l)
                        slots_open_counter -= 1

                    else:
                        # Scheduling club members without a penalty every other week
                        if l.penalty == 0:
                            for week, value in l.scheduled_weeks.items():
                                if week == f'Week: {i.week_number - 1}':
                                    if value == 0:
                                        schedule(i, session, l)
                                        slots_open_counter -= 1
                                    else:
                                        eligible_weekly.append(l)

                        # Scheduling club members with a penalty every third week
                        if l.penalty == 1:
                            for week, value in l.scheduled_weeks.items():
                                if week == f'Week: {i.week_number - 1}' and value == 0:

                                    for week2, value2 in l.scheduled_weeks.items():
                                        if week2 == f'Week: {i.week_number - 2}' and value2 == 0:
                                            schedule(i, session, l)
                                            slots_open_counter -= 1

            # Removing members with a penalty from the "eligible_weekly" list,
            # preventing them from being scheduled in other openings.
            for o in eligible_weekly:
                if o.penalty == 1:
                    eligible_weekly.remove(o)

            # Scheduling members who have had a session last week
            for m in sorted(eligible_weekly, key=lambda member_x: member_x.total_sessions):
                if slots_open_counter > 0:

                    for week, value in m.scheduled_weeks.items():
                        if week == f'Week: {i.week_number - 1}':
                            if value == 1:
                                schedule(i, session, m)
                                slots_open_counter -= 1

            # Setting all members who did not get a slot this week to 0 in their scheduled_weeks dictionary
            for n in members:
                for week, value in n.scheduled_weeks.items():
                    if week == f'Week: {i.week_number}':
                        if value == 9:
                            no_schedule_wk(i, n)


# Assigning a user-generated PATH in which to save the resulting csv files
path = str(input("Where would you like to save the files? "))
print('''
In the following field, enter an identifier for the semester to which this schedule applies.

Ex: _spring2022 or _fall2023
''')
csv_id = str(input('Optional identifier for new files: '))


# Generating a schedule stats file
name_lst = []
total_sessions_lst = []
for s in members:
    name_lst.append(s.name)
    total_sessions_lst.append(s.total_sessions)
name_df = pd.DataFrame(name_lst, columns=['Name'])
total_sessions_df = pd.DataFrame(total_sessions_lst, columns=['Total Sessions'])
stats_df = pd.concat([name_df, total_sessions_df], axis=1)
stats_df.to_csv(f'{path}new_stats{csv_id}.csv')
print("Preview of new_stats file:")
print(stats_df)

# Generating the final schedule output
week_dfs = []
for p in weeks_in_schedule:
    column = []

    for q in p.sessions_scheduled:
        column.append(f'Day: {q.day_of_week}')

        for r in q.members_scheduled:
            column.append(r.name)

    indexes = list(range(0, len(column)))
    col_df = pd.DataFrame(column, columns=[f'Week: {p.week_number}'])
    week_dfs.append(col_df)

all_weeks_df = pd.concat(week_dfs, axis=1)
all_weeks_df.to_csv(f'{path}new_schedule{csv_id}.csv')
print("Preview of new_schedule file:")
print(all_weeks_df)
end = str(input("You're all done! Press enter to end the program. "))
