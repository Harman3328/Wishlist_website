// Harmandeep Mangat || hm15mx || 6021109
window.addEventListener('load', function() {    
    var cols = ['Name', 'Remove']

    var t = document.createElement('table');
    t.classList.add('products', 'listing');

    t.appendChild(document.createElement('thead'));
    t.querySelector('thead').appendChild(document.createElement('tr'));

    for (var i = 0; i < cols.length; i++) {
        var heading = document.createElement('td');
        var h = document.createElement('h3'); 
        h.textContent = cols[i];
        heading.appendChild(h);
        t.querySelector('thead tr').appendChild(heading);
    }

    document.getElementById('wrapper').appendChild(t);

    // Create rows
    for (var i = 0; i < localStorage.length; i++) {
        var p = localStorage.getItem(localStorage.key(i));
        var r = document.createElement('tr');

        r.id = p.toLowerCase() + "-row";

        var nameCell = document.createElement('td');
        nameCell.textContent = p;
        nameCell.classList.add('name');

        var button = document.createElement("button"); 
        button.textContent = "Remove"; 
        button.classList.add('button'); 
        button.id = p;

        r.appendChild(nameCell);
        r.appendChild(button);

        t.appendChild(r);
    }

    function action1(e) {
        for (i=0; i<localStorage.length; i++) {
            var p = localStorage.getItem(localStorage.key(i));
            
            if (e.currentTarget.id === p) {
                localStorage.removeItem(localStorage.key(i)); 
                document.querySelector(".listing").deleteRow(i+1);
                break
            }
        }
    }


    var cells = document.querySelectorAll("button.button");

    for (var i = 0; i < cells.length; i++) {
        cells[i].addEventListener('click', action1);
    } 
});