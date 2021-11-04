//Harmandeep Mangat || 6021109 || hm15mx
function remove() {
    st = event.currentTarget.id;
    var i = document.getElementById(st).parentNode.parentNode.rowIndex;
    res = st.split(".");
    request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (this.readyState == 4 & this.status == 200) {
                document.getElementById("mytable").deleteRow(i);
        }
    };
    request.open("GET", "delete.cgi?product=" + res[1], true);
    request.send();
}