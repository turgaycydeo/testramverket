Teorifrågor
1. Vad är skillnaden mellan enhetstest, integrationstest, regressionstest och prestandatest?
Ett enhetstest testar en liten del av koden isolerat, oftast en metod eller en klass. Om klassen är beroende av något annat ersätter man beroendet med en mock eller fake, så att det bara är själva enheten som testas. I mitt projekt testar jag till exempel BookStore med en mockad FavoriteBooks.

Ett integrationstest kontrollerar att flera delar fungerar ihop och att data skickas mellan dem på rätt sätt. Här använder man de riktiga klasserna, till exempel när jag testar att en bok hamnar i FavoriteBooks när man kör toggleFavorite i BookStore.

Ett regressionstest ser till att saker som fungerade tidigare inte går sönder när man lägger till ny kod. Det är egentligen ingen egen typ av test, utan snarare ett syfte med testerna. Alla tester som man sparar och kör igen blir med tiden regressionstester. Ofta skriver man också ett nytt test när man hittat en bugg, så att samma fel inte kommer tillbaka.

Ett prestandatest mäter hur snabbt och stabilt systemet är, till exempel körtid, svarstid och resursanvändning. Det blir särskilt viktigt när datamängden eller belastningen ökar. I kursen använde vi pytest-benchmark för att jämföra olika versioner av en funktion.

2. Beskriv hur det går till när man arbetar med TDD.
När man arbetar med TDD skriver man testet innan koden. Först skriver man ett test för något som ännu inte finns och kör det – då ska testet bli rött. Därefter skriver man så lite kod som möjligt för att få testet grönt. När testet är grönt städar man upp och förbättrar koden, vilket kallas refactor, och kör testerna igen för att säkerställa att allt fortfarande fungerar. Sedan tar man nästa lilla krav och upprepar processen: red, green, refactor.

Fördelen är att man hela tiden vet att koden gör det den ska, och att man tänker igenom kraven innan man börjar koda.

3. Beskriv hur BDD skiljer sig från TDD.
BDD bygger på TDD, men fokuserar mer på hur systemet ska bete sig för användaren än på enskilda funktioner. Testerna skrivs på nästan vanligt språk med Gherkin – Given, When, Then – i feature-filer. Det gör att även kunden och personer som inte programmerar kan läsa och bidra till testerna. Varje mening kopplas sedan till kod i step-filer, i vårt fall med behave.

TDD är mer riktat mot utvecklaren och handlar om små kodenheter, medan BDD skapar ett gemensamt språk för hela teamet och utgår från verkliga behov. I båda fallen skrivs testerna innan koden.

4. Vilka sorters tester skulle du vilja använda för en webbsida som liknar Läslistan?
För backend skulle jag använda enhetstester för alla klasser och metoder, eftersom de är snabba och visar exakt var ett fel finns. Jag skulle också ha integrationstester för de delar som arbetar ihop, till exempel katalogen och favoritlistan, samt mot databasen om det finns en.

För frontend skulle jag använda BDD med behave och Playwright. Då kan user stories direkt omvandlas till tester, och feature-filerna kan visas för beställaren. E2E-testerna visar att hela flödet fungerar som när en riktig användare använder sidan. Eftersom de är långsammare skulle jag inte testa varje detalj där, utan fokusera på de viktigaste användarflödena.

Alla tester skulle köras i CI vid varje push, så att regressioner upptäcks direkt. Om sidan växer och får fler användare, till exempel med quiz och diskussioner som planeras, skulle jag också lägga till prestandatester för att säkerställa att den klarar större listor och fler användare samtidigt.
