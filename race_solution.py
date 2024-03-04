"""
This is a stub for the comp16321 midterm.
Do not edit or delete any lines given in this file that are marked with a "(s)".
(you can move them to different lines as long as you do not change the overall structure)

Place your code below the comments marked "#Your code here".

Each method is documented to explain what work is to be placed within it.

NOTE: You can create as many more methods as you need. However, you need to add 
self as a parameter of the new method and to call it with the prefix self.name 

EXAMPLE:

def class_table_result(self, boat_type, race_results):#(s)
    strings_value = "0601-0501-0702-0803-0904-0405-0306-0207-1008-0609-0110"
    single_boat = self.remove_highest_value(strings_value)
    return(single_boat)

def remove_highest_value(self, strings_value):
    strings_value.pop(10)
    return strings_value

"""

class Races:#(s)

    def read_results(self):#(s)
    
        """
        Read in the text file and save the races_results into a python list

        :return: A list of strings denoting each race_result
        """
        results_string=[]
        with open("input.txt", "r") as file:
            lines=file.readlines()
        for line in lines:
            results_string.append(line.strip())
        return results_string
    
        pass#(s)


    def race_result(self, boat_type, race_number, results_string):#(s)

        """
        Query results_string which is read form the input.txt and  get the  result
        for the given params
        
        :param: boat_type: An integer denoting which type of boat 
        :param: race_number: An integer denoting which race
        :return: A string with the race result for the given boat_type and race_number
        """
        results_string=self.read_results()
        if(boat_type<10):
            n="0"+str(boat_type)
        else:
            n=str(boat_type)
        races=[] #to store all the races boat 'n' took part in
        for i in range(len(results_string)):
            result=str(results_string[i])
            if(result.startswith(n)):
                races.append(result[5:]) #getting only the race results
        if(race_number-1>len(races)):
            return ""
        else:
            return races[race_number-1]

        pass#(s)


    def class_table_result(self, boat_type, results_string):#(s)
        
        """
        Output the results for a given boat_type

        :param: boat_type: An integer denoting which type of boat 
        :return: A string in the specified format as shown in the pdf
        """
        results_string=self.read_results()
        boat_number=""
        if(boat_type<10):
            boat_number="0"+str(boat_type)
        else:
            boat_number=str(boat_type)
        race_type=[]
        races=[] #to store all the races boat 'n' took part in
        for i in range(len(results_string)):
            result=str(results_string[i])
            if(result.startswith(boat_number)):
                races.append(result[5:]) #getting only the race results
                race_type.append(result[2:4])
        lists=[]
        for race in races:
            l=race.split("-")
            lists.append(l)

        dictionary={"01":0, "02":0, "03":0, "04":0, "05":0, "06":0, "07":0, "08":0, "09":0, "10":0}
        countries = list(dictionary.keys())
        for i in range(len(lists)):
            rtype=int(race_type[i])
            flag=0
            disqualified_countries=[]
            disqualified_index=[]
            for j in range(len(lists[i])):
                s=str(lists[i][j])
                for x in range(len(dictionary)):
                    if s.startswith(countries[x]):
                        if(s[2:]!="xx"):
                            p=int(s[2:])
                            if(rtype==1):
                                points=p
                            elif(rtype==2):
                                points=p*2
                            dictionary[countries[x]]+=points
                        else:
                            disqualified_countries.append(countries[x]+"xx")
                            disqualified_index.append(j)
                            flag=1 #updating when there is a disqualification
                            if(rtype==1):
                                points=11
                            elif(rtype==2):
                                points=22
                            dictionary[countries[x]] += points
            #changing according to disqualification
            ctr=0
            if(flag==1):
                for j in range(len(lists[i])):
                    for k in disqualified_index:
                        if(j==k):
                            ctr+=1
                        elif(j>k):   
                            for x in range(j, len(countries)):
                                s=str(lists[i][x])
                                for y in range(len(countries)):
                                    if(s.startswith(countries[y])):
                                        if(s[2:]!="xx"):
                                            if(rtype==1):
                                                dictionary[countries[y]]-=ctr
                                            elif(rtype==2):
                                                dictionary[countries[y]]-=ctr*2
                            ctr=0
        #tiebreaker
        scores=list(dictionary.values())
        country=list(dictionary.keys())
        tied_countries=[]
        for i in range(10):
            count=0
            for j in range(10):
                if(scores[i]==scores[j]):
                    count+=1
                    if(count>1):
                        tied_countries.append(country[i])
                        break
        tied_order=[]
        last_race=lists[-1]
        for i in range(len(last_race)):
            s=str(last_race[i])
            for j in range(len(tied_countries)):
                if(s.startswith(tied_countries[j])):
                    tied_order.append(s[:2])

        for country in tied_order:
            if country in dictionary:
                value = dictionary.pop(country)
                dictionary[country] = value
            
        sortedDictionary = dict(sorted(dictionary.items(), key=lambda item: item[1]))

        final=""
        i=1
        for key,value in sortedDictionary.items():
            if(value<10):
                value_string="0"+str(value)
            else:
                value_string=str(value)
            if (i<10):
                final+=key+"-0"+str(i)+"-"+value_string+", "
            else:
                final+=key+"-"+str(i)+"-"+value_string
            i+=1
        return final

        pass#(s)

    def class_table_discard_result(self, boat_type, results_string):#(s)

        """
        Output the class table discard string

        :param: boat_type: An integer denoting which type of boat 
        :return: A string in the specified format as shown in the pdf
        """
        results_string=self.read_results()
        boat_number=""
        if(boat_type<10):
            boat_number="0"+str(boat_type)
        else:
            boat_number=str(boat_type)
        race_type=[]
        races=[] #to store all the races boat 'n' took part in
        for i in range(len(results_string)):
            result=str(results_string[i])
            if(result.startswith(boat_number)):
                races.append(result[5:]) #getting only the race results
                race_type.append(result[2:4])
        lists=[]
        for race in races:
            l=race.split("-")
            lists.append(l)

        final_lists=[]
        dictionary={"01":0, "02":0, "03":0, "04":0, "05":0, "06":0, "07":0, "08":0, "09":0, "10":0}
        countries = list(dictionary.keys())
        for i in range(len(lists)):
            final_list=[]
            qualified=[]
            rtype=int(race_type[i])
            flag=0
            disqualified_countries=[]
            disqualified_index=[]
            for j in range(len(lists[i])):
                s=str(lists[i][j])
                for x in range(len(dictionary)):
                    if s.startswith(countries[x]):
                        if(s[2:]!="xx"):
                            qualified.append(s)
                            p=int(s[2:])
                            if(rtype==1):
                                points=p
                            elif(rtype==2):
                                points=p*2
                            dictionary[countries[x]]+=points
                        else:
                            disqualified_countries.append(countries[x]+"xx")
                            disqualified_index.append(j)
                            flag=1 #updating when there is a disqualification
                            if(rtype==1):
                                points=11
                            elif(rtype==2):
                                points=22
                            dictionary[countries[x]] += points
            for a in qualified:
                final_list.append(a)
            for a in disqualified_countries:
                final_list.append(a)
            final_lists.append(final_list)

            ctr=0
            if(flag==1):
                for j in range(len(lists[i])):
                    for k in disqualified_index:
                        if(j==k):
                            ctr+=1
                        elif(j>k):   
                            for x in range(j, len(countries)):
                                s=str(lists[i][x])
                                for y in range(len(countries)):
                                    if(s.startswith(countries[y])):
                                        if(s[2:]!="xx"):
                                            if(rtype==1):
                                                dictionary[countries[y]]-=ctr
                                            elif(rtype==2):
                                                dictionary[countries[y]]-=ctr*2
                            ctr=0

        #tiebreaker
        scores=list(dictionary.values())
        country=list(dictionary.keys())
        tied_countries=[]
        for i in range(10):
            count=0
            for j in range(10):
                if(scores[i]==scores[j]):
                    count+=1
                    if(count>1):
                        tied_countries.append(country[i])
                        break
            
        #discarding the worst results
        def worst_result(country):
            ctr_rtype_1=0
            ctr_rtype_2=0
            position1, position2=[], []
            for i in range(len(final_lists)):
                rtype=int(race_type[i])
                if(rtype==1):
                    ctr_rtype_1+=1
                    for j in range(len(final_lists[i])):
                        s=str(final_lists[i][j])
                        if(s.startswith(country)):
                            if(s[2:]!="xx"):
                                position1.append(final_lists[i].index(final_lists[i][j])+1)
                            else:
                                position1.append(11)
                elif(rtype==2):
                    ctr_rtype_2+=1
                    for j in range(len(final_lists[i])):
                        s=str(final_lists[i][j])
                        if(s.startswith(country)):
                            if(s[2:]!="xx"):
                                position2.append((final_lists[i].index(final_lists[i][j])+1)*2)
                            else:
                                position2.append(22)
            if position1:
                worst_result1=max(position1)
            else:
                worst_result1=0
            if position2:
                worst_result2=max(position2)
            else:
                worst_result2=0
            return ctr_rtype_1, ctr_rtype_2, worst_result1, worst_result2

        for i in range(len(countries)):
            ctr_rtype_1, ctr_rtype_2, worst_result1, worst_result2 = worst_result(countries[i])
            if(ctr_rtype_1>2):
                dictionary[countries[i]]-=worst_result1
            if(ctr_rtype_2>2):
                dictionary[countries[i]]-=worst_result2

        scores=list(dictionary.values())
        country=list(dictionary.keys())
        tied_countries=[]
        for i in range(10):
            count=0
            for j in range(10):
                if(scores[i]==scores[j]):
                    count+=1
                    if(count>1):
                        tied_countries.append(country[i])
                        break
        tied_order=[]
        last_race=lists[-1]
        for i in range(len(last_race)):
            s=str(last_race[i])
            for j in range(len(tied_countries)):
                if(s.startswith(tied_countries[j])):
                    tied_order.append(s[:2])

        for country in tied_order:
            if country in dictionary:
                value = dictionary.pop(country)
                dictionary[country] = value

        sortedDictionary = dict(sorted(dictionary.items(), key=lambda item: item[1]))

        final=""
        i=1
        for key,value in sortedDictionary.items():
            if(value<10):
                value_string="0"+str(value)
            else:
                value_string=str(value)
            if (i<10):
                final+=key+"-0"+str(i)+"-"+value_string+", "
            else:
                final+=key+"-"+str(i)+"-"+value_string
            i+=1

        return final
        pass#(s)

    def medal_table_result(self, results_string):#(s)

        """
        Output the class table discard string

        :param: boat_type: An integer denoting which type of boat 
        :return: A string in the specified format as shown in the pdf 
        """

        gold=[0]*10
        silver=[0]*10
        bronze=[0]*10
        medalscore=[0]*10
        countries=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
        for i in range(10):
            final=self.class_table_discard_result(i+1, "")
            final_list=final.split()
            for j in range(3):
                s=final_list[j]
                country=s[:2]
                for k in range(len(countries)):
                    if(country==countries[k]):
                        if(j==0):
                            gold[k]+=1
                            medalscore[k]+=3 
                        elif(j==1):
                            silver[k]+=1
                            medalscore[k]+=2
                        elif(j==2):
                            bronze[k]+=1
                            medalscore[k]+=1     


        for i in range(10):
            for j in range(i+1,10):
                if ((medalscore[j]>medalscore[i]) or \
                (medalscore[j]==medalscore[i] and gold[j]>gold[i]) or \
                (medalscore[j]==medalscore[i] and gold[j]==gold[i] and silver[j]>silver[i]) or \
                (medalscore[j]==medalscore[i] and gold[j]==gold[i] and silver[j]==silver[i] and bronze[j]>bronze[i]) or \
                (medalscore[j]==medalscore[i] and gold[j]==gold[i] and silver[j]==silver[i] and bronze[j]==bronze[i] and countries[j]<countries[i])):
                    
                    temp=medalscore[i]
                    medalscore[i]=medalscore[j]
                    medalscore[j]=temp

                    temp=countries[i]
                    countries[i]=countries[j]
                    countries[j]=temp

                    temp=gold[i]
                    gold[i]=gold[j]
                    gold[j]=temp

                    temp=silver[i]
                    silver[i]=silver[j]
                    silver[j]=temp

                    temp=bronze[i]
                    bronze[i]=bronze[j]
                    bronze[j]=temp

        main=""
        for i in range(10):
            c=str(countries[i]).zfill(2)
            g=str(gold[i]).zfill(2)
            s=str(silver[i]).zfill(2)
            b=str(bronze[i]).zfill(2)
            ms=str(medalscore[i]).zfill(2)
            if(i<9):
                main+=c+"-"+g+"-"+s+"-"+b+"-"+ms+", "
            else:
                main+=c+"-"+g+"-"+s+"-"+b+"-"+ms
        return main
        pass#(s)


if __name__ == '__main__':#(s)
    # You can place any ad-hoc testing here
    # e.g. my_instance = Races()
    # e.g. section_1 = my_instance.read_results()
    # e.g. print(section_1)
    my_instance=Races()
    sec3=my_instance.class_table_result(10, "")
    print(sec3)
    pass#(s)