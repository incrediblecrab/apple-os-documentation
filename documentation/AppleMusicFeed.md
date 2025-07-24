# Apple Music Feed

Access the content of the Apple Music Catalog in bulk.

**Platforms:** AppleMusicFeed 1.0+

## Overview

Apple Music Feed contains the catalog content of Apple Music products in bulk for consumption as feed exports. These bulk exports are appropriate for offline use cases, complementing Apple Music API, which is best for online use. Apple Music Feed includes content metadata for albums, songs, artists, and popularity charts, and fully refreshes every 24 hours. You access the Apple Music Feed using Apple Media Feed API to request an export of a data set.

With access to the raw data and the information in this documentation, you can use Apple Music Feed in many ways. For example, if you want to build a discovery engine for Apple Music, your team can examine the data and determine endpoint requests to serve such an engine.

Apple Music Feed uses the Parquet format, which is an open-source columnar storage file format that optimizes the storage and processing of large datasets. The Parquet format improves query performance and reduces storage costs in scenarios where you need to read or process data selectively. It achieves this by using columns and storing the values of each column together, which allows efficient compression and encoding techniques that you can apply specifically to each column. Many large-scale data-processing frameworks, like Hadoop and Spark, use this format.

Note: Although the feed is in Parquet format, this documentation provides data examples in JSON format for illustrative purposes.

### Use sample scripts

You can find sample Java and Python scripts in the music-feed-examples public GitHub repository that perform the following steps:

1. Generate a developer token.
2. Use the token to request metadata for the latest feed export for a specific data set.
3. Use the token to request links to parts of the data for a feed export.
4. Download the feed data to a specified output directory.
5. Load the data files in Parquet and run a simple query.

## Topics

### Essentials
- [Generating developer tokens](https://developer.apple.com/documentation/AppleMusicFeed/generating_developer_tokens) - Create a JSON Web Token to authorize your requests to Apple Media Feed API.
- [Requesting a feed export](https://developer.apple.com/documentation/AppleMusicFeed/requesting_a_feed_export) - Create requests for Apple Music Catalog metadata.
- [Interpreting responses](https://developer.apple.com/documentation/AppleMusicFeed/interpreting_responses) - Learn about responses from Apple Media Feed API to your Apple Music Feed requests.

### Objects
- **Album** - The data structure that represents an Album resource.
- **Song** - The data structure that represents a Song resource.
- **Artist** - The data structure that represents an Artist resource.
- **PopularityTopChartAlbums** - The data structure that represents an album popularity chart resource.
- **PopularityTopChartSongs** - The data structure that represents a song popularity chart resource.

---

*Source: [Apple Developer Documentation](https://developer.apple.com/documentation/AppleMusicFeed)*