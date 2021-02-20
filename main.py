# course slots
courses={   
            0:['S1','S2','S6','S7'],
            1:['S1','S7'],
            2:['S1','S2','S3','S4'],
            3:['S5','S3','S7'],
            4:['S6'],
            5:['S7'],
        }



# separate find dept and remove single dept to separate fn()




assigned={}
ass={1:'asd'}
def chk_Depth():
    single_depth={}
    minL=999
    if(not courses):
        return {},0
    print("courses")
    print(courses)
    for x in courses:
        print(x)
        minL=min(minL,len(courses[x]))
        if len(courses[x])==1:
            # x+=1        
            if courses[x][0] in single_depth.values():
                print('not possible')
                return False
            single_depth[x]=courses[x][0]
    print("minL")
    print(minL)
    return single_depth,minL

def remove_assigned_courses():
    for x in ass:
        del courses[x]

def remove_assigned_slots():
    for x in courses:
        # list comprehension neat👌
        courses[x]=[y for y in courses[x] if y not in ass.values()]
        
        # for y in ass.values():
        #     if y in courses[x]:
        #         courses[x].remove(y)
        

def check_courses():
    global ass,assigned
    minL=999
    while(ass and len(ass)):
        ass,minL=chk_Depth()
        print("inside")
        print(minL)
        if ass:
            remove_assigned_courses()
            remove_assigned_slots()
            assigned|=ass
            print('ass')

    return minL
import random
def rnd_pick(minL):
    global ass,assigned
    course,slt=0,0
    for x in courses:
        if len(courses[x])==minL:
            course=x
            slt=random.choice(courses[x])
            break
    ass={course:slt}
    print(ass)
    remove_assigned_courses()
    remove_assigned_slots()
    assigned|=ass

    


        

while(len(courses)):
    minL=check_courses()
    if not minL:
        break
    print(minL)
    # if minL!=999:
    rnd_pick(minL)
    
    print("while")
    print(courses)
    print(ass)
    print(len(courses))


print(courses)
print(assigned)
