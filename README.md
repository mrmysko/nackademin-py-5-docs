[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/J4YLUGjn)
# Uppgift 5 - Grundläggande förståelse för dokumentationen

## <a name='Syfte'></a>Syfte

Syftet med denna uppgift är att utveckla förmågan att självständigt navigera i
"The Python Language Reference" och "The Python Standard Library" för att förstå
Pythons syntax och utnyttja dess standardbibliotek.

<!-- vscode-markdown-toc -->

- [Syfte](#Syfte)
- [Förberedelser](#Frberedelser)
- [Beskrivning](#Beskrivning)
  - [Language Reference](#LanguageReference)
    - [Viktig avgränsning gällande BNF](#ViktigavgrnsninggllandeBNF)
  - [Standard Library](#StandardLibrary)
  - [Inlämningsinstruktioner](#Inlmningsinstruktioner)
- [Anteckningar](#Anteckningar)

<!-- vscode-markdown-toc-config
	numbering=false
	autoSave=true
	/vscode-markdown-toc-config -->
<!-- /vscode-markdown-toc -->

## <a name='Frberedelser'></a>Förberedelser

Läs och förstå dokumentet [Guide till Pythons
dokumentation](https://docs.google.com/document/d/1o9vcKHdu-XLkrc2o3fG_q3Nsip4gklomVY0_HBss5Ig/edit).
Det introducerar läsaren till Pythons dokumentation och förklarar hur
Backus-Naur Form (BNF) fungerar, vilket är nödvändigt för att navigera och tolka
dokumentationen effektivt.

## <a name='Beskrivning'></a>Beskrivning

Denna uppgift fokuserar på att fördjupa förståelsen för de två viktigaste
delarna av Pythons dokumentation: [The Python Language
Reference](https://docs.python.org/3/reference/index.html) och [The Python
Standard Library](https://docs.python.org/3/library/index.html). Att kunna
använda dessa delar är avgörande för att kunna utnyttja Pythons fulla potential
i programmeringsprojekt.

### <a name='LanguageReference'></a>Language Reference

1. **If-satser:**

   Beskriv detaljerat användningen av `if`-satser i Python, en viktig mekanism
   för villkorsstyrd exekvering. Presentera `if`-satsers BNF-notation och
   förklara dess struktur och funktion. Komplettera med kodexempel för att
   illustrera hur `if`-satser kan påverka programflödet genom att reagera på
   olika villkor.

2. **While-loopar:**

   Utforska användningen av `while`-loopar för att upprepa kodblock baserat på
   ett specifikt villkor. Presentera `while`-looparnas BNF-notation och förklara
   hur den beskriver loopens mekanik. Använd kodexempel för att visa
   `while`-loopar i praktiken.

3. **For-loopar:**

   Analysera `for`-loopar som en metod för iteration över sekvenser. Presentera
   `for`-looparnas BNF-notation och diskutera hur den återspeglar deras struktur
   och användningsområden. Ge exempel på kod som visar `for`-loopar i
   användning, och jämför dem med `while`-loopar för att framhäva deras unika
   fördelar.

#### <a name='ViktigavgrnsninggllandeBNF'></a>Viktig avgränsning gällande BNF

När BNF-notationen hänvisar till andra delar av dokumentationen, är det viktigt
att hålla förklaringen fokuserad och relevant. För "icke terminanter" i BNF som
länkar till andra dokumentationsdelar, som i exemplet nedan, ge en översiktlig
förklaring med några exempel istället för att utforska hela Python-språket:

```
if_stmt ::= "if" assignment_expression ":" suite
("elif" assignment_expression ":" suite)*
["else" ":" suite]
```

I detta fall, förklara kortfattat `assignment_expression` och `suite` med ett
par konkreta exempel, utan att dyka djupt in i varje aspekt.

### <a name='StandardLibrary'></a>Standard Library

4. **Strängmetoder**:

Analysera fyra strängmetoder (hitta typen `str`) i Python, till exempel
`.capitalize()`. För varje metod, inkludera ett exempel som demonstrerar dess
användning och beskriv ett specifikt scenario där metoden är användbar.

5. **Sekvenstyper och deras operationer**:

Fokusera på en vald sekvenstyp i Python, exempelvis `list`, `tuple`, eller
`range`. Använd kodexempel för att demonstrera hur man skapar en instans av
denna typ och genomför grundläggande operationer såsom att lägga till, ändra och
ta bort element, eller förklara varför vissa operationer inte är möjliga.

6. **Ordböcker**:

Beskriv ordböcker (`dict`) i Python, inklusive skapande, tillägg av
nyckel-värdepar, elementåtkomst och manipulation. Visa med kodexempel hur man
skapar en ordbok, lägger till och ändrar innehåll, samt itererar över den med en
loop.

7. **Inbyggda funktioner**:

Välj fyra **inbyggda funktioner** (som exempelvis `len()` och `print()`) i
Python och beskriv hur de används med text och kodexempel.

### <a name='Inlmningsinstruktioner'></a>Inlämningsinstruktioner

För att lämna in din uppgift, vänligen följ dessa steg:

1. **Använda Github Classroom:**

   - Du har troligen redan accepterat uppgiften via en länk som tillhandahålls
     av utbildaren och gjort en `git clone` av det tilldelade repositoriet då du
     läser denna text. Det är i detta repository du kommer att hitta `README.md`
     med ytterligare instruktioner.

2. **Modifiera `uppgift.md`:**

   - Din lösning på uppgiften ska skrivas i `uppgift.md`. Det finns en struktur
     att utöka med dina lösningar i `uppgift.md`.

3. **Lämna in med Git:**

   - När du är klar med din uppgift, använd kommandona `git add .`, `git commit`
     följt av `git push` för att skicka in dina ändringar till GitHub.

4. **Automatiska "smoke tests":**

   - Efter att du har pushat din kod kommer automatiska "smoke tests" att köras.
     Dessa tester indikeras med en grön bock om de passerar, eller ett rött
     kryss om de misslyckas. Om du får ett rött kryss, är det viktigt att du
     klickar dig fram i GitHub tills du kan se varför testerna inte passerade.

5. **Feedback och granskning från utbildaren:**

   - Om dina tester passerar med en grön bock, kan du invänta feedback från din
     utbildare. Utbildaren kan antingen sätta "request changes" om ytterligare
     förändringar behövs, eller "approve" om uppgiften är godkänd som den är.
     Det är viktigt att du inväntar någon av dessa innan du väljer Merge.
   - Efter att utbildaren har gjort "Approve" på din inlämning, får du göra en
     "Merge" av din "Feedback"-pull request, men inte förrän ett godkännande har
     erhållits.

6. **Initiera diskussioner i pull requesten:**

   - Som student är du uppmuntrad att aktivt delta i processen genom att
     initiera diskussioner i din "Feedback"-pull request. Detta är en viktig del
     av inlärningsprocessen, där du kan ställa frågor, begära förtydliganden
     eller diskutera lösningar och feedback med din utbildare. Att engagera sig
     i dessa diskussioner ger dig möjlighet att djupare förstå uppgiftens krav
     och förbättra din kod baserat på interaktionen.

## <a name='Anteckningar'></a>Anteckningar

Inga.
