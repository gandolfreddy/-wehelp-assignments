function showPage() {
    const content = document.querySelector(".content");
    /*
        <div class="box">
            <img src="./assets/Geralt_of_Rivia.jpg">
            <div class="img_description">Geralt of Rivia</div>
        </div>
    */
    for (let i = showCnt * showSize; i < (showCnt + 1) * showSize; i++) {
        if (i < dataLen) {
            //// stitle
            let stitle = data[i].stitle;

            //// file
            let file = `https://${data[i].file.split('https://')[1]}`;

            let box = document.createElement("div");
            box.className = "box";
            let img = document.createElement("img");
            img.src = file;
            let description = document.createElement("div");
            description.className = "img_description";
            description.textContent = stitle;

            box.appendChild(img);
            box.appendChild(description);
            content.appendChild(box);
        } else {
            let btn = document.querySelector(".load_more > button");
            btn.style.display = "none";
        }
    }
}


function loadMore() {
    showCnt++;
    showPage();
}


let data = null;
let dataLen = 0;
let showCnt = 0;
let showSize = 8;
let url = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json";

fetch(url).then((response) => {
    return response.json();
}).then((dataJson) => {
    dataLen = dataJson.result.count - 1;
    data = dataJson.result.results;
    showPage();
});
