
const dlBtn = document.querySelector(".download-btn");

dlBtn.addEventListener("click", function () {
    html2canvas(document.querySelector("#capture")).then(canvas => {
        if(window.innerWidth < 1024) {
            document.querySelector("#capture").setAttribute("style", "width=800px")
        }
        saveAs(canvas.toDataURL("image/png"), "card.png")
        //다운로드 되는 파일 이름 지정
    })
})

// 캡쳐된 파일을 이미지 파일로 내보냄
function saveAs(uri, filename) {
    const link = document.createElement("a");
    if (typeof link.download === 'string') {
        link.href = uri;
        link.download = filename;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    } else {
        window.open(uri);
    }
}

//체크박스에 클릭이벤트가 발생했을 때 선택된 값만 출력됨
const checkBoxes = document.querySelectorAll(".check-vaccine input")

checkBoxes.forEach((checkbox, i) => {
    checkbox.addEventListener("click", (e) => {
        let result = "";
        if (e.target.checked) {
            result = `코로나19 ${i + 1}차 백신 접종했음을 인증합니다.`
        } else {
            result = "현재 상태에 체크해주세요.";
        }

        document.querySelector(".card-text").innerText = result;
    })
})

const dressupBtns = document.querySelectorAll(".dressup-btns > li")
const charaCustom = document.querySelector(".chara__custom__wrap");
const customTitle = document.querySelector(".chara__custom__title")
const hatBtn = document.querySelector(".hat_btn")
const charaParts = [...document.querySelectorAll(".chara-parts")];
let hatIndex = 1,
    topIndex = 1,
    bottomIndex = 1,
    shoesIndex = 1,
    outerIndex = 1;
let thumb = document.querySelector(".chara__custom__img > img")

//이미지의 링크를 바꾸는 함수
function partsImgChange(id, index) {
    const partsImg = charaParts.find(element => element.dataset.value == id)
    partsImg.src = `../static/images/${id}_0${index}.png`
    thumb.src = `../static/images/${id}_0${index}.png`
}
//커스텀 창의 다음 버튼을 눌렀을 때 다음 사진으로 바뀌는 함수
function nextPhoto(id) {
    if (id == "hat") {
        hatIndex++;
        hatIndex %= 3;
        if (hatIndex == 0) hatIndex = 1;
        partsImgChange(id, hatIndex);
    }
    if (id == "top") {
        topIndex++;
        topIndex %= 3;
        if (topIndex == 0) topIndex = 1;
        partsImgChange(id, topIndex);
    }
    if (id == "bottom") {
        bottomIndex++;
        bottomIndex %= 3;
        if (bottomIndex == 0) bottomIndex = 1;
        partsImgChange(id, bottomIndex);
    }
    if (id == "shoes") {
        shoesIndex++;
        shoesIndex %= 3;
        if (shoesIndex == 0) shoesIndex = 1;
        partsImgChange(id, shoesIndex);
    }
    if (id == "outer") {
        outerIndex ++;
        outerIndex  %= 3;
        if (outerIndex  == 0) outerIndex  = 1;
        partsImgChange(id, outerIndex);
    }
}
//커스텀 창의 이전 버튼을 눌렀을 때 이전 사진으로 바뀌는 함수
function prevPhoto(id) {
    if (id == "hat") {
        hatIndex--;
        hatIndex %= 3;
        if (hatIndex == 0) hatIndex = 1;
        partsImgChange(id, hatIndex);
    }
    if (id == "top") {
        topIndex--;
        topIndex %= 3;
        if (topIndex == 0) topIndex = 1;
        partsImgChange(id, topIndex);
    }
    if (id == "bottom") {
        bottomIndex--;
        bottomIndex %= 3;
        if (bottomIndex == 0) bottomIndex = 1;
        partsImgChange(id, bottomIndex);
    }
    if (id == "shoes") {
        shoesIndex--;
        shoesIndex %= 3;
        if (shoesIndex == 0) shoesIndex = 1;
        partsImgChange(id, shoesIndex);
    }
    if (id == "outer") {
        outerIndex --;
        outerIndex  %= 3;
        if (outerIndex  == 0) outerIndex  = 1;
        partsImgChange(id, outerIndex);
    }

}
//커스텀 창의 다음 버튼 클릭 이벤트
document.querySelector(".custom--next").addEventListener("click", () => {
    const id = charaCustom.id;
    nextPhoto(id);
})
//커스텀 창의 이전버튼 클릭 이벤트
document.querySelector(".custom--prev").addEventListener("click", () => {
    const id = charaCustom.id;
    prevPhoto(id)
})

//버튼 클릭 이벤트 : 커스텀 창이 뜨는 함수
dressupBtns.forEach(btn => {
    btn.addEventListener("click", (e) => {
        const partsName = e.target.dataset.parts;
        dressupBtns.forEach(btn => {
            if (btn.classList.contains("on")) {
                btn.classList.remove("on")
                charaCustom.classList.remove("visible")
            }
        })
        btn.classList.toggle("on");
        customVisible(partsName)
    })
    // 커스텀 창의 close 버튼을 눌렀을 때 창이 닫히고 li의 on 클래스를 빼는 함수 
    document.querySelector(".close-btn").addEventListener("click", () => {
        btn.classList.remove("on");
        charaCustom.classList.remove("visible")
    })
})



// 커스텀 창에 해당 파츠 데이터를 전달해서 보여주는 함수
function customVisible(partsName) {
    charaCustom.id = partsName
    const id = charaCustom.id;
    customTitle.innerHTML = id;
    thumbUrl(id);
    charaCustom.classList.toggle("visible")

}

function thumbUrl(id) {
    if (id == "hat") {
        thumb.src = `../static/images/${id}_0${hatIndex}.png`
    }
    if (id == "top") {
        thumb.src = `../static/images/${id}_0${topIndex}.png`
    }
    if (id == "bottom") {
        thumb.src = `../static/images/${id}_0${bottomIndex}.png`
    }
    if (id == "shoes") {
        thumb.src = `../static/images/${id}_0${shoesIndex}.png`
    }
    if (id == "outer") {
        thumb.src = `../static/images/${id}_0${outerIndex}.png`
    }
}
