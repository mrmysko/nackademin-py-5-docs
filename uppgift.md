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

   Den börjar med nyckelordet "if", följt av ett uttryck, kolon och efter det en "suite".

   En suite definieras som:

   <pre>
   suite ::= stmt_list NEWLINE | NEWLINE INDENT statement+ DEDENT
   </pre>

   Efter kolonet i if-satsen kommer en newline eller en indenterad newline följt av minst ett statement. Suiten avslutas med en "dedent", en indent åt andra hållet.
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

   "An assignment expression (sometimes also called a “named expression” or “walrus”) assigns an expression to an identifier, while also returning the value of the expression."

   En assignment_expression har en optional identifier

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

   keyword 'in' följt av en 'starred_list':

   <pre>
   starred_list ::= starred_item ("," starred_item)* [","]
   </pre>

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
