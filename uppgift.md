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
     .upper()
     .lower()
     Kan användas för att normalisera användar-input så att t.ex. ett match case träffar både 'A' och 'a'.

     .strip()
     Tar bort whitespace och grejer i början/slutet på strängar.

5. **Sekvenstyper och deras operationer:**

   - **Svar:**

6. **Ordböcker:**

   - **Svar:**

7. **Inbyggda funktioner:**

   - **Svar:**
     print()
     int()
     str()
     enumerate()
