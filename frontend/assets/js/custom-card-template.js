// 6xN array of type:
// [
//     [Name, AI Score, Chances of Selection, Funding, Link1, Link2],
//     [Name, AI Score, Chances of Selection, Funding, Link1, Link2],
//     [Name, AI Score, Chances of Selection, Funding, Link1, Link2]
// ]

const getRecommendations = () => {
    let _cats = document.querySelectorAll('label[for="chips-input"] > span');
    let cats = Array.prototype.slice.call(_cats).map(ele => {
        return ele.innerText;
    });
    let profile = 'https://angel.co/company/' + document.getElementById('basic-url').textContent;

    $.ajax({
        url: 'http://localhost:8000/getResult/',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
            profile: profile,
            categories: cats,
        }),
        dataType: 'json',

        statusCode: {
            404: () => {
                alert('error');
            },
            200: (res) => {
                //generateCustomCards([['Name1', '55', '25', '35', 'L1.1', 'L1.2'],['Name2', '4', '5', '6', 'L2.1', 'L2.2'],['Name3', '7', '8', '9', 'L3.1', 'L3.2']]);
                const companies = res.companies[0];
                let companyList = [];
                for (const company in companies) {
                    let thisCompany = [];
                    thisCompany.push(company);
                    for (const data of companies[company]) {
                        thisCompany.push(data);
                    }
                    thisCompany = generateDummyCity(thisCompany);  // temporary fixture
                    companyList.push(thisCompany);
                }
                generateCustomCards(companyList);
            },
            500: () => {
                alert('error');
            }
        }
    });

};

// temporary function, supposed to be removed later
const generateDummyCity = (data) => {
    if (data[0] == 'company1') 
        data.push('Jaipur');
    else if (data[0] == 'company2')
        data.push('Mumbai');
    else if (data[0] == 'company3')
        data.push('Delhi');
    data[0] = data[0].replace('company', 'incubator');
    return data;
};

// params = ['inc name', 'score1', 'score2', 'score3', 'link1', 'link2', 'city']
//              0           1          2         3        4        5        6
const generateCustomCards = (params) => {
    let modalBody = document.querySelector("div.modal-dialog[role=document] div.modal-body div.custom-card-wrapper");
    let template = document.querySelector('#custom-card-template');

    for (const param of params) {
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
        modalBody.lastElementChild.setAttribute("city", param[6]);
    }
};

const handleModalClose = () => {
    $('#perfectIncubatorModal').on('hidden.bs.modal', (e) =>
        $("#perfectIncubatorModal div.custom-card").each((index, element) => element.remove())
    );
};

const cityFilterChange = (selectElement) => {
    const city = selectElement.value;
    // console.log(city);
    let cards = document.querySelector("div.modal-dialog[role=document] div.modal-body div.custom-card-wrapper").children;

    if (city === "Location Filter") {
        for (const card of cards)
            card.style.display = "";
        return;
    }

    for (const card of cards) {
        if (card.getAttribute('city') !== city)
            card.style.display = "none";
        else
            card.style.display = "";
    }
};

handleModalClose();