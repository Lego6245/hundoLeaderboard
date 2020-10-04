
async function getCurrentData() {
    const foo = await fetch('./current.json');
    const fooJson = await foo.json();
    const theTable = document.getElementById('table_body');
    fooJson.entries.forEach(appendRowToTable(theTable));
    const timeSpan = document.getElementById('last_time');
    timeSpan.textContent = fooJson.ranAt;
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