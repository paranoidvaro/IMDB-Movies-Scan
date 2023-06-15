#Data Loading

import pickle # this will load the pickle module necessary to work on pickle files.

title_basics = pickle.load(open('C:/Users/valer/Desktop/Uni/Programmi Luiss/Programmazione/Progetto di gruppo programmazione/coding project/title_basics.pkl','rb'))
title_ratings = pickle.load(open('C:/Users/valer/Desktop/Uni/Programmi Luiss/Programmazione/Progetto di gruppo programmazione/coding project/title_ratings.pkl','rb'))
title_principals = pickle.load(open('C:/Users/valer/Desktop/Uni/Programmi Luiss/Programmazione/Progetto di gruppo programmazione/coding project/title_principals.pkl','rb'))

#Define New Objects since we cannot modify original objects while iterating
temp_title_basics = title_basics[:]


#Task 1 - Data Cleaning


for lst in temp_title_basics:
    if '\\N' in lst:
        #Cleaning the noise
        title_basics.remove(lst)
        title_ratings.pop(lst[0])
        title_principals.pop(lst[0])

for lst in title_basics:
        #Converting numerical attributes in numerical datatypes
        lst[3] = int(lst[3])
        lst[5] = int(lst[5])
pickle.dump(title_basics,open('C:/Users/valer/Desktop/Uni/Programmi Luiss/Programmazione/Progetto di gruppo programmazione/coding project/clean_title_basics.pkl','wb'))
pickle.dump(title_principals,open('C:/Users/valer/Desktop/Uni/Programmi Luiss/Programmazione/Progetto di gruppo programmazione/coding project/clean_title_principals.pkl','wb'))

for key in title_ratings:
        #Converting numerical attributes in numerical datatypes
        title_ratings[key][0] = float(title_ratings[key][0])
        title_ratings[key][1] = int(title_ratings[key][1])
pickle.dump(title_ratings,open('C:/Users/valer/Desktop/Uni/Programmi Luiss/Programmazione/Progetto di gruppo programmazione/coding project/clean_title_ratings.pkl','wb'))












