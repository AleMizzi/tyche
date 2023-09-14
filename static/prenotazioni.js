const prenotazioni={};
prenotazioni.nPersonew = document.getElementById('npersonew'); // bottonep = NOMUERO PERSONE W, E LA CLASSE NON UN ID
prenotazioni.nPersone = document.getElementById('npersone'); //. npersone= NUMERO PERSONE, E L'ID CHE STA NELLA CLASSE BOTTONEP, LO SPAN

//SOLO ID, LE CLASSI LE USO PER GLI STILI


prenotazioni.nPersonew.addEventListener("click", (e) => {
    e.preventDefault();
    let nPersone = +prenotazioni.nPersone.textContent;
    if(e.target.id === 'add') {
        prenotazioni.nPersone.textContent = nPersone + 1;

    } else if(e.target.id === 'sub' && nPersone>1) {
        prenotazioni.nPersone.textContent = nPersone - 1;
    }
});
    