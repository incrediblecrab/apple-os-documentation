# Siri Event Suggestions Markup

Provide reservation data for Siri event suggestions through email and webpages.

**Format reference:** Siri Event Suggestions Markup 1.0 — a catalog version, not an Apple OS minimum.

## Overview

Participating services embed information about actual bookings in HTML so Mail and Safari can pass it to Siri. Supported categories include travel, lodging, dining, and scheduled events. This is reservation data for system suggestions, not an API that gives your service arbitrary calendar-write access or control over Do Not Disturb.

Apple describes a Siri Event Suggestions calendar and a reservation notice in Mail or Safari where the person can accept or reject an event. Do not equate that suggestions workflow with an unconditional addition to a person's ordinary calendars or a guaranteed follow-up action.

Only use confirmed status for a completed booking, not a promotional page or an unfinished checkout. Send accurate status in confirmations, updates, and cancellations.

Keep [`reservationId`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/reservationid) stable so updates, cancellations, and duplicate messages refer to the same reservation. When also donating from an app, use the same value for `INReservation.reservationNumber`.

Processing requires inclusion on the domain allow list. Submit working examples through the [Siri Event Suggestions Markup Information form](https://developer.apple.com/contact/request/siri-events/), following [Checking Your Reservation Markup](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/checking-your-reservation-markup). Development-device authentication/allow-list overrides are testing controls, not a production authorization path.

Follow [Providing Trusted Data](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/providing-trusted-data): use HTTPS for webpages, a static From address for reservation emails, and DKIM with SHA-256 and a key of at least 1024 bits. Follow Apple's signing-domain alignment requirement; do not send reservation markup in advertisements.

For native app donations and reservation actions, see [Siri Event Suggestions](https://developer.apple.com/documentation/sirikit/siri-event-suggestions).

### Format Reservation Data

Use JSON-LD in a `<script type="application/ld+json">` element, or schema.org Microdata using `itemscope`, `itemtype`, and `itemprop`. Apple's format specifies `http://schema.org` for JSON-LD's `@context`; this vocabulary identifier does not replace the HTTPS delivery requirement. Include the correct reservation `@type`. JSON-LD must be valid JSON, without JavaScript comments or unfinished payload placeholders.

Choose the relevant schema and supply its required fields, not just an ID. For example, [`TrainReservation`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/trainreservation) requires `@context`, `@type`, `reservationFor`, `reservationId`, `reservationStatus`, and `underName`; its nested objects also have schemas. Use the documented full status values `http://schema.org/ReservationConfirmed` and `http://schema.org/ReservationCancelled`.

Test future events, updates, cancellations, duration, and location. Include the relevant time zone for each start/end time, especially when departure and arrival locations differ. This structured-data format is not a new Safari 27 API or a substitute for [App Intents](AppIntents.md).

## Topics

### Essentials
- [Providing Trusted Data](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/providing-trusted-data) - Sign your content and avoid sending unnecessary or inaccurate information.
- [Checking Your Reservation Markup](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/checking-your-reservation-markup) - Preview reservation event data before the allow list includes your domain.

### Transportation
- [`FlightReservation`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/flightreservation) - A flight booking.
- [`TrainReservation`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/trainreservation) - A train booking.
- [`BusReservation`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/busreservation) - A bus booking.
- [`BoatReservation`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/boatreservation) - A boat booking.
- [`RentalCarReservation`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/rentalcarreservation) - A car rental, including pickup/drop-off details.

### Food, Lodging, and Events
- [`EventReservation`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/eventreservation) - A movie, sporting event, live show, or other scheduled booking.
- [`FoodEstablishmentReservation`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/foodestablishmentreservation) - A restaurant booking.
- [`LodgingReservation`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/lodgingreservation) - A hotel or other lodging booking.

### Common Reservation Data
- [`Person`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/person) - The passenger, guest, or attendee.
- [`Ticket`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/ticket) - Ticket identification and an optional reserved seat.
- [`Seat`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/seat) - Seat number, row, section, or class of service.
- [`Organization`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/organization) - A business or event/transport provider.
- [`Place`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/place) - A named location with an address and optional telephone.
- [`PostalAddress`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/postaladdress) - Prefer the physical destination, not an administrative mailing address.

### Basic Data Types
- [`@context`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/@context) - The format's schema.org vocabulary reference.
- [`dateTimeISO8601`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/datetimeiso8601) - An ISO-8601 date/time with the appropriate event time zone.
- [`reservationId`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/reservationid) - A stable, unique booking identifier.
- [`reservationStatus`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/reservationstatus) - One of the documented confirmed/cancelled status URLs.
- [`URL`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/url) - A webpage address.
- [`telephone`](https://developer.apple.com/documentation/sirieventsuggestionsmarkup/telephone) - A telephone-number string.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/SiriEventSuggestionsMarkup)*
