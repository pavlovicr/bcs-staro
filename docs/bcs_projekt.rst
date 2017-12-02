BCS
===

Standardizirani popisi del(Building Construction Specifications - Specifikacije del pri gradnjah)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Uvod 
----

V 28. členu " pravilnika o projektni dokumentaciji " piše "...., se za celovit opis objekta v projektu za izvedbo izdela zbirno tehnično poročilo, ki vsebuje tudi skupen popis materiala in opreme z rekapitulacijo stroškov izgradnje, pri čemer je za njegovo izdelavo zadolžen koordinator iz 5. člena tega pravilnika.)

Zahteve navedene v pravilniku , se le deloma prekrivajo z vsebino POPISA DEL, ki v praksi pomeni nepogrešljiv dokument pri gradnjah. V popisih del so opisane sestave gradbenih konstrukcij in njihovih delov , tehnologija gradnje, uporabljeni materiali in na njih vezane zahteve iz zakona o gradbenih proizvodih, pravila za zagotavljanje kvaliete, obračun in merjenje, varnostne zahteve itd..
Popisi del so pri gradnjah po sistemu " na enoto mere " ključni pri definiranju predmeta pogodbe in izračunu končne cene pogodbenih del.
Nelogično je, da je zakonodajalec v "pravilniku o vsebini in načinu vodenja dnevnika o izvajanju del ter o načinu označitve gradbišča " preciziral način vodenja knjige obračunskih izmer in predpisal obrazec, vsebine pa popolnoma prezrl.

Kljub temu, da so popisi del pomemben del gradbene dokumentacije, v Sloveniji ni enotne metodologija za njihovo izdelavo prav tako ni javno dostopnih zbirk popisov del, ki bi nadomestili zastarele standardizirane popise del (GIPPOS, Fabrizzio, ..). Ostali so le redki in to samo za določene zvrsti del.(Skupnost za ceste).
Zakaj ? Vprašanja ponujajo izziv.

Cilj projekta
-------------
Izdelati sistem priprave, urejanja in vzdrževanja standardiziranih popisov del prek spleta 

Aktivnosti in faznost
---------------------

	1. faza
		* Izdelava dokumentacije  vsebinskega dela in dela za razvoj aplikacije  
		* Razvoj aplikacije 
	2. faza
		* Produkcija
		* Urejanje specifikacij na vzorčnem primeru stanovanjske gradnje do III.FAZE
	3. faza 
		* Izdelava dokumentacije za upravljanje sistema
		 
1. Dokumentacija
---------------- 

	* Vsebine
 	* Orodja, procesi
 


Vsebina
_______


   * izhodišča
   * pomen izrazov
   * opis
   * vzorčni primer
   * shema
   * tabele medsebojnih relacij
   * Izdelava spletne aplikacije
   * Priprava sheme urejanja standardiziranih popisov
   * Rriprava sheme vzdrževanja standardiziranih popisov

Izhodišča
---------
GIPOS,knjiga 2003,nemsko,Fabrizzio
vsebine po različnih področjih , stan gradnja, cestgradnja, industrijski objekti 


Uporabljeni izrazi:
-------------------
.. glossary::

	postavka
<<<<<<< Updated upstream
		je popisna postavka sestavljena iz osnovne specifikacije in dopolnilne ??????? to je veliko vprašanje

	postavka
		opisuje  predmet posameznega dela in določa enote mere. Primer: "Izkop jarka"  
	specifikacija
		dopolnjuje opis postavke glede na možne tehnologije izvedbe, materiale, opremo, delovne pogoje ipd.(kriterij specifikacije). Primer: " v terenu III.ktg "

		opis predmeta posameznega dela z določitvijo enote mere. Primer: "Izkop jarka  em m3"  
	specifikacija
		dopolnitev opisa postavke glede na možno tehnologijo izvedbe, izbiro materiala, opreme, delovne pogoje ipd.(kriterij specifikacije). Primer: " v terenu III.ktg "
>>>>>>> Stashed changes
	kriterij specifikacije
		določa kriterij po katerem se specifikacije oblikujejo  po posameznih postavkah in delih. Primer: "klasifikacija zemljišča po kategorijah od I do VII"  	
	dela
			seznami postavk in kriterijev specifikacij zbranih po vrsti dela. Primer: "Izkopi"     
 
	standardizirani popisi del
		po vrsti del urejen seznam posameznih del, ki nastopajo pri gradnjah,  v vseh možnih variantah.
	postavka
		osnovna specifikacija posameznega dela
	specifikacija
		dodatna specifikacija posameznega delatavkejuje opis postavke glede na možne tehnologije izvedbe, materiale, opremo, delovne pogoje ipd.(kriterij specifikacije). Primer: " v terenu III.ktg "
	kriterij specifikacije
		kriterij po katerem določamo dopolnilno specifikacijodoloča kriterij po katerem se specifikacije oblikujejo  po posameznih postavkah in delih. Primer: "klasifikacija zemljišča po kategorijah od I do VII"  	
	dela
			osnovna skupina sorodnih posameznih postavk. Primer: "Izkopi"     

