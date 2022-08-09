from Model.People.Person import Person
from datetime import date
data = date.today()
# Many stupid design decisions were made with the explicit purpose to limit myself and force thought and problemsolving
# in order to learn the syntax faster
def main():
   print(Person("daniele", "cattabriga", "codicefiscale", date.today()).returnAsCSV())

if __name__ == '__main__':
   main()


