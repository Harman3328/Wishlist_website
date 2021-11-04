//Harmandeep Mangat || 6021109 || hm15mx
function merger() {
    if (localStorage.length !== 0) {
        for(i=0; i<localStorage.length; i++) {
            request = new XMLHttpRequest();
            
            request.open("GET", "add.cgi?product=" + localStorage.key(i), true);
            request.send();
        }
        localStorage.clear()
    }
}

function add() {
    st = event.currentTarget.id;
    res = st.split(".");
    request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (this.readyState == 4 & this.status == 200) {
                document.getElementById(st).style.textDecoration = "line-through";
        }
    };
    request.open("GET", "add.cgi?product=" + res[1], true);
    request.send();
}

function remove() {
    st = event.currentTarget.id;
    res = st.split(".");
    request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (this.readyState == 4 & this.status == 200) {
                document.getElementById("add."+res[1]).style.textDecoration = "none";
        }
    };
    request.open("GET", "remove.cgi?product=" + res[1], true);
    request.send();
}

window.addEventListener("load",function(){
    merger();  
});