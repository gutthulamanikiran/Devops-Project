// Client-side form validation
document.addEventListener('DOMContentLoaded', function() {
    const bookingForm = document.querySelector('.booking-form');
    if (bookingForm) {
        bookingForm.addEventListener('submit', function(e) {
            const ticketInput = document.getElementById('tickets');
            const maxTickets = parseInt(ticketInput.getAttribute('max'));
            const selectedTickets = parseInt(ticketInput.value);
            
            if (selectedTickets > maxTickets) {
                e.preventDefault();
                alert(`Sorry, only ${maxTickets} tickets are available.`);
            }
        });
    }
});