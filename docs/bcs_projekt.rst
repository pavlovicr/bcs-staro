***
BCS
***


Standardizirani popisi del(Building Construction Specifications - Tehnične specifikacije del za gradnje )
##################################################################################################################

Uvod 
****
28. člen pravilnika o projektni dokumentaciji pravi :

**.... se za celovit opis objekta v projektu za izvedbo izdela zbirno tehnično** 
**poročilo, ki vsebuje tudi skupen popis materiala in opreme z rekapitulacijo**
**stroškov izgradnje, pri čemer je za njegovo izdelavo zadolžen koordinator ....**


Vsebina Popisa materiala in opreme po zahtevah iz navedenega pravilnika  se le deloma prekriva z vsebino POPISOV DEL, ki v praksi pomenijo nepogrešljiv dokument pri gradnjah. V POPISIH DEL ni samo popisa materiala in opreme. V popisu del so opisane sestave gradbenih konstrukcij in njihovih delov , tehnologije izvedbe, uporabljeni materiali in na njih vezane zahteve iz zakona o gradbenih proizvodih, pravila za zagotavljanje kvaliete, pravila pri obračunu in merjenju količin, varnostne zahteve, navedbe standardov itd..
Popisi del so pri gradnjah po sistemu " na enoto mere " ključni pri definiranju predmeta pogodbe in izračunu končne cene pogodbenih del.

Kljub temu, da so popisi del pomemben del gradbene dokumentacije, Slovenija ne premore enotne metodologije za njihovo izdelavo prav tako ni javno dostopnih zbirk popisov del, ki bi nadomestili zastarele standardizirane popise del (GIPPOS, Fabrizzio, ..). Ostali so le redki in to samo za določene zvrsti del.(Skupnost za ceste).
Zanimivo, da se je zakonodajalec zelo potrudil pri oblikovanju knjige obračunskih izmer v "pravilniku o vsebini in načinu vodenja dnevnika o izvajanju del ter o načinu označitve gradbišča ", o vsebini pa ne duha ne sluha.

Pred več kot štiridesetimi leti smo bili slovenski gradbinci v svetovnem merilu pionirji tudi na področju standardiziranih popisov del, prirejenih celo za računalniško obdelavo. Danes, v obdobju globalizacije, standardizacije in digitalizacije imamo še vedno iste.   


Cilj projekta
*************
Izdelati sistem priprave, urejanja in vzdrževanja knjižnice standardiziranih popisov del , ki bo sodoben, digitaliziran, dostopen prek spleta in javen po principih "open source" ???

Aktivnosti in faznost
*********************
		1. faza
			* Izdelava dokumentacije
				- vsebinski del
				- razvoj aplikacije   
		2. faza
			* Produkcija
			* Urejanje specifikacij na vzorčnem primeru stanovanjske gradnje do III.FAZE
		3. faza 
			* Izdelava dokumentacije za upravljanje sistema
		 
1. Dokumentacija - vsebinski del
=================================

1.1 Splošno
------------

**Kaj je knjižnica popisov del ?**

**Knjižnica popisov del so sistematično urejeni seznami tehničnih specifikacij del (opisov del) , ki nastopajo pri gradnjah in z njimi povezanimi pravili oziroma določili.**
	* Tehnične specifikacije del opredeljujejo načine in postopke izvajanja del , izbiro uporabljenih materialov , strojev , opreme in orodja ter pogoje izvedbe del, ipd.
	* Določila opredeljujejo pravila vezana na merjenje in obračun specificiranih del, zagotavljanje kakovosti, izvajanje varnostnih ukrepov ter spoštovanje zahtev zakonodaje in standardov za specificirana dela, ipd.

**Kaj so standardizirani popisi del ?**

Popisi del sprejeti kot standardizirani popisi del, s konsenzom investitorjev gradenj, projektantov objektov in izvajalcev del.? 

1.2 Izhodišča
-------------

		* Standardizirane opise ločiti glede na vrste gradenj :
			- visoke gradnej
			- nizke gradnje
			- hidrotehnični objekti
		* Struktura in vsebine po zgledu SKUPNOST ZA CESTE 2008
		* Strukturo razčlenjena modularno ??
	
1.3 Pomen izrazov
-----------------
.. glossary::

	tehnične specifikacije del
		tehnični opisi del, ki nastopajo pri gradnjah 
	popisna postavke 
		tehnična specifikacija posameznega dela 
	postavka
		osnovna specifikacija posameznega dela
	specifikacija
		dodatna specifikacija posameznega dela	
	kriterij specifikacije 
		sorodna skupina specifikacij postavk
	dela
		ime skupine sorodnih postavk
	vrsta del
		ime skupine sorodnih del 
	splošna določila 
		pravila vezana na izvajanje skupine del
	posebna določila
		pravila vezana na izvajanje posameznih del
	kriterij določila
		sorodna skupina določil		 	


1.4 Vsebina
--------------------------------------------

* tehnične specifikacije del
* splošna in posebna določila
* popisi del

