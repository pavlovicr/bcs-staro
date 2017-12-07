***
BCS
***

>>> a = 1

Look in the `Django Documentation`_.
Poglej v Piton_ kodo.
`najdi <http://www.najdi.si/>`_

.. literalinclude:: conf.py 
:end-before: 'import os'


Standardizirani popisi del(Building Construction Specifications - Specifikacije del pri gradnjah)
################################################################

Uvod 
****
28. člen pravilnika o projektni dokumentaciji pravi::

	 	 ..., se za celovit opis objekta v projektu za izvedbo izdela zbirno tehnično poročilo,
	 ki vsebuje tudi skupen popis materiala in opreme z rekapitulacijo stroškov izgradnje, 
	 pri čemer je za njegovo izdelavo zadolžen koordinator .....


Popis materiala in opreme po zahtevah iz navedenega pravilnika  se le deloma prekrivajo z vsebino POPISOV DEL, ki v praksi pomenijo nepogrešljiv dokument pri gradnjah. V popisih del ni samo popisa materiala in opreme. V popisu del so opisane sestave gradbenih konstrukcij in njihovih delov , tehnologije izvedbe, uporabljeni materiali in na njih vezane zahteve iz zakona o gradbenih proizvodih, pravila za zagotavljanje kvaliete, pravila pri obračunu in merjenju količin, varnostne zahteve, navedbe standardov itd..
Popisi del so pri gradnjah po sistemu " na enoto mere " ključni pri definiranju predmeta pogodbe in izračunu končne cene pogodbenih del.

Kljub temu, da so popisi del pomemben del gradbene dokumentacije, Slovenija ne premore enotne metodologije za njihovo izdelavo prav tako ni javno dostopnih zbirk popisov del, ki bi nadomestili zastarele standardizirane popise del (GIPPOS, Fabrizzio, ..). Ostali so le redki in to samo za določene zvrsti del.(Skupnost za ceste).
Zanimivo, da se je zakonodajalec zelo potrudil pri oblikovanju knjige obračunskih izmer v "pravilniku o vsebini in načinu vodenja dnevnika o izvajanju del ter o načinu označitve gradbišča ", vsebine pa kot da bi se ustrašil.

Cilj projekta
*************
Izdelati sodoben sistem priprave, urejanja in vzdrževanja standardiziranih popisov del , ki bo javno dostopen prek spleta 

Aktivnosti in faznost
*********************
1. faza
	* Izdelava dokumentacije,  vsebinski del in del za razvoj aplikacije  
	* Razvoj aplikacije 
2. faza
	* Produkcija
	* Urejanje specifikacij na vzorčnem primeru stanovanjske gradnje do III.FAZE
3. faza 
	* Izdelava dokumentacije za upravljanje sistema
		 
1. Dokumentacija 
================

1.1 Izhodišča
-------------
	
1.2 Pomen izrazov
-----------------
.. glossary::

	standardizirani popisi del
		urejeni seznami podrobno opisanih posameznih del, ki nastopajo pri gradnjah
	postavka
		osnovni opis posameznega dela
	specifikacija
		dodatni opis postavk
	kriterij specifikacije
		kriterij po katerem določamo dopolnilno specifikacijodoloča kriterij po katerem se specifikacije oblikujejo  po posameznih postavkah in delih. Primer: "klasifikacija zemljišča po kategorijah od I do VII"  	
	določila
		opis zahtev in pravil vezanih na izvedbo postavke
	kriterij določila



	dela
			osnovna skupina sorodnih posameznih postavk. Primer: "Izkopi"     

1.3 Opis elementov in medsebojnih odvisnosti
--------------------------------------------
1.4 Shema
---------

ratata ena

1.5 Vzorčni primer
------------------

1.6 Izhodišča za spletno aplikacijo
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

.. _Django Documentation: http://docs.djangoproject.com


.. _Piton: http://najdi.si




























