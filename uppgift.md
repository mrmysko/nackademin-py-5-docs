# Uppgift 5 - Grundläggande förståelse för dokumentationen

## Language Reference

If, while och for är alla typer av "compound statements". De har en header som börjar med ett keyword, följt av ett uttryck och avslutas med ett kolon.

1. **If-satser:**

   - **Svar:**

   <pre>
   if_stmt ::= "if" assignment_expression ":" suite
               ("elif" assignment_expression ":" suite)*
               ["else" ":" suite]
   </pre>

   Den börjar med nyckelordet "if", sen kommer ett uttryck, kolon och efter det en "suite".

   En suite definieras som:

   <pre>
   suite ::= stmt_list NEWLINE | NEWLINE INDENT statement+ DEDENT
   </pre>

   Det är en lista av statements som avslutas med en newline, eller en indenterad newline följt av minst ett statement. Suiten avslutas med en "dedent", en indent åt andra hållet.

   Optionally kan man följa if-satsen med ingen eller oändligt många elif-satser, och en optional else-sats. Båda som har sina egna keywords, kolon och följs av en suite. Det behövs inget nytt "assignment_expression".

   <pre>
   user_input = input() # Ja

   if user_input == "Ja":
   user_input = "Nej"

   print(user_input) # Nej
   </pre>

   If-satsen ändrar användar-inputen till "Nej" om user_input matchar "Ja".

2. **While-loopar:**

   - **Svar:**

   <pre>
   while_stmt ::=  "while" assignment_expression ":" suite
                  ["else" ":" suite]
   </pre>

   Samma som if-satsen, men nyckelordet är while och den tillåter inte elif-satser.

   <pre>
   assignment_expression ::= [identifier ":="] expression
   </pre>

   En assignment_expression har en optional identifier av ett namn och en walrus operator ":=" (ny i python 3.8), sen kräver den ett uttryck.

   <pre>
   while i < range(11):
      print(i)
      i += 1
   </pre>

   Printar alla nummer mellan 0 och 10.

   Loopen kommer gå så länge uttrycket är True, men det är inte ett krav för ett expression att ha ett state där den blir False.

   Så den här loopen jämför två nummer och får tillbaka ett boolskt värde, men "while i + 1:" skulle vara en syntaxtiskt lika korrekt loop.

3. **For-loopar:**

   - **Svar:**
   <pre>
   for_stmt ::=  "for" target_list "in" starred_list ":" suite
                 ["else" ":" suite]
   </pre>

   Nyckelordet är 'for' och det följs av en 'target_list' som definieras som:

   <pre>
   target_list ::= target ("," target)* [","]
   </pre>

   Det är ett target som kan följas av 0 till oändligt många komma-serparerade targets, och kan följas av ett komma.

   Sen keyword 'in' följt av en 'starred_list':

   <pre>
   starred_list ::= starred_item ("," starred_item)* [","]
   </pre>

   Som ser likadan ut som target_list, men med starred_items istället för targets.

   Targets är assignment statements, och starred_items är assignment expressions.

   <pre>
   for key, value in dict.items():
      print(key, value)
   </pre>

   Det är lättare att iterera över en sekvens som har ett bestämt antal element, eller flera element samtidigt med en for-loop istället för en while-loop.

## Standard Library

4. **Strängmetoder:**

   - **Svar:**

   .upper() / .lower()

   Kan användas för att normalisera användar-input så att t.ex. ett match case träffar både 'A' och 'a'.
   <pre>
   name = input("What's your name?: ").upper() # John
   print(name) # JOHN
   </pre>

   \<var>.join()

   Gör om en "iterable" till en enhetlig sträng, med \<var> som mellantecken.
   <pre>
   some_list = ["1", "2", "3", "4"]
   joined_string = ".".join(some_list)
   print(joined_string) # "1.2.3.4"
   </pre>

   .capitalize()

   Gör första bokstaven till stor i en sträng.

   <pre>
   name = input("What's your name?: ").lower() # John
   print(name.capitalize()) # John
   </pre>

   Om man har konverterat ett namn till lowercase för att matcha det om någon skriver sitt namn som jOhN, så kan man skriva det med stor bokstav med .capitalize().

   Tydligen finns det en .casefold() som är bättre på att göra om fler bokstäver till lowercase än .lower().

5. **Sekvenstyper och deras operationer:**

   - **Svar:**

   Tuple: immutable ordnad sekvens av element.

   Man kan skapa en tom tuple med tuple(\<iterable>), eller \<variable> = (). För att skapa en tuple med ett element måste man lägga till ett komma efter elementet var2 = "a",

   Det viktiga för att skapa en tuple är komma-tecknen, inte paranteserna. variable = a, b, c blir en tuple (a, b, c). Men det skrivs oftast var = (a, b, c) för läsbarhet.

   Man kan bara lägga till andra tuple-objekt till en tuple, så man måste konvertera dom med tuple(\<iterable>) innan dom kan läggas till som string concatenation med "+".

   <pre>
   some_tup = ("a", )

   a_list = ["b", "c", "d"]

   some_tup = some_tup + a_list # TypeError

   some_tup = some_tup + tuple(a_list) # ("a", "b", "c", "d")
   </pre>

6. **Ordböcker:**

   - **Svar:**

   En dict är en oordnad samling av key-value pairs. Den skapas antingen med \<variable> = dict(), eller \<variable> = {}

   <pre>
   some_dict = dict()
   some_dict["value"] = "key" # Lägger till nyckeln "key" med värdet "value" i some_dict. Ser ut som {"key": "value"}

   for key, value in some_dict.items():   # Itererar över en dict och packar upp nyckeln och värdet till key, value variablerna.
   |   print(key, value)                  # Finns .keys() och .values() också om man bara vill ha den ena
   </pre>

   Man kan använda några liknande metoder för att ta bort en key ur en dict som ett värde i en lista. Men istället för att att peka på ett index så pekar man på en key.

   <pre>
   some_dict.pop("key")
   del some_dict["key"]
   some_dict.clear()    # Tar bort allt
   </pre>

7. **Inbyggda funktioner:**

   - **Svar:**

   round() - Avrundar en float till närmaste "n'th" decimal.

   <pre>
   45 / 23           # 1.9565217391304348
   round(45 / 23, 2) # 1.96
   round(45 / 23)    # 2 - Inget decimalantal angivet, avrundar till närmsta int istället.
   </pre>

   str() - Konverterar en variabel till en sträng.

   <pre>
   num = 666
   beast = str(num) + ", the number of the beast."
   print(beast) # "666, the number of the beast."
   </pre>

   enumerate() - Går igenom en iterable och skapar ett enumerate objekt med index och värdet.

   <pre>
   some_list = ["a", "b", "c", "d"]
   for x, y in enumerate(some_list)
    |  print(x, y) # 1 a
    |              # 2 b
    |              # 3 c etc.
   </pre>

   len() - Returnerar längden på en iterable som en int.

   <pre>
   some_list = ["apple", "pear", "banana", "orange"]
   print(len(some_list)) # 4
   </pre>