1.4.1 Tehnične specifikacije del 
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**Tehnične specifikacije del opredeljujejo vrsto del , načine in postopke izvajanja , izbiro uporabljenih materialov , strojev , opreme in orodja ter pogoje izvedbe del, ipd.**
Popisi del so sistematično urejene tehnične specifikacije posameznih del oziroma popisnih postavk.
Posamezna popisna postavka je sestavljena iz postavke, ki je osnovna tehnična specifikacija posameznega dela in specifikacijami postavke, ki dodatno specificirajo posamezno delo glede na različne kriterije. 

+-----------------------+------------------------+-----------------------------+
| skupina del           | gradbena dela          |                             |
+-----------------------+------------------------+                             |
| vrsta del             | betonska dela          |                             |
+-----------------------+------------------------+                             |
| dela                  | vgrajevanje betona     |                             | 
+-----------------------+------------------------+                             |
| postavka              | vgrajevanje betona     | kriterij                    |
+-----------------------+------------------------+                             |
| enota mere            | m3                     | specifikacije               |
+-----------------------+------------------------+-----------------------------+
|specifikacija 1        |preseka 0-12 m3/m2,m1   |presek konstrukcije          |
+-----------------------+------------------------+-----------------------------+
|specifikacija 2        |z dobavo betona C30/37  |z dobavo/ brez dobave        |
+-----------------------+------------------------+-----------------------------+

+-----------------------+------------------------+-----------------------------+
|specifikacija 3        |XC4				     |odpornost na karbonatizacijo |
+-----------------------+------------------------+-----------------------------+


+-----------------------+------------------------+----------------------------+
|specifikacija 4        |XF3                     |odpornost na zmrzovanje     |
+-----------------------+------------------------+----------------------------+
|specifikacija 5		|PVII					 |vodonepropustnost           |
+-----------------------+------------------------+----------------------------+
|specifikacija 6		|0-16 mm 				 |max. zrno                   |
+-----------------------+------------------------+----------------------------+
|specifikacija 7		|S4						 |konsistenca betona          |
+-----------------------+------------------------+----------------------------+
|specifikacija 8        |VB3					 |viden beton                 |
+-----------------------+------------------------+----------------------------+
|specifikacija 9        |P3						 |ravnost                     |
+-----------------------+------------------------+----------------------------+
|specifikacija 10       |T3						 |tekstura                    |
+-----------------------+------------------------+----------------------------+
|specifikacija 11       |C30                     |barvno odstopanje           |
+-----------------------+------------------------+----------------------------+






Popisne postavke sestavljajo postavke s specifikacijami, ki jim pripadajo in podrobneje opisujejo postavko. Specifikacije so organizirane v  okviru postavk in del , ki jim pripadajo ter po kriteriju, ki opredeljuje namen specifikacije.   
Popisne postavke so organizirane v okviru del in vrste del , ki jim pripadajo.

Popisne postavke niso organizirane v seznamih temveč jih sestavljamo modularno. 
Knjižnica  pri gradnja , ki nastopajo pri gradnjah. Postavka je jedro popisne postavke in sama po sebi opredeljuje osnovni predmet dela in enoto mere.
Specifikacije podrobneje definirajo postavko (prednmet dela)in pogoje izvedbe. Specifikacije so organizirane v okviru posameznih skupin , ki jih imenujemo kriterij specifikacije.
Postavke s specifikacijami tvorijo popisne postavke, ki jih sestavljamo modularno.

1.4.2 Splošna in posebna določila
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

** Določila opredeljujejo pravila vezana na merjenje in obračun specificiranih del, zagotavljanje kakovosti, izvajanje varnostnih ukrepov ter spoštovanje zahtev zakonodaje in standardov za specificirana dela, ipd.**




Določila niso nič drugega kot specifikacije specifikacij, postavk, del in vrst del ter določila, ki veljajo za gradnje nasplošno.Za razliko od tehnično tehnoloških specifikacij ta določajo pravila glede uporabe zakonodaje, obračunov, varnosti, kakovosti ipd.







1.5 Shema
---------

1.6 Vzorčni primer
------------------

1.7 Izhodišča za spletno aplikacijo
-----------------------------------








1.7 Vsebina
-----------

Dokumentacija je vsebinsko razdeljena na tri dele.

* specifikacije del
* splošna in posebna določila
* popisi del

.. note:: Sklop " specifikacije posameznih del " predstavlja knjižnico podrobnih opisov tehnologije izvedbe posameznih del pri gradnjah objektov, pogojev vezanih na izvajanja posameznih del in uporabljene materiale.
.. note::
V sklopu "splošna in posebna določila " so opredeljene skupine (VRSTA DEL, SKUPINA del po katerih združujemo posamezna dela in določila vezana na  način obračuna, merjenja , zahteve glede kvalitete skupin del, vrste del in posameznih specifikacij
.. rubric:: Sklop "popisi del " je vezan na konkreten primer gradnje objekta, vrsto gradnje, skupino del ali....










| strumno in veselo
| drug za drugim v ravni vrsti
| zdaj gremo na delo

To je normalen stavek do sem::

	od tu naprej je koda

in spet normalen stavek	

.. warning:: ratatata)



