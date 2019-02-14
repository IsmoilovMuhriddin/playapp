URL = "/poll_info"


function poll_info(data = {}) {
    console.log("entered to here")
    var form = new FormData(document.getElementById('search-form'));

    return fetch(URL, {
        method: "POST",
        body: form,
        credentials: 'same-origin'  
    })
        .then(data => { return data.json() })
        .then(res => { console.log(res) })
}

