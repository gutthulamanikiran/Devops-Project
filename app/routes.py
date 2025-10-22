from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import events, bookings

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/events')
def events_list():
    return render_template('events.html', events=events)

@main.route('/event/<int:event_id>')
def event_detail(event_id):
    event = next((e for e in events if e.id == event_id), None)
    if event:
        return render_template('booking.html', event=event)
    return "Event not found", 404

@main.route('/book/<int:event_id>', methods=['POST'])
def book_ticket(event_id):
    event = next((e for e in events if e.id == event_id), None)
    if event:
        tickets = int(request.form.get('tickets', 1))
        if tickets > 0 and tickets <= event.available_tickets:
            event.available_tickets -= tickets
            booking = {
                'event_id': event_id,
                'event_name': event.name,
                'tickets': tickets,
                'customer_name': request.form.get('name'),
                'customer_email': request.form.get('email')
            }
            bookings.append(booking)
            flash(f'Successfully booked {tickets} ticket(s) for {event.name}!', 'success')
            return redirect(url_for('main.events_list'))
        else:
            flash('Invalid number of tickets!', 'error')
    return redirect(url_for('main.event_detail', event_id=event_id))