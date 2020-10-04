import data from '../data/current.json';

async function getCurrentData() {
    const theTable = document.getElementById('table_body');
    data.entries.forEach(appendRowToTable(theTable));
    const timeSpan = document.getElementById('last_time');
    timeSpan.textContent = data.ranAt;
}

const appendRowToTable = (table) => (rowData) => {
    const newRow = document.createElement('tr');
    const userCell = document.createElement('td');
    userCell.textContent = rowData.userName;
    const frameCell = document.createElement('td');
    frameCell.textContent = rowData.frameCount;
    newRow.appendChild(userCell);
    newRow.appendChild(frameCell);
    table.appendChild(newRow);
}

getCurrentData();