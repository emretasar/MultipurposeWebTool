function updateDateTime() {
    const dateTimeElement = document.getElementById("datetime");
    const now = new Date();
    const options = { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: '2-digit', minute: '2-digit', second: '2-digit', timeZoneName: 'short' };
    const dateTimeString = now.toLocaleDateString('en-US', options);
    dateTimeElement.textContent = dateTimeString;
}

setInterval(updateDateTime, 1000);
updateDateTime();