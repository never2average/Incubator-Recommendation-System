// 6xN array of type:
// [
//     [Name, AI Score, Chances of Selection, Funding, Link1, Link2],
//     [Name, AI Score, Chances of Selection, Funding, Link1, Link2],
//     [Name, AI Score, Chances of Selection, Funding, Link1, Link2]
// ]
const generateCustomCards = (params) => {
    for (const param of params) {
        let modalBody = document.querySelector("div.modal-dialog[role=document] div.modal-body div.custom-card-wrapper");
        let template = document.querySelector('#custom-card-template');

        let clone = template.content.cloneNode(true);
        let dataFields = clone.querySelectorAll('div.custom-card-data');
        let title = clone.querySelector('.custom-card-header');
        let arrow = clone.querySelector('img');

        title.innerHTML = `<a href="${param[4]}">${param[0]}</a>`;
        dataFields[0].innerHTML = param[1];
        dataFields[2].innerHTML = param[2];
        dataFields[4].innerHTML = param[3];
        arrow.addEventListener('click', () => { location.href = param[5] });

        modalBody.appendChild(clone);
    }

    handleModalClose();
};

const handleModalClose = () => {
    let modal = document.querySelector("div.modal-dialog[role=document]");
    let cards = modal.querySelectorAll("div.custom-card-wrapper div.custom-card");
    let closeButton = modal.querySelector("button[data-dismiss=modal");

    closeButton.addEventListener("click", () => {
        cards.forEach(ele => ele.remove());
    });
};