# Send ad traffic straight to mobile booking

## Kas pakeista
- užsakymo forma įdėta tiesiai į kiekvieną paslaugos puslapį
- reklaminio puslapio CTA ir mobilus mygtukas veda į #bestill
- paslauga parenkama pagal puslapį arba service parametrą
- mobiliajame ekrane forma rodoma prieš kontaktinę informaciją
- nebūtini stogo dydžio, nuotraukų ir žinutės laukai suskleisti
- matuojami užsakymo mygtuko paspaudimai Google Analytics / Meta

## Patikra
- 
pm run typecheck
- 
pm run lint
- 
pm test (29 testai)
