function createBoard() {
    document.getElementById("start").innerText = "Restart";
    let size = Math.max(1, Math.min(9, document.getElementById("size").value));
    let sampleRow = document.getElementById("row0");
    console.log(sampleRow);
    let sampleCell = document.getElementById("cell00");

    document.getElementById("grid").innerHTML = "";

    sampleRow.style.display = "block";
    
    for (let rowNum = 1; rowNum <= size; rowNum++) {
        row = createRow(size, rowNum, sampleRow);
        
        for (let colNum = 1; colNum <= size; colNum++) {
            createCell(size, row, sampleCell, rowNum, colNum);
        }
    }
    
    sampleRow.style.display = "none";
    document.getElementById("turn").style.display = "block";
    return false;
}

function createRow(size, rowNum, sampleRow) {
    let row = sampleRow.cloneNode();
    // classes for highlighting
    row.id = "row" + rowNum;
    row.classList.add(rowNum == 1 ? "rowTop" : rowNum == size ? "rowBottom" : "rowMiddle");
    row.classList.add(rowNum % 2 ? "rowOdd" : "rowEven");
    grid.appendChild(row);
    return row;
}

function createCell(size, row, sampleCell, rowNum, colNum) {
    let cell = sampleCell.cloneNode(true);
    cell.id = "cell" + rowNum + colNum;
    cell.classList.add("row" + rowNum);
    cell.classList.add("column" + colNum);
    cell.classList.add(colNum == size ? "endCol" : "col");

    if (rowNum == colNum) {
        cell.classList.add("diagonal1");
    }

    if (colNum == size - rowNum + 1) {
        cell.classList.add("diagonal2");
    }
    row.appendChild(cell);
    return cell;

}


function playAt(cell) {
    if (cell.innerHTML == "&nbsp;") {
        playerElement = document.getElementById("player");
        cell.innerHTML = playerElement.innerHTML;
        playerElement.innerHTML = playerElement.innerHTML == "X" ? "O" : "X";

    }

    checkForWinAt(cell.innerHTML, cell.id[4], cell.id[5]);

}



function checkForWinAt(player, rowNum, colNum) {
    if (checkAndHighlight(player, "row" + rowNum) || checkAndHighlight(player, "column" + colNum) || checkAndHighlight(player, "diagonal1") || checkAndHighlight(player, "diagonal2")) {
        for (i = 1; i <= Math.max(1, Math.min(9, document.getElementById("size").value)); i++){
            for (j = 1; j <= Math.max(1, Math.min(9, document.getElementById("size").value)); j++){
                document.getElementById("cell" + i + j).onclick = null;
            }
        } 

        setTimeout(function () {
            let restart = confirm(player + " wins!\nDo you want to restart the game?");
            if (restart == true){createBoard();}
            else{return false;}
        }, 10);
        // https://stackoverflow.com/questions/40724697/javascript-do-something-before-alert
        // TODO: don't allow players to keep playing!
        return true;
    }
    return false;
}



function checkAndHighlight(player, className) {
    let cells = document.getElementsByClassName(className);
    for (let pos = 0; pos < cells.length; pos++) {
        if (cells[pos].innerHTML != player) {
            return false;
        }
    }

    for (let pos = 0; pos < cells.length; pos++) {
        cells[pos].classList.add("win");
    }
    return true;
}