Vsebina :
---------

Dokumentacija je vsebinsko razdeljena na tri dele.

* specifikacije del
* splošna in posebna določila
* popisi del

.. note::
   Sklop " specifikacije posameznih del " predstavlja knjižnico podrobnih opisov tehnologije izvedbe posameznih del pri gradnjah objektov, , pogojev vezanih na izvajanja posameznih del in uporabljene materiale.
.. note:: V sklopu "splošna in posebna določila " so opredeljene skupine (VRSTA DEL, SKUPINA del po katerih združujemo posamezna dela in določila vezana na  način obračuna, merjenja , zahteve glede kvalitete skupin del, vrste del in posameznih specifikacij
.. rubric:: Sklop "popisi del " je vezan na konkreten primer gradnje objekta, vrsto gradnje, skupino del ali....



Specifikacije del 
----------------------------


Knjižnica standardiziranih popisov je zbirka elementov generiranih popisnih postavk za izvajanje del, ki se pojavljajo pri gradnjah. Knjižnica vsebuje sezname elementov :
 postavk ,
specifikacij ,
kriterijev specifikacij ,
iz katerih so popisne postavke sestavljene in sezname
del  
in vrste del, 
v okviru katerih se popisne postavke združujejo. 

Vsaki postavki pripada več specifikacij , ki podrobneje opisujejo predmet in pogoje dela postavke. 

Popisne postavke sestavljajo postavke s specifikacijami, ki jim pripadajo in podrobneje opisujejo postavko. Specifikacije so organizirane v  okviru postavk in del , ki jim pripadajo ter po kriteriju, ki opredeljuje namen specifikacije.   
Popisne postavke so organizirane v okviru del in vrste del , ki jim pripadajo.

Popisne postavke niso organizirane v seznamih temveč jih sestavljamo modularno. 
Knjižnica  pri gradnja , ki nastopajo pri gradnjah. Postavka je jedro popisne postavke in sama po sebi opredeljuje osnovni predmet dela in enoto mere.
Specifikacije podrobneje definirajo postavko (prednmet dela)in pogoje izvedbe. Specifikacije so organizirane v okviru posameznih skupin , ki jih imenujemo kriterij specifikacije.
Postavke s specifikacijami tvorijo popisne postavke, ki jih sestavljamo modularno.

Splošna in posebna določila
----------------------------

Določila niso nič drugega kot specifikacije specifikacij, postavk, del in vrst del ter določila, ki veljajo za gradnje nasplošno.Za razliko od tehnično tehnoloških specifikacij ta določajo pravila glede uporabe zakonodaje, obračunov, varnosti, kakovosti ipd.



















	``Priprava standardiziranih| popisov del``\:sub:``vaja``\
	#. Priprava splošnih in posebnih določil

#. Projektna naloga
___________________


| naša četica koraka
| strumno in veselo
| drug za drugim v ravni vrsti
| zdaj gremo na delo

To je normalen stavek do sem::

	od tu naprej je koda

in spet normalen stavek	

.. warning:: ratatata)

























Postavke predstavljajo popis del, ki se pojavljajo pri gradnjah in se zbirajo v delih

Postavka skupaj s specifikacijami postavke 


Postavke so temeljni element specifikacije del pri gradnjah.  S postavko so opredeljene temeljne značilnosti posameznega dela. Postavka generalno definira predmet posameznega dela in enoto mere , ki ji pripada. Podrobneje je postavka opisana s specifikacijami postavke. Sorodne postavke se po vrsti dela združujejo v skupini "dela",  


	postavka
		opisuje  predmet posameznega dela in določa enote mere. Primer: "Izkop jarka"  
	specifikacija
		dopolnjuje opis postavke glede na možne tehnologije izvedbe, materiale, opremo, delovne pogoje ipd.(kriterij specifikacije). Primer: " v terenu III.ktg "
	kriterij specifikacije
		določa kriterij po katerem se specifikacije oblikujejo  po posameznih postavkah in delih. Primer: "klasifikacija zemljišča po kategorijah od I do VII"  	
	dela
			seznami postavk in kriterijev specifikacij zbranih po vrsti dela. Primer: "Izkopi"     
















Kaj imam povedati






Dela predstavljajo prvi nivo specifikacije, ki konkretno opredeljuje delo.

je temeljna specifikacija dela in pripada določenim delom
Specifikacija podrobno razlaga postavko glede na kriterije.
To je treba podrobneje opisati
Sledi opis medsebojnih relacij


















specifikacija postavke.......tuji ključ ------kriterij postavke
postavka ....................tuji ključ ......dela

specifikacija postavke      



















