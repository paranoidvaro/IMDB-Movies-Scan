#Task 3 - Query n2
import pickle
title_basics = pickle.load(open('C:/Users/valer/Desktop/Uni/Programmi Luiss/Programmazione/Progetto di gruppo programmazione/coding project/clean_title_basics.pkl','rb'))

genres_1900=[]
genres_01_50=[]
genres_51_00=[]
genres_2001=[]


final_lst = []

#Converting the fifth element of the list(string) in an accessible list
def genre_appender( genres_lst):
    if "," in lst[4]:
        temp_lst = lst[4].split(",")
        for genre in temp_lst:
            genres_lst.append(genre)
    else:
        genres_lst.append(lst[4])

#Finding the most popular genre   
def most_popular_genre( genres_lst):
    temp_genres_lst = []
    max_count = 0
    for genre in genres_lst:
        if genre in temp_genres_lst:
            continue
        else:
            temp_genres_lst.append(genre)
            count = genres_lst.count(genre)
            if count > max_count:
                    max_genre = genre
                    max_count = count
    final_lst.append(max_genre)
    final_lst.append(max_count)
    
#Diving the genres for time period
for lst in title_basics:
    if lst[5] <= 1900:
        genre_appender(genres_1900)
    elif lst[5] >= 1901 and lst[5] <= 1950:
        genre_appender(genres_01_50)
    elif lst[5] >= 1951 and lst[5] <= 2000:
        genre_appender(genres_51_00)
    else:
        genre_appender(genres_2001)

most_popular_genre(genres_1900)
most_popular_genre(genres_01_50)
most_popular_genre(genres_51_00)
most_popular_genre(genres_2001)

#print(final_lst)
pickle.dump(final_lst,open('C:/Users/valer/Desktop/Uni/Programmi Luiss/Programmazione/Progetto di gruppo programmazione/coding project/alt_query2.pkl','wb'))