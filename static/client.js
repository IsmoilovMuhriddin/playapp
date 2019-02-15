URL = "/poll_info"


function poll_info(url = '', data = {}) {

    console.log("entered to here")
    var form = new FormData(document.getElementById('search-form'));

    return fetch(url, {
        method: "POST",
        body: form
    })
        .then(data => { return data.json() })
        .then(res => {
            console.log(res);

        })
}

function postData(url = '', data = {}) {

    return fetch(url, {
        method: "POST",
        mode: "cors",
        headers: { "Content-Type": "application/json", },
        body: JSON.stringify(data),
    })
        .then(response => response.json())
        .then((data) => {
            console.log(data);
            document.getElementById("poll_result").innerHTML = JSON.stringify(data)
        });
}