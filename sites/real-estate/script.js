function contact(item) {
    const wa = "201012345678"; // Update your number
    const url = "https://wa.me/" + wa + "?text=I am interested in acquiring the " + item;
    window.open(url, '_blank');
}
