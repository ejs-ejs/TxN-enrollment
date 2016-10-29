# TxN-enrollment
Generate Technarium user agreement from the submitted information

Kopypasta iš https://github.com/Technariumas/txinvoice
Serveris iš ten pat;


Siųsti užklausą:

curl -X POST -d '{
"member": {
"Name": "Jonas Jonavičius",
"address": "Bistryčios g. 13, Vilnius",
"phone": "+10 34 223322",
"email": "jonas@jonavicius.net"
},
"number": "012345678"
}' http://127.0.0.1:8080/ > agreement.pdf
