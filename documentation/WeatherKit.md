# WeatherKit

Deliver weather conditions and alerts to your users.

**Platforms:** iOS 16.0+ | iPadOS 16.0+ | Mac Catalyst 16.0+ | macOS 13.0+ | tvOS 16.0+ | visionOS 1.0+ | watchOS 9.0+

## Overview

**WeatherKit** provides timely weather information including current conditions, minute precipitation, along with hourly, and daily forecasts. It also provides severe weather alerts.

## Topics

### Fundamentals
- [Fetching weather forecasts with WeatherKit](https://developer.apple.com/documentation/weatherkit/fetching-weather-forecasts-with-weatherkit) - Request and display weather data for destination airports in a flight-planning app.
- **Weather** - A model representing the aggregate weather data the caller requests.
- **WeatherService** - Provides an interface for obtaining weather data.

### Requests
- **WeatherQuery** - A structure that encapsulates a generic weather dataset request.
- **CurrentWeather** - A structure that describes the current conditions observed at a location.
- **WeatherAttribution** - A structure that defines the necessary information for attributing a weather data provider.
- **WeatherMetadata** - A structure that provides additional weather information.
- **WeatherSeverity** - A description of the severity of the severe weather event.

### Characteristics
- **Precipitation** - The form of precipitation.
- **PressureTrend** - The atmospheric pressure change over time.
- **UVIndex** - The expected intensity of ultraviolet radiation from the sun.
- **Wind** - Contains wind data of speed, direction, and gust.
- **WeatherCondition** - A description of the current weather condition.

### Alerts and forecasts
- **WeatherAlert** - A weather alert issued for the requested location by a governmental authority.
- **WeatherAvailability** - A structure that indicates the availability of data at the requested location.
- **Forecast** - A forecast collection for minute, hourly, and daily forecasts.
- **MinuteWeather** - A structure that represents the next hour minute forecasts.
- **HourWeather** - A structure that represents the weather conditions for the hour.
- **DayWeather** - A structure that represents the weather conditions for the day.

### Celestial information
- **SunEvents** - An enumeration that represents dates of solar events, including sunrise, sunset, dawn, and dusk.
- **MoonEvents** - A structure that represents lunar events.
- **MoonPhase** - An enumeration that specifies the moon phase kind.

### Errors
- **WeatherError** - An error WeatherKit returns.

### Structures
- **CloudCoverByAltitude** - Contains the percentage of sky covered by low, medium and high altitude cloud.
- **DailyWeatherStatistics** - A structure that holds a collection of day weather statistics data.
- **DailyWeatherStatisticsQuery** - A structure that encapsulates a generic daily weather statistics dataset request.
- **DailyWeatherSummary** - A structure that holds a collection of day weather summaries.
- **DailyWeatherSummaryQuery** - A structure that encapsulates a generic daily weather summary dataset request.
- **DayPartForecast** - A structure that represents the weather forecast for part of the day.
- **DayPrecipitationStatistics** - A structure that describes precipitation statistics for a day.
- **DayPrecipitationSummary** - A structure that describes the precipitation summary for a day.
- **DayTemperatureStatistics** - A structure that describes temperature statistics for a day.
- **DayTemperatureSummary** - A structure that describes the temperature summary for a day.
- **HistoricalComparisons** - A structure that represents the weather condition comparisons for a specific location. It's a list of comparisons between current readings and historical averages. The list is ordered by significance of deviation.
- **HourTemperatureStatistics** - A structure that describes temperature statistics for a specific hour.
- **HourlyWeatherStatistics** - A structure that holds a collection of hour weather statistics data.
- **HourlyWeatherStatisticsQuery** - A structure that encapsulates a generic hourly weather statistics dataset request.
- **MonthPrecipitationStatistics** - A structure that describes precipitation statistics for a specific month.
- **MonthTemperatureStatistics** - A structure that describes temperature statistics for a specific month.
- **MonthlyWeatherStatistics** - A structure that holds a collection of month weather statistics data.
- **MonthlyWeatherStatisticsQuery** - A structure that encapsulates a generic monthly weather statistics dataset request.
- **Percentiles** - A structure that describes probability distributions for a measurable weather condition.
- **PrecipitationAmountByType** - A structure that provides a breakdown of amounts of all forms of precipitation that is expected to occur over a period of time.
- **SnowfallAmount** - A structure that describes the snowfall amount over a period of time.
- **Trend** - A structure describing an observed pattern in the data for weather at a location for a specific condition.
- **TrendBaseline** - A type encapsulating everything there is to know about what a trend baseline is.
- **WeatherChange** - A structure that informs how certain measurable weather aspects are expected to change relative to before.
- **WeatherChanges** - A structure that represents the Weather Change forecast. It provides a qualitative assessment of whether upcoming weather is significantly different from prior conditions.

### Enumerations
- **Deviation** - Describes a comparison between two values in a trend.
- **HistoricalComparison** - An enum that represents a recognized comparison in the statistical analysis of a location's historical weather data.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/WeatherKit)*