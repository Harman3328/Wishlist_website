//Harmandeep Mangat || 6021109 || hm15mx
function share() {
    st = event.currentTarget.id;
    var i = document.getElementById(st).parentNode.parentNode.rowIndex;
    res = st.split(".");
    request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (this.readyState == 4 & this.status == 200) {
                alert("Shared with "+this.response)
        }
    };
    request.open("GET", "sharemy.cgi?sharewith=" + res[1], true);
    request.send();
}