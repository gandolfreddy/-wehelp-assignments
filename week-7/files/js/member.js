

function showName() {
    const searchUsernameElem = document.getElementById("search-input");
    const showUsernameElem = document.getElementById("query-username");
    let url = `http://127.0.0.1:3000/api/members?username=${searchUsernameElem.value}`;

    fetch(url).then((response) => {
        return response.json();
    }).then((dataJson) => {
        if (dataJson.data) {
            queryName = dataJson.data.name;
            showUsernameElem.textContent = `${queryName}（${searchUsernameElem.value}）`;
        } else {
            showUsernameElem.textContent = "無此會員";
        }
        searchUsernameElem.value = '';
    });
}


function setName() {
    const setNameElem = document.getElementById("setname-input");
    const setResultElem = document.getElementById("setname-result");
    let url = "http://127.0.0.1:3000/api/member";
    let data = {name: setNameElem.value};

    fetch(url, {
        method: "POST",
        headers: new Headers({"Content-Type": "application/json"}),
        body: JSON.stringify(data)
    }).then((response) => {
        return response.json();
    }).then((updateRes) => {
        if (updateRes.ok)
            setResultElem.textContent = "更新成功";
        else if (updateRes.error)
            setResultElem.textContent = "更新失敗";
        setNameElem.value = '';
    });
}


const searchBox = document.getElementById("search-input");
searchBox.addEventListener("keyup", function (event) {
    if (event.key === "Enter")
        document.getElementById("search-button").onclick();
});

const setnameBox = document.getElementById("setname-input");
setnameBox.addEventListener("keyup", function (event) {
    if (event.key === "Enter")
        document.getElementById("setname-button").onclick();
});