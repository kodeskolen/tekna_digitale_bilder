# Digital Bildebehandling med Python

Dette er et kræsjkurs i digital bildebehandling med programmeringsspråket Python. Kurset er utviklet av Simula i samarbeid med Tekna Helse og Teknologi. Målet med kurset er å gi deltakerene en introduksjon til hvordan man kan bruke Python til å analysere og behandle digitale bilder og automatisere oppgaver. Kurset varer i 3 timer, derfor er det naturligvis begrenset hvor mange ulike tema og eksempler vi kan rekke å dekke. Istedet for å ta et dypdykk på et bestemt tema prøver vi derfor å gi dere en god oversikt over ulike pakker og verktøy som kan brukes - samt gi infor om hvor du kan finne informasjon for å lære mer. Kurset er interaktivt, og vi setter av tid til at dere skal få prøve dere frem selv, med god hjelp fra oss.

Denne nettsiden er ment for å dele kursmaterialer, og gi utfyllende informasjon dersom du ønsker å lære mer på egenhånd.

## Kursplan

Vi deler kurset i tre hovedkomponenter:

1. Kort om det å jobbe i Python
2. Hvordan jobbe med digitale bilder i Python
	* Lese/lagre bildefiler
	* Hvordan bilder representes som `numpy` arrays
	* Plotte bilder
	* Jobbe med formater som DICOM-bilder
3. Digital bildebehandling
	* Edge detection
	* Thresholding
	* Jobbe med masker
	* etc

## Kursmateriale

Vi har laget et sett med forelesningsnotater som dekker det samme som vi kommer til å dekke i live-økten (lecture_notes_digital_image_analysis.ipynb). Dette er noe du kan lese igjennom i ettertid for å repetere det vi dekket på kurset, eller gå litt mer i dybden på visse detaljer. Notatene dekker nok mer, og noen fler eksempler, enn det vi klarer å rekke i live-økten. Forelesningsnotatene inneholder også noen oppgaver du kan prøve deg på, og vi har laget et eget dokument som kun inneholder disse oppgavene (exercises_digital_image_analysis.ipynb).

Om du ikke er så erfaren i Python og ønsker å lære mer har vi også lagt med en Python tutorial 

Disse dokumentene er Jupyter Notebooks. Det er best å laste ned hele repositoriet til egen maskin (enten med `git clone` om du kjenner til det, eller ved å klikke `Code -> Download ZIP`). Du kan ta bruker notebookene interaktivt, endre kode, kjøre på nytt og løse oppgaver rett i dokumentet. Om du ikke får til, eller ønsker, å jobbe i Jupyter - så ligger det .pdf kopier av alle tre notebooksene i mappen /pdf/. Disse bør du også bruke om du vil skrive ut noe til papir.

## Nødvendig programvare

Om du allerede er vandt med å jobbe i Python kan du bruke den programvaren (installasjon + editor) du er vandt til å jobbe i fra før. Om du ikke har en Python-installasjon allerede anbefaler vi at du laster ned Anaconda. Dette er en samlepakke der du får en Python-installasjon, en del tilleggspakker ferdiginstallert, en tekst-editor (Spyder) og Jupyter.
* https://www.anaconda.com/

Uansett hva du velger å bruke av programvare anbefaler vi at du bruker en nyere versjon av Python, gjerne 3.8+. Python 2 er noe utdatert, og mange pakker har ikke lenger aktiv utvikling for Python 2.

## Litt om Pakker 

For å jobbe med digital bildebehandling i Python trenger vi å benytte oss av pakker for å gjøre dette. De to største pakkene for å jobbe med digital bildebehandling er scikit-image og OpenCV. Vi kommer til å fokusere hovedsakelig på `scikit-image`, for dette er en moderne pakke utviklet spesielt for Python som er god for nybegynnere og allsidig. De har også meget gode nettsider og dokumentasjon, med mange fine eksempler. Se følgende nettsider for info og eksempler
* https://scikit-image.org/docs/stable/user_guide.html
* https://scikit-image.org/docs/stable/auto_examples/index.html

Til sammenligning er OpenCV også en meget godt utviklet pakke med mye funksjonalitet. Men denne er ikke utviklet kun for Python, og det er litt vanskligere å finne god dokumentasjon og gode eksempler spesielt for Python-versjonen av pakken. Vi tenker derfor i utgangspunktet at OpenCV kan være litt mer vrient å ta i bruk.

Det finnes også mer spesialiserte pakker det kan være nyttig å kjenne til. Pakken `dipy` er nyttig om man jobber med diffusjons MRI, og pakken `scipy.ndimage` kan inneholde mer spesialiserte bildebehandlingsalgoritmer.

For plotting bruker vi `matplotlib`-pakken. Et alternativ til denne er å bruke `plotly.express`, men dette dekker vi ikke i detalj i dette kurset. 

For å lese medisinske bilder trenger vi også noen mindre ekstrapakker, her bruker vi `pydicom` (for DICOM-bilder) og `nibabel` (for NIfTI-bilder).

Du kan lese mer om hvordan disse pakkene installeres og brukes i forelesningsnotatene.

## Ekstra ressurser

Om du ønsker å lære mer om digital bildebehandling i Python enn vi rekker å dekke i kurset har vi lagt med noen linker som inneholder nyttig informasjon her:

Scikit-image user guide
* https://scikit-image.org/docs/stable/user_guide.html

Scikit-image example gallery
* https://scikit-image.org/docs/stable/auto_examples/index.html

Data Carpentry image processing course module
* https://datacarpentry.org/image-processing/

Dipy package tutorial (for Diffusion MRI images)
* https://dipy.org/tutorials/

Pydicom package tutorial
* https://pydicom.github.io/pydicom/stable/auto_examples/index.html


## Ressurser for å lære Python

Om du føler du ikke kan nok Python til å begynne å bruke det til digital bildebehandling, og ønsker å lære mer "basics", er dette to åpent tilgjenglige digitale bøker

* [Introduction to Scientific Programming with Python](https://doi.org/10.1007/978-3-030-50356-7) by Joakim Sundnes. This is a so-called *Springer Brief*, which aims to give a concise introduction to scientific programming with Python, aimed at readers with little, to no, background in programming.
* [Automate the Boring Stuff](https://automatetheboringstuff.com/) by Al Sweigart. This is a free-to-read ebook about using Python for automating small tasks.

Det finnes også en populær åpen e-bok om å bruke Python til databehandling og analyse. Den forventer at du kan Python basics, men kan være fin om du ønsker å begynne å bruke Python til statistikk og databehandling.

* [The Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) by Jake VanderPlas. This free-to-read ebook assumes you know Python basics, but is a great resource if you want to learn more about working with data, data analysis and machine learning with Python.
