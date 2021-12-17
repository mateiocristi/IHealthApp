async function apiGet(url) {
    const request = await fetch(url);
    if (request.ok) {
        return request.json();
    }
    console.log('Error, pleas try again later');
    alert('Error, pleas try again later');
}