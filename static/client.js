URL = "/poll_info"

APP_ID = 'id'
APP_LANGUAGE = 'hl'



function get_parameters(text) {
    var res = text.split("?");
    var par_dict = {};
    if (res.length > 1) {

        var params = res[1].split("&");
        var par_dict = {};
        //console.log(params, par_dict)
        params.forEach(function (item) {
            key_val = item.split("=")
            if (key_val[0] === APP_ID) {
                par_dict[APP_ID] = key_val[1]
            }
            else if (key_val[0] === APP_LANGUAGE) {
                par_dict[APP_LANGUAGE] = key_val[1]
            }
        });
    }
    return par_dict;
}

function make_html_table(data){
    
    var result_table = ''

    var somed = data['permission_sets'][0]['permissions']
    somed.forEach(function (item) {
        row = `<tr>
        <td>${item["permission"]}</td>
        <td>${item["description"]}</td>
        </tr>`
        result_table += row;
    });
    // result_table += JSON.stringify(somed)
    // console.log("Making HTMl",somed);
    return result_table
} 

function postData(url = '') {
    var url_for_app = document.getElementById('search_field').value;
    var params = get_parameters(url_for_app);
    if (Object.keys(params).length === 0) {
        //console.log(params, "is empty")
        
    } else {
        //console.log("You are all set");
        return fetch(
            url, {
                method: "POST",
                mode: "cors",
                headers: { "Content-Type": "application/json", },
                body: JSON.stringify(params),
            }
        )
            .then(response => response.json())
            .then((data) => {
                //console.log(data);
                document.getElementById("poll_result").innerHTML = make_html_table(data)
            });
    }
    
}

