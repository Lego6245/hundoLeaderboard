
async function getCurrentData() {
    const foo = await fetch('./current.json', { mode: 'no-cors' });
    const fooJson = await foo.json();
    console.log(fooJson);
}
getCurrentData()