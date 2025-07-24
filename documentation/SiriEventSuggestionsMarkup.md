# Siri Event Suggestions Markup

Update users' calendars and inform suggestions from Siri with reservation data embedded in email and webpages.

**Platforms:** Siri Event Suggestions Markup 1.0+

## Overview

You can use the Siri Event Suggestions Markup data format to provide event details in webpages and emails. Siri parses travel arrangements, shows, restaurant reservations, and social events in order to augment related activities, like suggesting driving directions or a ride share to a scheduled event and activating Do Not Disturb just before a show starts.

When Mail receives an email or Safari loads a webpage with reservation markup, Siri also adds the event to the user's Siri Event Suggestions calendar. Mail and Safari also inform the user that the content they're viewing includes a reservation, so the user can accept or reject the event without leaving their current activity.

A diagram of the Siri Event Suggestions Markup process, which begins with a graphic representing a piece of reservation data. An arrow points from the reservation graphic to a Siri icon, and from the Siri icon to a calendar, a driving directions graphic, and a Siri Suggestion containing the text "Time to check-in" and "Reservation found in Mail".

Include reservation markup data when you communicate about confirmed reservations with your users. Use a consistent **reservationId** each time, so the system can manage duplicates between Safari and Mail and across the user's devices.

Fill out the form at Siri Event Suggestions Markup Information to request inclusion in the domain allow list for event suggestion processing. See Checking Your Reservation Markup for more details about testing your implementation before you apply.

**Tip:** Donate reservation information from your app as well, if you have one. For more information about providing event suggestions from your app, see Siri Event Suggestions.

### Format Reservation Data

If you offer reservations on a website or email reservation confirmations to users, you may provide reservation information embedded in HTML documents as either JSON-LD or Microdata. For JSON-LD, specify the @context and @type, as shown in this example:

```html
<script type="application/ld+json">
{
  "@context": "http://schema.org", 
  "@type": "TrainReservation",
  "reservationId": "ASDF1234"
  /* more data goes here */    
}
</script>
```

For Microdata, provide the schema.org URL for the reservation in an itemtype attribute like this:

```html
<section itemscope itemtype="http://schema.org/TrainReservation">
Your reservation
<span itemprop="reservationId">ASDF1234</span>
is confirmed!
/* more data goes here */
</section>
```

## Topics

### Essentials
- [Providing Trusted Data](https://developer.apple.com/documentation/sirideventsuggestionsmarkup/providing_trusted_data) - Sign your content and avoid sending unnecessary or inaccurate information.
- [Checking Your Reservation Markup](https://developer.apple.com/documentation/sirideventsuggestionsmarkup/checking_your_reservation_markup) - Preview your reservation event data before the Allow List includes your domain.

### Transportation
- **FlightReservation** - An airplane flight reservation.
- **TrainReservation** - A reservation for train travel.
- **BusReservation** - A reservation for bus travel.
- **BoatReservation** - A reservation for boat travel.
- **RentalCarReservation** - A reservation to rent a car.

### Food, Lodging, and Events
- **EventReservation** - A reservation for a movie, sporting event, live show, or other scheduled event.
- **FoodEstablishmentReservation** - A restaurant reservation.
- **LodgingReservation** - A hotel reservation or other booking for a place to stay.

### Common Reservation Data
- **Person** - A passenger, diner, lodging guest, or event attendee.
- **Ticket** - Details about a ticket for transportation or an event.
- **Seat** - The specific location reserved for the passenger.
- **Organization** - A business, transportation provider, or event organizer.
- **Place** - A business, transportation hub, or event venue.
- **PostalAddress** - A specific geographic location.

### Basic Data Types
- **@context** - The open standard reference for interpreting the markup contents.
- **dateTimeISO8601** - A time and date in the ISO-8601 format.
- **reservationId** - A stable, unique identifier for the reservation.
- **reservationStatus** - A string indicating that the reservation has been confirmed or canceled.
- **URL** - The address of a webpage.
- **telephone** - A phone number.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SiriEventSuggestionsMarkup)*