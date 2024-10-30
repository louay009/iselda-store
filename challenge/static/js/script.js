document.getElementById('check-stock-btn').onclick = function() {
    const productId = this.getAttribute('data-product-id'); // Get product ID from the button's data attribute
    const xmlRequest = `<?xml version="1.0" encoding="UTF-8"?>
<request>
    <product_id>${productId}</product_id>
</request>`; // Removed leading spaces

    console.log("Sending XML Request:", xmlRequest); // Log the XML request

    fetch('/check_stock', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/xml',
        },
        body: xmlRequest,
    })
    .then(response => response.text())
    .then(data => {
        document.getElementById('stock-result').innerText = data;
    })
    .catch(error => {
        console.error('Error:', error);
    });
};
