//Harmandeep Mangat || 6021109 || hm15mx
function ban() {
    st = event.currentTarget.id;
    var i = document.getElementById(st).parentNode.parentNode.rowIndex;
    res = st.split(".");
    request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (this.readyState == 4 & this.status == 200) {
                document.getElementById(st).value = "Unban";
        }
    };
    request.open("Post", "ban.cgi?user=" + res[1]+"&command="+res[0], true);
    request.send();
}

function Unban() {
    st = event.currentTarget.id;
    var i = document.getElementById(st).parentNode.parentNode.rowIndex;
    res = st.split(".");
    request = new XMLHttpRequest();
    request.onreadystatechange = function () {
        if (this.readyState == 4 & this.status == 200) {
                document.getElementById(st).value = "Ban";
        }
    };
    request.open("Post", "ban.cgi?user=" + res[1]+"&command="+res[0], true);
    request.send();
}