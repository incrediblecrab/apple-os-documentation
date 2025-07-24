# WeatherKit REST API

Obtain historical, current, and predictive weather for your app or service.

**Platforms:** Weather API 1.0.0+

## Overview

Use the WeatherKit REST API web service to provide weather data to your apps and services that offer both current and forecasted weather information to your users.

To provide weather information to a web app or other platform, like Android, use the WeatherKit REST API. For native iOS, macOS, tvOS, and watchOS apps, use WeatherKit.

Important: Using this API requires attribution. See WeatherKit - Data Sources to learn more.

## Topics

### Fundamentals
- [Request authentication for WeatherKit REST API](https://developer.apple.com/documentation/WeatherKitRESTAPI/request_authentication_for_weatherkit_rest_api) - Create a developer token to access weather data.

### Obtaining weather information for a location
- [GET /api/v1/availability/{latitude}/{longitude}](https://developer.apple.com/documentation/WeatherKitRESTAPI/get_api_v1_availability_latitude_longitude) - Determine the data sets available for the specified location.
- [GET /api/v1/weather/{language}/{latitude}/{longitude}](https://developer.apple.com/documentation/WeatherKitRESTAPI/get_api_v1_weather_language_latitude_longitude) - Obtain weather data for the specified location.
- **Weather** - The collection of all requested weather data.
- **Latitude** - A numeric value indicating the latitude of the coordinate between -90 and 90.
- **Longitude** - A numeric value indicating the longitude of the coordinate between -180 and 180.
- **DataSet** - The collection of weather information for a location.

### Obtaining current weather information
- **CurrentWeather** - The current weather conditions for the specified location.
- **Metadata** - Descriptive information about the weather data.
- **ProductData** - A base type for all weather data.

### Obtaining minute-to-minute forecast weather
- **ForecastPeriodSummary** - The summary for a specified period in the minute forecast.
- **ForecastMinute** - The precipitation forecast for a specified minute.

### Obtaining hourly weather information
- **HourWeatherConditions** - The historical or forecasted weather conditions for a specified hour.
- **HourlyForecast** - A collection of hour forecasts for a specified range of hours.
- **NextHourForecast** - A minute-by-minute forecast for the next hour.

### Obtaining daily weather information
- **DayWeatherConditions** - The historical or forecasted weather conditions for a specified day.
- **DayPartForecast** - A summary forecast for a daytime or overnight period.
- **DailyForecast** - A collection of day forecasts for a specified range of days.

### Obtaining weather alerts
- [GET /api/v1/weatherAlert/{language}/{id}](https://developer.apple.com/documentation/WeatherKitRESTAPI/get_api_v1_weatheralert_language_id) - Receive an active weather alert.
- **WeatherAlert** - An official message indicating severe weather from a reporting agency.
- **WeatherAlertCollection** - A collection of severe weather alerts for a specified location.
- **WeatherAlertSummary** - Detailed information about the weather alert.
- **ResponseType** - The recommended action from a reporting agency.
- **Severity** - The level of danger to life and property.
- **Urgency** - An indication of urgency of action from the reporting agency.

### Identifying weather events
- **UnitsSystem** - The system of units that the weather data is reported in.
- **MoonPhase** - The shape of the moon as seen by an observer on the ground at a given time.
- **PrecipitationType** - The type of precipitation forecasted to occur during the day.
- **PressureTrend** - The direction of change of the sea level air pressure.

### Obtaining event information
- **EventText** - The official text describing a severe weather event from the agency.
- **Certainty** - How likely the event is to occur.

### Performing attribution
- [GET /attribution/{language}](https://developer.apple.com/documentation/WeatherKitRESTAPI/get_attribution_language) - Receive attribution information.
- **Attribution** - A list of image asset URLs for attribution.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/WeatherKitRESTAPI)*