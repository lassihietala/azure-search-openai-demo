# Malliratkaisuja

## Toimijan tyypin vaihto organisaatiosta henkilöksi antaa joskus virheilmoituksen
Joskus tallennus antaa virheilmoituksen, vaikka tyyppi vaihtuukin. Näissä tapauksissa sovelluksen taustalla lähtee kaksi yhtäaikaista päivityskutsua tietokantaan. Virheilmoitus on kuitenkin käyttäjälle aiheeton, sillä muutos on tallentunut onnistuneesti tietokantaan.

## Classicin toteumakirjaus ei nouse Enterprisen työmaan toteumiin
Tarkista, puuttuuko Classicin työkohteen tiedoista tilaustunnus. Jos tilaustunnus puuttuu, toimi seuraavasti:

1. Lisää ja tallenna oikea tilaustunnus työkohteen tietoihin
2. Avaa työkirjaus/toteuma, lisää Lisätiedot-tekstikenttään piste eli . ja tallenna työkirjaus/toteuma
3. Päivitä Enteprisen Työmaan toteumat -välilehti ja tarkista, löytyykö toteuma

Tarkista, puuttuuko työkohteelta työmaalinkki. Työmaan työlajilla näkyy statuksena Luo työkohde, vaikka työkohde on jo luotu. Toteutettu työkohde ei ole todennäköisesti päivittänyt statusta tilaustuotteelle eikä muodostanut tilaukselle toteumatuotetta. Avaa Enterprisestä Puukauppa ja metsänhoito -moduulista Työkohteet-listanäkymä ja etsi työkohde esimerkiksi nimen, työkohteen statuksen ja/tai työlajin avulla. Jos työkohteelta puuttuu työmaalinkki, toimi seuraavasti:

1. Valitse työkohde ja klikkaa Liitä työmaahan -toimintoa.<br/>
2. Etsi ja valitse oikea työmaa, minkä jälkeen tallenna.<br/>
3. Siirry Classicin työnhallintaan ja uudelleentallenna työkirjaus/toteuma (Merkitse Lisätiedot-tekstikenttään piste eli . ja tallenna).
4. Siirry Enterprisen Työmaan toteumat -välilehdelle ja tarkista, löytyykö toteuma.

Jos työkohteelta puuttuu työmaalinkki eikä linkityksen lisääminen onnistu yllä mainituilla ohjeilla, ota yhteys käytön tukeen.
Tarkista korjauksen jälkeen työkohdetta vastaavan tilaustuotteen status ja muokkaa se tarvittaessa ajan tasalle. Jos toteumatuotetta ei ole muodostunut tilaukselle, yritä muodostaa toteumatuote tilaustuote toteuttamalla (Toiminnot > Siirrä valitut toimitetuksi) tai luo uusi toteumatuote tilaustuotetta vastaavilla tiedoilla. Ota tarvittaessa  hteys käytön tukeen, jos et saa ongelmaa omatoimisesti korjattua. 
Onko urakoitsijatiedoissa puutteita. Urakoitsija täytyy olla sekä Enterprisessä että Classicissa ja y-tunnuksen pitää täsmätä.
Lisää urakoitsijan tietoihin tarvittaessa y-tunnus, minkä jälkeen udelleentallenna työkirjaus/toteuma (Merkitse Lisätiedot-tekstikenttään piste eli . ja tallenna).
Jos urakoitsijatiedoissa on enemmän puutteita:

1. Tutustu PDF-käyttöohjeen osioon Urakoitsijatiedot
2. Tee tarvittavat lisäykset/muutokset urakoitsijatietoihin
3. Siirry Classicin työnhallintaan ja uudelleentallenna työkirjaus/toteuma (Merkitse Lisätiedot-tekstikenttään piste eli . ja tallenna)
4. Siirry Enterprisen Työmaan toteumat -välilehdelle ja tarkista, löytyykö toteuma

Muita mahdollisia syitä: Kokeile uudelleentallentaa työkirjaus/toteuma Classicin työnhallinnassa (Merkitse Lisätiedot-tekstikenttään piste eli . ja tallenna).
Ostotuotteiden työlajikohdistuksissa puutteita (tutustu PDF-käyttöohjeen osioon Työkirjaukset/toteumat eivät näy ‘Työmaan toteumat’ -välilehdellä).
Jos ongelma ei ratkea yllä mainituilla ohjeilla, ota yhteys käytön tukeen.

