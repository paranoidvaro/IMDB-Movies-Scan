#Task 3 - Query n2

import pickle
#Clean Data Loading
clean_title_basics = pickle.load(open('C:/Users/valer/Desktop/Uni/Programmi Luiss/Programmazione/Progetto di gruppo programmazione/coding project/clean_title_basics.pkl','rb'))

#Different dictionaries for diffent time periods
counter_dct1 = {}
counter_dct2 = {}
counter_dct3 = {}
counter_dct4 = {}

final_lst = []

def genres_dct(counter_dct):
    #Converting the fifth element of the list(string) in an accessible list
     if "," in lst[4]:
         temp_lst = lst[4].split(",")
         #Adding key : value pairs to the dictionary
         for genre in temp_lst:
             if genre in counter_dct:
                 counter_dct[genre] += 1
             else:
                 counter_dct[genre] = 1
     else:
         #Adding key : value pairs to the dictionary
         if lst[4] in counter_dct:
             counter_dct[lst[4]] += 1
         else:
             counter_dct[lst[4]] = 1

#Defining the most popular genre
def most_popular( counter_dct):
    for key in counter_dct:
        try:
             if counter_dct[key] > counter_dct[max_genre]:
                max_genre = key
        except NameError:    
            max_genre = key

    final_lst.append(max_genre)
    final_lst.append(counter_dct[max_genre])

#Dividing genres for time periods
for lst in clean_title_basics:
    if lst[5] <= 1900:
        genres_dct( counter_dct1)
    elif lst[5] >= 1901 and lst[5] <= 1950:
        genres_dct( counter_dct2)
    elif lst[5] >= 1951 and lst[5] <= 2000:
        genres_dct(counter_dct3)
    else:
        genres_dct( counter_dct4)

most_popular(counter_dct1)
most_popular(counter_dct2)
most_popular(counter_dct3)
most_popular(counter_dct4)

#print(final_lst)
pickle.dump(final_lst,open('C:/Users/valer/Desktop/Uni/Programmi Luiss/Programmazione/Progetto di gruppo programmazione/coding project/fast_query2.pkl','wb'))