//Harmandeep Mangat || 6021109 || hm15mx
function add() {
    st = event.currentTarget.id;
    res = st.split(".");
    request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (this.readyState == 4 & this.status == 200) {
            if(localStorage.getItem(res[1]) === null) {
                localStorage.setItem(res[1],this.response)
                document.getElementById(st).style.textDecoration = "line-through";
            }
        }
    };
    request.open("GET", "name.cgi?product=" + res[1], true);
    request.send();
}

function remove() {
    st = event.currentTarget.id;
    res = st.split(".");
    if (localStorage.getItem(res[1]) !== null) {
        localStorage.removeItem(res[1])
        document.getElementById("add."+res[1]).style.textDecoration = "none";
    }
}