## Henkilön muuttaminen kuolinpesäksi antaa virheen Internal Server Error
Yleensä toimijatyypin muutokset toimivat sovelluksessa hyvin, mutta muutamia tällaisia tapauksia on ollut, että Service Deskin on muutettava tieto suoraan tietokantaan.

## Joillekin asiakkaille ei ole muodostunut asiakasnumeroa. 

Enterprisessä luoduille toimijoille ei generoidu asiakasnumeroa automaattisesti, sillä asiakasnumero ei ole Enterprisen toimintojen kannalta välttämätön tieto. Nostoaineistossa aiemmassa järjestelmässä olleet asiakasnumerot ovat tulleet Enterpriseen aineistonoston yhteydessä. Asiakasnumeroa voi tarvittaessa ylläpitää asiakastietoja muokkaamalla.

## OmaMetsään rekisteröityneen käyttäjän valtuutuspyyntöä ei saa lähetettyä.

Käyttäjä on rekisteröitynyt OmaMetsä-käyttäjäksi, mutta valtuutuspyyntöä ei saa lähetettyä. Valtuutuksen vahvistaminen edellyttää pakollisten tietojen löytymisen ja myös virheelliset tiedot saattavat estää vahvistamisen. Pakollisiin tietoihin kuuluu vähintään yhden dokumentin (valtakirja, lainhuutotodistus tms.) lisäämisen Dokumentit-välilehdelle ja vähintään yhden kiinteistön valitsemisen aktiiviseksi. Tarkista, että esimerkiksi vähintään yksi dokumentti on lisätty."


## Työmaalla kuvion työlajin tietoja ei pysty muokkaamaan, koska Tallenna-painike jää harmaaksi. 

Ongelma liittyy kyseisen kuvion avohakkuun tietoihin. Classicissa kuviolle on kirjattu hakkuun puutavaralajeihin muuta lehtipuuta, mutta keskijäreyksien puolella puulajina on haapa. Tämä aiheuttaa tietojen siirtymisen vajavaisena LeafPointin puolelle, koska sovellukset eivät osaa yhdistää noita kahta toisiinsa.

## En saa katkontaennustetta luotua, koska tukkiprosentit puuttuvat. Tukkiprosentteja ei enää pääsee muokkaamaan, vaan ne ovat lukossa. 

Työmaa ja sen kuviot ovat lukossa, jos jokin tarjouspyyntö on lähetetty Pinjaan ja/tai Kuutioon ja kyseinen tarjouspyyntö on vielä voimassa ts. tarjouksen viimeinen jättöpäivä ei ole vielä umpeutunut. Lukituksen saa avattua seuraavasti: 
- Perumalla tarjouspyynnöltä Kuutio- ja/tai Pinja-lähetyksen TAI
- Odottamalla lähetetyllä tarjouspyynnöllä tarjouksen viimeisen jättöpäivän umpeutumista.

## Haluaisin muuttaa myynti- ja ostolaskujen oletusarvoista maksuehtoa

LeafPointin ostolaskutulosteille muodostuu vakiona maksuehdoksi 14 pv netto eikä sitä voi toistaiseksi valitettavasti muuttaa. Tämä tarve on kuitenkin tunnistettu ja kehitysehdotus kirjattu (Käyttäjäorganisaationa haluan hallita myynti- ja ostolaskujen oletusarvoista maksuehtoa). Työmaan toteumilla on saatavilla oheiset toiminnot tällä hetkellä, jos niistä on mitään apua:

- Hyväksy tilitykseen -toiminnon yhteydessä laskulle voi asettaa tietyn päivämäärän, mikä vaikuttaa osaltaan laskun oletusarvoiseen eräpäivään. 
- Jos ostolaskun luo manuaalisesti, niin sekä laskutus- että eräpäivän voi asettaa vapaasti.

Edellä mainitut toimenpiteet eivät kuitenkaan muuta ostolaskutulosteilla näkyvää Maksuehto-tietoa.

