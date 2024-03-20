from Himar import Himar
from Realist import Realist
from Pozitiv import Pozitiv
import random
person_1 = Realist("Արմեն")
person_2 = Himar("Ալեքսանդր")
person_3 = Pozitiv("Նարինե")
person_4 = Realist("Բաղդասար")
person_5 = Pozitiv("Անահիտ")
person_lst = [person_1, person_2, person_3, person_4, person_5]

for i in person_lst:
    person_lst.remove(i)
    for person in person_lst:
        # i = random.randint(0, len(person_lst)-1)
        file = open('conversation_log.txt', 'a', encoding='utf-8')
        file.write(str(i.process(person)+'\n'))
        file.write(str(person.process(i)+'\n'+'\n'))
        file.close()
        person_lst = [person_1, person_2, person_3, person_4, person_5]
