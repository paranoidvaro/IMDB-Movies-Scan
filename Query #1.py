#Task 2 - Query n1

import pickle

#Clean Data Loading
clean_title_basics = pickle.load(open('C:/Users/valer/Desktop/Uni/Programmi Luiss/Programmazione/Progetto di gruppo programmazione/coding project/clean_title_basics.pkl','rb'))
clean_title_principals = pickle.load(open('C:/Users/valer/Desktop/Uni/Programmi Luiss/Programmazione/Progetto di gruppo programmazione/coding project/clean_title_principals.pkl','rb'))

max_personnel = 0
for lst in clean_title_basics:
    if lst[3]>= 60:
        #Veryfing film duration above one hour
        directors = len(clean_title_principals[lst[0]]['director'])
        actors = len(clean_title_principals[lst[0]]['cast'])
        if directors + actors > max_personnel:
            max_personnel = directors + actors
            #Creating the final list with the plotted results
            final_lst = [lst[2], lst[3], directors, actors]

#print(final_lst)
pickle.dump(final_lst,open('C:/Users/valer/Desktop/Uni/Programmi Luiss/Programmazione/Progetto di gruppo programmazione/coding project/query1.pkl','wb'))