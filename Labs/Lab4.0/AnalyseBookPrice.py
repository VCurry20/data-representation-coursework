# Lab topic 4
# All functions are listed in another python script
# Here we can use functions to actively work on the data


# Average cost price for all books on the site

from Book_API_DAO import getAllbooks # imports my functions

books = getAllbooks()
total = 0
count = 0 
for book in books:
    # print(book)
    total += book["Price"]
    count += 1


print ("Average of", count, "books is", total/count)


# floating points are not accurate for this kind of analysis
