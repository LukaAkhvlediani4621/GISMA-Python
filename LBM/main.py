

#we are importing the book class from the book.py file. So the system displays the books authors, titles ect.
#I specifically chose Georgian authors and books i hope you will Check some of them <3

from book import book
book1 = book("ჯაყოს ხიზნები/Jayos Dependents by", "მიხეილ ჯავახიშვილი/Mikhail Javakhishvili", 1924)
book2 = book("მთვარის შუქზე/On The Moon light by", "გურამ დოჩანაშვილი/Guram Dochashvili", 1978)
book3 = book("მგზავრის წერილები/Letters of a Traveler by", "ილია ჭავჭავაძე/Ilia Chavchavadze", 1985)
book4 = book("ვეფხისტყაოსანი/The Knight in the Panther's Skin by", "შოთა რუსთაველი/Shota Rostaveli", 1180)
book5 = book("სტუმარ-მასპინძელი/Host by", "ვაჟა ფშაველა/Vazha Pshavali", 1985)

books = [book1, book2, book3, book4, book5]

